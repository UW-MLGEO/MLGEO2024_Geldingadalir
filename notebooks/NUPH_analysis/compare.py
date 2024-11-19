# compare the data in /home/jen/snap/MLGEO2024_Geldingadalir/notebooks/NUPH_analysis/Input_nuph.npy and /home/jen/snap/MLGEO2024_Geldingadalir/ClusTremor-main/src/Input.npy

import numpy as np
import matplotlib.pyplot as plt

nuph = np.load('/home/jen/snap/MLGEO2024_Geldingadalir/notebooks/NUPH_analysis/Input_nuph.npy')
clus = np.load('/home/jen/snap/MLGEO2024_Geldingadalir/ClusTremor-main/src/Input.npy')

print(nuph.shape)
print(clus.shape)

plt.plot(nuph[:,0], nuph[:,1], 'r.')
plt.plot(clus[:,0], clus[:,1], 'b.')

plt.show()

print(f'hello')
