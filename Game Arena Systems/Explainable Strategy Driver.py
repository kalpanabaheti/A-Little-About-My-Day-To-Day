#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipynb.fs.full.Feedback_Framework import *
from ipynb.fs.full.Pulls import *


# In[2]:


#What do you want? Give it in form of game-element:{features - default at first - None if it doesn't apply}
'''
default = [unit_type,
           team, 
           location,
           is_alive,
           level,
           mana,
           bounty,
           auto =  [speed, 
                    attack_type, 
                    attack_range, 
                    attack_target_handle,
                    can_move,
                    can_attack_with,
                    can_be_attacked_by,
                   ],
          attack_order 
          ]
          
states = {
            player_in_question,
            dota_time:{
                        game_element:{
                                        features_dict
                                     }
                      }
         }
'''


# In[3]:


level_xp_map = {
    
    '1':0,
    '2':230,
    '3':600,
    '4':1080,
    '5':1660,
    '6':2260,
    '7':2980,
    '8':3730,
    '9':4620,
    '10':5550,
    '11':6520,
    '12':7530,
    '13':8580,
    '14':9805,
    '15':11055,
    '16':12330,
    '17':13630,
    '18':14955,
    '19':16455,
    '20':18045,
    '21':19645,
    '22':21495,
    '23':23595,
    '24':25945,
    '25':28545,
    '26':32045,
    '27':36545,
    '28':42045,
    '29':48545,
    '30':56045
}



def extract_player_pos(unit):
    if not unit.location.x:
        return None
    return (unit.location.x, unit.location.y)

def extract_mana_fraction(unit):
    if unit.mana_max==0:
        return None
    return unit.mana/unit.mana_max

def get_xp(unit):
    
    try:
        level = unit.level
        to_add = unit.xp_needed_to_level
        level_xp = level_xp_map[str(level)]
        total_xp = int(level_xp) + int(to_add)

        return total_xp
    
    except:
        return 0

def get_gold(unit):
    
    try:
        rel = unit.reliable_gold
        unrel = unit.unreliable_gold
        total_gold = int(rel) + int(unrel)

        return total_gold
    
    except:
        return 0

# This is a dictionary of short_name: feature_extrator, which is a funciton
# that takes a CMsgbBotWorldState.Unit and returns a feature we care about
# or None if that feature isn't present
feature_extractors = {
    "unit_type":lambda unit: unit.unit_type,
    "team_id": lambda unit: unit.team_id,
    "is_alive":lambda unit: unit.is_alive,
    "location":lambda unit: extract_player_pos(unit),
    "level":lambda unit: unit.level,
    "mana_fraction":lambda unit: extract_mana_fraction(unit),
    "xp":lambda unit: unit.bounty_xp,
    "current_movement_speed":lambda unit: unit.current_movement_speed*0.85,
    "attack_damage":lambda unit: unit.attack_damage,
    "attack_range":lambda unit: unit.attack_range,    
    "attack_acquisition_range": lambda unit: unit.attack_acquisition_range,
    "attack_target_handle":lambda unit: unit.attack_target_handle,
    "name":lambda unit: unit.name,
    "handle":lambda unit: unit.handle,
    "xp":lambda unit: get_xp(unit),
    "gold":lambda unit: get_gold(unit),
    "last_hits":lambda unit: unit.last_hits,
    "is_illusion":lambda unit: unit.is_illusion,
    "active_ability_handle":lambda unit: unit.active_ability_handle
    
}


# In[4]:


elements = [4,3]
default_outer = ['active_ability_handle','name','handle','unit_type','is_illusion','team_id','is_alive','location','level','mana_fraction','gold','xp','attack_acquisition_range','last_hits'] #player_ids for players, unit_types for all else
default_inner = ['attack_damage','attack_range','attack_target_handle','attack_range']
my_file = None

def reset_connection(filename):
    
    global my_file
    import hmnparser
    from hmnparser import HMNParser
 
    my_file = HMNParser(filename)
    match_metadata = my_file.get_match_meta()
    print("Connection reset!")


def reset_variables():
    
    global states
    global elements
    global default_outer
    global default_inner
    
    print("Global variables reset!")


# In[5]:



def get_time(tick):
    
    time = tick.radiantstate.dota_time
    if time>0:
        return str(time)

    return False
    
    
def get_player_in_question(player_id):
    
    global elements
    
    if 1 not in elements:
        elements.append(1)
        
    return player_id


def get_inner_features(unit, inn = default_inner):
   
    d = dict()
    
    for name, extractor in feature_extractors.items():
        if name in inn:
            feature = extractor(unit)
            if feature is not None or feature is not False:
                d[name] = feature
            
    return d


