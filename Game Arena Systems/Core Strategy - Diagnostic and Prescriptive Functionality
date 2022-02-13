#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic Functions

def dist(tuple1,tuple2):
    
    x1 = tuple1[0]
    y1 = tuple1[1]
    x2 = tuple2[0]
    y2 = tuple2[1]
    
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return abs(d)

def dist_line(tuple1,line):
    #blah blah
    return 

def chain_aggro(state, elem_set, creep_val):
    
    the_type = creep_val['unit_type']
    aggro = creep_val['attack_acquisition_range']
    
    for key, val in state.items():
        
        if val['unit_type']==the_type and dist(creep_val['location'],val['location'])<=2*aggro and (key not in elem_set) and val['is_alive']==True:
            
            elem_set.append(int(key))
            
    elem_set = list(set(elem_set))
            
            
def reset(switch, attribute, case, priority, elements, actions): #element order as per feedback rules
    
    l = [priority,(attribute,case), elements, actions]
    if l not in switch:
        switch.append(l)
    
    return switch
    
def remove(switch, attr_case, priority):
    
    i = 0
    while i < len(switch):
        
        if switch[i][1]==attr_case and switch[i][0]==priority:
            s = switch.pop(i)
        else:
            i += 1
            
    return switch

def get_name(h):
    
    hero = h['name']
    
    if "hero" in hero:
        hero = hero.split("hero_")
        hero = hero[1]
    
    
    new = hero.replace("_"," ")
    return new
   


# In[1]:



#THE PULL FUNCTION 1 - Provoking the jungle creep(s)

   
def pull_reset1(switch, name):
    
    switch = reset(switch, 'unit_type', 'absence', 1, ['you','the jungle creep'],['attacked'])
    switch = reset(switch, 'attack_target_handle', 'absence', 2, ['you','the jungle creep'],['targetted for attack'])
        
    return switch

def pull_reset2(switch, name):
    
    switch = reset(switch, 'unit_type', 'absence', 1, ['you','the lane creep'],['aggro-ed'])
    switch = reset(switch, 'unit_type', 'absence', 2, ['the jungle creep','you'],['attacked'])
    switch = reset(switch, 'location', 'wrong_place', 2, ['you','the lane creep'],['attempted to aggro'])
    switch = reset(switch, 'location', 'wrong_place', 3, ['you','the jungle creep'],["baited the jungle creep onslaught"])
    switch = reset(switch, 'attack_target_handle', 'absence', 4, ['the jungle creep','you'],['targetted for attack'])
   
    return switch

def pull_reset3(switch, name):
    
    switch = reset(switch, 'unit_type', 'absence', 1, ['the jungle creep camp', 'the lane creep camp'],['battled'])
    switch = reset(switch, 'unit_type', 'absence', 2, ['the lane creep','the jungle creep'],['attacked'])
    switch = reset(switch, 'unit_type', 'wrong_type', 3, ['the jungle creeps','the lane creep camp'],['suffered an attack'])
    
    return switch
        

