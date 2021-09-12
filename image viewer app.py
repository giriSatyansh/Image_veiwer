#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import ImageTk,Image
root=Tk()
f=1
c=f
def forward(image_number):
    global f
    mylabel1.grid_forget()
    if image_number>=5:
        buttonforward=Button(root,text=">>",state=DISABLED)
    else:
        image_number=image_number+1
        mylabel2=Label(image=imagelist[image_number-1])
        mylabel2.grid(row=0,column=0,columnspan=3)
        f=f+1
def backward(image_number):
    global f
    mylabel1.grid_forget()
    if image_number<=1:
        buttonback=Button(root,text="<<",state=DISABLED)
    else:    
        image_number=image_number-1
        mylabel3=Label(image=imagelist[image_number-1])
        mylabel3.grid(row=0,column=0,columnspan=3)
        f=f-1
myimage1=ImageTk.PhotoImage(Image.open("a.gif"))
myimage2=ImageTk.PhotoImage(Image.open("b.gif"))
myimage3=ImageTk.PhotoImage(Image.open("c.gif"))
myimage4=ImageTk.PhotoImage(Image.open("d.gif"))
myimage5=ImageTk.PhotoImage(Image.open("e.gif"))
imagelist=[myimage1,myimage2,myimage3,myimage4,myimage5]

mylabel1=Label(image=myimage1)
mylabel1.grid(row=0,column=0,columnspan=3)
buttonback=Button(root,text="<<",command=lambda:backward(f))
buttonexit=Button(root,text="exit program",command=root.quit())
buttonforward=Button(root,text=">>",command=lambda:forward(f))

buttonback.grid(row=1,column=0)
buttonexit.grid(row=1,column=1)
buttonforward.grid(row=1,column=2)
root.mainloop()


# In[ ]:




