import numpy as np
import scipy


new_str = '# id	Reactions'                           	
with open('wang_eff.txt') as f:
    for line in f.readlines():
        if not line.startswith("#") and line.split(): 

            if not line.startswith("effi"):
                new_str += line
            
            else:
                
                
                new_str += new_line
                
     
with open('vulcan_eff.txt', 'w+') as f: f.write(new_str)   
