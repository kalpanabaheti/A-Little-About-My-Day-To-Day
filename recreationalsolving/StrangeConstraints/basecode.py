#Problem 4.1 - page 3 from the book - Problem Solving Through Recreational Mathematics

#s = number of seats
#l = list of people
#c = constraint list - c1 = [l1,R/L,jumps,l2]

import copy
import itertools
from pyvis.network import Network 
import math
import networkx as nx

'''
Instructions for constraints: 
Every constraint is a list that contains -
0th index - First entity is a tuple of (name,type) where type is either person or profession.
1st index - Number of jumps from the entity represented by the first tuple.
2nd index - Direction of jump with respect to first entity. 
3rd index - Second entity is a tuple of (name,type) where type is either person or profession and is found after the jumps.
'''

constraints = [
    [('1','person'),2,'L',('2','profession')],
    [('4','person'),2,'R',('4','profession')], 
    [('3','person'),1,'L',('3','profession')],
    [('5','profession'),1,'R',('2','person')]
]
'''
constraints = [
    [('1','person'),2,'R',('2','profession')],
    [('4','person'),3,'L',('4','profession')], 
    [('3','person'),1,'L',('3','profession')],
    [('4','profession'),1,'R',('2','person')]
]
'''

total_seats = int(input("\nEnter total number of seats: "))
first = {'person':dict(),'profession':dict()}
people = dict()
peeps = int(input("\nEnter total number of people: "))

for x in range(1,peeps+1):
    
    name = input("\nEnter the profession: ")
    key = str(x)
    people[key]=name
    
for p in people.keys():
    
    first['person'][p]=[i for i in range(1,total_seats+1)]
    first['profession'][p]=[i for i in range(1,total_seats+1)]
    
collection = [first]


def add(current_seat, direction, jump):
    
    global total_seats
    if direction == "R":
        raw = current_seat + jump
        raw = raw % total_seats
    else:
        raw = current_seat - jump
    
    if raw<=0:
          raw = total_seats + raw
    final = raw 
          
    return final
    

def in_check(setting): #[person,profession]
    
    per = setting[0]
    prof = setting[1]
    
    s = list()
    
    for k,v in per.items():
        if len(v)==1 and v in s:
            return False
        else:
            s.append(v)
            
    s = list()
    
    for k,v in prof.items():
        if len(v)==1 and v in s:
            return False
        else:
            s.append(v)
    
    return True
    
    
def cross_check(setting): #[person,profession]
    
    per = setting[0]
    prof = setting[1]
    
    for k,v in per.items():
        
        if v==prof[k] and len(v)==1:
            return False
        
    return True
    
    
def in_removal(person,key,val):
    
    for k,v in person.items():
        
        if k!=key and (val in v) and len(v)!=1:
            
            person[k].remove(val)
            
            
def cross_removal(p_other,key,val):
    
    if val in p_other[key] and len(p_other[key])!=1:
        p_other[key].remove(val)
    
    
def set_seats(trial,person,profession): #[entity1-[name,type], seat, jump, direction, entity2-[name,type]]
    
    global total_seats
    
    per = person
    prof = profession
    
    e1 = trial[0]
    e2 = trial[-1]
    seat1 = trial[1]
    jump = trial[2]
    dtn = trial[3]
    seat2 = add(seat1,dtn,jump)
    
    ######################
    
    if e1[1]=='person':
        x1=per
        x2=prof
    else:
        x2=per
        x1=prof
        
    if seat1 in x1[e1[0]]:
        x1[e1[0]]=[seat1]
        in_removal(x1,e1[0],seat1)
        cross_removal(x2,e1[0],seat1)
        
    if e1[1]=='person':
        per = x1
        prof = x2
    else:
        prof = x1
        per = x2
        
    ###########################
        
    if e2[1]=='person':
        y1=per
        y2=prof
    else:
        y2=per
        y1=prof
     
    if seat2 in y1[e2[0]]:
        y1[e2[0]]=[seat2]
        in_removal(y1,e2[0],seat2)
        cross_removal(y2,e2[0],seat2)
        
    if e2[1]=='person':
        per = y1
        prof = y2
    else:
        prof = y1
        per = y2  
        
    ############################
    
    setting = [per,prof]
    flag1 = in_check(setting)
    flag2 = cross_check(setting)
    
    if (not flag1) or (not flag2):
        return False
    
    return [per,prof]
    
    
        
