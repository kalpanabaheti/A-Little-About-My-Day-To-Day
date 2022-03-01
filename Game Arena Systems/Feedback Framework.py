#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The Pull

pull = [
    
    [[ 
    
    "To start a pull, ", "To pull your lane creeps, ", "How do we do a pull? ","If you need to pull lane creeps, "
    
    ],[

        "you begin with attacking a jungle creep camp. ","you fire at a jungle creep camp. ","you attack jungle creeps. ","you target a jungle creep that isn't contested. ","you would need to attack idle jungle creeps. "

    ]],[[

        "Then ","After that, ","Following that, ","Next thing, ","From there "

    ],[

        "as the jungle creeps pursue you, ","after getting the jungle creeps to follow, ","make sure the jungle creeps chase you and "
    ],[

        "run to the lane creep camp that you want to pull and aggro them. ","you make your way to lane creeps that need to be denied and aggro them. ","you aggro the lane creeps you want to deny. "

    ]],[[

        "Make sure you have a jungle creep attack you while near the lane creep and ","Ensure that the lane creeps are close enough to perceive that you're being attacked by jungle creeps and ","Move straight into the lane creeps with the jungle camp at your tail and "

    ],[

        "get out of the way to while the lane and jungle creeps fight. ","allow the lane creeps to become the jungle creeps' targets. ","effectively let the jungle creeps deny the lane creeps. "

    ]]

]

mistake = [
    
    "But, in your case, what you need to understand is that ","Observe for next time, because according to what we saw ","Unfortunately, as it happens, this time "
]


# In[2]:


#Common Phrases

'''
Example - 

Let's check this out. Here's a moment where there were no enemy heroes in the vicinity and you attacked a jungle creep camp. 
That was a golden opportunity to farm and earn yourself gold, either that or do a neat pull for your team. 
You might want to think of how you could've lead the jungle creeps to the lane creeps walking into the enemy.
Don't feed into the enemy's power! Let's stay calm and kick-ass.


'''
feedback_opening0 = ["Okay! ","Well, ","Ah! ", "Awesome! ", "Beauty! ", "Right then, ", "Hmm... ", "Hmmm... ", "Hmmmm... ", "Well, well! "]
feedback_opening11 = ["So ", "Let's ", 
                    "We'd like you to ", "We should ", "How about we ", "How 'bout we ", "Time to ", "Great game to ",
                    "This is a perfect time to ", "You might want to ", "It's all about keen observation so let us ", "Now "]
feedback_opening12 = ["check this out, maybe? ", "take a look at this one here. ", "see what we have here? ", "take a bit to observe this; ", "kick more ass, shall we! ",
                    "watch this... ", "take it by storm. ", "make your game magnificent. ", "take it deeper... ", "give it all you've got! " ]
feedback_opening2 = ["So here we go! ", "Let's break a leg and get better at this... ", "Here's to kicking more ass. "]

feedback_overall0 = []

feedback_overall11 = ["you could do a pull here by running to the nearest lane creep camp! ",
                     "this is a good time to farm. Make sure you don't get overwhelmed by creeps when you last hit them "]
feedback_overall12 = ["get out of harms way after the lane and jungle creeps have met. You've done the job well already "]
feedback_overall2 = []

feedback_conclude1 = []
feedback_conclude2 = []

in_conjunction_and = ['and ', 'and also ', 'and as observed ']
in_conjunction_or = ['or ',' either that, or ', 'or besides that ','or alternatively ']
in_disjunction = ['but ','however ', 'even so ','but mind you ']
in_negation = ['not ']

extend_conjunction_and = ["furthermore ", 'besides that ', 'besides, ','also ', 'and this too, that ', 
                          'and ', 'also remember that ', 'and furthermore ']
extend_conjunction_or = ['also remember that ','or otherwise ', 'alternatively ', 'either that, or ', 'another thing is that ']
extend_disjunction = ['however ', 'but at the same time ', "but don't forget ", "but here's something to heed ",
                     "however there's this too, that ", "but also watch out that ", "but nonetheless observe that ",
                     'nevertheless ', 'nonetheless ','despite that, remember that ']
