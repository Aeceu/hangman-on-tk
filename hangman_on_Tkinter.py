from glob import glob
from tkinter import *
from tkinter import messagebox
import random

#Game variables
guess = ['smile', 'angers', 'depress','happy','excite','memorize']
word_chose = random.choice(guess)
word = 'ANGERS'#word_chose.upper()
lives = len(word) + 3
letters = ''

root = Tk()
root.title("Hangman")
root.geometry('400x600+700+200')
root.configure(bg = "#1f1f1f")
root.resizable = (False, False)




def get_user_A():
    global letters
    global lives
    global word_to_guess
    letter = 'A'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_B():
    global letters
    global lives
    global word_to_guess
    letter = 'B'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_C():
    global letters
    global lives
    global word_to_guess
    letter = 'C'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_D():
    global letters
    global lives
    global word_to_guess
    letter = 'D'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_E():
    global letters
    global lives
    global word_to_guess
    letter = 'E'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_F():
    global letters
    global lives
    global word_to_guess
    letter = 'F'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_G():
    global letters
    global lives
    global word_to_guess
    letter = 'G'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_H():
    global letters
    global lives
    global word_to_guess
    letter = 'H'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_I():
    global letters
    global lives
    global word_to_guess
    letter = 'I'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_J():
    global letters
    global lives
    global word_to_guess
    letter = 'J'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_K():
    global letters
    global lives
    global word_to_guess
    letter = 'K'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_L():
    global letters
    global lives
    global word_to_guess
    letter = 'L'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_M():
    global letters
    global lives
    global word_to_guess
    letter = 'M'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_N():
    global letters
    global lives
    global word_to_guess
    letter = 'N'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_O():
    global letters
    global lives
    global word_to_guess
    letter = 'O'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_P():
    global letters
    global lives
    global word_to_guess
    letter = 'P'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_Q():
    global letters
    global lives
    global word_to_guess
    letter = 'Q'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_R():
    global letters
    global lives
    global word_to_guess
    letter = 'R'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_S():
    global letters
    global lives
    global word_to_guess
    letter = 'S'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_T():
    global letters
    global lives
    global word_to_guess
    letter = 'T'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_U():
    global letters
    global lives
    global word_to_guess
    letter = 'U'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_V():
    global letters
    global lives
    global word_to_guess
    letter = 'V'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_W():
    global letters
    global lives
    global word_to_guess
    letter = 'W'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_X():
    global letters
    global lives
    global word_to_guess
    letter = 'X'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_Y():
    global letters
    global lives
    global word_to_guess
    letter = 'Y'
    if letter not in letters:
        word_to_guess.pack_forget()
        letters+=letter
        lives-=1
        word_list = [i if i in letters.upper() else '-' for i in word]
        word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
        word_to_guess.pack()
    else:
        messagebox.showerror("Invalid","Already been type!")
    return word_to_guess,lives
def get_user_Z():
        global letters
        global lives
        global word_to_guess
        letter = 'Z'
        if letter not in letters:
            word_to_guess.pack_forget()
            letters+=letter
            lives-=1
            word_list = [i if i in letters.upper() else '-' for i in word]
            word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
            word_to_guess.pack()
        else:
            messagebox.showerror("Invalid","Already been type!")
        return word_to_guess,lives
def game_over():
    root.withdraw()
    screen = Toplevel(root)
    screen.title("Hangman")
    screen.geometry('400x600+700+200')
    screen.configure(bg = "#1f1f1f")
    Label(screen,text="Hello Everyone!",bg = '#1f1f1f',fg='white',font = ('Calibri(Body)',30,'bold')).pack(expand=True)
    screen.mainloop()





#Text at the top
game_title = Label(root,text='Hangman', fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',23,'bold'))
game_title.pack()

#Blanks words and need to be reveal 
word_list = [i if i in letters.upper() else '-' for i in word]
word_to_guess = Label(root, text = word_list, fg = 'white', bg = '#1f1f1f',font =('Microsoft Yahei UI Light',30))
word_to_guess.pack()
if '-' not in word_list:
    messagebox.showerror("HANGMAN","YOU WON!!!")

a = Button(root,text='A',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_A).place(x=10,y=300)
b = Button(root,text='B',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_B).place(x=60,y=300)
c = Button(root,text='C',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_C).place(x=110,y=300)
d = Button(root,text='D',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_D).place(x=160,y=300)
e = Button(root,text='E',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_E).place(x=210,y=300)
f = Button(root,text='F',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_F).place(x=260,y=300)
g = Button(root,text='G',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_G).place(x=310,y=300)
h = Button(root,text='H',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_H).place(x=360,y=300)
i = Button(root,text='I',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_I).place(x=10,y=370)
j = Button(root,text='J',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_J).place(x=60,y=370)
k = Button(root,text='K',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_K).place(x=110,y=370)
l = Button(root,text='L',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_L).place(x=160,y=370)
m = Button(root,text='M',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_M).place(x=210,y=370)
n = Button(root,text='N',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_N).place(x=260,y=370)
o = Button(root,text='O',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_O).place(x=310,y=370)
p = Button(root,text='P',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_P).place(x=360,y=370)
q = Button(root,text='Q',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_Q).place(x=10,y=440)
r = Button(root,text='R',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_R).place(x=60,y=440)
s = Button(root,text='S',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_S).place(x=110,y=440)
t = Button(root,text='T',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_T).place(x=160,y=440)
u = Button(root,text='U',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_U).place(x=210,y=440)
v = Button(root,text='V',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_V).place(x=260,y=440)
w = Button(root,text='W',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_W).place(x=310,y=440)
x = Button(root,text='X',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_X).place(x=360,y=440)
y = Button(root,text='Y',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_Y).place(x=160,y=510)
z = Button(root,text='Z',width=5,height=3,font = ('Times new roman',10,'bold'),command=get_user_Z).place(x=210,y=510)  
restart = Button(root,text='Enter',width=25,height=3,font = ('Times new roman',10,'bold'),command=game_over).place(x=260,y=510)


root.mainloop()






    



