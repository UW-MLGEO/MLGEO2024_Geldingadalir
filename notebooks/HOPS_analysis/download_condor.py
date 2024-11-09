import obspy
from obspy import UTCDateTime as utc
from obspy.clients.fdsn import Client
import numpy as np
import os

def download_data(client, net, sta, loc, cha, starttime, endtime, buffer, filepath):
    dates = np.array([])
    tr_length = 24 * 60 * 60

    for day in range((endtime - starttime) // tr_length):
        print(f'Downloading data for day {day + 1}')
        st = client.get_waveforms(
            network=net,
            station=sta,
            location=loc,
            channel=cha,
            starttime=starttime - buffer,
            endtime=starttime + buffer + tr_length
        )

        st.merge(fill_value='interpolate')
        name = f'{day + 1}_9fhops.mseed'
        st.write(os.path.join(filepath, name), format='MSEED')
        dates = np.append(dates, starttime.date)
        starttime += tr_length

    np.save(os.path.join(filepath, 'date_list.csv'), dates)
    print(f'Data download complete, saved to {filepath}')

def main():
    client = Client('GEOFON')
    NUM_DAYS = 100
    starttime = utc('2021-06-24T00:00:00')
    endtime = starttime + NUM_DAYS * (60 * 60 * 24)
    buffer = 60 * 60 * 24 * 0.05
    net = '9F*'
    sta = 'HOPS'
    loc = '*'
    cha = 'HHE'

    os.makedirs('data/raw', exist_ok=True)
    filepath = os.path.join(os.getcwd(), 'data/raw')

    print(f'Downloading data from {starttime} to {endtime}')
    download_data(client, net, sta, loc, cha, starttime, endtime, buffer, filepath)

if __name__ == "__main__":
    main()
