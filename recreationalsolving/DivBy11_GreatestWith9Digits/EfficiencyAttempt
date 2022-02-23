#largestnumdivby11
from collections import Counter
import time
from itertools import permutations

 = '9876543210'

initial = time.time()
for i in range(int(len(s)/2)):

     cutindex = -2*(i+1)
     new = s[:cutindex]
     collect = list(s[cutindex:])
     perm = [int(x) for x in collect]
     permute = permutations(perm)

     addfirst = (len(new)/2)
     maxi = 0

     for fiddle in permute:

          #print(fiddle)
          if fiddle[0]!=0:
               addsecond = 0
               end = ''
               jump =0
               while jump<len(fiddle):

                    addsecond += fiddle[jump]-fiddle[jump+1]
                    end += (str(fiddle[jump])+str(fiddle[jump+1]))
                    jump+=2

               if (addfirst+addsecond)%11==0 and int(new+end)>maxi:
                    maxi = int(new+end)

     if maxi!=0:
          final = time.time()
          print(maxi)
          print(final-initial)
          break
     
