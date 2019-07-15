import numpy as np 
import pickle


vul = '../output/0D-800K_1e-3bar.vul'

with open(vul, 'rb') as handle:
  vul = pickle.load(handle)

#nr =  vul['variable']['nr']
#from chem_funs import ni, nr
nr =  282

species = vul['variable']['species'] 

output = open('../output/Test4_rate_list.txt', "w")

ost = '#' + '{:<8s}'.format('(bar)')  + '{:>9s}'.format('(K)')+'\n'
ost += '{:<8s}'.format('Pressure')  + '{:>9s}'.format('Temp')
for re in range(1,11): ost += '{:>11s}'.format('R') + str(re)
for re in range(11,100): ost += '{:>10s}'.format('R') + str(re)
for re in range(100,nr+1): ost += '{:>9s}'.format('R') + str(re)
ost += '\n'

ost += '{:<8.3E}'.format(vul['atm']['pco'][0]/1.e6)  + '{:>8.1f}'.format(vul['atm']['Tco'][0])
for re in range(1,nr+1): ost +=  '{:>12.3E}'.format(vul['variable']['k'][re][0])

ost += '\n'

vul = '../output/0D-800K_1e2bar.vul'
with open(vul, 'rb') as handle:
  vul = pickle.load(handle)

ost += '{:<8.3E}'.format(vul['atm']['pco'][0]/1.e6)  + '{:>8.1f}'.format(vul['atm']['Tco'][0])
for re in range(1,nr+1): ost +=  '{:>12.3E}'.format(vul['variable']['k'][re][0])
ost += '\n'

vul = '../output/0D-2000K_1e-3bar.vul'
with open(vul, 'rb') as handle:
  vul = pickle.load(handle)


ost += '{:<8.3E}'.format(vul['atm']['pco'][0]/1.e6)  + '{:>8.1f}'.format(vul['atm']['Tco'][0])
for re in range(1,nr+1): ost +=  '{:>12.3E}'.format(vul['variable']['k'][re][0])

ost += '\n'

vul = '../output/0D-2000K_1e2bar.vul'
with open(vul, 'rb') as handle:
  vul = pickle.load(handle)

ost += '{:<8.3E}'.format(vul['atm']['pco'][0]/1.e6)  + '{:>8.1f}'.format(vul['atm']['Tco'][0])
for re in range(1,nr+1): ost +=  '{:>12.3E}'.format(vul['variable']['k'][re][0])

output.write(ost)
output.close()

