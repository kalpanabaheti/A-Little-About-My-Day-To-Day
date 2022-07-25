from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


import sys
import numpy
import random
from numpy import zeros, float32
import pgmpy

def make_power_plant_net(): #power plant problems: "alarm","faulty alarm", "gauge","faulty gauge", "temperature". (for the tests to work.)
   
    BayesNet = BayesianModel()
    
    BayesNet.add_node('alarm') #a
    BayesNet.add_node('faulty alarm') #fa
    BayesNet.add_node('gauge') #g
    BayesNet.add_node('faulty gauge') #fg
    BayesNet.add_node('temperature') #t

    # Faulty alarm and gauge reading affects the alarm
    BayesNet.add_edge('faulty alarm','alarm')
    BayesNet.add_edge('gauge','alarm')

    # Faulty gauge and temperature affects the gauge
    BayesNet.add_edge('faulty gauge','gauge')
    BayesNet.add_edge('temperature','gauge')

    # High temperature can cause faulty gauge
    BayesNet.add_edge('temperature','faulty gauge')
    return BayesNet


def set_probability(bayes_net):
    """Set probability distribution for each node in the power plant system.
    Use the following as the name attribute: "alarm","faulty alarm", "gauge","faulty gauge", "temperature". (for the tests to work.)
    """
    # TODO: set the probability distribution for each node
    # P(T) = 20% and P(~T) = 80%
    cpd_a = TabularCPD('temperature', 2, values=[[0.8], [0.2]])

    # P(Fa) = 15% and P(~Fa) = 85%
    cpd_fa = TabularCPD('faulty alarm', 2, values=[[0.85], [0.15]])

    # P(Fg|T) = 80% and P(Fg|~T) 5%
    cpd_fgt = TabularCPD('faulty gauge', 2, values=[[0.95, 0.2], [0.05, 0.80]], evidence=['temperature'], evidence_card=[2])
    

    # P(G|Fg,T) = 20% and P(G|~Fg,T) = 95%
    # P(G|Fg,~T) = 80% and P(G|~Fg,~T) = 5%
    # vector FF,FT,TF,TT - [0.05,0.95,0.80,0.20]
    cpd_gfgt = TabularCPD('gauge', 2, values=[[0.95, 0.05, 0.20, 0.80],[0.05,0.95,0.80,0.20]], evidence=['faulty gauge', 'temperature'], evidence_card=[2, 2])

    
    # P(A|Fa,G) = 55% and P(A|~Fa,G) = 90%
    # P(A|Fa,~G) = 45% and P(A|~Fa,~G) = 10%
    # vector FF,FT,TF,TT - [0.10,0.90,0.45,0.55]
    cpd_afag = TabularCPD('alarm', 2, values=[[0.90, 0.10, 0.55, 0.45],[0.10,0.90,0.45,0.55]], evidence=['faulty alarm', 'gauge'], evidence_card=[2, 2])
    
    bayes_net.add_cpds(cpd_a, cpd_fa, cpd_fgt, cpd_gfgt, cpd_afag)

    return bayes_net
    

def get_alarm_prob(bayes_net):
    """Calculate the marginal 
    probability of the alarm 
    ringing in the 
    power plant system."""
    
    solver = VariableElimination(bayes_net)
    marginal_prob = solver.query(variables=['alarm'], joint=False)
    alarm_prob = marginal_prob['alarm'].values
    return alarm_prob[1]

def get_gauge_prob(bayes_net):
    """Calculate the marginal
    probability of the gauge 
    showing hot in the 
    power plant system."""
    
    solver = VariableElimination(bayes_net)
    marginal_prob = solver.query(variables=['gauge'], joint=False)
    gauge_prob = marginal_prob['gauge'].values
    return gauge_prob[1]


def get_temperature_prob(bayes_net):
    """Calculate the conditional probability 
    of the temperature being hot in the
    power plant system, given that the
    alarm sounds and neither the gauge
    nor alarm is faulty."""
    
    #In other words - 1 - P('temperature' = False | 'faulty alarm' = False, 'alarm' = True, 'faulty gauge'= False))
    solver = VariableElimination(bayes_net)
    conditional_prob = solver.query(variables=['temperature'],evidence={'faulty alarm':0,'alarm':1,'faulty gauge':0}, joint=False)
    temp_prob = conditional_prob['temperature'].values
    return temp_prob[1]


def get_game_network():
    """Create a Bayes Net representation of the game problem.
    Name the nodes as "A","B","C","AvB","BvC" and "CvA".  """
    
    BayesNet = BayesianModel()
    BayesNet.add_node('A') #a
    BayesNet.add_node('B') #b
    BayesNet.add_node('C') #c
    BayesNet.add_node('AvB') #a vs. b
    BayesNet.add_node('BvC') #b vs. c
    BayesNet.add_node('CvA') #c vs. a

    # A and B affect AvB
    BayesNet.add_edge('A','AvB')
    BayesNet.add_edge('B','AvB')

    # B and C affect BvC
    BayesNet.add_edge('B','BvC')
    BayesNet.add_edge('C','BvC')

    # C and A affect CvA
    BayesNet.add_edge('C','CvA')
    BayesNet.add_edge('A','CvA')
    
    prior = [[0.15],[0.45],[0.30],[0.10]]
    cpd_a = TabularCPD('A', 4, values=prior)
    cpd_b = TabularCPD('B', 4, values=prior)
    cpd_c = TabularCPD('C', 4, values=prior)
    
    condprob = {
        'w1': [0.1,0.1,0.8],
        'w2': [0.2,0.6,0.2],
        'w3': [0.15,0.75,0.1],
        'w4': [0.05,0.9,0.05],
        'w5': [0.6,0.2,0.2],
        'w6': [0.1,0.1,0.8],
        'w7': [0.2,0.6,0.2],
        'w8': [0.15,0.75,0.1],
        'w9': [0.75,0.15,0.1],
        'w10': [0.6,0.2,0.2],
        'w11': [0.1,0.1,0.8],
        'w12': [0.2,0.6,0.2],
        'w13': [0.9,0.05,0.05],
        'w14': [0.75,0.15,0.1],
        'w15': [0.6,0.2,0.2],
        'w16': [0.1,0.1,0.8]
    }
    
    vector = list()
    
    for i in range(3):
        
        sub_vec = list()
        for diff in range(1,17):
            
            key = 'w'+str(diff)
            val = condprob[key]
            sub_vec.append(val[i])
            
        vector.append(sub_vec)
        
    cpd_avb = TabularCPD('AvB', 3, values=vector, evidence=['A', 'B'], evidence_card=[4, 4])
    cpd_bvc = TabularCPD('BvC', 3, values=vector, evidence=['B', 'C'], evidence_card=[4, 4])
    cpd_cva = TabularCPD('CvA', 3, values=vector, evidence=['C', 'A'], evidence_card=[4, 4])
    
    BayesNet.add_cpds(cpd_a,cpd_b,cpd_c,cpd_avb,cpd_bvc,cpd_cva)
    
    return BayesNet
    


def calculate_posterior(bayes_net):
    """Calculate the posterior distribution of the BvC match given that A won against B and tied C. 
    Return a list of probabilities corresponding to win, loss and tie likelihood."""
    posterior = [0,0,0]
    
    #In other words - P('BvC' = 0 | 'AvB' = 0, 'CvA' = 2)
    solver = VariableElimination(bayes_net)
    conditional_prob = solver.query(variables=['BvC'],evidence={'AvB': 0, 'CvA': 2}, joint=False)
    prob = conditional_prob['BvC'].values
    posterior[0]=prob[0]
    posterior[1]=prob[1]
    posterior[2]=prob[2]
    print(posterior)
    
    return posterior # list    
    
    
def get_ind1(node,x):
    
    if x <= node[0]:
        return 0
    elif x > node[0] and x <= (node[0] + node[1]):
        return 1
    elif x > (node[0] + node[1]) and x <= (node[0] + node[1] + node[2]):
        return 2
    elif x > (node[0] + node[1] + node[2]) and x <= (node[0] + node[1] +node[2] + node[3]):
        return 3
    
    
def get_ind2(node,x):
    
    if x <= node[0]:
        return 0
    elif x > node[0] and x <= (node[0] + node[1]):
        return 1
    elif x > (node[0] + node[1]) and x <= (node[0] + node[1] + node[2]):
        return 2
    
    
def transform(node):
    
    a = node.T

    for i in a:

        for j in i:

            temp = j[0]
            j[0] = j[1]
            j[1] = temp
            
    return a


