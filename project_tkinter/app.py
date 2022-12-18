import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import sys
import glob
import os

my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 
my_w.title('Classify Objects')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload a file to classfy',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload Files', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4)
l2 = tk.Label(my_w,text='',width=30,font=my_font1)  
l2.grid(row=8,column=1,columnspan=4)



def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        print("CHECK",f)
        img_file_name=f.split('/')[-1]
        os.system('python3 ../yolov5_working_project/detect.py --weights ../yolov5_working_project/yolov5s.pt --img 640 --conf 0.5 --source '+f+' --save-txt --data ../yolov5_working_project/data/coco128.yaml')
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column 
    l2.config(text="your prediction image")
    list_of_files = glob.glob('../yolov5_working_project/runs/detect/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime) + "/" + img_file_name
    print("CHECK LASTES FILe",latest_file) 

    img_2=Image.open(latest_file) # read the image file
    img_2=img_2.resize((300,300)) # new width & height
    img_2=ImageTk.PhotoImage(img_2)
    e2 =tk.Label(my_w)
    e2.grid(row=10,column=1)
    e2.image = img_2
    e2['image']=img_2              
my_w.mainloop()  # Keep the window open