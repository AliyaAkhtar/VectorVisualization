from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import Axes3D

#main window
root=Tk()
root.title("VECTOR APPLICATION")
root.geometry("1530x790+0+0")

#title label
title_label=Label(root,text="DOT PRODUCT OF TWO VECTORS ALONG WITH THE GRAPHICAL REPRESENTATION",font=("Times New Roman",27,"bold"),bg="blue",fg="red")
title_label.place(x=0,y=0,width=1530,height=100)

#main frame
f=LabelFrame(root,bd=2,bg="white")
f.place(x=5,y=100,width=1520,height=685)

#background image
img1=Image.open(r"C:\Users\user\Downloads\vectors.png")
img1=img1.resize((1520,690))
photoimg1=ImageTk.PhotoImage(img1)
bg_photo=Label(f,image=photoimg1)
bg_photo.place(x=0,y=0,width=1520,height=685)

#left label frame
lf=LabelFrame(bg_photo,bd=5,bg="white",relief=RIDGE)
lf.place(x=5,y=5,width=730,height=670)

#main label
main_label=Label(lf,text="VECTORS AND THEIR DOT PRODUCT",font=("Times New Roman",20,"bold"),bg="orange")
main_label.place(x=70,y=5,width=550,height=40)

# first vector
l1=Label(lf,text="Enter the components for 1st vector:",font=("Times New Roman",16,"bold"),bg="white")
l1.place(x=0,y=60,width=350,height=30)

vector_entry1=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry1.place(x=30,y=100)

l1_i=Label(lf,text=("i","+"),font=("Times New Roman",15,"bold"),bg="white")
l1_i.place(x=135,y=100,width=20,height=30)

vector_entry2=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry2.place(x=160,y=100)

l1_j=Label(lf,text=("j","+"),font=("Times New Roman",15,"bold"),bg="white")
l1_j.place(x=265,y=100,width=20,height=30)

vector_entry3=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry3.place(x=290,y=100)

l1_k=Label(lf,text="k",font=("Times New Roman",15,"bold"),bg="white")
l1_k.place(x=390,y=100,width=20,height=30)

# second vector
l2=Label(lf,text="Enter the components for 2nd vector:",font=("Times New Roman",16,"bold"),bg="white")
l2.place(x=0,y=150,width=360,height=30)

vector_entry4=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry4.place(x=30,y=190)

l2_i=Label(lf,text=("i","+"),font=("Times New Roman",15,"bold"),bg="white")
l2_i.place(x=135,y=190,width=20,height=30)

vector_entry5=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry5.place(x=160,y=190)

l2_j=Label(lf,text=("j","+"),font=("Times New Roman",15,"bold"),bg="white")
l2_j.place(x=265,y=190,width=20,height=30)

vector_entry6=ttk.Entry(lf,width=10,font=("Times New Roman",13,"bold"))
vector_entry6.place(x=290,y=190)

l2_k=Label(lf,text="k",font=("Times New Roman",15,"bold"),bg="white")
l2_k.place(x=390,y=190,width=20,height=30)

#defining the function for dot product
def dot_product():
    global C     
    A=[float(vector_entry1.get()),float(vector_entry2.get()),float(vector_entry3.get())]
    B=[float(vector_entry4.get()),float(vector_entry5.get()),float(vector_entry6.get())]
    C=np.dot(A,B)
    dp_label.config(text=C)    

#dot product
dp=Label(lf,text="Dot Product of the two given vectors will be:",font=("Times New Roman",16,"bold"),bg="white")
dp.place(x=0,y=240,width=425,height=30)

dp_label=ttk.Label(lf,width=40,font=("Times New Roman",13,"bold"))
dp_label.place(x=30,y=280)

dp_button=Button(lf,command=dot_product,text="CLICK HERE",font=("Times New Roman",15,"bold"),bg="light green")
dp_button.place(x=500,y=280,width=150,height=31)

#ploting the vectors
def plot():
    fig=plt.figure()
    plt.figure(figsize=(15,10))
    ax=fig.add_subplot(111,projection="3d")
    canvas=FigureCanvasTkAgg(fig,master=rf)
    canvas.get_tk_widget().place(x=20,y=50,width=700,height=550)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    A=[float(vector_entry1.get()),float(vector_entry2.get()),float(vector_entry3.get())]
    B=[float(vector_entry4.get()),float(vector_entry5.get()),float(vector_entry6.get())]
    x_min = min(0, A[0], B[0], C)
    x_max = max(0, A[0], B[0], C)
    y_min = min(0, A[1], B[1], C)
    y_max = max(0, A[1], B[1], C)
    z_min = min(0, A[2], B[2], C)
    z_max = max(0, A[2], B[2], C)
    ax.set_xlim([x_min-1, x_max+1])
    ax.set_ylim([y_min-1, y_max+1])
    ax.set_zlim([z_min-1, z_max+1])
    start=[0,0,0]
    ax.quiver(start[0],start[1],start[2],A[0],A[1],A[2],color='red',arrow_length_ratio=0.2)
    ax.quiver(start[0],start[1],start[2],B[0],B[1],B[2],color='blue',arrow_length_ratio=0.2)
    ax.scatter(C, 0, 0, c='green', marker='.',s=50)
    
#plot button
plot=Button(lf,command=plot,text="PLOT THE VECTORS",font=("Times New Roman",15,"bold"),bg="light green")
plot.place(x=200,y=320,width=250,height=31)

#picture frame
pic_frame=LabelFrame(lf,bd=5,bg="white",relief=RIDGE)
pic_frame.place(x=0,y=370,width=720,height=290)

img2=Image.open(r"C:\Users\user\Downloads\dotproductofvectors.png")
img2=img2.resize((720,320))
photoimg2=ImageTk.PhotoImage(img2)
pic=Label(pic_frame,image=photoimg2)
pic.place(x=0,y=0,width=720,height=290)

#right label frame
rf=LabelFrame(bg_photo,bd=5,bg="white",relief=RIDGE)
rf.place(x=750,y=5,width=760,height=670)

#graph label
graph_label=Label(rf,text="3D PLOTTING OF VECTORS",font=("Times New Roman",20,"bold"),bg="orange")
graph_label.place(x=150,y=5,width=450,height=40)

r_color=ttk.Label(rf,background="red")
r_color.place(x=540,y=630,width=10,height=10)
red=ttk.Label(rf,text="FIRST VECTOR",font=("Times New Roman",9,"bold"),background="white")
red.place(x=550,y=620,width=95,height=30)

b_color=ttk.Label(rf,background="blue")
b_color.place(x=380,y=630,width=10,height=10)
blue=ttk.Label(rf,text="SECOND VECTOR",font=("Times New Roman",9,"bold"),background="white")
blue.place(x=390,y=620,width=120,height=30)

g_color=ttk.Label(rf,background="green")
g_color.place(x=100,y=630,width=10,height=10)
green=ttk.Label(rf,text="DOT PRODUCT OF THE TWO VECTORS",font=("Times New Roman",9,"bold"),background="white")
green.place(x=110,y=620,width=240,height=30)

root.mainloop()