def pull_check1(state, trail, player, elem_set, hero_name, switch):
    
    #switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]
        #name = get_name(hero_name)
        
        #switch = reset(switch, 'unit_type', 'absence', 1, [str(name),'jungle creep'],['attacked'])
        #switch = reset(switch, 'attack_target_handle', 'absence', 2, [str(name),'jungle creep'],['targetted for attack'])
        
        jungle_creep = None
        for key, val in state.items():
            
            flag1 = False
            #switch = reset(switch, 'unit_type', 'absence', 1, [str(name),'jungle creep'],['attacked'])
            
            flag2 = False
            #switch = reset(switch, 'attack_target_handle', 'absence', 2, [str(name),'jungle creep'],['targetted for attack'])
            
            flag3 = False

            if val['unit_type']==4:
                
                flag1 = True
                switch = remove(switch, ('unit_type','absence'), 1)
            
                if hero['auto']['attack_target_handle']==int(key): 
                    
                    flag2 = True
                    switch = remove(switch, ('attack_target_handle','absence'), 2)
                
                #if dist(hero['location'],val['location'])<=hero['auto']['attack_range']:
                    flag3 = True
                    
                jungle_creep_val = val
                jungle_creep_key = key
                    
                if flag2 and flag3:
                    flag4 = True
                    #switch = remove(switch, ('unit_type','excessive'), 3)
                    
                    for key1, val1 in state.items():
                        
                        neut_lane = dist(val['location'],val1['location'])
                        hero_lane = dist(hero['location'],val1['location'])
                        

                        if val1['unit_type']==3 and (neut_lane<=val1['attack_acquisition_range'] or hero_lane<=val1['attack_acquisition_range']):
                            flag = 1
                            flag4 = False
                            switch = reset(switch, 'unit_type', 'excessive', 3, [str(name),'jungle creep'], ['battled'])
            
                            break


            if flag2 and flag3 and flag4: #flag == 0: 
                
                elem_set.append(int(jungle_creep_key))
                chain_aggro(state, elem_set, jungle_creep_val)
                #print(switch)
                
                return (state, hero['name'], elem_set)
                                      
    
    return (False, switch)
                
    
    
def pull_check2(state, trail, player, elem_set, hero_name, switch):
    
    #switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]  
        #name = get_name(hero_name)
       
        for key, val in state.items():
            
            flag1 = False
            
            if val['unit_type']==3 and val['team_id']==hero['team_id']:
                
                flag1 = True
                switch = remove(switch, ('unit_type','absence'), 1)
                    
                for key1, val1 in state.items():
                    
                    flag2 = False
                    
                    flag3 = False
                    
                    flag4 = False
                    
                    flag5 = False
                    
                    
                    flag6 = False
                    flag7 = False
                    
                    if val1['unit_type']==4:
                        
                        flag2 = True
                        switch = remove(switch, ('unit_type','absence'), 2)
                        
                        if dist(hero['location'],val['location'])<=val['attack_acquisition_range']: 
                            
                            flag3 = True
                            switch = remove(switch, ('location','wrong_place'), 2)
                        
                        if dist(hero['location'],val1['location'])<=val1['auto']['attack_range']:
                            
                            flag4 = True
                            switch = remove(switch, ('location','wrong_place'), 3)
                            
                            
                        if val1['auto']['attack_target_handle']==int(hero['handle']):
                            
                            flag5 = True
                            switch = remove(switch, ('attack_target_handle','absence'), 4)
                            
                            
                        if int(key1) in elem_set:
                            
                            flag6 = True
 
                                     
                        if dist(val['location'],val1['location'])<=val['attack_acquisition_range'] and int(key1) in elem_set:
            
                            flag7 = True
                
                        if (flag3 and flag4 and flag5 and flag6) or flag7:
                        
                            elem_set.append(key)
                            elem_set.append(key1)
                            chain_aggro(state, elem_set, val1)
                            chain_aggro(state, elem_set, val)

            
                            return (state, hero['name'], elem_set)
           
                                        
            
    return (False, switch)
                            
    
def pull_check3(state, trail, player, elem_set, hero_name, switch):
    
    #switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]
        #name = get_name(hero_name)
        
        
        for key, val in state.items():
            
            flag1 = False
            
            if val['unit_type']==3 and val['team_id']==hero['team_id']:
                
                flag1 = True
                switch = remove(switch, ('unit_type','absence'), 1)
                    
                for key1, val1 in state.items():
                    
                    flag2 = False
                    
                    flag3 = False
                    
                    if val1['unit_type']==4 and val['auto']['attack_target_handle']==int(key1):
                        
                        flag2 = True
                        switch = remove(switch, ('unit_type','absence'), 2)
                        
                    if int(key1) in elem_set:
                        
                        flag3 = True
                        switch = remove(switch, ('unit_type','wrong_type'), 3)
                        #print("weird2")
                        
                    if flag2 and flag3:
                    
                        return (state, hero['name'], elem_set)
                            
                            
    return (False, switch)


