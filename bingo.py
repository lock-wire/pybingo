#!/usr/bin/env python3
"""Bingo Card Number Generator
"""
from base64 import b16decode
import os
import sys
import random
import pandas as pd
#import openpyxl


def createList(r1, r2, letter):
 
 # Testing if range r1 and r2
 # are equal
 if (r1 == r2):
  return r1
 
 else:
 
  # Create empty list
  globals()[letter] = []
 
  # loop to append successors to
  # list until r2 is reached.
  while(r1 < r2+1 ):
    
   globals()[letter].append(r1)
   r1 += 1
  return globals()[letter]
  
# Driver Code
x=0
bingo=['B', 'I', 'N', 'G', 'O']
bingomin=1
bingomax=75
bingorow=len(bingo)
bingowindow=int(bingomax//bingorow)
r1, r2 = 0, 0

for letter in bingo:
    x=x+1
    r1=((bingowindow*x)-bingowindow)+1
    r2=(bingowindow*x)
    #print(r1)
    #print(r2)
    createList(r1, r2, letter)
    random.shuffle(globals()[letter])
    #print (globals()[letter][0:5])

N[2]='FREE'
N[7]='FREE'
N[12]='FREE'
df1 = pd.DataFrame({'B':B[0:5], 'I':I[0:5], 'N':N[0:5], 'G':G[0:5], 'O':O[0:5]})
df2 = pd.DataFrame({'B':B[5:10], 'I':I[5:10], 'N':N[5:10], 'G':G[5:10], 'O':O[5:10]})
df3 = pd.DataFrame({'B':B[10:15], 'I':I[10:15], 'N':N[10:15], 'G':G[10:15], 'O':O[10:15]})
card1 = df1.to_string(index=False)
card2 = df2.to_string(index=False)
card3 = df3.to_string(index=False)
print(card1)
print('')
print(card2)
print('')
print(card3)
#df.to_excel('bingo_card.xlsx', index=False, header=False)