def get_features(unit, out = default_outer, inn = default_inner):
 
    d = dict()
    
    for name, extractor in feature_extractors.items():
        if name in out:
            feature = extractor(unit)
            if feature is not None or feature is not False:
                d[name] = feature
                
    d['auto'] = get_inner_features(unit, inn)

    return d


def get_element_ids(units, e = elements):
    
    ids = []
    
    for unit in units:
        
        t = unit.unit_type
        
        if t in e and t != 1:
            
            ids.append(unit.handle)
            
        elif t in e and t == 1:
            
            ids.append(unit.player_id)
            
    return ids


def construct_state(tick, player):

    global elements
    global default_outer
    global default_inner
    
    timestamp = get_time(tick)
    
    
    if player < 5:
        team_units = tick.radiantstate.units
    else:
        team_units = tick.direstate.units
    
    
    d = dict()
    parts = get_element_ids(team_units, elements)
    
    for unit in team_units:
        
        if (unit.handle in parts):
            
            key = unit.handle
            
            features = get_features(unit, default_outer, default_inner)
            
            d[str(key)] = features
            
        elif (unit.player_id in parts) and ('hero' in unit.name):
            
            key = unit.player_id
            
            features = get_features(unit, default_outer, default_inner)
            
            d[str(key)] = features
            
    l = [timestamp, d]
    return l


# In[6]:



def invoke_data(file, player):
    
    if player>=5:
        side = 'dire team'
    else:
        side = 'radiant team'
    
    filename = 'C:\\Users\\kalpa\\Downloads\\Testing HMN files\\train-'+str(file)+'.hmn.bz2'

    reset_connection(filename)
    reset_variables()
    
    state_dict = dict()
    states = list()

    player = get_player_in_question(player)
    states.append(player)
    
    i = 0

    while True:

        try:

            tick = my_file.get_tick()
            time = get_time(tick)

        except:

            break

        if time!=False:

            tick_state = construct_state(tick, player)
            timestamp = int(float(tick_state[0]))
            state = tick_state[1]
            states.append(tick_state)
            state_dict[str(timestamp)]=state

        i += 1
        if float(time) > 700.00:
            break

    
    print("\n",file," ",side," Processed!")
    print("Done! -ticks, states: ",i,len(states)-1)
    return states, state_dict


# In[7]:


class SubstateCollection:
    
  
    def __init__(self, player, states, state_dict):
        
        self.substates = []
        self.totalsubstateno = 3
        self.totalstatelim = float(15)
        self.timelimpergoal = float(3)
        self.fulfilled = []
        self.prospects = []
        self.exceptions = []
        self.elements = []
        self.player = player
        self.raw_feedback = []
        self.feedback = []
        self.without_farm = []
        self.stack = []
        self.states = states
        self.state_dict = state_dict
        
        
        
    def store_prospective_states(self):
        
        states = self.states
        state_dict = self.state_dict
        
        player = self.player #states[0]
        hero = 0
        
        for i in range(2,len(states)):
            
            state = states[i][1]
            y = i-self.totalsubstateno
            limit = (int(y) if y>0 else 0)
            trail = states[i-1:limit:-1]
            record = False
            flag = 0
            
            for subgoalID, evaluator in PossibleStates.items():
            
                elem_set = self.elements
                stateID = evaluator[0](state, trail, player, elem_set)
                
                if stateID[0]!=False:
                    
                    self.elements = stateID[2]
                    #print(self.elements)
                    
                    state_info = [subgoalID, states[i][0],i]
                    hero = stateID[1]
                    
                    
                    #if len(self.substates)==0 or (len(self.substates)>0 and (self.substates[-1][0]=='3' and state_info[0]=='1' or (self.substates[-1][0]!=state_info[0] and self.substates[-1][0]!='3'))):
                        #self.substates.append(state_info)
                    
                    if len(self.substates)!=0:
                        if (self.substates[-1][0]=='3' and state_info[0]!='3') or self.substates[-1][0]!='3':
                            self.substates.append(state_info)
                    else:
                        self.substates.append(state_info)
                
                        
            #self.elements = update_elements(state, self.elements)
                    
            
        #print(len(self.substates))
        if hero!=0:
            print('\n',hero)
        #print(self.substates)
                    


    def clean_stateset(self):
        
        states = self.states
        state_dict = self.state_dict
        
        self.store_prospective_states()
        
        limit = self.totalstatelim

        sequence = self.substates

        i = 0
        while i<len(sequence)-1:

            if sequence[i][0]=='3':

                #print(sequence[i])

                s = [sequence[i]]
                j = i
                while j>-1:

                    if j-1!=-1 and int(sequence[j-1][0])<=int(sequence[j][0]) and float(sequence[j-1][1])-float(sequence[i][1])<=limit and sequence[j][0]!='1':

                            s = [sequence[j-1]] + s
                            #print("adding: ",sequence[j-1])

                    else:
                            break

                    j -= 1


                #print("s: ",s)
                if s[0][0]=='1':

                    self.fulfilled.append(s) #start and end time of successful pull
                    sequence = sequence[:j] + sequence[i+1:]
                    #print("fulfilled: ",self.fulfilled)
                    #print("new seq: ",sequence)
                    i = j

                else:
                    
                    self.exceptions.append(s[-1][1]) #time when pull succeeded without strategy
                    sequence = sequence[:i] + sequence[i+1:]
                    #print("exceptions: ",self.exceptions)
                    #print("new seq: ",sequence)

            else:

                i += 1



        i = 0
        while i<len(sequence)-2:

            if sequence[i][0]=='1':

                s = [sequence[i]]
                j = i
                while j<len(sequence)-1:

                    if j+1!=len(sequence) and int(sequence[j+1][0])>=int(sequence[j][0]) and float(sequence[j+1][1])-float(sequence[i][1])<=limit and sequence[j][0]!='2':

                            s += [sequence[j+1]]
                            #print("adding: ",sequence[j+1])

                    else:
                        
                            break

                    j += 1


                #print("s: ",s)
                if len(s)>1:

                    self.prospects.append(s)
                    sequence = sequence[:i] + sequence[j+1:]
                    #print("new seq: ",sequence)

                else:
                    
                    i+=1

            else:

                i += 1

        #print("\nprospects: ",self.prospects)
        
        
    def clean_prospects(self):
        
        #print(self.prospects)
        
        states = self.states
        state_dict = self.state_dict
        
        limit = self.totalstatelim
        
        final_list = []
        
        for i in self.prospects:
            
            count = 0
            time0 = float(i[0][1])
            state0 = i[0][0]
            l = []
            
            for j in range(len(i)):
                
                if count == 0:
                    count = 1
                    l.append(i[j])
                    continue
                    
                time = float(i[j][1])
                state = i[j][0]

                if state!=i[j-1][0] and time <= time0 + 10.0:

                    l.append(i[j])

                elif time > time0 + 10.0:

                    break
                    
            final_list.append(l)
        
        self.prospects = final_list
        
        
        prev = 0.0
        f = self.prospects
        i = 0
        
        while i < len(f):
            
            current = float(f[i][0][1])
            if current <= prev + float(10):
                
                f = f[:i]+f[i+1:]
                
            else:
                
                prev = float(f[i][-1][1])
                i += 1
           
        self.prospects = f
        
        
        if self.prospects!=[]:
            print("\nprospects: ",self.prospects,'\n')
        
            
            
    def clean_fulfilled(self):
        
        states = self.states
        state_dict = self.state_dict
        
        prev = 0.0
        f = self.fulfilled
        i = 0
        
        while i < len(f):
            
            current = float(f[i][0][1])
            if current <= prev + float(2) or current==float(f[i][1][1]):
                
                f = f[:i]+f[i+1:]
                
            else:
                
                prev = float(f[i][-1][1])
                i += 1
                
        self.fulfilled = f
        if self.fulfilled!=[]:
            print("\nfulfilled: ")
            for i in self.fulfilled:
                print(i[0][1]," - ",i[-1][1],"\n")
                
                
    def farm_check(self):
        
        states = self.states
        state_dict = self.state_dict
        
        self.without_farm = []
        
        for i in self.prospects:
            
            if i[-1][0]=='1':
                cutoff = float(i[0][1])+15.0
                player = str(self.player)
                index = i[0][2]
                
                try:

                    farm = last_hit_check(states,index,cutoff,player)
                    if farm == False:
                        self.without_farm.append(i)
                    
                except:
                    
                    print("Cancelled Case")

        self.prospects = self.without_farm
        
        
    def remove_illusion(self):
        
        states = self.states
        state_dict = self.state_dict
        
        temp = []
        
        for i in self.prospects:
            
            if i[-1][0]=='1':
                cutoff = float(i[0][1])+15.0
                player = str(self.player)
                index = i[0][2]

                illusion = (states,index,cutoff,player)
                if illusion == False:
                    temp.append(i)
                    

        self.prospects = temp
            
            
    def stack_check(self):
        
        states = self.states
        state_dict = self.state_dict
        
        self.stack = []
        
        for i in self.prospects:
            
            if i[-1][0]=='1':
                cutoff = float(i[0][1])+15.0
                player = str(self.player)
                index = i[0][2]

                s = stacking(states,index,cutoff,player)
                if s == True:
                    self.stack.append(i)
                    

        if self.stack!=[]:
            temp = []
            print("\nStacks:\n")
            for i in self.prospects:
                if i in self.stack:
                    print(i)
                else:
                    temp.append(i)
        
            self.prospects = temp
    
                

    
    def safe_assessment(self): 
        
        states = self.states
        state_dict = self.state_dict
        
        jump = self.timelimpergoal
        feedback = []
        hero = 'you '
        
        try:
            hero = get_name(states[1][1][str(self.player)])
            #print(hero)
        except:
            print("\nHERO ",self.player,"DOES NOT EXIST!")
            return
        
        for i in self.prospects:
                
            last_time = float(i[-1][1])
                    
            last_state = i[-1][0]
                    
            next_time = str(int(float(last_time)+jump))
            
            index = i[0][2]

            #next_state = state_dict[next_time]
            check_state = str(int(last_state)+1)

            interval = (i[0][1],str(float(next_time)+3.00))

            check = CheckStates[check_state][0]
            reset = ResetSwitch[check_state][0]
                
            switch = reset([],hero)

            for the_time in range(int(last_time),int(next_time)+1):
                
                next_state = state_dict[str(the_time)]
                the_false = check(next_state, [], self.player, [], hero, switch)
                switch = the_false[1]
                
                
            raw_feed = switch

            pack = [interval,raw_feed, index]
            feedback.append(pack)
                

                    
        self.raw_feedback = feedback
        '''
        if self.raw_feedback!=[]:
            print("\nRaw Feed: \n")
            for i in self.raw_feedback:

                print(i,"\n")
        '''
             
                
        
    def scripting(self,farm=0): #if farm is assigned to 1, then all farm cases will be removed for feedback
        
        states = self.states
        state_dict = self.state_dict
        
        if farm == 0:
            temp = self.raw_feedback
            print('\nWith Farms Included -\n')
        
        elif farm!=0:
            print('\nWithout Farming Instances -\n')
            temp = self.raw_feedback
            if temp == []:
                print('\nNO INSTANCES!\n')
                return 
        
        l = []
        for i in temp:
            
            switch = i[1]
            t1 = i[0][0]
            t2 = i[0][1]
            print(i[0],'\n')
                
            intro = construct_intro()
            print('\n',intro)
            phrase_set = construct_feedback(switch)
            #print(phrase_set)
            feedback = intro+"\n"
            for p in phrase_set:
                feedback += p
                print("\n",p,'\n')
                
            tup = [self.player,t1,t2,feedback]
            l.append(tup)
            
        return l
                
        
                
        
    