extend_negation_prefix = ["you have not ensured that ","you have not made it so that ","it isn't so that ", "it is not the case where ", "what doesn't happen is "]
extend_negation_postfix = [",and this doesn't happen ", ";something that doesn't happen ", "doesn't happen ",
                          "does not take place ", "now do we see that? No ", "which didn't happen, did it ", 
                           "and that didn't manifest ", "and that didn't manifest, did it "]
in_implication = ["it means that ","it follows that ", "that causes ", ",so what happens is that", 
                     "think about what would happen next ", "from there we go to a place where ", 
                      "we jump to the moment where", "then what happens in our game is ", "the next thing you know "]

extend_implication = []




# In[3]:


common_switchboard = {
    
    '1': feedback_opening0,
    '2': feedback_opening11,
    '3': feedback_opening12,
    '4': feedback_opening2,
    '5': feedback_overall0,
    '6': feedback_overall11,
    '7': feedback_overall12,
    '8': feedback_overall2,
    '9': feedback_conclude1,
    '10': feedback_conclude2,
    '11': in_conjunction_and,
    '12': in_conjunction_or,
    '13': in_disjunction,
    '14': in_negation,
    '15': in_implication,
    '16': extend_conjunction_and,
    '17': extend_conjunction_or,
    '18': extend_disjunction,
    '19': extend_negation_prefix,
    '20': extend_negation_postfix,
    '21': extend_implication
}
 


# In[4]:


#Attribute Adjectives - Isolated

attribute_switchboard = {
    
    
    "unit_type":{
        
        #noun1-verb2-noun2, noun2-verb1-noun1
        'absence':(["the 12 ","was not available to be 2 ","by 11 "],["11 ","need to find the right 12 ", "to be 2 " ]), 
        'wrong_type':(["the wrong 12 ","was 2 ","by 11 "],["11 ","2 ","the wrong 12 " ]),
        'excessive':(["the 12 ","should've been 2 ONLY ","by 11 "],["11 ALONE ","should have 2 ","the 12 " ])
        
    },
    "team_id": {
        
        #noun1-verb2, verb1-noun1
        'wrong_type':(["the wrong team element ","was 2 here ","by 11 " ],["11 ","2 ","the wrong team here "])
    },
    "is_alive":{
        
        #noun1-verb2-noun2, noun2-verb1-noun1
        'wrong_type':(["the 12 ","was already dead when 2 ","by the 11 "],["the 11 ","2 an ","already dead 12"])
        
    },
    "location":{
        
        #noun1-verb1-noun2, noun2-verb1-noun1
        'wrong_place':(["11 ","2 ","from an inadequate place when considering where the 12 was "],["seeing where the 12 was, ","11 ","2 from the wrong spot "]),
        'stalling':(["the 11 ","should have stalled and 2 ","the 12 all things considered "])
        
    },
    "level":{
        
        'should_improve':(["there was  a chance to level up here and you should have taken it "]),
        
    },
    "mana_fraction":{
        
        #noun1
        'cannot_risk':(["11 ","have a very low mana here "]),
        'can_risk':(["there is enough mana for 11 ","to withstand the attack and 11 should've charged "])
        
    },
    "bounty_xp":{
        
        'should_improve':(["this was a time to gain experience and gold, and you could've used it "])
        
    },
    "current_movement_speed":{
        
        #noun1-noun2
        'absence':(["11 ","were not quick enough and didn't move quickly enough considering the movement of the 12 "]),
        'excessive':(["11 ","shouldn't have moved too quickly and acted on time, while the 12 played out "])
        
    },
    "attack_damage":{
        
        
        'absence':(["11 should have ","2 the ","12 when he had the chance " ],["the 12 ought to have been ","2 by ","11 "]),
        'wrong_amount':(["11 ","2 in a very unfocused manner instead of just focusing on "," 12"],["in place of just attacking the 12 ","too many enemy elements spent 11 out, by being 2 ","by 11"])
        
    },
    "attack_range":{
        
        'absence':(["11 ","need to be in range to attack 12 "],["12 wasn't within ","the range of attack 11 possessed "]),
        
    },    
    "attack_acquisition_range":{ 
        
        'absence':(["the 12's ","aggro range needs cover the location at which 11 were "],["11 weren't close enough to ","aggro 12 "]),
        'excessive':(["11 ","aggro-ed 12 which 11 shouldn't have "],["12 was aggro-ed to ","11, disrupting the plan "])
        
    },
    "attack_target_handle":{
        
        'absence':(["12 ","missed the 11 that needed to attacked "],["11 didn't suffer an attack from ","12, though that should've happened "]),
        'wrong_type':(["11 ","attacked 13 ","but should have targetted 12 "],["12 wasn't what 11 were targetting ","but it should've been the focus of attack "]),
        'backwards':(["11 ","suffered an attack from 12 ","that 11 couldn't afford and should've tried to escape"],["12's decision to attack ","11 is what created trouble for 11 "])
        
    },
    "name":{
        
        'do_not_attack':([],[]),
        'attack':([],[])
        
    }
    
}




