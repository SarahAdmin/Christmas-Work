import random 
def FestiveDice(): 
  dice = random.randrange(1,7) 
  if (dice == 1): 
     print(dice) 
     print('One is Pear Tree')
  elif (dice == 2): 
       print(dice) 
       print('Two Types of Christmas Cakes')
  elif (dice == 3): 
      print(dice) 
      print('Three Colourful Christmas Baubles') 
  elif (dice == 4): 
      print(dice) 
      print('Four Types of Glitter Tinsels')
  elif (dice == 5): 
      print(dice) 
      print('Five Golden Rings') 
  elif (dice == 6): 
      print(dice)
      print('You got six gifts')
  else: 
     print('No Prizes, sorry') 

if __name__ == "__main__": 
  RollADice = FestiveDice() 
  print(RollADice)