def update_elements(state, elem_set):
        
    i = 0
    while i < len(elem_set):
        
        flag = 0
        for key, val in state.items():
            
            if str(val['handle'])==str(elem_set[i]) and val['is_alive']==False:
                flag = 1
                r = elem_set.pop(i)
                
            elif str(val['handle'])==str(elem_set[i]):
                flag = 1
                i += 1
                
        if flag == 0:
            r = elem_set.pop(i)
    
    return elem_set
    
                            
    
CheckStates = {'1':(pull_check1,'begin the pull here'),'2':(pull_check2,'run to the lane'),'3':(pull_check3,'draw the lane creeps away from the lane')}
ResetSwitch = {'1':(pull_reset1,'begin the pull here'),'2':(pull_reset2,'run to the lane'),'3':(pull_reset3,'draw the lane creeps away from the lane')}
 

print("Done!")
                      


# In[3]:



#THE PULL FUNCTION 2 - Getting the jungle creep(s) to meet the lane creep(s) 

def pull1(state, trail, player, elem_set):
    
    switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]
        
        jungle_creep = None
        for key, val in state.items():
            
            flag = -1

            if val['unit_type']==4:
            
                if hero['auto']['attack_target_handle']==int(key): 
                    flag = 0
                       
                #if dist(hero['location'],val['location'])<=hero['auto']['attack_range']
                    
                jungle_creep_val = val
                jungle_creep_key = key
                    
                if flag == 0:
                    
                    for key1, val1 in state.items():
                        
                        neut_lane = dist(val['location'],val1['location'])
                        hero_lane = dist(hero['location'],val1['location'])
                        

                        if val1['unit_type']==3 and (neut_lane<=val1['attack_acquisition_range'] or hero_lane<=val1['attack_acquisition_range']):
                            flag = 1

                            
                            break
                
            

            if flag == 0: 
                
                elem_set.append(int(jungle_creep_key))
                chain_aggro(state, elem_set, jungle_creep_val)
                #print(switch)
                
                return (state, hero['name'], elem_set)
                                      
    
    return (False, switch)
                
    
    
def pull2(state, trail, player, elem_set):
    
    switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]  

        for key, val in state.items():
    
            if val['unit_type']==3 and val['team_id']==hero['team_id']:
                   
                for key1, val1 in state.items():
                    
                    flag1 = False
                    
                    flag2 = False
                    
                    if val1['unit_type']==4:
                         
                        if dist(hero['location'],val['location'])<=val['attack_acquisition_range'] and dist(hero['location'],val1['location'])<=val1['auto']['attack_range'] and val1['auto']['attack_target_handle']==int(hero['handle']) and int(key1) in elem_set: 
                            
                            flag1 = True
                                     
                        if dist(val['location'],val1['location'])<=val['attack_acquisition_range'] and int(key1) in elem_set:
            
                            flag2 = True
                
                        if flag1 or flag2:
                        
                            elem_set.append(key)
                            elem_set.append(key1)
                            chain_aggro(state, elem_set, val1)
                            chain_aggro(state, elem_set, val)

            
                            return (state, hero['name'], elem_set)
            
                                      
            
    return (False, switch)
                            
    
def pull3(state, trail, player, elem_set):
    
    switch = []
    if str(player) in state.keys():
    
        hero = state[str(player)]

        for key, val in state.items():
    
            if val['unit_type']==3 and val['team_id']==hero['team_id']:
                
                for key1, val1 in state.items():
                    
                    if val1['unit_type']==4 and val['auto']['attack_target_handle']==int(key1) and int(key1) in elem_set:
                    
                        return (state, hero['name'], elem_set)
                            
                            
    return (False, switch)

        
    
PossibleStates = {'1':(pull1,'begin the pull here'),'2':(pull2,'run to the lane'),'3':(pull3,'draw the lane creeps away from the lane')}
 

print("Done!")


# In[ ]:


