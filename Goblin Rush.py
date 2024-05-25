from ast import Not
from random import Random, randint
from tracemalloc import stop
Goblin_hp = 100
Player_hp = 100
Recharge = 0
ERecharge = 0
import random
print("𝐆𝐎𝐁𝐋𝐈𝐍 𝐑𝐔𝐒𝐇")
input("Press ENTER to play")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
win = 0




#Player\/



while (Goblin_hp > 0 and Player_hp > 0):
     print("Goblin HP:",Goblin_hp)
     print("Player HP:",Player_hp)
     print("")
     if (Recharge == 0):
          inputy = input("enter A to attack or B to use a strong attack   ")
          if (inputy == "a" or inputy == "A"):
            roll = randint(3, 20)
            Goblin_hp = Goblin_hp - roll
            print("")
            print("You attack the goblin")
            print("")
            if (Goblin_hp < 0):
                Goblin_hp = 0
            print("You deal",roll,"damage leaving the goblin at",Goblin_hp,"HP")
            print("")
            input("Press ENTER to continue")
            print("")
            print("")
            print("")
            if (Goblin_hp < 1):
                print("You win🎉🎉🎉🎉")
                win = 1
          else:
            if (inputy == "b" or inputy == "B"):
              roll = randint(10, 60)
              Goblin_hp = Goblin_hp - roll
              print("")
              print("You attack the goblin with a strong attack")
              print("")
              if (Goblin_hp < 0):
                Goblin_hp = 0
              print("You deal",roll,"damage leaving the goblin at",Goblin_hp,"HP")
              print("")
              input("Press ENTER to continue")
              print("")
              print("")
              print("")
              Recharge = 1
              if (Goblin_hp < 1):
                print("You win🎉🎉🎉🎉")
                win = 1
     else:
          print("")
          print("You are regaining energy from the last attack")
          Recharge = 0
          print("")
          input("Press ENTER to continue")
          print("")
          print("")
          print("")



#Goblin\/


     if (win == 0):
       if (Goblin_hp > 79):
           inputy = random.choice (["b", "b", "b", "b", "a"])
       else:
           if (Goblin_hp > 59):
             inputy = random.choice (["a", "b", "b"])
           else:
               if (Goblin_hp > 19):
                 inputy = random.choice (["a", "a", "a" "b"])
               else:
                       inputy = random.choice (["a", "b", "b", "b"])
       if (ERecharge == 0):
             if (inputy == "a" or inputy == "A"):
               roll = randint(3, 20)
               Player_hp = Player_hp - roll
               print("")
               print("The goblin attacks you")
               print("")
               if (Player_hp < 0):
                   Player_hp = 0
               print("The goblin deals",roll,"damage leaving you at",Player_hp,"HP")
               print("")
               input("Press ENTER to continue")
               print("")
               print("")
               print("")
               if (Player_hp < 1):
                 print("You lose💀💀💀💀")
             else:
               if (inputy == "b" or inputy == "B"):
                 roll = randint(10, 60)
                 Player_hp = Player_hp - roll
                 print("")
                 print("The goblin attacks you with a strong attack")
                 print("")
                 if (Player_hp < 0):
                   Player_hp = 0
                 print("The goblin deals",roll,"damage leaving you at",Player_hp,"HP")
                 print("")
                 input("Press ENTER to continue")
                 print("")
                 print("")
                 print("")
                 ERecharge = 1
                 if (Player_hp < 1):
                   print("You lose💀💀💀💀")
       else:
             print("")
             print("The goblin is regaining energy from the last attack")
             print("")
             input("Press ENTER to continue")
             print("")
             print("")
             print("")
             ERecharge = 0