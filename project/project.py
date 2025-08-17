import sys
import re

def greeting():
    name=input("Name:")
        
    if " " in name:
        first,last=name.split(" ")
        if not first.isalpha() or not last.isalpha():
            sys.exit("Not a name.")
        elif not name.isalpha():
            sys.exit("Not a name.")
            
    mood= input(f"Hello, {name}, how is your feeling day?")
    if not re.match(r"^.+\w+[!.~\s]*$", mood):
        sys.exit("Invalid input.")
    
    else:
        print("♡ Let's start with a survey to see your stress level.")
        
answers=[]
def get_answer():
    #questions from PSS4(Cohen et al. 1983)
    questions=["In the last month, how often have you felt that you were unable to control the important things in your life? A:Never; B:Almost never; C:Sometimes; D:Fairly often; E:Very often",
               "In the last month, how often have you felt confident about your ability to handle your personal problems? A:Never; B:Almost never; C:Sometimes; D:Fairly often; E:Very often",
               "In the last month, how often have you felt that things were going your way? A:Never; B:Almost never; C:Sometimes; D:Fairly often; E:Very often",
               "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them? A:Never; B:Almost never; C:Sometimes; D:Fairly often; E:Very often"]
    
   
    print("Please answer with the correct corresponding letter.")
    for question in questions:
        while True:
            answer=input(question).upper()
            if answer in ["A","B","C","D","E"]:
                global answers
                answers.append(answer)
                break
                
            print("Invalid answer, please enter A,B,C,D or E.")
    return answers
            
def result():
    Q1_Q4={"A":0,"B":1,"C":2,"D":3,"E":4}
    Q2_Q3={"A":4,"B":3,"C":2,"D":1,"E":0}
    
    global answers
    
    Q1=Q1_Q4.get(answers[0])
    Q2=Q2_Q3.get(answers[1])
    Q3=Q2_Q3.get(answers[2])
    Q4=Q1_Q4.get(answers[3])
    result=Q1+Q2+Q3+Q4
    
    if result in range(0,5):
        print(f"Excellent news! Stress level:{result}. You are in a state of optimal performance.A blank page is now available for you. Feel free to use it to document this positive data, or create a to-do list to make the most of your joyful energy. Let's make today productive and happy")
        low_open_file()
    
    elif result in range(6,10):
        print(f"How are you feeling? Stress level :{result}. This is within a manageable range, but a brief pause is recommended. Let's play a game together. I have several ready to launch to help reset your mood.")
        mid_game_()
    
    elif result in range(11,16):
        print(f"Stress level :{result}.A high stress level has been detected. Let's take a break together. It's time to put down your work. I am now accessing my database for relaxing music to help you decompress. I'm here to help you get back to feeling balanced")
        high_music()
        
    return result
    
def low_open_file():
    diary= input("Welcome to write anything here.")
    with open("diary.txt", "a") as file:
        file.write(f"{diary}")
    

#def m7id_game_():
    #from games import 3 games.haha
    
    
#def high_music():
     #API youtube music for relaxing.


            
def main():
    greeting()
    get_answer()
    result()

main()
    
    