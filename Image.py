from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import font
from skimage.metrics import structural_similarity
import cv2
import numpy as np
import time


# from newSetting import *

# thesholdResult = 50
 

root = Tk()
root.title('Connector checker by Image detection')
root.geometry('720x480+100+100')


# Image
image = Image.open("yamaha.png")
photo = ImageTk.PhotoImage(image)

root_label = Label(root, image=photo)
root_label.place(x=30,y=20)


# Comparison Mode
Label(text='Comparison Mode', font="-weight bold").place(x=315,y=50)
choice = StringVar(value='Select mode')
selectMode = choice.get()
combo=ttk.Combobox(textvariable=choice)
combo['value'] = ('Auto Mode', 'Manual Mode')
combo.place(x=315,y=80)


# Threshold setting
Label(text='Threshold (0.00% ~ 100.00%)',font="-weight bold").place(x=315,y=120)
radius = DoubleVar()
ed1 = Entry(width=15,textvariable=radius,font=50)
ed1.place(x=315,y=150)


def workInstruction():
    wiWindow = Tk()
    wiWindow.title('Connector checker by Image detection')
    wiWindow.geometry('720x500+100+100')
    
    # wiWindow.mainloop()

    descriptionLabel = Label(wiWindow,text='WORK INSTRUCTION',fg='blue', bg='yellow',font="-weight bold").place(x=20,y=20)
    Label_1 = Label(wiWindow,text='1. Have to capture good part at the checking area to make the master image.',fg='blue',font="-weight normal").place(x=20,y=70)
    Label_2 = Label(wiWindow,text='2. Pick the part to the checking arae for capture with master.',fg='blue',font="-weight normal").place(x=20,y=100)
    Label_3 = Label(wiWindow,text='3. Press spacebar button on keyborad to capture image of part.',fg='blue',font="-weight normal").place(x=20,y=130)
    Label_4 = Label(wiWindow,text='4. Software will calculate and show the matching result.',fg='blue',font="-weight normal").place(x=20,y=160)
    Label_5 = Label(wiWindow,text='5. Please input threshold(%) if the result incorrect.',fg='blue',font="-weight normal").place(x=20,y=190)
    
    BT = Button(wiWindow, text='     OK     ', background='blue', fg='white',font="-weight bold", command=wiWindow.destroy).place(x=200, y=250)
    
    wiWindow.mainloop()


def aboutUs():
    
    aboutUsWindow = Tk()
    aboutUsWindow.title('Connector checker by Image detection')
    aboutUsWindow.geometry('500x300+150+150')

    descriptionLabel = Label(aboutUsWindow,text='ABOUT US',fg='blue', bg='yellow',font="-weight bold").place(x=20,y=20)
    Label_1 = Label(aboutUsWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=50)
    Label_2 = Label(aboutUsWindow,text='Yamaha Robotics Manufacturing Asia(YRMA)',fg='blue',font="-weight normal").place(x=20,y=80)
    Label_3 = Label(aboutUsWindow,text='Version : 1.0.0',fg='blue',font="-weight normal").place(x=20,y=110)
    Label_4 = Label(aboutUsWindow,text='Release Date : 01-January-2022',fg='blue',font="-weight normal").place(x=20,y=140)
    Label_5 = Label(aboutUsWindow,text='Developer : Electrical Designer Team (802, 808)',fg='blue',font="-weight normal").place(x=20,y=170)
    Label_6 = Label(aboutUsWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=200)
    
    BT = Button(aboutUsWindow, text='     OK     ', background='blue', fg='white',font="-weight bold", command=aboutUsWindow.destroy).place(x=200, y=250)
  
    aboutUsWindow.mainloop()
    
 
    
