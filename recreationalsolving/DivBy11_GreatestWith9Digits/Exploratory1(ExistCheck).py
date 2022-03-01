#largestnumdivby11
from collections import Counter
import time
from itertools import permutations

initial = time.time()
s = '9876543210'
c1 = Counter(s)
#print(c1)

top = 9876543210
check = int(top-(top%11))

while len(str(check))==10:

     c2 = Counter(str(check))
     if c2==c1 and check%11==0:
          final = time.time()
          print(check)
          print(final-initial)
          break
     check -= 11
     
