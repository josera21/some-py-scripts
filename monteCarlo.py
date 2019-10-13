import random

# Global variable
throws = 0

def rollDice():
  dice = random.randint(1,6)
  return dice

def playGame(n = 3):
  global throws
  info = []
  point = 0

  for i in range(0,n):
    gameId = i+1
    balance = 0
    throws = 0
    result = rollDice() + rollDice()
    throws += 1

    print("Juego " + str(i+1))
    print("Suma de dados: " + str(result))
    

    if result == 7 or result == 11:
      balance += 10
    else:
      point = result
      endgame = False
      print("** etapa 2 **")
      while not endgame:
        result = rollDice() + rollDice()
        throws += 1
        print("Suma de dados: " + str(result))
        if result == 7:
          balance -= 10
          endgame = True
        else:
          if result == point:
            balance += 5
            endgame = True
    info.append({ "balance": balance, "throws": throws, "gameId": gameId })
  return info


if __name__=="__main__":
  n = 3
  games = playGame(n)
  prom = 0
  
  for data in games:
    prom += data["balance"]

    
    print("Juego: " + str(data["gameId"]))
    print("Ganancia: "+ str(data["balance"]))
    print("Lanzamientos: " + str(data["throws"]))
    
  print("--- Despues de " + str(n) + " juegos ---")
  print("Ganancia promedio: ", round((prom / float(n)), 2))