def get_initstate(bayes_net):
    
    initial_state = [0,0,0,0,0,0]
    
    A_cpd = bayes_net.get_cpds("A")
    A_node = A_cpd.values
    B_cpd = bayes_net.get_cpds("B")
    B_node = B_cpd.values
    C_cpd = bayes_net.get_cpds("C")
    C_node = C_cpd.values
    
    AvB_cpd = bayes_net.get_cpds("AvB")
    AvB_node = transform(AvB_cpd.values)
    BvC_cpd = bayes_net.get_cpds("BvC")
    BvC_node = transform(BvC_cpd.values)
    CvA_cpd = bayes_net.get_cpds("CvA")
    CvA_node = transform(CvA_cpd.values)

    x = random.uniform(0,1)
    initial_state[0] = get_ind1(A_node,x)     

    x = random.uniform(0,1)
    initial_state[1] = get_ind1(B_node,x)     

    x = random.uniform(0,1)
    initial_state[2] = get_ind1(C_node,x)     

    # Fix AvB to 0
    initial_state[3] = 0

    # Fix CvA to 2
    initial_state[5] = 2

    t_node = []
    sample = initial_state
    
    x = random.uniform(0,1)
    i0 = A_node[sample[0]] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[sample[0],sample[1],sample[3]]\
                * BvC_node[sample[1],sample[2],0] * CvA_node[sample[2],sample[0],sample[5]]
    i1 = A_node[sample[0]] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[sample[0],sample[1],sample[3]]\
                * BvC_node[sample[1],sample[2],1] * CvA_node[sample[2],sample[0],sample[5]]
    i2 = A_node[sample[0]] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[sample[0],sample[1],sample[3]]\
                * BvC_node[sample[1],sample[2],2] * CvA_node[sample[2],sample[0],sample[5]]
    
    t_node.append(i0/(i0+i1+i2))
    t_node.append(i1/(i0+i1+i2))
    t_node.append(i2/(i0+i1+i2))
                  
    initial_state[4] = get_ind2(t_node,x)
    

    return initial_state

    

def Gibbs_sampler(bayes_net, initial_state): #Gibbs single iteration
    
    if len(initial_state) == 0:
        initial_state = get_initstate(bayes_net)
        
    
    sample = initial_state
    
    #index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
    A_cpd = bayes_net.get_cpds("A")
    A_node = A_cpd.values
    B_cpd = bayes_net.get_cpds("B")
    B_node = B_cpd.values
    C_cpd = bayes_net.get_cpds("C")
    C_node = C_cpd.values
    
    #index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)
    AvB_cpd = bayes_net.get_cpds("AvB")
    AvB_node = transform(AvB_cpd.values)
    BvC_cpd = bayes_net.get_cpds("BvC")
    BvC_node = transform(BvC_cpd.values)
    CvA_cpd = bayes_net.get_cpds("CvA")
    CvA_node = transform(CvA_cpd.values)
    
    
    t_node = []
    numbers = list(range(0,3)) + list(range(4,5))
    r = random.choice(numbers)

    if r == 0:
        
        i0 = A_node[0] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[0,sample[1],sample[3]]\
                    * CvA_node[sample[2],0,sample[5]]
        i1 = A_node[1] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[1,sample[1],sample[3]]\
                    * CvA_node[sample[2],1,sample[5]]
        i2 = A_node[2] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[2,sample[1],sample[3]]\
                    * CvA_node[sample[2],2,sample[5]]
        i3 = A_node[3] * B_node[sample[1]] * C_node[sample[2]] * AvB_node[3,sample[1],sample[3]]\
                    * CvA_node[sample[2],3,sample[5]]
        
        x = random.uniform(0,1)
        t_node.append(i0/(i0+i1+i2+i3))
        t_node.append(i1/(i0+i1+i2+i3))
        t_node.append(i2/(i0+i1+i2+i3))
        t_node.append(i3/(i0+i1+i2+i3))
        samp_indx = get_ind1(t_node,x)
        sample[0] = samp_indx
        
    elif r == 1:
        
        i0 = A_node[sample[0]] * B_node[0] * C_node[sample[2]] * AvB_node[sample[0],0,sample[3]]\
                    * BvC_node[0,sample[2],sample[4]] 
        i1 = A_node[sample[0]] * B_node[1] * C_node[sample[2]] * AvB_node[sample[0],1,sample[3]]\
                    * BvC_node[1,sample[2],sample[4]] 
        i2 = A_node[sample[0]] * B_node[2] * C_node[sample[2]] * AvB_node[sample[0],2,sample[3]]\
                    * BvC_node[2,sample[2],sample[4]] 
        i3 = A_node[sample[0]] * B_node[3] * C_node[sample[2]] * AvB_node[sample[0],3,sample[3]]\
                    * BvC_node[3,sample[2],sample[4]]
        
        x = random.uniform(0,1)
        t_node.append(i0/(i0+i1+i2+i3))
        t_node.append(i1/(i0+i1+i2+i3))
        t_node.append(i2/(i0+i1+i2+i3))
        t_node.append(i3/(i0+i1+i2+i3))
        samp_indx = get_ind1(t_node,x)
        sample[1] = samp_indx
        
    elif r == 2:
        
        i0 = A_node[sample[0]] * B_node[sample[1]] * C_node[0]\
                    * BvC_node[sample[1],0,sample[4]] * CvA_node[0,sample[0],sample[5]]
        i1 = A_node[sample[0]] * B_node[sample[1]] * C_node[1]\
                    * BvC_node[sample[1],1,sample[4]] * CvA_node[1,sample[0],sample[5]]
        i2 = A_node[sample[0]] * B_node[sample[1]] * C_node[2]\
                    * BvC_node[sample[1],2,sample[4]] * CvA_node[2,sample[0],sample[5]]
        i3 = A_node[sample[0]] * B_node[sample[1]] * C_node[3]\
                    * BvC_node[sample[1],3,sample[4]] * CvA_node[3,sample[0],sample[5]]
    
        x = random.uniform(0,1)
        t_node.append(i0/(i0+i1+i2+i3))
        t_node.append(i1/(i0+i1+i2+i3))
        t_node.append(i2/(i0+i1+i2+i3))
        t_node.append(i3/(i0+i1+i2+i3))
        samp_indx = get_ind1(t_node,x)
        sample[2] = samp_indx
        
    elif r == 4:
        
        # The random variable to update is 'BvC'
        i0 = B_node[sample[1]] * C_node[sample[2]] * BvC_node[sample[1],sample[2],0]
        i1 = B_node[sample[1]] * C_node[sample[2]] * BvC_node[sample[1],sample[2],1]
        i2 = B_node[sample[1]] * C_node[sample[2]] * BvC_node[sample[1],sample[2],2]
        
        x = random.uniform(0,1)
        t_node.append(i0/(i0+i1+i2))
        t_node.append(i1/(i0+i1+i2))
        t_node.append(i2/(i0+i1+i2))
        samp_indx = get_ind2(t_node,x)
        sample[4] = samp_indx

    sample = tuple(sample)
    #Returns new state sampled from the probability distribution 
    return sample
        
    
    raise NotImplementedError
    


