
import main
import tkinter as tk


root = tk.Tk()

root.configure(bg='yellow')
root.geometry("600x300")
input_text=tk.StringVar();
img = tk.PhotoImage(file=r'C:\Users\HP-PC\Desktop\minipsdl\backhang.png')
label = tk.Label( root, image=img)
label.place(x=18,y=10)
tk.Label(root,text="Welcome to CoWinMan!!!",font="Helvetica 15 bold",fg="white",bg="black").pack(side="top")
tk.Label(root,text="Hint:Words related to covid!",font="Helvetica 10 bold",fg="white",bg="black").pack(side="bottom")
button = tk.Button(root, text="START", bg='White', fg='Black',
                              command=lambda:main.New_window() )

button.pack(side="top")
'''list_data=[E1,main1.score]
with open('CSVFILE.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(list_data)  
    f_object.close()
'''
root.mainloop()