def tree(constraints):
    
    global total_seats
    global collection
    
    ic = constraints[0]
    
    e1 = ic[0] #entity1
    e2 = ic[-1] #entity2
    seat = 1
    jump = ic[1] #jump
    dtn = ic[2] #direction
    
    trial = [e1,seat,jump,dtn,e2]
    person = collection[0]['person']
    profession = collection[0]['profession']
    
    result = set_seats(trial,person,profession)
    
    collection = []
    constraints.remove(ic)
    
    if result!=False: 
        collection.append({'person':result[0],'profession':result[1]})
        
    #print(constraints)
    #print(collection)
        
    for cns in constraints:
        
        ic = cns
        #print(ic)

        e1 = ic[0] #entity1
        e2 = ic[-1] #entity2
        jump = ic[1] #jump
        dtn = ic[2] #direction
        
        temp = copy.deepcopy(collection)
        for curr in temp:
            
            collection.remove(curr)
            if e1[1]=='person':
                seats = curr['person'][e1[0]]
            else:
                seats = curr['profession'][e1[0]]
                
            poss = []
            for seat in seats:
                
                #print(seat)

                trial = [e1,seat,jump,dtn,e2]
                #print(trial)
                person = copy.deepcopy(curr['person'])
                profession = copy.deepcopy(curr['profession'])
                #print('\n',person,'\n',profession)

                result = set_seats(trial,person,profession)
                if result!=False:
                    new = {'person':result[0],'profession':result[1]}
                    #print('\n',new)

                    if new not in collection and new not in poss: 
                        poss.append(new)
                    
            
        if poss!=[]:
            collection.extend(poss)
                
        #print('\n',collection)
        
        
#MAIN ENVIRONMENT

tree(constraints)
def printer(c):
    
    d = dict()
    print("\n")
    for i in range(1,total_seats+1):
    
        for k,v in c['person'].items():
            if i in v and isinstance(v,list):
                if str(i) not in d.keys():
                    d[str(i)] = ['Mr. '+str(people[k])]
                else:
                    d[str(i)].append('Mr. '+str(people[k]))
                
        for k,v in c['profession'].items():
            if i in v and isinstance(v,list):
                if str(i) not in d.keys():
                    d[str(i)] = [people[k]]
                else:
                    d[str(i)].append(people[k])
                
    graphs.append(d)
    for k,v in d.items():
        
        print("\n",k,":\t",v)
        
    return d
    

temp = copy.deepcopy(collection)
save = []

#print(temp)

for curr in temp:
    
    per = []
    prof = []
    for i in range(1,len(curr['person'].keys())+1):
        
        per.append(curr['person'][str(i)])
        prof.append(curr['profession'][str(i)])
        
    comb1 = list(itertools.product(*per))
    comb2 = list(itertools.product(*prof))
    #print(comb1)
    #print(comb2)
    
    per = dict()
    prof = dict()
    for i in comb1:
        
        for x in range(1,len(i)+1):
            
            per[str(x)]=[i[x-1]]
            
        #print('\n',per,'\n')
        for j in comb2:
            
            for y in range(1,len(j)+1):
                
                prof[str(y)]=[j[y-1]]
                
            #print(prof) 
            setting = copy.deepcopy([per,prof])
            flag1 = in_check(setting)
            flag2 = cross_check(setting)
    
            if (flag1) and (flag2):
            
                a = copy.deepcopy({'person':per,'profession':prof})
                save.append(a)
                #printer(a)
                

'''
wormtail is 3 to left of mr.wormtail
padfoot is 2 to the right of mr. wormtail
prongs is to the left of moony
'''

#graphing

final = []
for ins in save:
    
    flag = 0
    for ic in constraints:
        
        e1 = ic[0] #entity1
        e2 = ic[-1] #entity2
        j = ic[1] #jump
        d = ic[2] #direction
        
        key1 = e1[1] #type1
        key2 = e2[1] #type2
        #print(key1,key2)
        
        start = copy.deepcopy(ins[key1][e1[0]][0])
        #print(start,d,j)
        finish = add(start, d, j)
        land = copy.deepcopy(ins[key2][e2[0]][0])
        
        if land!=finish:
            flag = 1
            break
            
    if flag == 0:
        final.append(ins)
        

if final==[]:
    print("No possible cases!!")
    
graphs = []
for f in final:
    p = printer(f)
    print("\n")
    if p not in graphs:
        graphs.append(p)
        
        
pi = math.pi
def PointsInCircum(r,n=0):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

count = 0
#print(graphs)
for table in graphs:
    
    v = []
    t = []
    l = []
    c = []
    n = []

    for node in range(1,(total_seats+1)):

        key = copy.deepcopy(str(node))
        #print(node)
        if key in table.keys():
            c.append('blue')
            n.append(key)
            label = copy.deepcopy(table[key])
            desc = copy.deepcopy(label)
            l.append(desc)
            v.append(400)

    pos = PointsInCircum(250,len(table))
    
    g = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')   
    #print(n)

    for i in range(len(n)):

        g.add_node(n[i], 
                   value=v[i],
                   label=l[i],
                   x=pos[-(i+1)][0],
                   y=pos[-(i+1)][1],
                   color=c[i],
                   physics=False)

    count += 1
    gname = 'graph'+str(count)+'.html'
    g.show(gname)
    
