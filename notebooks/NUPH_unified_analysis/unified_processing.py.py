import os
from obspy.clients.fdsn import Client
from obspy import UTCDateTime, Stream
from scipy.signal import spectrogram
import numpy as np
import matplotlib.pyplot as plt
import time

# Set parameters
CLIENT_NAME = "GEOFON"  # or "IRIS"
NETWORK = "9F"  # Example: IU network
STATION = "NUPH"  # Replace with your station
LOCATION = "*"  # Location code, * for any
CHANNEL = "HHE"  # Vertical component
START_DATE = UTCDateTime("2021-03-12T00:00:00")  # Start of analysis
END_DATE = UTCDateTime("2021-06-24T00:00:00")  # End of analysis
FREQ_MIN = 1.0  # Min frequency for bandpass filter
FREQ_MAX = 4.0  # Max frequency for bandpass filter
RESAMPLE_RATE = 8.0  # Target sampling rate in Hz
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")  # Directory to save processed data

os.makedirs(OUTPUT_DIR, exist_ok=True)

# List to collect all spectrograms
all_spectrograms = []

def download_data_for_day(client, network, station, location, channel, date):
    """
    Downloads one day of seismic data and skips if unavailable.
    """
    try:
        start_time = date
        end_time = date + 86400  # 24 hours
        st = client.get_waveforms(network, station, location, channel, start_time, end_time)
        print(f"Data downloaded for {date}.")
        return st
    except Exception as e:
        print(f"No data available for {date}: {e}")
        return None

def preprocess_data(stream):
    """
    Preprocess seismic data: detrend, demean, resample, and bandpass filter.
    """
    stream.detrend("linear")
    stream.detrend("demean")
    stream.filter("bandpass", freqmin=FREQ_MIN, freqmax=FREQ_MAX)
    stream.resample(RESAMPLE_RATE)
    return stream

def segment_data(stream, segment_length=3600):
    """
    Segments data into one-hour windows.
    """
    segments = []
    for tr in stream:
        start = tr.stats.starttime
        while start + segment_length <= tr.stats.endtime:
            segment = tr.slice(starttime=start, endtime=start + segment_length)
            segments.append(segment)
            start += segment_length
    return Stream(segments)

def compute_spectrogram(segment, nfft=256, overlap=0.5):
    """
    Computes the spectrogram of a given data segment.
    """
    n_overlap = int(nfft * overlap)
    f, t, Sxx = spectrogram(segment.data, fs=segment.stats.sampling_rate, nperseg=nfft, noverlap=n_overlap)
    Sxx = np.log1p(Sxx)  # Log scale for better visualization
    return Sxx

def normalize_spectrogram(sxx):
    """
    Normalize spectrogram values for neural network input.
    """
    return (sxx - np.mean(sxx)) / np.std(sxx)

def process_and_collect_segments(segments, date):
    """
    Process each segment, compute spectrogram, normalize, and collect all into one array.
    """
    global all_spectrograms  # To accumulate across multiple days
    for segment in segments:
        Sxx = compute_spectrogram(segment)
        Sxx_normalized = normalize_spectrogram(Sxx)
        all_spectrograms.append(Sxx_normalized)  # Append normalized spectrogram to the list

def save_all_spectrograms():
    """
    Save all collected spectrograms into a single NumPy array file (Input.npy).
    """
    spectrogram_array = np.array(all_spectrograms)  # Convert list to NumPy array
    output_path = os.path.join(OUTPUT_DIR, "Input.npy")
    np.save(output_path, spectrogram_array)  # Save the array to a file
    print(f"Saved all spectrograms to {output_path}")

def main():
    client = Client(CLIENT_NAME)
    current_date = START_DATE

    while current_date < END_DATE:
        # Step 1: Download data for the day
        raw_data = download_data_for_day(client, NETWORK, STATION, LOCATION, CHANNEL, current_date)
        if raw_data is None:
            current_date += 86400  # Skip to the next day
            continue

        # Step 2: Preprocess data
        processed_data = preprocess_data(raw_data)

        # Step 3: Segment data
        segments = segment_data(processed_data)
        print(f"Segmented into {len(segments)} one-hour windows for {current_date}.")

        # Step 4: Process and collect all spectrograms into one list
        process_and_collect_segments(segments, current_date)

        # Move to the next day
        current_date += 86400

    # Step 5: Save all spectrograms as a single NumPy array
    save_all_spectrograms()

if __name__ == "__main__":
    main()