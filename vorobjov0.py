
from tkinter import *
foto_list=["pilt1.png","pilt2.png","pilt3.png","pilt4.png"]
def list_to_txt(event):
    global can,foto#----------------
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)#---------------
    foto=PhotoImage(file=foto_list[valik[0]])#-------------
    can.create_image(0,0,image=foto,anchor=NW)#-----------------
def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)
win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)
lbox.grid(row=0,column=0)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=1,width=20,wrap=WORD)
text.tag_add("start","1.0","1.5")
txt.grid(row=0,column=1)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=130,bg="gold")#--------------
can.grid(row=1,column=0,columnspan=2)#--------------------
foto=PhotoImage(file="pilt2.png")#----------------
can.create_image(0,0,image=foto,anchor=NW)#-----------------
win.mainloop()