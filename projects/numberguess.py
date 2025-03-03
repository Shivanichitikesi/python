import random
from tkinter import *
from tkinter import messagebox
 
root=Tk()
root.geometry('400x350')
root.title("Number Guessing Game by Shivani Chitikesi")

Label(root,text='Number Guessing Game',font='arial 20 bold').pack()
  
target=0
score=10
guess=0

def add():
    return "The sum of target and guess is"+str(target+guess)
def sub():
    return "The difference of target and guess is"+str(target-guess)
def multi():
    return "The product of target and guess is"+str(target*guess)
def div():
    return "The division of target and guess is"+str(target/guess)
def comparision():
    if target>guess:
       return "The target is greater than guess "
    elif target<guess:
       return "The target is less than guess "

def clues():
    swicther={
        0:add(),
        1:sub(),
        2:multi(),
        3:div(),
        4:comparision()
    }
    return swicther.get(random.randint(0,4))

def target_generator():
    global target
    target=random.randint(1,50)
    messagebox.showinfo(message="Target Generated.Start guessing! Score is 10")
    random_num_button['state']=DISABLED
    guess_button['state']=NORMAL

def guess_and_score():
    global guess
    global score
    try:
        guess=0
        guess=int(guess_entry.get())
    except:
        messagebox.showerror(message="Enter a integer to guess")
        return
    if target==guess:
        messagebox.showinfo(message="Congrats correct guess!!! Your score is"+str(score))
        random_num_button['state']=NORMAL
        guess_button['state']=DISABLED
        return
    elif score==0:
        messagebox.showwarning(message="Oops!!! You run out off guesses")
        random_num_button['state']=NORMAL
        guess_button['state']=DISABLED
        return
    else:
        score-=1
        message=clues()
        messagebox.showinfo(message=message)

random_num_button=Button(root,text="Generate random number",font='arial 15 bold',command=target_generator)
random_num_button.pack()
Label(root,text='Enter your guess').pack()
guess_entry=Entry(root,width=5)
guess_entry.pack()
guess_button=Button(root,text="Guess",font='arial 15',command=guess_and_score,state=DISABLED)
guess_button.pack()

root.mainloop()