import numpy as np
import matplotlib.pyplot as plt
from obspy import read
import os
import glob

# # Load and display the .mseed file
# file_path = "notebooks/NUPH_analysis/data/segmented/9F_NUPH_HHE_20210312T134059.mseed"
# st = read(file_path)
# print(st)
# # Uncomment the following lines to see more details and plot the data
# # tr = st[0]
# # print(tr.stats)
# # st.plot()

# # display some data from numpy array of the trace
# tr = st[0]
# data = tr.data
# print(data)
# print("Data length: ", len(data))

# Delete all .npy files from the data/segmented folder
npy_files = glob.glob("notebooks/NUPH_analysis/data/segmented/*.npy")
for npy_file in npy_files:
    os.remove(npy_file)
    print(f"Deleted file: {npy_file}")
