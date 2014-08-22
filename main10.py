import sys
import tkMessageBox
import Tkinter
from Tkinter import *
import tkFileDialog
import os
from notebook import *
top = Tkinter.Tk()
# Code to add widgets will go here...
top.title('Log Analysis Tool')
global addedHandsFreeFrame, addedHCIFrame,addedAVRCPFrame,addedSDPFrame,addedAVRCPAVDTFrame
global text,text2,text3,text4
global avdtpFilename,avrcpFilename
addedHandsFreeFrame=0
addedHCIFrame=0
addedAVRCPFrame=0
addedSDPFrame=0
addedAVRCPAVDTFrame=0
#w = Frame(top)
#w.pack(expand=YES, fill=BOTH)
print "Main Started"
filename='s'

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
def clearTextWindow():
	text.delete(4.0,END)
	text2.delete(1.0,END)
	text3.delete(1.0,END)
	text4.delete(1.0,END)
def sendToTextFile(entry,outputFileName,inputFrame):
	print "Inside sendToTextFile"
	data=text.get(2.0,END)
	e1=str(entry.get())
	print e1
	print outputFileName
	#print "DATA:" , data
	file = open(e1+'.txt','w')
	file.write(data)
	print "Successfully Written to " + e1 + ".txt"
	l1=Label(inputFrame,text='SUCCESS !!')
	l1.pack(side=BOTTOM)
	#l1.place(x=20,y=20)
	#tkMessageBox.showinfo("Success", "Output Successfully written to" + outputFileName)
def sendToTextFileWindow():
	print "Inside sendToTextFileWindow"
	input=Tkinter.Tk()
	input.title('Enter the Output File')
	inputFrame=Frame(input)
	label = Label(inputFrame, text='Enter the Output File Name:')
	entry = Entry(inputFrame)
	label.pack(side=TOP)
	entry.pack(side=LEFT)
	
	input.bind('<Return>', (lambda event, e=str(entry.get()): sendToTextFile(entry,e,inputFrame)))   
	bb1 = Button(inputFrame, text='OK',
          command=(lambda e=str(entry.get()): sendToTextFile(entry,e,inputFrame)))
	bb1.pack(side=LEFT, expand=YES)
	inputFrame.pack(side=TOP, expand=YES)
	#bb2 = Button(input, text='Quit', command=input.quit)
	#bb2.pack(side=BOTTOM, padx=5, pady=5)
	
	#inputBox = Tkinter.Button(inputFrame, text ="OK", command = sendToTextFile(str(entry.get())))
	#inputBox.pack(side=BOTTOM,expand=YES)
	input.mainloop()
