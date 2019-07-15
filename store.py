import numpy as np
import scipy
import vulcan_cfg
from chem_funs import ni, nr, spec_list  # number of species and reactions in the network
from vulcan_cfg import nz

class Variables(object):
    """
    store the essential variables for calculation  
    """
    def __init__(self): # self means the created object
        #self.nz = vulcan_cfg.nz
        self.k = {}  # k[] follows the same shape as Tco in read_rate() in op.py
        self.y = np.zeros((nz,ni))
        self.y_prev = np.zeros((nz,ni))
        self.ymix = np.zeros((nz,ni))
        self.y_ini = np.zeros((nz,ni))
        self.y_conden = np.zeros((nz,ni))  # to store the species removed by condensation
        
        self.t = 0
        self.dt = vulcan_cfg.dttry
        self.dy = 1.
        self.dy_prev = 1.
        self.dydt = 1.
        self.longdy = 1.
        self.longdydt = 1.
        
        self.dy_time = []
        self.dydt_time = []
        self.atim_loss_time = []
        self.ymix_time = []
        self.y_time = []
        self.t_time = []
        self.dt_time = []
        self.atom_loss_time = []
        
        # self.atom_tot = [0] * na
        self.atom_ini = {}
        self.atom_sum = {}
        self.atom_loss = {}
        self.atom_loss_prev = {}
        #  self.mean_mass = np.zeros(nz) 
        self.atom_conden = {}
        
        self.Rf = {}  # reaction equation
        self.Rindx = {}
        self.a, self.n, self.E, self.a_inf, self.n_inf, self.E_inf,= [{} for i in range(6)]
        self.k, self.k_fun, self.k_inf = [{} for i in range(3)] 
        self.photo_sp = set()  
        self.pho_rate_index, self.n_branch, self.wavelen, self.br_ratio = {}, {}, {}, {}
        
        self.kinf_fun = {}
        self.k_fun_new = {}
        
        # For O. Venot's network
        self.troe, self.effic = {}, {}
        self.irre_indx = 0 # the reaction index of the start of the irreversible reactions
        
        # the max change of the actinic flux (for convergence)
        # if photochemistry is off, the value remaines 0 for checking convergence
        self.aflux_change = 0.
        
        self.def_bin_min = 2. #20.
        self.def_bin_max = 800.1
        
        
        ### ### ### ### ### ### ### ### ### ### ###
        # List the names variables defined in op here!
        ### ### ### ### ### ### ### ### ### ### ###
        
        # User define what to save!
        self.var_save = ['k','y','ymix','y_ini','y_conden','t','dt','longdy','longdydt',\
        'atom_ini','atom_sum','atom_loss','atom_conden','aflux_change','Rf','t_time', 'y_time'] 
        if vulcan_cfg.use_photo == True: self.var_save.extend(['nbin','bins','dbin','tau','sflux','aflux','cross','cross_scat','cross_J', 'J_sp','wavelen','n_branch','br_ratio'])
        self.var_evol_save = []
        self.conden_re_list = []        
        

class AtmData(object):
    """
    store the data of atmospheric structure  
    """
    def __init__(self):
        self.pco = np.zeros(1)
        self.Tco = np.zeros(1)
        self.M = np.zeros(1)
        self.n_0 = np.zeros(1)
        
        self.sat_p = {}
        # condensation excluding non-gaseous species
        if vulcan_cfg.use_condense == True:
            self.exc_conden = [_ for _ in range(ni) if spec_list[_] not in vulcan_cfg.non_gas_sp]
        # TEST condensation excluding non-gaseous species

class Parameters(object):
    """
    store the overall parameters for numerical method and counters  
    """
    def __init__(self):
        self.nega_y = 0
        self.small_y = 0
        self.delta = 0
        self.count = 0
        self.nega_count =0
        self.loss_count = 0
        self.delta_count= 0
        self.end_case = 0
        self.solver_str = '' # for assigning the name of solver
        self.switch_final_photo_frq = False