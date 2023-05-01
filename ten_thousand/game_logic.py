from abc import ABC
from collections import Counter
import random

class GameLogic :
  
  @staticmethod
  def calculate_score(t):
   result = 0
   d_counter = Counter(t)

   if(d_counter[5]==1):
     result +=  50

   if (d_counter[1]==1):
     result += 100

   if(d_counter[5]==2):
      result +=  100

   if(d_counter[1]==2):
      result +=  200

   if(d_counter[2]==1 or d_counter[2]==2 ):
      result +=  0
    
   if(d_counter[5]==3):
      result +=  500
    
   if(d_counter[1]==3):
      result +=  1000
   
   if( d_counter[1]==1 and d_counter[2]==1 and d_counter[3]==1 and d_counter[4]==1 and d_counter[5]==1 and d_counter[6]==1):
     result =  1500
    
   if(d_counter[2]==3):
     result += 200
    
   if(d_counter[2]==4):
     result += 400

   if(d_counter[2]==5):
     result += 800

   if(d_counter[2]==6):
     result = 1600

   if(d_counter[1]==6):
     result = 8000
    
   if(d_counter[1]==4):
     result = 2000
    
   if(d_counter[1]==5):
     result += 4000

   if(d_counter[3]==1 or d_counter[3]==2):
     result += 0 

   if(d_counter[3]==3):
     result += 300

   if(d_counter[3]==4):
     result += 600

   if(d_counter[3]==5):
     result += 1200

   if(d_counter[3]==6):
     result = 2400

   if(d_counter[4]==1 or d_counter[4]==2):
     result += 0 
    
   if(d_counter[4]==3):
     result += 400 
    
   if(d_counter[4]==4):
     result += 800 

   if(d_counter[4]==5):
     result += 1600 

   if(d_counter[4]==6):
     result += 3200 
    
   if(d_counter[5]==4):
     result += 1000 

   if(d_counter[5]==5):
     result += 2000 

   if(d_counter[5]==6):
     result += 4000 
    
   if(d_counter[6]==1 or d_counter[6]==2):
     result += 0 
    
   if(d_counter[6]==3):
     result += 600 
    
   if(d_counter[6]==4):
     result += 1200 

   if(d_counter[6]==5):
     result += 2400 

   if(d_counter[6]==6):
     result += 4800 
    
   if(d_counter[2]==2 and d_counter[3]==2 and d_counter[6]==2 ):
     result =1500

   return result
 
   
  @staticmethod
  def roll_dice(dice_num=6):
       random_numbers = []

       for i in range(dice_num):
         num = random.randint(1, 6)
         random_numbers.append(num)
       tuple1=tuple(random_numbers)
       return tuple1
  
  @staticmethod
  def validate_keepers(roll,keeper):
    roll_counter = Counter(roll)
    keeper_counter = Counter(keeper)
    same = keeper_counter - roll_counter
    if (len(same)==0):
      return True
    else:
      return False

  @staticmethod
  def get_scorers(t):
      listt =[]
      for  i in t:
        if(GameLogic.calculate_score((i,))!=0):
          listt.append(i)
      tt = tuple(listt)
      return tt