# In[8]:


#testing functions

#file = 6098289305
def evaluate(file):
    
    csv_dump = []
    
    states, state_dict = invoke_data(file,0)
    
    for i in range(5):
        print(i,'\n')
        collect = SubstateCollection(i, states, state_dict)
        #collect.store_prospective_states()
        collect.clean_stateset()
        collect.clean_prospects()
        collect.farm_check()
        collect.stack_check()
        #collect.remove_illusion()
        collect.clean_fulfilled()
        collect.safe_assessment()
        if collect.raw_feedback!=[]:
            #collect.scripting(0)
            feed = collect.scripting(1)
            for x in feed:
                x.insert(0,str(file))
                csv_dump.append(x)
            

    states, state_dict = invoke_data(file,5)
    
    
    for i in range(5, 10):
        print(i,'\n')
        collect = SubstateCollection(i, states, state_dict)
        #collect.store_prospective_states()
        collect.clean_stateset()
        collect.clean_prospects()
        collect.farm_check()
        collect.stack_check()
        #collect.remove_illusion()
        collect.clean_fulfilled()
        collect.safe_assessment()
        if collect.raw_feedback!=[]:
            #collect.scripting(0)
            feed = collect.scripting(1)
            for x in feed:
                x.insert(0,str(file))
                csv_dump.append(x)
        
            
    
    
    print("\n",file," is DONE...")
    print('\n\n\n')
    return csv_dump

file = sys.argv[1]
csv_dump = evaluate(file)


# In[11]:


import csv
from csv import reader
import pandas as pd

import os.path
from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

if os.path.isfile('DotaPulls.csv'):
    print ("Opening DotaPulls...")
    
else:
    
    Details = ['GameID', 'playerNO', 'StartTime', 'EndTime','Feedback']  
    
    with open('DotaPulls.csv', 'w') as f: 
        write = csv.writer(f) 
        write.writerow(Details) 
        
if csv_dump!=[]:
    
    df = pd.read_csv('DotaPulls.csv', delimiter=',')
    list_of_rows = [list(row)[:-1] for row in df.values]
    #list_of_rows.insert(0, df.columns.to_list())
     
    rows = csv_dump
    print(len(rows))
    '''
    with open('DotaPulls.csv', 'a') as f: 
        write = csv.writer(f) 
    '''
    for row in rows:
        if list(row[:-1]) not in list_of_rows:
            append_list_as_row('DotaPulls.csv', row) #write.writerow(row)
    
    print(list_of_rows)
    print(len(list_of_rows))

