from tkinter import messagebox
import tkinter as tk

import random
from tkinter import *
import time
import sys
import os
_width=200
_height=500
score=0

def New_window():
    window = tk.Toplevel()
    window.title("CowinMan")
    window.geometry("900x900")
    window.configure(bg='SkyBlue')
    word_list= ['VIRUS','SANITIZER','MASK','PANDEMIC','OUTBREAK','REOPNEN','LOCKDOWN','PATIENT','DISEASE','RECOVER','MEDICINE','IMPACT','ANTIBODY',
            'ISOLATION','OUTBREAK','TEST','RECOVER','ANTIBODY','SYMPTOM','CRISIS','APPOINTMENT','HEALTH','REOPEN']
    global chances
    chances =0
    label0=tk.Label(window,text=" COWINMAN!!  LET THE GAME BEGIN!",font=('Helvatica 25 bold '),fg="black").place(x=150,y=50)
    #canvas.create_window(150, 50, window=label0)
    Keypad=tk.Label(window,bg="pink",width=100,height=500).place(x=350,y=250)

    canvas=Canvas(window , width= _width , height=_height ,bg='white' )
    canvas.place(x=100,y=250)

    background_image=PhotoImage(file="Hanger.png")  
    my_background=canvas.create_image(0,0,image=background_image ,anchor=NW) 




    #adding all body parts        

    def restart_program():
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)         

    def newGame():

        global word_withSpaces
        """
        global chances
        chances =0 """

        word=random.choice(word_list)
        word_withSpaces = " ".join(word)
        display_word.set(' '.join("_"*len(word)))
        

    def guess(letter):
      global score
      wrong_word_count=0
      global chances
      if chances<7:
         txt = list(word_withSpaces)
         guessed = list(display_word.get())
      if word_withSpaces.count(letter)>0:
         for c in range(len(txt)):
             if txt[c]==letter:
                  guessed[c]=letter

             display_word.set("".join(guessed))




         if display_word.get()==word_withSpaces:
             score=6-chances
             convertedScore=str(score)
             messageString="You guessed it!Your score is "+convertedScore
             messagebox.showinfo("Hangman",messageString)

      else:
         chances += 1
         if chances<=6:
             if(chances==1) :
                wrong_guess_face() 
             if(chances==2) :
                wrong_guess_torso() 
             if(chances==3) :
                wrong_guess_right_hand()
             if(chances==4) :
                wrong_guess_left_hand()
             if(chances==5) :
                wrong_guess_right_leg()
             if(chances==6) :
                wrong_guess_left_leg()
         else :
             messagebox.showwarning("Hangman","Game Over")
            
            
            
            
            
            
            
            
            
            



    def wrong_guess_face():
            xvelocity=0
            yvelocity=-2
            #move head to the posituion of the hanger
            while(True) :
                coordinates_face= canvas.coords(my_image_face)
                print(coordinates_face)
                if(coordinates_face[1]==120):
                    yvelocity = 0
                    xvelocity=1
                    if(coordinates_face[0]==142) :
                        xvelocity=0
                        break;
                #canvas.move(my_image,yvelocity,yvelocity)
                canvas.move(my_image_face, xvelocity,yvelocity)
                time.sleep(0.0001)
                window.update()
    def wrong_guess_torso():
            xvelocity=0
            yvelocity=-2
            #move torso to the image
            while(True) :  #or while running :
                 coordinates = canvas.coords(my_image)
                 print(coordinates)
                # if(coordinates[0]>=20 or coordinates[0]<0):
                #     xVelocity = -xVelocity
                 if(coordinates[1]==178):
                     yvelocity = 0
                     xvelocity=1
                     if(coordinates[0]==144) :
                         xvelocity=0
                         break;
                 #canvas.move(my_image,yvelocity,yvelocity)

                 canvas.move(my_image, xvelocity,yvelocity)
                 time.sleep(0.0001)
                 window.update()

    def wrong_guess_right_hand() :
            xvelocity=0
            yvelocity=-2
            #move right hand to the torso
            #to move right hand
            while(True) :
                coordinates_hand= canvas.coords(my_image_righthand)
                print(coordinates_hand)
               # if(coordinates[0]>=20 or coordinates[0]<0):
               #     xVelocity = -xVelocity
                if(coordinates_hand[1]==174):
                    yvelocity = 0
                    xvelocity=1
                    if(coordinates_hand[0]==178) :
                        xvelocity=0
                        break;
                #canvas.move(my_image,yvelocity,yvelocity)
                canvas.move(my_image_righthand, xvelocity,yvelocity)
                time.sleep(0.0001)
                window.update()
    def wrong_guess_left_hand() :
            #move left hand to th
            xvelocity=0
            yvelocity=-2
            #move left hand to the torso
            #to move left hand
            while(True) :
                coordinates_lefthand= canvas.coords(my_image_lefthand)
                print(coordinates_lefthand)

                if(coordinates_lefthand[1]==180):
                    yvelocity = 0
                    xvelocity=-1
                    if(coordinates_lefthand[0]==125) :
                        xvelocity=0
                        break;
                #canvas.move(my_image,yvelocity,yvelocity)
                canvas.move(my_image_lefthand, xvelocity,yvelocity)
                time.sleep(0.0001)
                window.update()       

    def wrong_guess_right_leg() :
               xvelocity=0
               yvelocity=-2
                 #to move right leg
               while(True) :
                     coordinates_right_leg= canvas.coords(my_image_rightleg)
                     print(coordinates_right_leg)

                     if(coordinates_right_leg[1]==232):
                         yvelocity = 0
                         xvelocity=1
                         if(coordinates_right_leg[0]==158) :
                             xvelocity=0
                             break;
                     #canvas.move(my_image,yvelocity,yvelocity)
                     canvas.move(my_image_rightleg, xvelocity,yvelocity)
                     time.sleep(0.0001)
                     window.update()
    def wrong_guess_left_leg() :
            #to move left leg
               xvelocity=0
               yvelocity=-2
                 #move left hand to the torso
                 #to move right leg
               while(True) :
                     coordinates_left_leg= canvas.coords(my_image_leftleg)
                     print(coordinates_left_leg)

                     if(coordinates_left_leg[1]==230):
                         yvelocity = 0
                         xvelocity=1
                         if(coordinates_left_leg[0]==128) :
                             xvelocity=0
                             break;
                     #canvas.move(my_image,yvelocity,yvelocity)
                     canvas.move(my_image_leftleg, xvelocity,yvelocity)
                     time.sleep(0.0001)
                     window.update()
                     
    display_word = tk.StringVar()
    tk.Label(window, textvariable  =display_word,fg="black",height=5,width=30).place(x=550,y=150)
    tk.Button(window,text="A",font=('Helvatica 10 bold '),command=lambda: guess("A"),bg="white",fg="black",height="3",width="4").place(x=500,y=300)

    tk.Button(window,text="B",font=('Helvatica 10 bold '),command=lambda: guess("B"),bg="white",fg="black",height="3",width="4").place(x=550,y=300)

    tk.Button(window,text="C",font=('Helvatica 10 bold '),command=lambda: guess("C"),bg="white",fg="black",height="3",width="4").place(x=600,y=300)


    tk.Button(window,text="D",font=('Helvatica 10 bold '),command=lambda: guess("D"),bg="white",fg="black",height="3",width="4").place(x=650,y=300)

    tk.Button(window,text="E",font=('Helvatica 10 bold '),command=lambda: guess("E"),bg="white",fg="black",height="3",width="4").place(x=700,y=300)
    tk.Button(window,text="F",font=('Helvatica 10 bold '),command=lambda: guess("F"),bg="white",fg="black",height="3",width="4").place(x=500,y=375)
    tk.Button(window,text="G",font=('Helvatica 10 bold '),command=lambda: guess("G"),bg="white",fg="black",height="3",width="4").place(x=550,y=375)
    tk.Button(window,text="H",font=('Helvatica 10 bold '),command=lambda: guess("H"),bg="white",fg="black",height="3",width="4").place(x=600,y=375)
    tk.Button(window,text="I",font=('Helvatica 10 bold '),command=lambda: guess("I"),bg="white",fg="black",height="3",width="4").place(x=650,y=375)



    tk.Button(window,text="J",font=('Helvatica 10 bold '),command=lambda: guess("J"),bg="white",fg="black",height="3",width="4").place(x=700,y=375)
    tk.Button(window,text="K",font=('Helvatica 10 bold '),command=lambda: guess("K"),bg="white",fg="black",height="3",width="4").place(x=500,y=450)
    tk.Button(window,text="L",font=('Helvatica 10 bold '),command=lambda: guess("L"),bg="white",fg="black",height="3",width="4").place(x=550,y=450)
    tk.Button(window,text="M",font=('Helvatica 10 bold '),command=lambda: guess("M"),bg="white",fg="black",height="3",width="4").place(x=600,y=450)
    tk.Button(window,text="N",font=('Helvatica 10 bold '),command=lambda: guess("N"),bg="white",fg="black",height="3",width="4").place(x=650,y=450)


    tk.Button(window,text="O",font=('Helvatica 10 bold '),command=lambda: guess("O"),bg="white",fg="black",height="3",width="4").place(x=700,y=450)
    tk.Button(window,text="P",font=('Helvatica 10 bold '),command=lambda: guess("P"),bg="white",fg="black",height="3",width="4").place(x=500,y=525)
    tk.Button(window,text="Q",font=('Helvatica 10 bold '),command=lambda: guess("Q"),bg="white",fg="black",height="3",width="4").place(x=550,y=525)
    tk.Button(window,text="R",font=('Helvatica 10 bold '),command=lambda: guess("R"),bg="white",fg="black",height="3",width="4").place(x=600,y=525)
    tk.Button(window,text="S",font=('Helvatica 10 bold '),command=lambda: guess("S"),bg="white",fg="black",height="3",width="4").place(x=650,y=525)

    tk.Button(window,text="T",font=('Helvatica 10 bold '),command=lambda: guess("T"),bg="white",fg="black",height="3",width="4").place(x=700,y=525)
    tk.Button(window,text="U",font=('Helvatica 10 bold '),command=lambda: guess("U"),bg="white",fg="black",height="3",width="4").place(x=500,y=600)
    tk.Button(window,text="V",font=('Helvatica 10 bold '),command=lambda: guess("V"),bg="white",fg="black",height="3",width="4").place(x=550,y=600)
    tk.Button(window,text="W",font=('Helvatica 10 bold '),command=lambda: guess("W"),bg="white",fg="black",height="3",width="4").place(x=600,y=600)
    tk.Button(window,text="X",font=('Helvatica 10 bold '),command=lambda: guess("X"),bg="white",fg="black",height="3",width="4").place(x=650,y=600)
    tk.Button(window,text="Y",font=('Helvatica 10 bold '),command=lambda: guess("Y"),bg="white",fg="black",height="3",width="4").place(x=700,y=600)
    tk.Button(window,text="Z",font=('Helvatica 10 bold '),command=lambda: guess("Z"),bg="white",fg="black",height="3",width="4").place(x=750,y=600)
    #n=0
    #for c in ascii_uppercase:
        #tk.Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'),bg="white",fg="black",width=30,height=5).grid(row=1+n//9,column=n%9)
        #n+=1

    tk.Button(window,text="RESTART",font=('Helvatica 7 bold '),bg="white",fg="red",height="4",width="6", command=restart_program).place(x=750,y=525)

    tk.Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).place(x=750,y=300) 
    photo_image_face=PhotoImage(file="face.png") 
    my_image_face=canvas.create_image(20,340,image=photo_image_face ,anchor=SW)
    #leftleg
    photo_image_leftleg=PhotoImage(file="left.png")
    my_image_leftleg=canvas.create_image(80,400, image=photo_image_leftleg , anchor =SW)
    #right leg
    photo_image_rightleg=PhotoImage(file="right.png")
    my_image_rightleg=canvas.create_image(140,400, image=photo_image_rightleg , anchor =SW)
    #lefthand
    photo_image_lefthand=PhotoImage(file="left_hand.png")
    my_image_lefthand=canvas.create_image(140,340,image=photo_image_lefthand , anchor=SW)
    #righthand
    photo_image_righthand =PhotoImage(file="Right_hand.png" )
    my_image_righthand=canvas.create_image(80,340,image=photo_image_righthand , anchor=SW)

    photo_image=PhotoImage(file="torso.png")
    #add photo image to canvas
    my_image=canvas.create_image( 20,400 ,image= photo_image , anchor=SW)  
    window.mainloop()