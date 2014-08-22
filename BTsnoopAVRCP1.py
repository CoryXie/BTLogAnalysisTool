import csv
import sys
import sets
from array import *
from datetime import datetime
from datetime import timedelta
import utilities
def code(text,text2,filepath):
	print filepath
	responseTimeObjectTimeObject = datetime.now()
	#util1 = utilities()
	fieldNames=[]
	rowData=[]
	lineInCSV =1
	isDone=0
	masterDetails={}
	slaveDetails={}
	packetDetails={}
	print "AVRCP CSV"
	str1 ="\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox(text2,str1)
	str1= "\t\tBTSNOOP LOG AVRCP LAYER ANALYSIS\n\n"
	utilities.writeOnGUITextBox1(text,str1,"title")
	utilities.writeOnGUITextBox1(text2,str1,"title")
	print "\nFrame#\t Action\t\t Timestamp"
	str1= "Frame#\t Action\t\t Timestamp\n"
	utilities.writeOnGUITextBox1(text,str1,"subtitle")
	utilities.writeOnGUITextBox1(text2,str1,"subtitle")
	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		for row in csvReader:
				if lineInCSV == 1:
					for i in range (0,len(row)):
						fieldNames.append(row[i])
					#print "1", fieldNames
				lineInCSV= lineInCSV + 1
				
				if lineInCSV > 2:
					for i in range (0,len(row)):
						rowData.append(row[i])
					#print rowData[1]
					#print len(str(rowData[int(fieldNames.index('OpCode'))]))
					#print rowData[int(fieldNames.index('Operation ID'))]
					if len(str(rowData[int(fieldNames.index('Operation ID'))])) != 0 and  rowData[int(fieldNames.index('ctype'))] == 'CONTROL':
						packetDetails['Frame#']= rowData[int(fieldNames.index('Frame#'))]
						packetDetails['Operation ID']= rowData[int(fieldNames.index('Operation ID'))]
						packetDetails['Timestamp']= rowData[int(fieldNames.index('Timestamp'))]
						responseTime = packetDetails['Timestamp'].translate(None, '=\"')
						responseTime=responseTime.replace("/","-")
						#print responseTime	
						responseTimeObject = datetime.strptime(responseTime, '%m-%d-%Y %H:%M:%S.%f %p')
						#print '--',rowData[int(fieldNames.index('Operation ID'))]
						print '\n', packetDetails['Frame#'], '\t' ,packetDetails['Operation ID'], '\t\t', str(responseTimeObject)
						str1= packetDetails['Frame#'] + '\t' + packetDetails['Operation ID'] + '\t\t' + str(responseTimeObject) + '\n'
						utilities.writeOnGUITextBox(text,str1)
						utilities.writeOnGUITextBox(text2,str1)
					for i in range (0,len(row)):
						rowData.pop()