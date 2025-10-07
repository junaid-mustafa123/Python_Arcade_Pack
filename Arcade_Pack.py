import random as rd 
class Arcade_Pack:
    def __init__(self):
        self.total_Win = 0
        self.total_lose = 0
        self.total_game = 0
        self.attempts = 0
        self.user = 0
        self.comp = 0
      
    
    def Welcome(self):
        print("""
===============================================
              WELCOME TO PYTHON ARCADE PACK
              _______________________________
              (MINI GAMES COLLECTION)
              HERE YOU WILL PLAY DIFFERENT GAMES 
              ON YOUR CHOICE TOTAL FOUR GAMES 
===============================================
""")
        
    def User_Info(self):
        print("""
------------------------------------------              
| BEFORE STARTING THE GAME .......
| WE NEED USER DATA SO GIVING DATA 
| IS MOST IMPORTANT ,AND THIS DATA
| WILL BE STORE IN TXT FILE FOR PERMINANT
-------------------------------------------""")
        with open("User_Data.txt",'w') as f:
            name = input("ENTER YOUR NAME : ").strip().upper()
            dept = input("ENTER YOUR DEPT NAME : ").strip().upper()
            r_no = input("Enter YOUR  ROLL NUMBER : ")
            phone = input("ENTER YOUR PHONE NUMBER : ")
            f.writelines("""\n---------------------------\n    USER INFORMATION  \n ---------------------------\n""")
            f.writelines(f"NAME : {name}\nDEPT : {dept}\nROLL_NO : {r_no}\nPHONE : {phone}\n")
            return """
-------------------------------
DATA HAS BEEN SAVED IN TXT FILE
---------------------------------"""
    def  Game_Menu(self):
        return """
======MENU======        
1️⃣  Number Guessing.
2️⃣  Rock Paper Scissors.
3️⃣  Dice Rolling Game.
4️⃣  Lottery Simulator.
5️⃣  Exit.
=================
"""
    def Number_Guessing(self):
        self.total_game+=1
        print("""
YOU SELECTED OPTION 1 TO PLAY NUMBER GUESSING
              -------
              LEVELS 
              --------
              |1.EASY (1 T0 10)
              |2.MEDIUM (1 T0 50)
              |3.HARD (50 TO 100)
""")
        option = int(input("SELECT THE LEVEL YOU WANT TO PLAY : "))
        level_name = input("ENTER THE LEVEL NAME : ").upper()
        try:
            if option == 1:
                for i in range(3):
                    self.attempts +=1
                    r1=rd.randint(1,10)
                    num = int(input("ENTER A NUMBER BETWEEN (1 TO 10) : "))
                    if r1==num:
                        self.total_Win+=1
                        self.user +=1
                        print("----------------")
                        print(f"YOU WIN ! :{r1}")
                        print("----------------")
                        break
                    else:
                        self.total_lose+=1
                        self.user+=1
                        print("----------------")
                        print(f"YOU LOSE ! :{r1}")
                        print("----------------")
                else:
                    print("-----------------------")
                    print("RANGE HAS BEEN COMPLETE")
                    print("-------------------------")       
            elif option == 2:
                r1 = rd.randint(1,50)
                for i in range(3):
                    r1 = rd.randint(1,50)
                    self.attempts +=1
                    num = int(input("ENTER A NUMBER BETWEEN (1 TO 50) : "))
                    if r1==num:
                        self.total_Win+=1
                        self.user +=1
                        print("----------------")
                        print(f"YOU WIN ! :{r1}")
                        print("----------------")
                        break
                    else:
                        self.total_lose+=1
                        self.comp +=1
                        print("------------------")
                        print(f"YOU LOSE ! :{r1}")
                        print("-------------------")
                else:
                    print("-----------------------")
                    print("RANGE HAS BEEN COMPLETE")
                    print("-------------------------") 
                        
            elif option == 3:
                for i in range(3):
                    self.attempts +=1
                    r1 = rd.randint(1,100)
                    num = int(input("ENTER A NUMBER BETWEEN (1 TO 100) : "))
                    if r1==num:
                        self.total_Win+=1
                        self.user +=1
                        print("----------------")
                        print(f"YOU WIN ! :{r1}")
                        print("----------------")
                        break
                    else:
                        self.total_lose+=1
                        self.comp +=1
                        print("----------------")
                        print(f"YOU LOSE ! :{r1}")
                        print("----------------")
                else:
                    print("-----------------------")
                    print("RANGE HAS BEEN COMPLETE")
                    print("-------------------------")         

            else:
                print("---------------------")
                print("❌ OPTION SORRY !")
                print("---------------------")
        except Exception as e :
            print(f"ERROR : {e}")  
        record_dict = {"ATTEMPTS":self.attempts,
                       "USER SCORE":self.user,
                       "COMPUTER":self.comp}  
        for i in record_dict:
            print(i,":",record_dict[i])  
        else:
            print("--------------------------")    
        with open("Number_Guessing_Record",'w') as f:   
            f.write("----------------------------\n") 
            f.write("GAME NAME : NUMBER GUESSING\n")
            f.writelines(f"LEVEL NAME : {level_name}\nWIN : {self.user}\nLOSE : {self.comp}\nATTEMPTS : {self.attempts}")
            return """
            ===========================
            RECORD HAS BEEN SAVED IN TXT
            ============================""" 
           
        
    def Rock_Paper_Scissors(self):
        self.total_game+1
        print("""
        ___________________      
        Rock Paper Scissors
        ___________________  
THIS GAME CONTAIN THREE EMOJI
              1.ROCK 
              2.PAPER
              3.SCISSOR
_____________________________________________              
THIS WILL BE PLAYED BETWEEN TWO USER..... 
ONE IS COMPUTER AND SECOND IS USER..... 
SCORE WILL BE ADD ON THE BEHALF OF EMOJI......
____________________________________________              
""")
        emoji_list = ['🪨','📃','✂️']
        for i in range(3):
            self.attempts +=1
            result = rd.choice(emoji_list)
            emj = input("Enter the Emoji( ✂️ , 🪨 , 📃 ) which you want to show : ").strip()
            if result == '🪨' and emj == '✂️':
                self.total_lose +=1
                self.comp +=1
                print("----------------------------------------")
                print(f"COMPUTER : {result}  AND   USER : {emj}")
                print("----------------------------------------")
                print("COMPUTER WIN !")
                print("----------------")
            elif result == '✂️' and emj == '🪨':
                self.total_Win+=1
                self.user +=1
                print("----------------------------------------")
                print(f"COMPUTER : {result}  AND   USER : {emj}")
                print("----------------------------------------")
                print("USER WIN !")

            elif result == '📃' and emj == '🪨':
                self.total_lose +=1
                self.comp +=1
                print("----------------------------------------")
                print(f"COMPUTER : {result}  AND   USER : {emj}")
                print("----------------------------------------")
                print("COMPUTER WIN ")
            elif result ==  '📃' and emj == '✂️':
                self.total_Win+=1
                self.user +=1
                print("----------------------------------------")
                print(f"COMPUTER : {result}  AND   USER : {emj}")
                print("----------------------------------------")
                print("USER WIN ")

            elif result =='📃' and  emj == '📃': 
                print("----------") 
                print("BOTH LOSE")  
                print("----------") 

            elif result =='✂️' and emj == '✂️':  
                print("----------") 
                print("BOTH LOSE")  
                print("----------")
            elif result == '🪨' and emj == '🪨':  
                print("----------") 
                print("BOTH LOSE")  
                print("----------")   
            else:
                print("-----------------")
                print("❌  WRONG INPUT") 
                print("------------------") 
        else:
            pass        
        print("    FINAL RESULT      ")
        print("------------------------")    
        record_dict = {"ATTEMPTS ":self.attempts,
                           "USER SCORE":self.user,
                           "COMPUTER SCORE":self.comp}   
        for i in record_dict:
            print(i, ":",record_dict[i])
        else:
            print("------------------------")    

        with open("Rock_Paper_Scissors_Record.txt",'w') as f:
            f.write("\n------------------------\n")
            f.write("GAME NAME :  Rock Paper Scissors")    
            f.writelines(f"ATTEMPTS : {self.attempts}\nUSER SCORE : {self.user}\nCOMPUTER SCORE : {self.comp}")
            return """
            ===========================
            RECORD HAS BEEN SAVED IN TXT
            ============================""" 

    def Dice_Rolling_Game(self):
        self.total_game+=1
        for i in range(3):
            self.attempts +=1
            result = rd.randint(1,6)
            user_dice = int(input("ROLL THE DICE (1 TO 6) : "))
            if result >user_dice:
                self.total_lose+=1
                self.comp +=1
                print("--------------------------")
                print(f"COMPUTER WIN : {result}")
                print("---------------------------")
            elif result < user_dice:
                self.total_Win+=1
                self.user +=1
                print("--------------------------")
                print(f"USER  WIN {result}")
                print("---------------------------")
                break
            elif result == user_dice :
                print("-------------------------")
                print(f"BOTH lose : {result}")    
                print("-------------------------")
            else:
                pass
        else:
            print("-----------------------------")
            print("GAME RANGE HAS BEEN COMPLETE") 
            print("-----------------------------")  
        r_dict = {"ATTEMPTS":self.attempts,
                  "USER SCORE":self.user,
                  "COMPUTER SCORE":self.comp}
        print("      FINAL RESULT ")
        print("------------------------------")
        for i in r_dict:
            print(i, ":" , r_dict[i])  
        else:
            print("------------------------------") 
        with open("Dice_Rolling_Game_Record.txt",'w') as f:
            f.write("\n---------------------------------\n")
            f.write("GAME NAME : Dice Rolling Game\n")  
            f.writelines(f"USER SCORE : {self.user}\nCOMPUTER SCORE : {self.comp}\nATTEMPTS : {self.attempts}")      
            return """
            ===========================
            RECORD HAS BEEN SAVED IN TXT
            ============================""" 
            
        
    def Lottery_Simulator(self):
        self.total_game+=1
        print("""
              ============================
              WELCOME TO LOTTERY SIMULATOR
              =============================
              THIS PROGRAM TAKE 6 DIGIT AND 
              CAMPARE WITH 6 COMPUTER GENER-
              ATED NUMBERS IF EQUAL MEANS U-
              SER WIN IT NOT EUQAL MEANS COM-
              PUTER WIN.....
              =============================
              """)
        num_list = [123456,234567,345678,456789,567890,678900]
        result = rd.choice(num_list)
        for i in range(3):
            self.attempts +=1
            result = rd.choice(num_list)
            num = int(input("ENTER 6 DIGITS : "))
            if num == result:
                self.total_Win+=1
                self.user +=1
                print("-----------")
                print("USER WIN !")
                print("------------")
                break
            else:
                self.comp+=1
                self.total_lose+=1
                print("-------------")
                print("Computer win")
                print("--------------")
        else:
            print("-----------------------------")
            print("GAME RANGE HAS BEEN COMPLETE") 
            print("------------------------------")
        r_dict = {"ATTEMPTS":self.attempts,
                  "USER SCORE":self.user,
                  "COMPUTER SCOR":self.comp} 
        for i in r_dict:
            print(i, ":", r_dict[i])    

        with open("Lottery_Simulator_Record.txt",'w') as f:
            f.write("\n---------------------\n")
            f.write("GAME NAME :Lottery Simulator\n")     
            f.writelines(f"ATTEMPTS : {self.attempts}\nUSER SCORE : {self.user}\nCOMPUTER SCORE : {self.comp}") 
            return """
            ===========================
            RECORD HAS BEEN SAVED IN TXT
            ============================""" 
  

    def Exit(self):
        try:
            with open("User_Data.txt",'r') as f:
                l1=f.readlines()
                for i in l1:
                    print(i)
            with open("Number_Guessing_Record",'r') as j:
                l2=j.readlines()  
                for i in l2:
                    print(i) 
            with open("Rock_Paper_Scissors_Record.txt",'r') as k:
                l3 = k.readline()
                for i in l3:
                    print(i)     
            with open("Dice_Rolling_Game_Record.txt",'r') as l:
                l4 = l.readlines()
                for i in l4:
                    print(i)  
            with open("Lottery_Simulator_Record.txt",'r') as m:
                l5 = m.readlines()
                for i in l5:
                    print(i)                     
        except FileExistsError as e:
            print(f"Error : {e}")    

    def final_record(self):
        return f"""
=====================================
TOTAL GAMES : {self.total_game}
TOTAL WINS : {self.total_Win}
TOTAL LOSE : {self.total_lose}
=====================================
"""  
    def thanks(self):

        return ("""============================================="
            I hope you enjoyed this Arcade Pack project! 💻 
            It’s a small step in my Python learning journey,
            and I hope it inspires you too. Keep learning — 
            and remember me in your prayers! 🙏✨
            =============================================""")


pack = Arcade_Pack()
pack.Welcome()   
print(pack.User_Info())  
while True:
    print(pack.Game_Menu()) 
    Choice = int(input("SECLECT THE GAME WHICH U WANT TO PLAY (1 TO 4) : "))
    match Choice:
        case 1:
            print(pack.Number_Guessing())
        case 2:
            print(pack.Rock_Paper_Scissors())
        case 3: 
            print(pack.Dice_Rolling_Game()) 
        case 4:
            print(pack.Lottery_Simulator())       
        case 5:
            print(pack.final_record())
            pack.Exit()  
            print(pack.thanks())
            break    
        case _:
            print("------------------------------------")
            print("❌ WRONG INPUT ! TRY AGAIN")
            print("------------------------------------")
   








        






    


