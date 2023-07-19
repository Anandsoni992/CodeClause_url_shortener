import pyshorteners 
from tkinter import * 

window = Tk() 
window.geometry("400x270") 
window.configure(bg="black") 
#button function 
def shortenurl(): 
    url = ent.get() 
    s = pyshorteners.Shortener().tinyurl.short(url) 

    ent2.insert(END,s)

#label 
Label(window,text="Enter your url link", font = "impack 17 bold",bg ="white",fg="black").pack(fill="x")  
#entry 
ent = Entry(window, font="10",bd=3,width=40) 
ent.pack(pady=20) 
#button 
Button(window,text="Submit", font="impack 12 bold",bg="white",fg="black",width="14",command= shortenurl).pack() 
#exit 
ent2 = Entry(window,font="impack 10 bold",bg="black",fg="white", width=34,bd=0) 
ent2.pack(pady=30)
mainloop() 
