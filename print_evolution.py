import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.legend as lg
import vulcan_cfg
import os, sys
import pickle


# Setting the vulcan output file to read in    
vul_data = 'output/0D-2000K_1e2bar.vul'
# Setting the output file name
output = open('output/ISSI_0D_test4-2000K_1e2bar.txt', "w")

with open(vul_data, 'rb') as handle:
  data = pickle.load(handle)
species = data['variable']['species']


ost = '{:<8s}'.format('Time(s)') + ' '
for sp in species: ost += '{:>10s}'.format(sp)
ost += '\n'
 
for n, t in enumerate(data['variable']['t_time']):
    ost += '{:<8.3E}'.format(t) + ' '
    for sp in species: ost +=  '{:>10.3E}'.format(np.array(data['variable']['y_time'])[n,0,species.index(sp)]/float(data['atm']['n_0'])) 
    ost += '\n'
ost = ost[:-1]
    

output.write(ost)
output.close()
