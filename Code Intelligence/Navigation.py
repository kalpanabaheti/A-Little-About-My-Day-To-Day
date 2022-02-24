
import json
from pathlib import Path
import sys
import re
import os
from collections import defaultdict

class Navigate:

     def __init__(self):
          self.fdic = list()
          self.nested = list()

     def lister(self,od): #nested will have [ [[sequence][file,line,ins]..[] ] ]

          nd = self.nested

          fn = od['filename']
          t = od['trace']

          for d in t:
               if d['context']=='inc':
                    l1=d['variables']
                    for m in l1:
                         v = m['value_seq']
                         n = m['name']

                         temp = defaultdict(list) #key is tuple, value is list of values
                         for seq in v:
                              line = seq['lineno']
                              val = seq['value']
                              key = (fn, line, n)

                              temp[key].append(val)

                         for k,v0 in temp.items():
                              if len(v0)>1:
                                   flag = 0
                                   for i in nd:
                                        if i[0]==v0:
                                             i.append(list(k))
                                             flag = 1
                                   if flag == 0:
                                        nd.append([v0,list(k)])
                                                                           

          return nd

                                                 
     
     def order(self,od): #fdic will have [[single_val,[file,line,ins]..[]]]

          nd = self.fdic

          fn = od['filename']
          t = od['trace']
          
          for d in t:
               if d['context']=='inc':
                    l1 = d['variables']
                    for m in l1:
                         v = m['value_seq']
                         n = m['name']

                         for seq in v:
                              line = seq['lineno']
                              val = seq['value']
                              k = [fn, line, n]

                              flag = 0
                              
                              for i in range(len(nd)):
                                   if nd[i][0]==val:
                                        nd[i].append(k)
                                        flag = 1
                              if flag == 0:
                                   nd.append([val,k])

          return nd


     

     def func0(self,data): #takes a list of values

          nd = self.fdic
          s = set()
          for el in nd:
               for f in el[1:]:
                    s.add(tuple(f))
          #s = set(s)
          for i in s:
               #print('Total: ',len(s))
               #print('Example: ',i)
               break
          

          flag = 0
          f = 0
          for el in nd:
               if el[0] in data:
                    temp = set()
                    for i in el[1:]:
                         temp.add(tuple(i))
                         if f==0:
                              for b in temp:
                                   #print('temp: ',temp)
                                   f = 1
                    s = s.intersection(temp)
                    flag = 1
          if flag == 0:
               return set()
          for i in s:
               #print('return: ',i)
               break

          return s

     def func1(self,data):
          return set()

     def func2(self,data): #takes a list of lengths

          nd = self.nested
          s = set()       

          flag = 0
          f = 0
          for el in nd:
               l = len(el[0])
               if int(l) in data:
                    print(l)
                    temp = set()
                    for i in el[1:]:
                         temp.add(tuple(i))
                    s = s.union(temp)
                    flag = 1
          if flag == 0:
               return set()

          return s

          

     def update(self,basepath):

          flag = 0

          for path2 in basepath.iterdir():

               if os.path.isfile(path2):
                    
                    with open(path2,'r',errors='ignore') as fp:
                                
                         data = json.load(fp)
                         self.fdic = self.order(data)
                         self.nested = self.lister(data)

          print("\nIteration results of size 6")
          for el in self.nested:
               if len(el[0]) == 6:
                    print(el[0])

          check = ['3915735.py', 4, 'iteri']
          for el in self.nested:
               if check in el[1:]:
                    print('\n',el[0])
          
          return [self.fdic,self.nested]

               
#main environment
c = Navigate()

while True:

     print('\nSource filepaths: \n1. /Kalpana Related /SENSE RESEARCH STUDY/100101\n2. /Kalpana Related /SENSE RESEARCH STUDY/11111111\n3. /Kalpana Related /SENSE RESEARCH STUDY/1110\n')

     path1 = input("Enter source folder path: ")
     basepath = Path(path1)

     data = c.update(basepath)

     while True:

          print('''/nInput controls 1 -
                    \n1. Choose data point(s)
                    \n2. Choose loops(s)
                    \n3. Choose loop length(s)
                    \nEnter as a comma separated series like this - 1,0,1
                    \nSet 1 if you want it, 0 if you don't:''')

          s1 = input('\n')
          s1 = list(s1.split(','))
          print(s1)
          r1,r2,r3 = set(),set(),set()

          if s1[0] == '1':
               
               i = input('\nEnter data point(s) comma separated: \n')
               j = input('\nEnter data types of subsequence - int, str, bool: \n')
               i = list(i.split(','))
               j = list(j.split(','))
               
               for x in range(len(i)):
                              
                         if j[x]=='int':
                              try:
                                   i[x] = int(i[x])
                              except:
                                   print("Type ",x+1," not possible.")

                         if j[x]=='bool':
                              try:
                                   i[x] = bool(i[x])
                              except:
                                   print("Type ",x+1," not possible.")
                                   
               r1 = c.func0(i)

          if s1[1] == '1':

               d = []

               print("\nType 'whew' when you want to stop")

               while True:

                    i = input('\nEnter subsequence comma separated: \n')
                    j = input('\nEnter data types of subsequence - int, str, bool: \n')


                    if i == 'whew' or j == 'whew':
                         break
                    else:
                         i = list(i.split(','))
                         j = list(j.split(','))

                         for x in range(len(i)):
                              
                              if j[x]=='int':
                                   try:
                                        i[x] = int(i[x])
                                   except:
                                        print("Type ",x+1," not possible.")

                              if j[x]=='bool':
                                   try:
                                        i[x] = bool(i[x])
                                   except:
                                        print("Type ",x+1," not possible.")
                                       
                    d.append(i)
                         
               r2 = c.func1(d)

          if s1[2] == '1':

               i = input('\nEnter lengths comma separated: \n')
               i = list(i.split(','))
               i = [int(j) for j in i]
                         
               r3 = c.func2(i)
     
          if len(r1)==0:
               r1 = r3
          if len(r2)==0:
               r2 = r1
          if len(r3)==0:
               r3 = r2 #r = r1 & r2 & r3

          r = set()
     
          for i in r1:
               for j in r2:
                    for k in r3:
                         if i[0]==j[0] and j[0]==k[0]:
                              r.add(k[0])

          #print(r3)
          print('Selected collection number: ',len(r))
          if len(r)<=30:
               for i in r:
                    print(i)
          print('Random check: ')
          c0 = 0
          l = [1,13,26,78,214,145]
          for i in r:
               c0+=1
               if c0 in l:
                    print(i)

          inner = input("\nIf you want to run combinations again print y, else print n:")
          if inner == 'n':
               break

     outer = input("Do you want to choose another input file? y or n..:")
     if outer == 'n':
          break

     

     

     

          

     
           
      