#Attribute Adjectives - Comparative and Superlative




# In[5]:


#Attribute Verbs


verb_active = {}
verb_passive = {}



p1 = "My name is *"
p2 = "Kalpana Baheti"
p1 = p1.replace("*",p2)
print(p1)


# In[6]:


import random

#check = [('597.387451171875', '607.0'), [[2, ('location', 'wrong_place'), ['slark', 'lane creep'], ['attempted to aggro']], [3, ('location', 'wrong_place'), ['slark', 'jungle creep'], ['baited the jungle creep onslaught']], [4, ('attack_target_handle', 'absence'), ['jungle creep', 'slark'], ['targetted for attack']]]] 
#switch = check[1]
#print(switch)


def construct_intro():

    
    compose = ''
    feed1 = random.choice(feedback_opening0)
    
    r = random.choice(range(7))

    if r%6==0:
        
        feed2 = random.choice(feedback_opening2)
        
    else:
        
        part1 = random.choice(feedback_opening11)
        part2 = random.choice(feedback_opening12)
        feed2 = part1 + part2
        
    compose = feed1 + feed2 
    
    strat = ""
    
    for part in pull:
        
        for j in part:
            
            add = random.choice(j)
            strat += add
            
    compose += strat       
    
    
    
    return compose
        
print(construct_intro())       
    



def construct_feedback(switch):
    
    #global mistake
    
    priority = 999
    for i in switch:
        if i[0]<priority:
            priority = i[0]
            
    #print("\n",priority)
    
    compose = []
    for i in switch:
        
        if i[0]==priority:
            compose.append(i)
            
    #print(compose)
    phrases = []
    for raw in compose:

        outer = raw[1][0]
        inner = raw[1][1]


        attr_val = attribute_switchboard[outer][inner]
        rand_phrase = random.choice(attr_val)

        nouns = raw[2]
        verbs = raw[3]

        for i in range(len(nouns)):

            for j in range(len(rand_phrase)):

                r = '1'+str(i+1)
                if r in rand_phrase[j]:

                    phr = rand_phrase[j]
                    phr = phr.replace(r,nouns[i])
                    rand_phrase[j]=phr
                        
            
        for j in range(len(rand_phrase)):
                
            r = '2'
            if r in rand_phrase[j]:
                    
                phr = rand_phrase[j]
                phr = phr.replace(r,verbs[0])
                rand_phrase[j]=phr
                
        construct = ''
        for i in rand_phrase:
            
            construct += i
        
        if construct not in phrases:
            phrases.append(construct)
        #print(phrases)
        
    add = random.choice(mistake)
    phrases[0] = add+phrases[0]
    
    return phrases

#print(construct_feedback(switch))


# In[ ]:




