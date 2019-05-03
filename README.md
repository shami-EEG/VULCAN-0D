# VULCAN: 0-D box version
The original VULCAN is a Chemical kinetics model for exoplanetary atmospheres.
The theory paper of VULCAN can be found at https://arxiv.org/abs/1607.00409

## Requirements
VULCAN is developed with Python 3. It should also be compatibal with python 2.X. 

VULCAN requires the following python packages:
- numpy
- scipy
- Sympy
- matplotlib
- PIL/Pillow (optional)

If any of the first four packages are not installed, the easiest way is to install the full SciPy Stack. e.g.
```bash
python -m pip install --upgrade pip
``` 
```bash
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```
The above commands update pip and install SciPy via pip. Further information can be found at http://www.scipy.org/install.html

PIL or Pillow is a plotting library. If installed, the plots will be conveniently shown by the os-built-in image viewer. See https://github.com/python-pillow/Pillow for more information.  

## Quick Start

Go to the main folder of VULCAN, run 
```
python vulcan.py 
```


After the run successfully finished, we can plot the results from the output print_evolution.py
The series of timesteps and mixing ratios can be access from data['variable']['t_time'] and np.array(data['variable']['y_time'])[:,0,species.index(sp)]/float(data['atm']['n_0']), respectively (data['atm']['n_0'] is the total number density). 


## Full instruction

### Structure
```
├── VULCAN/
│   ├── atm/
│   ├── /thermo/
│   │   ├── HOC_compose.txt
│   │   ├── gibbs_text.txt
│   │   ├──/NASA9/
│   │   ├── XXX_netowrk.txt
│   ├── build_atm.py  
│   ├── chem_funs
│   ├── CHO_netowrk.txt
│   ├── op.py
│   ├── prepipe.py
│   ├── plot_vulcan.py
│   ├── phy_const.py
│   ├── store.py
│   ├── vulcan.py
│   ├── vulcan_cfg.py
``` 

`/atm/` : for input atmospheric files  
`/thermo/` : for thermodynamic data  
`/thermo/HOC_compose` : basic physical property e.g. number of atoms and molecular weight   
`/NASA9/` : to store NASA-9 polynomials for the Gibbs free energy of every species   
`build_atm.py` : modules to construct the atmospheric structure and to read in reaction rates  
`chem_funs.py` : the functions of chemical sources, Jacobian matrix and the equilibrium constants    
`XXX_netowrk.txt` : the kinetics network  
`op.py` : modules for the main computation  
`prepipe.py` : pre-pipeline routine to produce `chem_funs.py`    
`plot_vulcan.py` : read-in and plotting script  
`phy_const.py` : physical constants  
`store.py` : modules to store all the variables  
`vulcan.py` : the main file of VULCAN  
`vulcan_cfg.py` : the configuration file for VULCAN  

```vulcan_cfg.py``` includes all the settings and parameters, e.g. the atmospheric parameters, the elemental abundance etc. Typically this is the only file you need to edit for each specific run. A summary of every setting is listed in ```vulcan_cfg_readme.txt```. 

### Input Files
The key input files of VULCAN include the chemical network and the atmospheric file.
```CHO_network.txt``` is the deafult reaction network including carbon, hydrogen, and oxygen species. It is constructed for  thermochemistry from 500 to 2500 K using a reduced network with 29 gaseous species and less than 300 reactions to benefit for efficiency. The rate coefficients A, B, C are written in A, B, C as in the Arrhenius formula k = A T^B exp(-C/T) (See the section of editing or using a different chemical network.)  The input temperature-pressure profiles are placed in the `/atm` folder by default. As the form of the included example files for HD 189733b and HD 209458b, the first line is always commented for units, and the second line specifies the column names: **Pressure	Temp** or **Pressure	Temp  	Kzz** (if Kzz-P profile is provided). So the file consists of two columns without K<sub>zz</sub> and three columns with K<sub>zz</sub>. When K<sub>zz</sub> is provided, set
```python
Kzz_prof = 'file'
```
in the configuration file ```vulcan_cfg.py```.
  
### pre-pipeline
VULCAN is developed in a flexible way that the chemical network is _not_ hard coded. Instead, ```prepipe.py``` generates all the required funtions from ```CHO_netowrk.txt``` into ```chem_funs.py``` . ```prepipe.py``` is executed prior to the release to make ```chem_funs.py``` from the default network. Once any change is made to the file of chemical network, ```prepipe.py``` has to be executed again before running the main code to regenerate the corresponding functions, by simply run
```
python prepipe.py 
```
One can examine the information, e.g. the reaction table in the comments in ```chem_funs.py```, being updated.

### Editing or Using a different chemical network
You can edit the default netowrk, to remove or add reactions, to change rate constats, etc. You can also use a different chemical network, as long as it is in the same format as ```CHO_netowrk.txt```. Noted that however, changing or using a different chemical network is not warranted, unrealistic values could lead to numerical issues. In the network file, the reactions should be writen in the form of [ A + B -> C + D ], including the square brackets. Only the forward reactions are listed, since VULCAN reverses the forward reactions to obtain the reverse reactions using the thermodynamic data. The reaction number, i.e. **id**, is irrelevent as it will be automatically generated (and writing into the network file) while running ```prepipe.py```. Three-body or dissociation reactions should be separately listed after the comment line 
```python
# 3-body and Disscoiation Reactions
```
Next, make sure all the species are included in the ```NASA9``` folder. If not, they need to be add manually by looking over ```nasa9_2002_E.txt``` and save them into txt files with the same name as used in the network. The format of the NASA 9 polynomials is as follows
```
a1 a2 a3 a4 a5
a6 a7 0. a8 a9
```
Noted that a7 and a8 are separated by 0. The first two rows are for low temperature (200 - 1000 K) and the last two rows are for high temperature (1000 - 6000 K).

Finally, run ```prepipe.py``` as described before.

## License
VULCAN is distributed under the terms of the GNU General Public License (GPL) license. For more information, see ```GPL_license.txt``` in the main directory.

## Remarks
The project is financially support from the Center for Space and Habitability (CSH), the PlanetS NCCR framework and the Swiss- based MERAC Foundation.
The Exoclime Simulation Platform ([ESP][1]) develops a set of open-source codes
for research on exoplanets. The three parts of the ESP are
  - [HELIOS][2] radiative transfer and retrieval,
  - [THOR][3] atmospheric fluid dynamics,
  - [VULCAN][4] atmospheric chemistry.

[1]: http://www.exoclime.net
[2]: https://github.com/exoclime/HELIOS
[3]: https://github.com/exoclime/THOR
[4]: https://github.com/exoclime/VULCAN
