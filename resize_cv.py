from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def cal():
    file1 = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    e1.delete(0,END)
    e1.insert(END,file1)
    global a
    a = file1

def display():
    import cv2
    b = c1.get() 
    if int(b) == 0:
        c = e3.get()
        img = cv2.imread(a,1)
        cv2.imshow("image1",img)
        cv2.imwrite(c,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        c = e3.get()
        img = cv2.imread(a,1)
        img1 = cv2.resize(img,(img.shape[1]//int(b),img.shape[0]//int(b)))
        cv2.imshow("Original_image",img)
        cv2.imshow(c,img1)
        cv2.imwrite(c,img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

win = Tk()
win.geometry('300x300')
win.title(" Image Converter ")

l4 = Label(win,text=" Image Converter ",font=('Arial',18,'bold','italic','underline'))
l4.place(x=50,y=30)

l3 = Label(win,text=" New Image Name :")
l3.place(x=30,y=200)

e3 = Entry(win)
e3.place(x=150,y=200,width=140)

l1 = Label(win,text=" Your Image Name : ")
l1.place(x=30,y=100)

e1 = Entry(win)
e1.place(x=150,y=100,width=140)

l2 = Label(win,text=" Resize Image Pixels : ")
l2.place(x=30,y=150)#

c1 = ttk.Combobox(win)
c1.place(x=150,y=150)
c1['values'] = (2,3,4,0)

b1 = Button(win,text="Select Image",command=cal)
b1.place(x=70,y=250)

b2 = Button(win,text="Print Image",command=display)
b2.place(x=160,y=250)


win.mainloop()