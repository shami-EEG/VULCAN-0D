import numpy as np
import scipy

new_str = '# C/N/O/H reduced network based on Venot et al. (2019)\n' 
new_str += '# Two-body Reactions\n\n'
new_str += '# id	Reactions                           	A       	B       	C\n'    		

#three_body = '3-body reactions without high-pressure rates"\n'


with open('reactions_1.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 9:
            tmp = '   	[ ' + ls[0] + ' + ' + ls[1] + ' -> ' + ls[2] + ' + ' + ls[3]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[4])*300**(-1*float(ls[5])) ) + '{:<10.3f}'.format(float(ls[5])) + '{:>6.1f}'.format(float(ls[6])) 
        
        elif len(ls) == 8:
            tmp = '   	[ ' + ls[0] + ' + ' + ls[1] + ' -> ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5]))
            
        elif len(ls) == 10:
            tmp = '   	[ ' + ls[0] + ' + ' + ls[1] + ' -> ' + ls[2] + ' + ' + ls[3] + ' + ' + ls[4]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[5])*300**(-1*float(ls[6])) ) + '{:<10.3f}'.format(float(ls[6])) + '{:>6.1f}'.format(float(ls[7])) 
        
        else: raise IOError ('\n Different format of number of reactants!')

        new_str += ls_str + '\n'

# file4: AB -> A + B without M
txt_f4 = '\n'       
with open('reactions_4.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 8:
            tmp = '   	[ ' + ls[0] + ' -> ' + ls[1] + ' + ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5])) + '\n'
        else: raise IOError ('\n Different format of number of reactants!')
        txt_f4 += ls_str
        
txt_f3 = '# 3-body and Disscoiation Reactionss\n'
txt_f3 += '# id	Reactions                           	A_0        B_0        C_0         A_inf     B_inf     C_inf\n'       
with open('reactions_3.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 39:
            tmp = '   	[ ' + ls[0] + ' + ' + ls[1] + ' + M -> M + ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5])) + '    '
            ls_str += '{:<13.2e}'.format(float(ls[8])*300**(-1*float(ls[9])) ) + '{:<10.3f}'.format(float(ls[9])) + '{:>6.1f}'.format(float(ls[10])) + '\n'
            ls_str += "Troe (" +ls[13] +", "+ ls[14]+", " +ls[15]+", " +ls[16] + ")\n" 
            ls_str += "effi {'O2':" + ls[17] +",'CO':" + ls[18] + ",'CO2':" + ls[19]+ ",'H2O':"+ ls[20] + ",'CH4':"+ ls[21] + ",'H2':"+ ls[22] + ",'N2':"+ ls[25] + ",'He':"+ ls[26]+ ",'NH3':"+ ls[33] + "}\n"
        else: raise IOError ('\n Different format of number of reactants!')
        
        txt_f3 += ls_str

txt_f6 = ''    
with open('reactions_6.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 39:
            tmp = '   	[ ' + ls[0] + ' + M -> M + ' + ls[1] + ' + ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5])) + '    '
            ls_str += '{:<13.2e}'.format(float(ls[8])*300**(-1*float(ls[9])) ) + '{:<10.3f}'.format(float(ls[9])) + '{:>6.1f}'.format(float(ls[10])) + '\n'
            ls_str += "Troe (" +ls[13] +", "+ ls[14]+", " +ls[15]+", " +ls[16] + ")\n" 
            #ls_str += "effi {'O2':" + ls[17] +",'CO':" + ls[18] + ",'CO2':" + ls[19]+ ",'H2O':"+ ls[20] + ",'CH4':"+ ls[21] + ",'H2':"+ ls[22] + ",'N2':"+ ls[25] + ",'He':"+ ls[26]+ ",'NH3':"+ ls[33] + "}\n"
        else: raise IOError ('\n Different format of number of reactants!')
        
        txt_f6 += ls_str



txt_f2 = '# 3-body reactions without high-pressure rates\n'
txt_f2 += '# id	Reactions                           	A_0        B_0        C_0\n'       
with open('reactions_2.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 30:
            tmp = '   	[ ' + ls[0] + ' + ' + ls[1] + ' + M -> M + ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5])) + '\n'
            ls_str += "effi {'O2':" + ls[8] +",'CO':" + ls[9] + ",'CO2':" + ls[10]+ ",'H2O':"+ ls[11] + ",'CH4':"+ ls[12] + ",'H2':"+ ls[13] + ",'N2':"+ ls[16] + ",'He':"+ ls[17]+ ",'NH3':"+ ls[24] + "}\n"
        else: raise IOError ('\n Different format of number of reactants!')
        
        txt_f2 += ls_str
        
        

#txt_f5 = '# 3-body reactions without high-pressure rates\n'
#txt_f5 += '# id	Reactions                           	A_0        B_0        C_0\n'
txt_f5 = '\n'       
with open('reactions_5.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 30:
            tmp = '   	[ ' + ls[0] + ' + M -> M + ' + ls[1] + ' + ' + ls[2]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[3])*300**(-1*float(ls[4])) ) + '{:<10.3f}'.format(float(ls[4])) + '{:>6.1f}'.format(float(ls[5])) + '\n'
            ls_str += "effi {'O2':" + ls[8] +",'CO':" + ls[9] + ",'CO2':" + ls[10]+ ",'H2O':"+ ls[11] + ",'CH4':"+ ls[12] + ",'H2':"+ ls[13] + ",'N2':"+ ls[16] + ",'He':"+ ls[17]+ ",'NH3':"+ ls[24] + "}\n"
        else: raise IOError ('\n Different format of number of reactants!')
        
        txt_f5 += ls_str

txt_f7 = '\n'       
with open('reactions_7.txt') as f:
    for line in f.readlines():
        ls = line.split()
        
        if len(ls) == 29:
            tmp = '   	[ ' + ls[0] + ' + M -> M + ' + ls[1]
            ls_str = '{:<42s}'.format(tmp) + ']  '
            ls_str += '{:<13.2e}'.format(float(ls[2])*300**(-1*float(ls[3])) ) + '{:<10.3f}'.format(float(ls[3])) + '{:>6.1f}'.format(float(ls[4])) + '\n'
            ls_str += "effi {'O2':" + ls[7] +",'CO':" + ls[8] + ",'CO2':" + ls[9]+ ",'H2O':"+ ls[10] + ",'CH4':"+ ls[11] + ",'H2':"+ ls[12] + ",'N2':"+ ls[15] + ",'He':"+ ls[16]+ ",'NH3':"+ ls[23] + "}\n"
        else: raise IOError ('\n Different format of number of reactants!')
        
        txt_f5 += ls_str
        
new_str += txt_f4 
new_str += txt_f3 + txt_f6
new_str += txt_f2
new_str += txt_f5 
new_str += txt_f7
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
#             if 'N2D' in li or 'N4S' in li or 'O3P' in li or '3CH2' in li:
#                 new_str += line
#             else:
#                 pass
#                 # new_str += line


            
with open('vulcan_venot_reduced.txt', 'w+') as f: f.write(new_str)   
#new_str += three_body    
 
        