def newSetting():
    newWindow = Tk()
    newWindow.title('Setting new connector ')
    newWindow.geometry('720x500+100+100')
    
    descriptionLabel = Label(newWindow,text='HOW TO SETTING THE MASTER CONNECTOR IMAGE',fg='blue', bg='yellow',font="-weight bold").place(x=20,y=20)
    Label_1 = Label(newWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=50)
    Label_2 = Label(newWindow,text='1. Drop the master connector to the capture area',fg='blue',font="-weight normal").place(x=20,y=80)
    Label_3 = Label(newWindow,text='2. Press START button then will show the image from camera',fg='blue',font="-weight normal").place(x=20,y=110)
    Label_4 = Label(newWindow,text='Release Date : 01-January-2022',fg='blue',font="-weight normal").place(x=20,y=140)
    Label_5 = Label(newWindow,text='Developer : Electrical Designer Team (802, 808)',fg='blue',font="-weight normal").place(x=20,y=170)
    Label_6 = Label(newWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=200)
    
    BTๅ = Button(newWindow, text='     OK     ', background='blue', fg='white',font="-weight bold", command=capScreenForSetting).place(x=200, y=250)
    BT2 = Button(newWindow, text='   CLOSE   ', background='blue', fg='white',font="-weight bold", command=newWindow.destroy).place(x=300, y=250)
       
    newWindow.mainloop()    
    
def capScreenForSetting():
    cam = cv2.VideoCapture('Feeder NG.mp4')
    # cam = cv2.VideoCapture(0)

    cv2.namedWindow("Connector checker viewer")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Connector checker viewer", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "master_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            
            break

    cam.release()
        
    cv2.destroyAllWindows()    
    
    
def thresholdSetting():
    
    thresholdWindow = Tk()
    thresholdWindow.title('Connector checker by Image detection')
    thresholdWindow.geometry('500x300+150+150')
    
    descriptionLabel = Label(thresholdWindow,text='THRESHOLD',fg='blue', bg='yellow',font="-weight bold").place(x=20,y=20)
    Label_1 = Label(thresholdWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=50)

    Label(thresholdWindow, text='Threshold (0.00% ~ 100.00%)',font="-weight bold").place(x=20,y=90)
    radius = DoubleVar()
    ed1 = Entry(thresholdWindow, width=10,textvariable=radius,font=100)
    ed1.place(x=25,y=130)

    Label_6 = Label(thresholdWindow,text='===============================================',fg='blue',font="-weight normal").place(x=20,y=180)
       
    thesholdResult = radius.get()
    
    if thesholdResult > 100:
        thesholdResult = 100
  
    print(thesholdResult) 
    
    startButton = Button(thresholdWindow, text='        OK        ', background='green', fg='white',font="-weight bold", ).place(x=20, y=220)
    
    cancelButton = Button(thresholdWindow, text='     Cancel     ', background='gray', fg='white',font="-weight bold", command=thresholdWindow.destroy).place(x=200, y=220)
    
    thresholdWindow.mainloop()   
     
 
def clrResult():
    scoreLabel = Label(root,text='                                                               ',font=("-weight bold", 20)).place(x=310,y=240) 
    resultLabel = Label(root,text='                                                              ',font=("-weight bold", 100)).place(x=300,y=280) 
    # ed1.delete(0,END)         
     
def capScreen():
    cam = cv2.VideoCapture('Feeder NG.mp4')
    # cam = cv2.VideoCapture(0)

    cv2.namedWindow("Connector checker viewer")

    img_counter = 1

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Connector checker viewer", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            
            break

    cam.release()
        
    cv2.destroyAllWindows()
    
        

def manualImgCompare():
    
    capScreen()
       
    before = cv2.imread('master_frame_0.png')
    after = cv2.imread('opencv_frame_1.png')
    
    # before = cv2.imread('2.jpg')
    # after = cv2.imread('4.jpg')

    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    # print("Image similarity", score)

    convert_score = np.float64(score).item() 
    # print("Image score is",convert_score)
        
    tr = radius.get()
    if tr > 100:
        tr = 100
    convert_tr = tr/100
      
    if convert_score >= convert_tr:
        scoreLabel = Label(root,text='Image similarity',fg='green',font=("-weight bold", 20)).place(x=310,y=240) 
        resultLabel = Label(root,text='OK',fg='green',font=("-weight bold", 100)).place(x=300,y=280) 
        #print(type(score))
        print("Image similarity", score)
        
    else:
        scoreLabel = Label(root,text='Image similarity',fg='red',font=("-weight bold", 20)).place(x=310,y=240) 
        resultLabel = Label(root,text='NG',fg='red',font=("-weight bold", 100)).place(x=300,y=280)  
        #print(type(score))
        print("Image similarity", score)
        
        
        
