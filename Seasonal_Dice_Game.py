import random
def FestiveDice(): 
  dice = random.randrange(1,13)
  if (dice == 1): 
    print(dice)
    print('A Partridge in a pear tree') 
  elif(dice == 2): 
    print(dice)
    print('Two Turtle Doves') 
  elif(dice == 3): 
    print(dice)
    print('Three French Hens') 
  elif(dice == 4): 
    print(dice)
    print('Four Calling Birds') 
  elif(dice == 5): 
    print(dice)
    print('Five Golden Rings') 
  elif(dice == 6): 
    print(dice)
    print('Six Geese Laying') 
  elif(dice == 7): 
    print(dice)
    print('Seven Swans Swmming') 
  elif(dice == 8): 
    print(dice)
    print('Eight Maids Milking') 
  elif(dice == 9): 
    print(dice)
    print('Nine Ladies Dancing') 
  elif(dice == 10): 
    print(dice)
    print('Ten Lords Leaping') 
  elif(dice == 11): 
    print(dice)
    print('Eleven Pipers Piping') 
  elif(dice == 12): 
    print(dice)
    print('Twelve Drummers Drumming') 
  else: 
    print('No Number.') 

if __name__ == "__main__": 
    game_output = FestiveDice()
    print(game_output)
