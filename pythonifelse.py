import math
import os
import random
import re
import sys


n = int(input())
n in range(1,101) 
if (n%2==0 and n>=2 and n<=5):
    print("Not Weird")
elif (n>=6 and n<=20):
   print("Weird")
elif (n%2==0 and n > 20):
  print("Not Weird")
elif (n%2!=0):
 print("Weird")