def executeTwoFileFunction(avdtpFilename,avrcpFilename):
	print "executeTwoFileFunction:",avdtpFilename,avrcpFilename
	import OTAAvdtpAvrcp
	global addedAVRCPAVDTFrame
	global text,text2
	if addedAVRCPAVDTFrame == 0 :
		f3 = Frame(n()) # second page
		scrollbar2 = Scrollbar(f3)
		scrollbar2.pack( side = RIGHT, fill=Y)
		n.add_screen(f3,"AVRCP Stats")
		text3 = Text(f3,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
		text3.tag_config("title", background="Cornflower Blue", foreground="black")
		text3.tag_config("subtitle", background="Lawn Green", foreground="black")
		text3.pack(side=TOP,expand=YES, fill=BOTH)
		scrollbar2.config(command = text3.yview )
		addedAVRCPAVDTFrame=1
	#BTsnoopAVRCP1.code(text,text2,avdtpFilename,avrcpFilename)
	OTAAvdtpAvrcp.code(text,text3,avdtpFilename,avrcpFilename)

def openBrowseWindow1():
	global filename
	currdir = os.getcwd()
	filename = tkFileDialog.askopenfilename(parent=top, initialdir=currdir, title='Please select CSV File')
	textSingleFiles.insert(INSERT,filename)
	print filename
	executeFunction()
def openBrowseWindow2():
	global filename,avdtpFilename,avrcpFilename
	files=[]
	avdtpFlag=0
	avrcpFlag=0
	textSingleFiles.delete(1.0,END)
	currdir = os.getcwd()
	#filename = tkFileDialog.askopenfilename(parent=top, initialdir=currdir, title='Please select CSV File')
	filez = tkFileDialog.askopenfilenames(parent=top,initialdir=currdir,title='Choose a file')
	textSingleFiles.insert(INSERT,filez)
	print len(filez)
	print filez
	for i in range(0,len(filez)):
		#print "inside for",filez[i].lower()
		files.append(filez[i].lower())
	#print "outside",files
	files=sorted(files)
	print "sorted:\n",files
	for filename in files:
			print "filename:",filename
			if ("avrcp" in  filename):
				print "avrcp found"
				avrcpFilename=filename
				avrcpFlag=1
				executeFunction()
				if avdtpFlag==1 and avrcpFlag==1:
					print "both found"
					print avrcpFilename,avdtpFilename
					executeTwoFileFunction(avdtpFilename,avrcpFilename)
			elif ("avdtp" in  filename):
				avdtpFilename=filename
				print "avdtp found"
				avdtpFlag=1
				if avdtpFlag==1 and avrcpFlag==1:
					print "both found!!!!"
					print avrcpFilename,"!!",avdtpFilename
					executeTwoFileFunction(avdtpFilename,avrcpFilename)
			else:
				print "execute only"
				executeFunction()
#def writeOnGUITextBox(data):
#	text.insert(INSERT,data)

def executeFunction():
	print "Inside Execute"
	print filename
	if ("handsfree" in  filename.lower()) and '.csv' in filename:
		print "BTsnoopHandsFree1"
		import BTsnoopHandsFree1
		global addedHandsFreeFrame
		global text,text2,text3
		if addedHandsFreeFrame == 0 :
			f2 = Frame(n()) # second page
			f3= Frame (n())
			scrollbar2 = Scrollbar(f2)
			scrollbar2.pack(side = RIGHT, fill=Y)
			scrollbar3 = Scrollbar(f3)
			scrollbar3.pack( side = RIGHT, fill=Y)

			n.add_screen(f2,"AT Commands ")
			n.add_screen(f3, "AT Commands Responses")
			text2 = Text(f2,width=80,height=40,yscrollcommand = scrollbar2.set,fg="blue")
			text2.tag_config("title", background="Cornflower Blue", foreground="black")
			text2.tag_config("subtitle", background="Lawn Green", foreground="black")
			#text2.insert(INSERT,"Awesome..............................................")
			
			text2.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar2.config( command = text2.yview )
			text3 = Text(f3,width=80,height=40,yscrollcommand = scrollbar3.set,fg="blue")
			#text3.insert(INSERT,"Awesome Three..............................................")
			text3.tag_config("title", background="Cornflower Blue", foreground="black")
			text3.tag_config("subtitle", background="Lawn Green", foreground="black")
			text3.tag_config("error", foreground="red")
			text3.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar3.config( command = text3.yview )
			addedHandsFreeFrame=1
		BTsnoopHandsFree1.code(text,text2,text3,filename)
	elif  ('hci' in  filename.lower()) and '.csv' in filename:
		print "HCI"
		import BtsnoopHCI5
		global addedHCIFrame
		global text,text2,text3,text4
		if addedHCIFrame == 0 :
			f2 = Frame(n()) # second page
			f3= Frame (n())
			f4= Frame (n())
			scrollbar2 = Scrollbar(f2)
			scrollbar2.pack( side = RIGHT, fill=Y)
			scrollbar3 = Scrollbar(f3)
			scrollbar3.pack( side = RIGHT, fill=Y)
			scrollbar4 = Scrollbar(f4)
			scrollbar4.pack( side = RIGHT, fill=Y)

			n.add_screen(f2,"Host-Controller Info")
			n.add_screen(f3, "Connection Latency")
			n.add_screen(f4, "Inquiry Latency")
			
			text2 = Text(f2,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
			text2.tag_config("title", background="Cornflower Blue", foreground="black")
			text2.tag_config("subtitle", background="Lawn Green", foreground="black")
			text2.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar2.config( command = text2.yview )
			
			text3 = Text(f3,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
			text3.tag_config("title", background="Cornflower Blue", foreground="black")
			text3.tag_config("subtitle", background="Lawn Green", foreground="black")
			text3.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar3.config( command = text3.yview )
			
			text4 = Text(f4,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
			text4.tag_config("title", background="Cornflower Blue", foreground="black")
			text4.tag_config("subtitle", background="Lawn Green", foreground="black")
			text4.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar4.config( command = text4.yview )
			
			addedHCIFrame=1
		BtsnoopHCI5.code(text,text2,text3,text4,filename)
	elif ('sdp' in  filename.lower()) and '.csv' in filename:
		print "SDP"
		import BTsnoopSDPProfiles
		global addedSDPFrame
		global text,text2
		if addedSDPFrame == 0 :
			print "Inside addedSDPFrame"
			f2 = Frame(n()) # second page
			scrollbar2 = Scrollbar(f2)
			scrollbar2.pack( side = RIGHT, fill=Y)

			n.add_screen(f2,"Profiles Supported")
			text2 = Text(f2,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
			text2.tag_config("title", background="Cornflower Blue", foreground="black")
			text2.tag_config("subtitle", background="Lawn Green", foreground="black")
			text2.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar2.config( command = text2.yview )
			addedSDPFrame=1
		BTsnoopSDPProfiles.code(text,text2,filename)
	elif 'avrcp' in  filename.lower() and '.csv' in filename:
		print "BTsnoopAVRCP1"
		import BTsnoopAVRCP1
		global addedAVRCPFrame
		global text,text2
		if addedAVRCPFrame == 0 :
			f2 = Frame(n()) # second page
			scrollbar2 = Scrollbar(f2)
			scrollbar2.pack( side = RIGHT, fill=Y)
			n.add_screen(f2,"AVRCP Controls")
			text2 = Text(f2,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")
			text2.tag_config("title", background="Cornflower Blue", foreground="black")
			text2.tag_config("subtitle", background="Lawn Green", foreground="black")
			text2.pack(side=TOP,expand=YES, fill=BOTH)
			scrollbar2.config( command = text2.yview )
			addedAVRCPFrame=1
		BTsnoopAVRCP1.code(text,text2,filename)
	else:
		tkMessageBox.showerror("Failure", "Incorrect File chosen: Please select a .CSV File")
		textSingleFiles.delete(1.0,END)
print '=31=',top

def sel():
   if var.get() == 1:
      openBrowseWindow1()
   if var.get() == 2:
		openBrowseWindow2()

frame11= Frame(top)
frame11.pack(side=TOP)

var=IntVar()
R1 = Radiobutton(frame11, text="Single File", value=1,variable =var)
R1.pack(anchor=W, side=LEFT )
R1.select()
R2 = Radiobutton(frame11, text="Multiple Files", value=2,variable =var)
R2.pack(anchor=W,side =LEFT )

frame1= Frame(top)
frame1.pack(side=TOP)

Label1= Label(frame1,text='Select a CSV File :')
Label1.pack(side=LEFT)

textSingleFiles = Text(frame1,width=40,height=1)
textSingleFiles.insert(END,"")
textSingleFiles.pack(side = LEFT)

B1 = Tkinter.Button(frame1, text ="Browse", command = sel)
B1.pack(side = LEFT)

frame3= Frame(top)
frame3.pack(side=TOP)

scrollbar = Scrollbar(frame3)
scrollbar.pack( side = RIGHT, fill=Y)

n = notebook(frame3)
f1 = Frame(n()) # first page, which would get widgets gridded into it

n.add_screen(f1, "All Information")

text = Text(f1,width=80,height=40,yscrollcommand = scrollbar.set,fg="blue")

text.tag_config("title", background="Cornflower Blue", foreground="black")
text.tag_config("there", background="yellow", foreground="black")
text.tag_config("badtitle", background="yellow", foreground="black")
text.tag_config("subtitle", background="Lawn Green", foreground="black")
text.tag_config("back", background="green", foreground="red")
text.tag_config("main", background="Orange Red", foreground="black")
text.tag_config("up", background="blue", foreground="red")
text.tag_config("r2", background="red", foreground="blue")
text.tag_config("r3", background="red", foreground="green")
text.tag_config("r4", background="red", foreground="yellow")
text.tag_config("error", foreground="red")
#startTag= text.index(INSERT)
text.insert(END,"\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","main")
text.tag_add("start",INSERT,END)
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","r3")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","back")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","front")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","everywhere")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","all")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","r4")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","up")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","there")
#text.insert(INSERT,"\t\t\tHi ! Welcome To Bluetooth Log Analysis Demo\n\n","r2")


#endTag=text.index(INSERT)
#text.tag_add("here", startTag, endTag)

text.pack(side=TOP,expand=YES, fill=BOTH)



#text.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = text.yview )

frame4= Frame(frame3)
frame4.pack(side=BOTTOM)

B31 = Tkinter.Button(frame4, text ="Clear", command = clearTextWindow)
B31.pack(side=LEFT,expand=YES, fill=BOTH)

B32 = Tkinter.Button(frame4, text ="Send to Text File", command = sendToTextFileWindow)
B32.pack(side=LEFT,expand=YES, fill=BOTH)

#B33 = Tkinter.Button(frame4, text ="Search(NF)", command = openBrowseWindow2)
#B33.pack(side=LEFT,expand=YES, fill=BOTH)
#"C:\Python27\GUI\main11\OtaAvdtpSignalingHondaCivic.csv"
#"C:\Python27\GUI\main11\OtaAvrcpHondaCivic.csv"
#"C:\Users\akkawade\Desktop\sampleAVRCP1.csv"
#"C:\Users\akkawade\Desktop\sampleAVDTPSignaling1.csv"
#executeTwoFileFunction("C:\Users\akkawade\Desktop\sampleAVDTPSignaling1.csv","C:\Users\akkawade\Desktop\sampleAVRCP1.csv")
print "Here i am"
top.mainloop()