def MH_sampler(bayes_net, initial_state): #MH single iteration
  
    if len(initial_state) == 0:
        initial_state = get_initstate(bayes_net)
        
    oSample = initial_state  
    nSample = []             
    fSample = initial_state  
    
    #index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
    A_cpd = bayes_net.get_cpds("A")
    A_node = A_cpd.values
    B_cpd = bayes_net.get_cpds("B")
    B_node = B_cpd.values
    C_cpd = bayes_net.get_cpds("C")
    C_node = C_cpd.values
    
    #index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)
    AvB_cpd = bayes_net.get_cpds("AvB")
    AvB_node = transform(AvB_cpd.values)
    BvC_cpd = bayes_net.get_cpds("BvC")
    BvC_node = transform(BvC_cpd.values)
    CvA_cpd = bayes_net.get_cpds("CvA")
    CvA_node = transform(CvA_cpd.values)
    
   
    t_node = []
    a = random.randint(0,3)
    b = random.randint(0,3)
    c = random.randint(0,3)
    bvc = random.randint(0,2)
    nSample = [a,b,c,0,bvc,2] 

    old = A_node[oSample[0]] * B_node[oSample[1]] * C_node[oSample[2]] * AvB_node[oSample[0],oSample[1],oSample[3]]\
                * BvC_node[oSample[1],oSample[2],oSample[4]] * CvA_node[oSample[2],oSample[0],oSample[5]]
    
    new = A_node[nSample[0]] * B_node[nSample[1]] * C_node[nSample[2]] * AvB_node[nSample[0],nSample[1],nSample[3]]\
                * BvC_node[nSample[1],nSample[2],nSample[4]] * CvA_node[nSample[2],nSample[0],nSample[5]]

    
    #Returns new state sampled from the probability distribution 
    if new > old:
        fSample = nSample
    else:
        
        alpha = min(1, new / old)
        u = random.uniform(0,1)
        if u < alpha:
            
            fSample = nSample
            
        else:
            #burn in here
            fSample = oSample
                
    sample = tuple(fSample)

    return sample
 
    
    
