import csv
import sys
from array import *
from sets import Set
import utilities
from datetime import datetime
from datetime import timedelta

def code(text,text2,avdtpFilename,avrcpFilename):
	lineInCSV=1
	fieldNames=[]
	rowData=[]
	packetDetails={}
	print "OTAAvdtpAvrcp!!!"
	global avdtpFilename1
	global avrcpFilename1
	avdtpFilename1=avdtpFilename
	avrcpFilename1=avrcpFilename
	with open(avdtpFilename, 'rb') as csvFile1:
		csvAVDTPReader = csv.reader(csvFile1, quoting=csv.QUOTE_ALL)
		print csvAVDTPReader
		with open(avrcpFilename, 'rb') as csvFile2:
			csvAVRCPReader = csv.reader(csvFile2, quoting=csv.QUOTE_ALL)
			print csvAVRCPReader
			for  AVRCProw in csvAVRCPReader:
				if lineInCSV == 1:
					for i in range (0,len(AVRCProw)):
						fieldNames.append(AVRCProw[i])
					print fieldNames
				lineInCSV= lineInCSV + 1
				#print lineInCSV
				if lineInCSV > 2:
					for i in range (0,len(AVRCProw)):
						rowData.append(AVRCProw[i])
					#print rowData
					if len(str(rowData[int(fieldNames.index('Operation ID'))])) != 0 and  rowData[int(fieldNames.index('ctype'))] == 'CONTROL':
						packetDetails['Frame#']= rowData[int(fieldNames.index('Frame#'))]
						packetDetails['Operation ID']= rowData[int(fieldNames.index('Operation ID'))]
						packetDetails['Timestamp']= rowData[int(fieldNames.index('Timestamp'))]
						responseTime = packetDetails['Timestamp'].translate(None, '=\"')
						responseTime=responseTime.replace("/","-")
						#print responseTime	
						responseTimeObject = datetime.strptime(responseTime, '%m-%d-%Y %H:%M:%S.%f %p')
						#print '--',rowData[int(fieldNames.index('Operation ID'))]
						
					if (rowData[int(fieldNames.index('Operation ID'))] == 'play') or (rowData[int(fieldNames.index('Operation ID'))] == 'pause'): ## eNTER AND CONDITION FOR REPEATED PROFILES
						print "\n\n\n\nOPERATION: ",rowData[int(fieldNames.index('Operation ID'))],"Frame #:",rowData[int(fieldNames.index('Frame#'))]
						result=AVRCPanalyse(rowData[int(fieldNames.index('Operation ID'))],rowData[int(fieldNames.index('Frame#'))])
						if result == 1:
							packetDetails['result']= "Success"
						if result == 0:
							packetDetails['result']= "Failed"
						print "RESULT :",result
						print '\n', packetDetails['Frame#'], '\t' ,packetDetails['Operation ID'],'\t',packetDetails['result'], '\t\t', str(responseTimeObject)
						str1= packetDetails['Frame#'] + '\t' + packetDetails['Operation ID'] + '\t' + packetDetails['result'] + '\t\t' + str(responseTimeObject) + '\n'
						utilities.writeOnGUITextBox(text,str1)
						utilities.writeOnGUITextBox(text2,str1)
					
					for i in range(0,len(AVRCProw)):
						rowData.pop()
			

def AVRCPanalyse(operation,frameNum):
	global avdtpFilename1,avrcpFilename1
	lineInCSV=1
	fieldNames=[]
	rowData=[]
	print "frameNum:",frameNum,"operation:",operation
	with open(avdtpFilename1, 'rb') as csvFile1:
		csvAVDTPReader = csv.reader(csvFile1, quoting=csv.QUOTE_ALL)
		#print csvAVDTPReader
		found=0
		for AVDTProw in csvAVDTPReader:
			if lineInCSV == 1:
				for i in range (0,len(AVDTProw)):
					fieldNames.append(AVDTProw[i])
				print fieldNames
			lineInCSV= lineInCSV + 1
				#print lineInCSV
			if lineInCSV > 2:
				for i in range (0,len(AVDTProw)):
					rowData.append(AVDTProw[i])
				#print rowData[int(fieldNames.index('Frame#'))] 
				#print rowData,"\n"
				if int(rowData[int(fieldNames.index('Frame#'))]) >= int(frameNum) and int(rowData[int(fieldNames.index('Frame#'))]) < (int(frameNum) + 1000):
					#print "operation:",operation,"\nDATA",rowData
					if operation == 'play' and rowData[int(fieldNames.index('Signal ID'))] == 'START':
						#print "PLAY/START-->",rowData,"\n"
						found=1
						return 1
					elif operation == 'pause' and rowData[int(fieldNames.index('Signal ID'))] == 'SUSPEND':
						#print "PAUSE/SUSPEND-->",rowData,"\n"
						found=1
						return 1
				
				#for int(rowData[int(fieldNames.index('Frame#'))]) in range(frameNum,frameNum + 100):
						#print rowData[int(fieldNames.index('Frame#'))]
		
				for i in range(0,len(AVDTProw)):
					rowData.pop()
		if found == 0:
			return 0
			
		#for frame in range(frameNum,