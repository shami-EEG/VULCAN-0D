# This is the configuration file for the 0D model
# Note that the prescribed pressure is fixed

# ============================================================================= 
# Configuration file of VULCAN:  
# ============================================================================= 

# ====== Setting up the elements included in the network ======
atom_list = ['H', 'O', 'C', 'He'] # For checking element conservation

# ====== Set up paths and filenames for the input and output files  ======
use_venot_network = True # Only True while running Olivia's netowrk
network = 'thermo/wang_venot_network.txt' 
gibbs_text = 'thermo/gibbs_text.txt' # all the nasa9 files must be placed in the folder: thermo/NASA9/
com_file = 'thermo/all_compose_venot.txt' # basic chemistry data (stoichiometric numbers and mass)
output_dir = 'output/' # output directory
plot_dir = 'plot/'  # plot directory
out_name =  '0D_2000K_1e-3bar.vul' # output name  
y_time_freq = 1 # The frequency (every _ steps) to store the calculation




# ====== Setting up the elemental abundance ======
use_solar = False 
# If True: using the default solar abundance from Table 10. (K.Lodders 2009)
# if False, using the customized elemental abundance below
# customized elemental abundance
O_H = 6.0618E-4 
C_H = 2.7761E-4 
N_H = 8.1853E-5
He_H = 0.09691

ini_mix = 'const_mix'  # The initial abundances
# Options: 'EQ' -- equilibrium chemistry , 'const_mix' -- prescribed below
const_mix = {'H':0.9081, 'C':3.632E-4, 'O':7.265E-4, 'He':9.081E-2}

# ====== Reactions to be switched off  ======
remove_list = []

# ====== Setting up parameters for the 0-D "box" ======
nz = 1  # always 1 for 0D 
T_box = 2000. # temperature (K)
p_box = 1e3   # pressure (dyne/cm^2)
# Both T_box and p_box are always kept fixed (even when the total number density changes due to chemical reactions)
atm_base = 'H2' # The bulk gas: changes the efficeny factor in 3-body reactions in Venot's network
# options: 'H2','O2','CO','CO2','H2O','CH4','N2','NH3'

# condensation
use_condense = False
condesne_sp = ["H2O"]  
non_gas_sp = ['H2O_l_s']
start_conden_time = 1e7
use_sharks = False

# ====== Setting up the photochemistry (Not relevant for the 0D box wo. photochemistry) ======
use_photo = False
excit_sp = ['O_1', 'CH2_1'] # N_D to avoid in the initial abundances by fc
scat_sp = ['N2', 'O2'] # # the molecules that contribute to Rayleigh scattering
r_star = 1. #0.752 HD209: 1.118
orbit_radius = 1. #0.03142 # planet-star distance in A.U.
sl_angle = 48 /180.*3.14159 # the zenith angle of the star
edd = 0.669 #(cos(48 deg) )  # the Eddington coefficient
dbin = 0.2


# ====== Setting up general parameters for the ODE solver (No need to change anything here) ====== 
ode_solver = 'Ros2' 
use_print_prog = True
use_height = True
print_prog_num = 200
use_live_plot = False
use_live_flux = 0
use_save_movie = 0
use_flux_movie = True
live_plot_frq = 10
use_plot_end = False
use_plot_evo = False
plot_TP = 1
output_humanread = False
#plot_spec = ['H', 'H2', 'CH3', 'CH4', 'CO', 'CH3OH', 'CH2OH', 'He']
#live_plot_spec = ['H', 'H2', 'H2O', 'CH4', 'CO', 'CO2', 'C2H2', 'C2H4', 'C2H6', 'CH3OH']
#live_plot_spec = ['H2O', 'H2O_l_s', 'CO2', 'CH4', 'NO', 'NO2', 'HNO3', 'O3','N2O', 'NH3', 'O2']
# frequency to update the flux and tau
# ini_update_photo_frq = 20
# final_update_photo_frq = 5
# update_frq = 100 # for updating dz and dzi due to change of mu

# ====== steady state check ======
st_factor = 0.9  
count_min = 100

# ====== Setting up numerical parameters for the ODE solver ====== 
dttry = 1.E-10  # the initial stepsize (s) 
#dt_std = 1.     
trun_min = 1e2
runtime = 1.E24  # max runtime
count_max = int(5E4)  # max steps
dt_min = 1.E-14  # min stepsize
dt_max = runtime*0.01  # mxn stepsize
dt_var_max = 2.  # max factor of varing the stepsize
dt_var_min = 0.5  # min factor of varing the stepsize
atol = 1.e-2   # absolute tolorence
mtol = 1.E-30  # relative tolorence
mtol_conv = 1.E-20  
pos_cut = 0
nega_cut = -1.
loss_eps = 1e3 #1e-1
yconv_cri = 0.01 # for checking steady-state
slope_cri = 1.e-10
yconv_min = 0.1

flux_cri = 5.e-2  #0.1
flux_atol = 1. # the tol for actinc flux (# photons cm-2 s-1 nm-1)


# ====== Setting up numerical parameters for Ros2 ODE solver ====== 
rtol = 0.1  # the tolorence for the numerical truncation errors. Larger values run faster but might be unstable
# suggested values: 0.01 ~ 0.1 

# ====== Setting up numerical parameters for SemiEu/SparSemiEU ODE solver (Not relavent) ====== 
PItol = 0.1
use_PIL = True