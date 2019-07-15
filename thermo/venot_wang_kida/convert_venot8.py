import numpy as np
import scipy


# to collect all 3body reactions in the end of the file

new_str = '# C/N/O/H reaction network based on Venot et al. (2012) with some revision\n' 
new_str += '# Two-body Reactions\n'
new_str += '# id	Reactions                           	A       	B       	C\n'    		

three_body = '3-body reactions without high-pressure rates"\n'


with open('wang_reaction8.txt') as f:
    for line in f.readlines():
        
        if not line.startswith("#") and line.split(): 
            
            line = line.replace('[',']\t\t\t\t')
            line = line.replace('],','')
            line = line.replace(',','\t')
            line = line.replace('three_body_reaction(','    [ ')
    
            line = line.replace('"','')
            line = line.replace('<=','-')
            
            line = line.replace(' efficiencies =', 'effi')
            
            
            if not line.startswith("effi"):
                new_str += line
            
            else:
                new_line = 'effi {'
                new_effi = []
                li = line.split()
                for ele in li:
                    if ("O2" in ele or "CO" in ele or "CO2" in ele or "H2O" in ele or"CH4" in ele \
                    or "H2" in ele or "N2" in ele or "H2" in ele or "NH3" in ele) and 'H2O2' not in ele and 'N2H4' not in ele\
                    and 'N2O' not in ele and 'N2O4'not in ele and 'NO2' not in ele: 
                        #print ele
                        new_effi.append("'" + ele.replace(':',"':"))
                
                for ele in new_effi:
                    new_line += ele
                    new_line += ","
                
                new_line = new_line[:-1]
                new_line += '}\n\n'
                
                new_str += new_line
                
            
       
            # if 'N2D' in li or 'N4S' in li or 'O1D' in li or 'O3P' in li or '3CH2' in li or '1CH2' in li:
            #     pass
            # else:
                
            
            #last_prod = line.split()[-3]
            #print line.split()
            #print last_prod 
            #line = line.replace(last_prod,last_prod + ' ]\t\t\t')
            
            #li = line.split()
            #newline = li[0] + ' ' + '{:>6}'.format(li[1]) + '{:>4}'.format(li[1])+ '{:>6}'.format(li[1])
            #[newline + '{:>6}'.format(el) for el in li[2:] ]

            # if 'M' in line: three_body += line
            # else: new_str += line 

# with open('wang_reaction7.txt') as f:
#     for line in f.readlines():
#
#         if not line.startswith("#") and line.split():
#             line = line.replace('[',' ]\t\t\t\t')
#             line = line.replace('])','')
#             line = line.replace(',','  ')
#             line = line.replace('reaction(','[ ')
#
#             line = line.replace('"','')
#             line = line.replace('<=','-')
#
#             li = line.split()
#             if 'N2D' in li or 'N4S' in li or 'O1D' in li or 'O3P' in li or '3CH2' in li or '1CH2' in li:
#                 pass
#             else:
#                 new_str += line
#
#
#     
with open('vulcan_venot_8.txt', 'w+') as f: f.write(new_str)   
#new_str += three_body    
 
