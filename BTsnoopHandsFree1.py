import csv
import sys
import sets
from array import *
from datetime import datetime
from datetime import timedelta
import utilities
def code(text,text2,text3,filepath):
	print filepath
	fieldNames=[]
	rowData=[]
	num= 0
	lineInCSV =1
	isDone=0
	masterDetails={}
	slaveDetails={}
	packetDetails={}
	masterATTCommandList=[]
	slaveATTCommandList=[]
	ATTCommandIntListList=[]
	str1 ="\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox1(text,str1,"title")
	utilities.writeOnGUITextBox1(text2,str1,"title")
	utilities.writeOnGUITextBox1(text3,str1,"title")
	print "Handsfree CSV"
	str1 = "\t\tBTSNOOP LOG HANDSFREE LAYER ANALYSIS\n\n"
	utilities.writeOnGUITextBox1(text,str1,"title")
	utilities.writeOnGUITextBox1(text2,str1,"title")
	utilities.writeOnGUITextBox1(text3,str1,"title")
	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		for row in csvReader:
				if lineInCSV == 1:
					for i in range (0,len(row)):
						fieldNames.append(row[i])
					print "1", fieldNames
				lineInCSV= lineInCSV + 1
				if lineInCSV > 2:
					for i in range (0,len(row)):
						rowData.append(row[i])
					#print rowData
					if str(rowData[int(fieldNames.index('Role'))]) == 'Master' or str(rowData[int(fieldNames.index('Role'))]) == 'M (HF)' or str(rowData[int(fieldNames.index('Role'))]) == '* Master':
						masterATTcommand = str(rowData[int(fieldNames.index('Hands-Free data'))])
						#print 'L:', masterATTcommand
						if masterATTcommand[:2] == 'AT' or masterATTcommand[:4] == '* AT':
							masterATTCommandList.append(masterATTcommand)
							#print 'M:',masterATTCommandList
					if str(rowData[int(fieldNames.index('Role'))]) == 'Slave' or str(rowData[int(fieldNames.index('Role'))]) == 'S (AG)' or str(rowData[int(fieldNames.index('Role'))]) == '* Slave':
						slaveATTcommand = str(rowData[int(fieldNames.index('Hands-Free data'))])
						if slaveATTcommand[:2] == 'AT' or slaveATTcommand[:4] == '* AT':
							slaveATTCommandList.append(slaveATTcommand)
					
					for i in range (0,len(row)):
						rowData.pop()
		
		slaveATTCommandList=list(set(slaveATTCommandList))
		masterATTCommandList=list(set(masterATTCommandList))
		print "\nATT Commands by Slave\n"
		str1 = "ATT Commands by Slave\n"
		utilities.writeOnGUITextBox1(text,str1,"subtitle")
		utilities.writeOnGUITextBox1(text2,str1,"subtitle")
		print "\n".join(slaveATTCommandList)
		str1 = "\n".join(slaveATTCommandList)
		utilities.writeOnGUITextBox(text,str1)
		utilities.writeOnGUITextBox(text2,str1)
		str1 ="\n"
		utilities.writeOnGUITextBox(text,str1)
		utilities.writeOnGUITextBox(text2,str1)
		print "\nATT Commands by Master\n"
		str1 = "ATT Commands by Master\n"
		utilities.writeOnGUITextBox1(text,str1,"subtitle")
		utilities.writeOnGUITextBox1(text2,str1,"subtitle")
		print "\n".join(masterATTCommandList)
		str1 = "\n".join(masterATTCommandList)
		utilities.writeOnGUITextBox(text,str1)
		utilities.writeOnGUITextBox(text2,str1)
		str1 ="\n"
		utilities.writeOnGUITextBox(text,str1)
		utilities.writeOnGUITextBox(text2,str1)
	csvFile.close()

	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		print "\nFrame#\t", "By\t", "\tCommand\t\t","Response"
		str1 = "Frame#\t" + "By\t" + "Command\t\t" + "Response\t\t" + "AT Info"+"\n"
		utilities.writeOnGUITextBox1(text,str1,"subtitle")
		utilities.writeOnGUITextBox1(text3,str1,"subtitle")
		print "\n-----------------------------------------------------------"
		str1 = "\n--------------------------------------------------------------------------------"
		utilities.writeOnGUITextBox(text,str1)
		utilities.writeOnGUITextBox(text3,str1)
		for row in csvReader:
				if lineInCSV == 1:
					for i in range (0,len(row)):
						fieldNames.append(row[i])
					print "1", fieldNames
				lineInCSV= lineInCSV + 1
				if lineInCSV > 2:
					for i in range (0,len(row)):
						rowData.append(row[i])
					#print rowData
					command=str(rowData[int(fieldNames.index('Hands-Free data'))])
					#print 'C:',command
					if command[:2] == 'AT' or command[:4] == '* AT':
						if command[:4] == '* AT':
							packetDetails['Initiated By']=str(rowData[int(fieldNames.index('Role'))])[2:]
							packetDetails['Command'] = command[2:]
							packetDetails['Command'] = packetDetails['Command'].translate(None, ' .')
							packetDetails['Info']=str(rowData[int(fieldNames.index('AT Cmd'))])
							num = int(rowData[int(fieldNames.index('Frame#'))]) + 2
							num1 =int(rowData[int(fieldNames.index('Frame#'))]) + 3
							num2 =int(rowData[int(fieldNames.index('Frame#'))]) + 1
						else:
							packetDetails['Initiated By']=str(rowData[int(fieldNames.index('Role'))])
							packetDetails['Command'] = command
							packetDetails['Command'] = packetDetails['Command'].translate(None, ' .')
							packetDetails['Info']=str(rowData[int(fieldNames.index('AT Cmd'))])
							num = int(rowData[int(fieldNames.index('Frame#'))]) + 2
							num1 =int(rowData[int(fieldNames.index('Frame#'))]) + 3
							num2 =int(rowData[int(fieldNames.index('Frame#'))]) + 1
						isDone =1
					if isDone ==1 and (rowData[int(fieldNames.index('Frame#'))]== str(num) or rowData[int(fieldNames.index('Frame#'))]== str(num1) or rowData[int(fieldNames.index('Frame#'))]== str(num2)):
						packetDetails['Status']= rowData[int(fieldNames.index('Hands-Free data'))][2:]
						packetDetails['Status'] = packetDetails['Status'].translate(None, ' .")(')
						packetDetails['Frame#'] = rowData[int(fieldNames.index('Frame#'))]
						#print rowData[int(fieldNames.index('Hands-Free data'))][2:]
						if packetDetails['Status'][:5] == 'ERROR':
							print "\n",packetDetails['Frame#'],"\t",packetDetails['Initiated By'],"\t",packetDetails['Command'],"\t\t",packetDetails['Status'],"\t\t",packetDetails['Info'],""
							str1 = "\n"+packetDetails['Frame#']+"\t"+packetDetails['Initiated By']+"\t"+packetDetails['Command']+"\t\t"+packetDetails['Status']+"\t\t"+packetDetails['Info'][:30]+'..'
							utilities.writeOnGUITextBox1(text,str1,"error")
							utilities.writeOnGUITextBox1(text3,str1,"error")
						elif len(str(packetDetails['Status'])) >= 12 or len(str(packetDetails['Info'])) >= 30:
							print "\n",packetDetails['Frame#'],"\t",packetDetails['Initiated By'],"\t",packetDetails['Command'],"\t\t",packetDetails['Status'][:12],"\t\t",packetDetails['Info'],""
							str1 = "\n"+packetDetails['Frame#']+"\t"+packetDetails['Initiated By']+"\t"+packetDetails['Command']+"\t\t"+packetDetails['Status'][:12]+'..'+"\t\t"+packetDetails['Info'][:30]+'..'
							utilities.writeOnGUITextBox(text,str1)
							utilities.writeOnGUITextBox(text3,str1)
						else:
							print "\n",packetDetails['Frame#'],"\t",packetDetails['Initiated By'],"\t",packetDetails['Command'],"\t\t",packetDetails['Status'],"\t\t",packetDetails['Info'],""
							str1 = "\n"+packetDetails['Frame#']+"\t"+packetDetails['Initiated By']+"\t"+packetDetails['Command']+"\t\t"+packetDetails['Status']+"\t\t"+packetDetails['Info']
							print "\n---",str1
							utilities.writeOnGUITextBox(text,str1)
							utilities.writeOnGUITextBox(text3,str1)
						#print packetDetails
					#	print int(rowData[int(fieldNames.index('Frame#'))]
						#print 'fram# from rowData',int(rowData[int(fieldNames.index('Frame#'))])
						#print 'P:',packetDetails
					#print int(rowData[int(fieldNames.index('Frame#'))]
					#num = packetDetails['Frame#']
					#print num
					#if int(rowData[int(fieldNames.index('Frame#'))] ==num and isDone==1:
					#	print 'AT :',str(rowData[int(fieldNames.index('Hands-Free data'))])
					#	print 'P:',packetDetails
					for i in range (0,len(row)):
						rowData.pop()
