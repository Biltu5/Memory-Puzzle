###### Important libraries
from tkinter import  *
from tkinter.messagebox import  *
from  PIL import  (Image,ImageTk)
import random
import time
from tkinter.ttk import  *
from pygame import  mixer

###### Root mathods
root=Tk()
root.geometry('425x640+450+15')
root.resizable(False,False)
root.configure(bg='ghost white')
root.title('Memory Booster')

###### Resources
gallery= {}
gallery1={}
db= {}
btn=[]
c1=c2=False
old=''
old_number=None
chance=20
score=0

gallery1['base.jpg']=ImageTk.PhotoImage(Image.open('Images/base.jpg'). resize(( 75,105)))
gallery1['bg.jpg']=ImageTk.PhotoImage(Image.open('Images/bg.jpg'). resize(( 75,105)))
for i in range (1,46):
    photo=Image.open(f'Images/{i}.jpg').resize( (75,105))
    img=ImageTk.PhotoImage(photo)
    gallery[f'{i}.jpg']=img

###### check game over
def check():
    global score,chance
    bool=False
    
    if score==200:
        bool=True
        showinfo('hurrah!!',f'  You win\nYour score : {score}')
        
    if score!=200 and chance==0:
        bool=True
        showinfo('Ohho!!',f'Your score : {score}\n   You lose')
        
    if bool:
        ans=askyesno('Author','Do you want to continue ?')
        if ans:
            score=0
            chance=20
            for i in range(0,20):
                btn[i].configure(image=gallery1['base.jpg'])
            distribution()
        else:
            root.destroy()

###### head of my game
def click(event):
    global c1,c2, old,old_number,score,chance
    t=event.widget.cget("image")
    if t[0]=='pyimage2' :
        return 
        
    if c1:
        c2=True
    
    #play music when you touch a file
    mixer.init()    
    mixer.music.load('Sounds/wing.ogg')
    mixer.music.play()
    
    c1=True
    text = event.widget.cget("text")
    n=int(text)
    btn[n].configure(image=db[text],text=text)
    btn[n].update()
    
    if c1 and c2:
        chance-=1
        c1=False
        c2=False
        time.sleep(1)
        if old==db[text] and old_number!=n:
            #play music when you score
            mixer.music.load('Sounds/point.ogg')
            mixer.music.play()
            score+=20
            btn[old_number].configure(image=gallery1['bg.jpg'])
            btn[n].configure(image=gallery1['bg.jpg'])
        else:
            btn[old_number].configure(image=gallery1['base.jpg'])
            btn[n].configure(image=gallery1['base.jpg'])
    
    check()      
    old=db[text]
    old_number=n

###### Database for game
###### heart of my game
def distribution():
    global db
    number_list=[]
    for I in range(0,20):
        number_list.append(I)
        
    for i in range(0,10):
        c=random.choice(list(gallery.values()))
        n1=random.choice(number_list)
        number_list.remove(n1)
        n2=random.choice(number_list)
        number_list.remove(n2)
        db[f'{n1}']=c
        db[f'{n2}']=c
    showinfo('Rule','You have 20 chances \nto complete this game !!')
    
###### Start game 
def start():
    global btn
    
    for i in range(1,21):
        btn.append(Button(root,text=f'{i-1}',image=gallery1['base.jpg']))
        btn[i-1].bind("<Button-1>",click)
    
    btn[0].place(x=20,y=10)
    btn[1].place(x=120,y=10)
    btn[2].place(x=220,y=10)
    btn[3].place(x=320,y=10)
    btn[4].place(x=20,y=135)
    btn[5].place(x=120,y=135)
    btn[6].place(x=220,y=135)
    btn[7].place(x=320,y=135)
    btn[8].place(x=20,y=260)
    btn[9].place(x=120,y=260)
    btn[10].place(x=220,y=260)
    btn[11].place(x=320,y=260)
    btn[12].place(x=20,y=385)
    btn[13].place(x=120,y=385)
    btn[14].place(x=220,y=385)
    btn[15].place(x=320,y=385)
    btn[16].place(x=20,y=510)
    btn[17].place(x=120,y=510)
    btn[18].place(x=220,y=510)
    btn[19].place(x=320,y=510)
    distribution()

#Handling the event when the user want to close window 
def close_window():
    feedback=askyesno("Memory Booster","If you close this window, \ngame will be automatically stopped ")
    if feedback:
        root.destroy()
        
start()
root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()
