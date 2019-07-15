import numpy as np
import scipy


# to collect all 3body reactions in the end of the file

new_str = '# C/N/O/H reaction network based on Venot et al. (2012) with some revision\n' 
new_str += '# Two-body Reactions\n'
new_str += '# id	Reactions                           	A       	B       	C\n'    		

three_body = '3-body reactions without high-pressure rates"\n'


with open('wang_reaction1.txt') as f:
    for line in f.readlines():
        
        if not line.startswith("#") and line.split(): 
            
            line = line.replace('[',']\t\t\t\t')
            line = line.replace('])','')
            line = line.replace(',','')
            line = line.replace('reaction(','[ ')
    
            line = line.replace('"','')
            line = line.replace('<=','-')
            
            li = line.split()
            if 'N2D' in li or 'N4S' in li or 'O3P' in li or '3CH2' in li:
                new_str += line
            else:
                pass
                # new_str += line
            
            #last_prod = line.split()[-3]
            #print line.split()
            #print last_prod 
            #line = line.replace(last_prod,last_prod + ' ]\t\t\t')
            
            #li = line.split()
            #newline = li[0] + ' ' + '{:>6}'.format(li[1]) + '{:>4}'.format(li[1])+ '{:>6}'.format(li[1])
            #[newline + '{:>6}'.format(el) for el in li[2:] ]

            # if 'M' in line: three_body += line
            # else: new_str += line 

with open('wang_reaction7.txt') as f:
    for line in f.readlines():

        if not line.startswith("#") and line.split():
            line = line.replace('[',' ]\t\t\t\t')
            line = line.replace('])','')
            line = line.replace(',','  ')
            line = line.replace('reaction(','[ ')

            line = line.replace('"','')
            line = line.replace('<=','-')

            li = line.split()
            if 'N2D' in li or 'N4S' in li or 'O3P' in li or '3CH2' in li:
                new_str += line
            else:
                pass
                # new_str += line


            
with open('vulcan_venot_1_and7_left.txt', 'w+') as f: f.write(new_str)   
#new_str += three_body    
 
        
        
        # # switch to 3-body and dissociation reations
#         if line.startswith("# 3-body"):
#             re_tri = True
#
#         if line.startswith("# 3-body reactions without high-pressure rates"):
#             re_tri_k0 = True
#
#         if line.startswith("# special"):
#             special_re = True # switch to reactions with special forms (hard coded)
#
#         # skip common lines and blank lines
#         # ========================================================================================
#         if not line.startswith("#") and line.strip() and special_re == False: # if not starts
#
#             Rf[i] = line.partition('[')[-1].rpartition(']')[0].strip()
#             li = line.partition(']')[-1].strip()
#             columns = li.split()
#             Rindx[i] = int(line.partition('[')[0].strip())
#
#             a[i] = float(columns[0])
#             n[i] = float(columns[1])
#             E[i] = float(columns[2])
#
#             if build_table == True:
#                 ofstr += re_label + str(i) + '\n'
#                 ofstr +=  Rf[i] + '\n'
#
#             # switching to trimolecular reactions (len(columns) > 3 for those with high-P limit rates)
#             if re_tri == True and re_tri_k0 == False:
#                 a_inf[i] = float(columns[3])
#                 n_inf[i] = float(columns[4])
#                 E_inf[i] = float(columns[5])
#                 list_tri.append(i)
#
#             if columns[-1].strip() == 'He': re_He = i
#             elif columns[-1].strip() == 'ex1': re_CH3OH = i
#
#             # Note: make the defaut i=i
#             k_fun[i] = lambda temp, mm, i=i: a[i] *temp**n[i] * np.exp(-E[i]/temp)
#
#
#             if re_tri == False:
#                 k[i] = k_fun[i](Tco, M)
#
#             # for 3-body reactions, also calculating k_inf
#             elif re_tri == True and len(columns)>=6:
#
#
#                 kinf_fun[i] = lambda temp, i=i: a_inf[i] *temp**n_inf[i] * np.exp(-E_inf[i]/temp)
#                 k_fun_new[i] = lambda temp, mm, i=i: (a[i] *temp**n[i] * np.exp(-E[i]/temp))/(1 + (a[i] *temp**n[i] * np.exp(-E[i]/temp))*mm/(a_inf[i] *temp**n_inf[i] * np.exp(-E_inf[i]/temp)) )
#
#                 #k[i] = k_fun_new[i](Tco, M)
#                 k_inf = a_inf[i] *Tco**n_inf[i] * np.exp(-E_inf[i]/Tco)
#                 k[i] = k_fun[i](Tco, M)
#                 k[i] = k[i]/(1 + k[i]*M/k_inf )
#
#
#             else: # for 3-body reactions without high-pressure rates
#                 k[i] = k_fun[i](Tco, M)
#
#             ### TEST CAPPING
#             # k[i] = np.minimum(k[i],1.E-11)
#             ###
#
#             i += 2
#             # end if not