def autoImgCompare():
    
    cam = cv2.VideoCapture('Feeder NG.mp4')
    # cam = cv2.VideoCapture(0)

    img_counter = 1
    ng_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            # print("failed to grab frame")
            break
        cv2.imshow("Connector checker viewer", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:     # ESC pressed
            # print("Escape hit, closing...")
            break

        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))
        
        
        before = cv2.imread('master_frame_0.png')  # master 
        after = cv2.imread('opencv_frame_1.png')
        
        # Convert images to grayscale
        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

        # Compute SSIM between two images
        (score, diff) = structural_similarity(before_gray, after_gray, full=True)
        # print("Image similarity", score)

        convert_score = np.float64(score).item() 
            
        tr = radius.get()
        if tr > 100:
            tr = 100
        convert_tr = tr/100
        
        ng_counter = ng_counter + 1
        
        if (convert_score >= convert_tr) or (ng_counter >= 100):
            break
    
    cam.release()
        
    cv2.destroyAllWindows()
    if convert_score >= convert_tr:
        scoreLabel = Label(root,text='Image similarity',fg='green',font=("-weight bold", 20)).place(x=310,y=240) 
        resultLabel = Label(root,text='OK',fg='green',font=("-weight bold", 100)).place(x=300,y=280) 
        #print(type(score))
        print("Image similarity", score)
        
    else:
        scoreLabel = Label(root,text='Image similarity',fg='red',font=("-weight bold", 20)).place(x=310,y=240) 
        resultLabel = Label(root,text='NG',fg='red',font=("-weight bold", 100)).place(x=300,y=280)  
        #print(type(score))
        print("Image similarity", score)
      
                
def processCompare():
    # clrResult()
    if choice.get() == 'Auto Mode':
        clrResult()
        print('Auto mode')
        autoImgCompare()
    elif choice.get() == 'Manual Mode':
        clrResult()
        print('Manual mode')  
        manualImgCompare()   
    else :
        print('Please select mode')   
        clrResult()
        scoreLabel = Label(root,text='Calculation false',fg='red',font="-weight bold").place(x=300,y=300)
        resultLabel = Label(root,text='Please select comparison mode',fg='red',font="-weight bold").place(x=300,y=350)
              
                
startButton = Button(root, text='CALCULATE', background='green', fg='white',font="-weight bold", command=processCompare).place(x=30, y=300)
clearButton = Button(root, text='     CLEAR     ', background='red', fg='white',font="-weight bold", command=clrResult).place(x=30, y=350)

root.geometry('720x480+100+100')



# Create Menu
myMenu = Menu()
root.config(menu=myMenu)

# Sub Menu
menuFile = Menu()
menuFile.add_command(label='New', command= newSetting)
menuFile.add_command(label='Open')
menuFile.add_command(label='Save')
menuFile.add_command(label='Save as')
menuFile.add_command(label='Info')
menuFile.add_command(label='Close')

# Sub Menu
menuSetting = Menu()
menuSetting.add_command(label='Threshold', command= thresholdSetting)


# Sub Menu
menuHelp = Menu()
menuHelp.add_command(label='About us',command = aboutUs)
menuHelp.add_command(label='Work Instruction',command = workInstruction)

# Add Menu
myMenu.add_cascade(label='File', menu=menuFile)
myMenu.add_cascade(label='Setting', menu=menuSetting)
myMenu.add_cascade(label='Help', menu=menuHelp)



root.mainloop()