def update_elements(state, elem_set):
        
    i = 0
    while i < len(elem_set):
        
        flag = 0
        for key, val in state.items():
            
            if str(val['handle'])==str(elem_set[i]) and val['is_alive']==False:
                flag = 1
                r = elem_set.pop(i)
                
            elif str(val['handle'])==str(elem_set[i]):
                flag = 1
                i += 1
                
        if flag == 0:
            r = elem_set.pop(i)
    
    return elem_set

def gold_check(state_dict, hero_key, time1, time2):
    
    init_gold = state_dict[str(time1)][hero_key]['gold']
    final_gold = state_dict[str(time2)][hero_key]['gold']
    
    if final_gold==init_gold:
        return False
    
    return True

def xp_check(state_dict, hero_key, time1, time2):
    
    init_xp = state_dict[str(time1)][hero_key]['xp']
    final_xp = state_dict[str(time2)][hero_key]['xp']
    
    if final_xp==init_xp:
        return False
    
    return True


def last_hit_check(states, index, cutoff, player):

    state = states[index][1]
    if str(player) in state.keys():
        
        try:
        
            hero = state[str(player)]

            target_key = int(hero['auto']['attack_target_handle'])

            target_val = state[str(target_key)]

            elements = [target_key]

            chain_aggro(state, elements, target_val)
            #print(elements)
        
        except:
            
            return True
        
    else:
        
        return True
    
    try:
        
        if state[str(player)]['active_ability_handle']!=0:
            return True
        
    except:
        
        pass
    
    time = float(states[index][0])
    
    prev = states[index-1][1]
    i = index
    
    while time <= float(cutoff+1):
        
        if len(states)>i and str(player) in state.keys():
            
            curr = states[i][1]
        
            hero1 = prev[str(player)]
            hit1 = int(hero1['last_hits'])
            target = int(hero1['auto']['attack_target_handle'])
            gold1 = int(hero1['gold'])
            

            hero2 = curr[str(player)]
            hit2 = int(hero2['last_hits'])
            gold2 = int(hero2['gold'])
            
            if target!=0:
                
                elements.append(target)
                chain_aggro(curr,elements,curr[str(target)])
            
            if (hit2!=hit1) and target in elements:
                
                return True
            
        prev = curr
        
        i += 1
        
        time = float(states[i][0])
        
    return False


def stacking(states, index, cutoff, player):
    
    state = states[index][1]
    
    if str(player) in state.keys():
        
        try:
            target_key = str(state[str(player)]['auto']['attack_target_handle'])
            c = state[target_key]['location']
        
        except:
            return True
        '''
        m = 10000
        camp = -1
        for key, val in jcamps.items():
            
            distance = dist(val,loc)
            #print(distance)
            if distance < m:
                m = distance
                camp = key
                
        print(m)
        print(camp)
        '''
        
        time = float(states[index][0])
        
        prev = states[index-1][1]
        i = index
        bound = 150
        
        while time <= float(cutoff+1):
            
            if len(states)>i and str(player) in state.keys():
            
                curr = states[i][1]
                
                
                s1 = set()
                for key, val in prev.items():
                    
                    if val['unit_type']==4:
                            
                        s1.add(int(key))
                
                
                s2 = set()
                for key, val in curr.items():
                    
                    if val['unit_type']==4 and (int(key) not in s1) and dist(val['location'],c)<=200:
                        
                        s2.add(int(key))
                        
                        
                if len(s2)!=0:
                    #print(time)
                    #print(s2)
                    return True
                        
            prev = curr
        
            i += 1
        
            time = float(states[i][0])
 
    return False


def check_illusion(states, index, cutoff, player):
    
    time = float(states[index][0])
    i = index
    
    while time<=float(cutoff+1):
        
        state = states[i][1]
        if str(player) not in state.keys():
            
            return True
        
        if state[str(player)]['is_illusion']==True:
            #print(state[str(player)]['is_illusion'])
            
            return True
        
        
        i += 1
        time = float(states[i][0])
        
    return False

                            