def gibbs_iter(bayes_net, initial_state, delta, G):
    
    burn_in = 67000
    Gibbs_count = 0
    sample = initial_state
    BvC_Cnt = [0,0,0]
    nCnt = 0
    nItr = 0
    
    p0 = float('-inf')
    p1 = float('-inf')
    p2 = float('-inf')
    
    c0 = 0
    c1 = 0
    c2 = 0
    
    for i in range(0,500000):
        
        sample = Gibbs_sampler(bayes_net, sample)
        sample = list(sample)
        
        if sample[4] == 0:
            BvC_Cnt[0] += 1
        elif sample[4] == 1:
            BvC_Cnt[1] += 1
        elif sample[4] == 2:
            BvC_Cnt[2] += 1
            
        if i<burn_in:
            continue

        c0 = float(BvC_Cnt[0]) / (i+1)
        c1 = float(BvC_Cnt[1]) / (i+1)
        c2 = float(BvC_Cnt[2]) / (i+1)
        d1 = abs(c0 - p0)
        d2 = abs(c1 - p1)
        d3 = abs(c2 - p2)
        if (d1 != 0 and d1 < delta) and \
            (d2 != 0 and d2 < delta) and \
            (d3 != 0 and d3 < delta):                
            if (i - nItr) == 1:
                nCnt += 1
            nItr = i

            if nCnt >= G:
                Gibbs_convergence = [c0, c1, c2]
                Gibbs_count = i+1
                return Gibbs_convergence, Gibbs_count
            
        p0 = c0
        p1 = c1
        p2 = c2
    
    return [0,0,0],0


def MH_iter(bayes_net, initial_state, delta, M):
    
    burn_in = 67000
    MH_count = 0
    MH_rejection_count = 0
    sample = initial_state
    BvC_Cnt = [0,0,0]
    nCnt = 0
    nItr = 0
    # old distribution
    p0 = float('-inf')
    p1 = float('-inf')
    p2 = float('-inf')
    # current distribution
    c0 = 0
    c1 = 0
    c2 = 0
    pSample = []
    
    for i in range(0,500000):
        
        pSample = sample[:]
        sample = MH_sampler(bayes_net, sample)
        sample = list(sample)
        if sample == pSample:
            MH_rejection_count += 1
        if sample[4] == 0:
            BvC_Cnt[0] += 1
        elif sample[4] == 1:
            BvC_Cnt[1] += 1
        elif sample[4] == 2:
            BvC_Cnt[2] += 1
            
        if i<burn_in:
            continue

        c0 = float(BvC_Cnt[0]) / (i+1)
        c1 = float(BvC_Cnt[1]) / (i+1)
        c2 = float(BvC_Cnt[2]) / (i+1)
        d1 = abs(c0 - p0)
        d2 = abs(c1 - p1)
        d3 = abs(c2 - p2)
        if (d1 != 0 and d1 < delta) and \
            (d2 != 0 and d2 < delta) and \
            (d3 != 0 and d3 < delta):                
            if (i - nItr) == 1:
                nCnt += 1
            nItr = i

            if nCnt >= M:
                MH_convergence = [c0, c1, c2]
                MH_count = i+1
                return MH_convergence, MH_count, MH_rejection_count

        p0 = c0
        p1 = c1
        p2 = c2
    
    return [0,0,0],0,0
    

def compare_sampling(bayes_net, initial_state): #gibbs vs. Metropolis
   
    
    Gibbs_convergence = [0,0,0] # posterior distribution of the BvC match as produced by Gibbs 
    MH_convergence = [0,0,0] # posterior distribution of the BvC match as produced by MH
    G = 10000
    M = 10000
    delta = 0.0001
    
    Gibbs_convergence, Gibbs_count = gibbs_iter(bayes_net, initial_state, delta, G)
    
    MH_convergence, MH_count, MH_rejection_count = MH_iter(bayes_net, initial_state, delta, M)
    
    print(Gibbs_convergence, Gibbs_count)
    print(MH_convergence, MH_count, MH_rejection_count)
    
    return Gibbs_convergence, MH_convergence, Gibbs_count, MH_count, MH_rejection_count
    
    raise NotImplementedError        
    

def sampling_question():
    """Question about sampling performance."""
    
    choice = 2
    options = ['Gibbs','Metropolis-Hastings']
    factor = 0
    
    gCon, mhCon, gCnt, mhCnt, mhRcnt = compare_sampling(get_game_network(),[])
    print('Gibbs Sample')
    print(gCon)
    print(gCnt)
    if gCnt < mhCnt:
        choice = 0
        factor = mhCnt / (gCnt * 1.0)
    else:
        choice = 1
        factor = gCnt / (mhCnt * 1.0)
  
    print('MH Sample')
    print(mhCon)
    print(mhCnt)
    print('MH Rejection Count : ',mhRcnt)

    print('choice : ',options[choice])
    print('factor : ',factor)

    return options[choice], factor



