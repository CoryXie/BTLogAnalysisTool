import csv
import sys
from array import *
from datetime import datetime
from datetime import timedelta
import datetime as dt
import utilities
#import main2
def code(text,text2,text3,text4,filepath):
	print filepath
	fieldNames=[]
	sum1 = dt.timedelta(seconds=0)
	print sum1
	rowData=[]
	lineInCSV =1
	searchResponse1 = 0
	searchResponse2 = 0
	isDone=0
	mnameDone=0
	mManufactureFound=sManufactureFound=0
	snameDone=0
	masterName=0
	responseFound=0
	masterDetails={}
	slaveDetails={}
	latencyOfInquiryList=[]
	latencyOfConnectionList=[]
	requestTimeObject = datetime.now()
	responseTimeObject = datetime.now()
	print "HCI4 LMP CSV"
	str1 ="\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox1(text,str1,"title")
	utilities.writeOnGUITextBox1(text2,str1,"title")
	utilities.writeOnGUITextBox1(text3,str1,"title")
	utilities.writeOnGUITextBox1(text4,str1,"title")
	str1 = "\t\tBTSNOOP LOG HCI LAYER ANALYSIS\n\n"
	utilities.writeOnGUITextBox1(text,str1,"title")
	utilities.writeOnGUITextBox1(text2,str1,"title")
	utilities.writeOnGUITextBox1(text3,str1,"title")
	utilities.writeOnGUITextBox1(text4,str1,"title")
	#print 'Filename:',main2.filename
	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		for row in csvReader:
			if isDone==0:
				if lineInCSV == 1:
					for i in range (0,len(row)):
						fieldNames.append(row[i])
					print "1", fieldNames
				lineInCSV= lineInCSV + 1
				if lineInCSV > 2:
					for i in range (0,len(row)):
						rowData.append(row[i])
					#print rowData
					if str(rowData[int(fieldNames.index('Opcode Command'))]) == 'Change_Local_Name' and mnameDone!= 1:
						masterDetails['DeviceName']= str(rowData[int(fieldNames.index('Name'))])
						mnameDone=1
					elif mnameDone==0:
						masterDetails['DeviceName']= 'Not Found'
					if str(rowData[int(fieldNames.index('Type'))]) == 'Event' and str(rowData[int(fieldNames.index('Opcode Command'))]) == 'Read_Local_Version_Information' and mManufactureFound!=1:
						masterDetails['Manufacture']= str(rowData[int(fieldNames.index('Manufacturer Name'))])
						#print "Inside mManu",rowData[int(fieldNames.index('Manufacturer Name'))], "--",masterDetails['Manufacture']
						masterDetails['Bluetooth']= rowData[int(fieldNames.index('LMP Version'))]
						masterDetails['Version']= rowData[int(fieldNames.index('LMP Subversion'))]
						mManufactureFound=1
					elif mManufactureFound==0:
						masterDetails['Manufacture']= 'Not Found'
						masterDetails['Bluetooth']= 'Not Found'
						masterDetails['Version']= 'Not Found'					
					if str(rowData[int(fieldNames.index('Event'))]) == 'Remote Name Request Complete':
						slaveDetails['DeviceName']= rowData[int(fieldNames.index('Name'))]			
						#print "Inside SDeviceManu",rowData[int(fieldNames.index('Name'))], "--",slaveDetails['DeviceName']
						snameDone=1
					elif snameDone==0:
						slaveDetails['DeviceName']= 'Not Found'
					if str(rowData[int(fieldNames.index('Event'))]) == 'Read Remote Version Information Complete' and sManufactureFound!=1:
						slaveDetails['Manufacture']= rowData[int(fieldNames.index('Manufacturer Name'))]
						slaveDetails['Bluetooth']= rowData[int(fieldNames.index('LMP Version'))]
						slaveDetails['Version']= rowData[int(fieldNames.index('LMP Subversion'))]
						sManufactureFound=1
					elif sManufactureFound==0:
						slaveDetails['Manufacture']= 'Not Found'
						slaveDetails['Bluetooth']= 'Not Found'
						slaveDetails['Version']= 'Not Found'										
						#isDone=1
					for i in range (0,len(row)):
						rowData.pop()
		csvFile.close()
	print "\n-------------------HOST-------------------"
	str1 = "-------------------HOST-------------------\n"
	utilities.writeOnGUITextBox1(text,str1,"subtitle")
	utilities.writeOnGUITextBox1(text2,str1,"subtitle")
	print "\nFriendly Name\t\t:", masterDetails['DeviceName'], "\nManufacture Name\t:", masterDetails['Manufacture'],"\nBluetooth Specification\t:", masterDetails['Bluetooth'],"\nVersion NUmber\t\t:", masterDetails['Version']
	str1 = "Friendly Name\t\t:"+masterDetails['DeviceName']+"\nManufacture Name\t:"+masterDetails['Manufacture']+"\nBluetooth Specification\t:"+masterDetails['Bluetooth']+"\nVersion NUmber\t\t:"+ masterDetails['Version']+"\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox(text2,str1)
	print "\n-------------------CONTROLLER-------------------"
	str1 = "-------------------CONTROLLER-------------------\n"
	utilities.writeOnGUITextBox1(text,str1,"subtitle")
	utilities.writeOnGUITextBox1(text2,str1,"subtitle")
	print "\nFriendly Name\t\t:", slaveDetails['DeviceName'], "\nManufacture Name\t:", slaveDetails['Manufacture'],"\nBluetooth Specification\t:", slaveDetails['Bluetooth'],"\nVersion NUmber\t\t:", slaveDetails['Version']
	str1 = "Friendly Name\t\t:"+slaveDetails['DeviceName']+"\nManufacture Name\t:"+slaveDetails['Manufacture']+"\nBluetooth Specification\t:"+slaveDetails['Bluetooth']+"\nVersion NUmber\t\t:"+slaveDetails['Version']+"\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox(text2,str1)
	#print "Device\tFriendly Name\t\tManufacture Name\t\tBluetooth Specification\t\tVersion Number\n"
	#print "\nMaster\t","\t\t".join(masterDetails)
	#print "\nSlave\t","\t\t".join(slaveDetails)

	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		#print "\nOPened"
		#print requestType
		#requestType= 'host_connection_req'
		lineInCSV=1
		#requestType = raw_input("Enter the Type of Request: ")	
		inquiryEndDone=inquiryStartDone=connectionStartDone=connectionEndDone=0
		for row in csvReader:
			if lineInCSV == 1:
				for i in range (0,len(row)):
					fieldNames.append(row[i])
				#print "2",fieldNames
			lineInCSV= lineInCSV + 1
			if lineInCSV > 2:
				#print "line>2"
				for i in range (0,len(row)):
					rowData.append(row[i])
				#print rowData
				if str(rowData[int(fieldNames.index('Type'))]) == 'Command' and str(rowData[int(fieldNames.index('Opcode Command'))]) == 'Inquiry':# and inquiryStartDone!=1:
					masterDetails['InquiryStartTime']= str(rowData[int(fieldNames.index('Timestamp'))])
					#print "IST",masterDetails['InquiryStartTime']
					inquiryStartDone=1
				if str(rowData[int(fieldNames.index('Type'))]) == 'Event' and str(rowData[int(fieldNames.index('Event'))]) == 'Inquiry Result with RSSI':# and inquiryEndDone!=1:
					masterDetails['InquiryEndTime']= str(rowData[int(fieldNames.index('Timestamp'))])
					#print "IET",masterDetails['InquiryEndTime']
					inquiryEndDone=1
					#print "\nOUT\n", masterDetails['InquiryStartTime'],"-",masterDetails['InquiryEndTime'],"\n",masterDetails['ConnectionStartTime'],"-",masterDetails['ConnectionEndTime']
					requestTime = masterDetails['InquiryStartTime'].translate(None, '=\"')
					requestTime=requestTime.replace("/","-")
					#print requestTime	
					requestTimeObject = datetime.strptime(requestTime, '%m-%d-%Y %H:%M:%S.%f %p')
					#print requestTimeObject
					#requestTime = (rowData[int(fieldNames.index('Timestamp'))]
							
					responseTime = masterDetails['InquiryEndTime'].translate(None, '=\"')
					responseTime=responseTime.replace("/","-")
					#print responseTime	
					responseTimeObject = datetime.strptime(responseTime, '%m-%d-%Y %H:%M:%S.%f %p')
					#print responseTimeObject
					latencyOfInquiry = responseTimeObject - requestTimeObject
					#print "\nINQUIRY LATENCY IS : " , latencyOfInquiry, "\n\n"
					latencyOfInquiryList.append(latencyOfInquiry)
					
				if str(rowData[int(fieldNames.index('Type'))]) == 'Command' and str(rowData[int(fieldNames.index('Opcode Command'))]) == 'Create_Connection':# and connectionStartDone!=1:
					masterDetails['ConnectionStartTime']= str(rowData[int(fieldNames.index('Timestamp'))])
					
					#print "CST",masterDetails['ConnectionStartTime']
					connectionStartDone=1
				if str(rowData[int(fieldNames.index('Type'))]) == 'Event' and str(rowData[int(fieldNames.index('Event'))]) == 'Connection Complete':# and connectionEndDone!=1:
					masterDetails['ConnectionEndTime']= str(rowData[int(fieldNames.index('Timestamp'))])
					#print "CET",masterDetails['ConnectionEndTime']
					connectionEndDone=1
					requestTime = masterDetails['ConnectionStartTime'].translate(None, '=\"')
					requestTime=requestTime.replace("/","-")
					#print requestTime	
					requestTimeObject = datetime.strptime(requestTime, '%m-%d-%Y %H:%M:%S.%f %p')
					#print requestTimeObject
					#requestTime = (rowData[int(fieldNames.index('Timestamp'))]
							
					responseTime = masterDetails['ConnectionEndTime'].translate(None, '=\"')
					responseTime=responseTime.replace("/","-")
					#print responseTime	
					responseTimeObject = datetime.strptime(responseTime, '%m-%d-%Y %H:%M:%S.%f %p')
					#print responseTimeObject
					latencyOfConnection = responseTimeObject - requestTimeObject
					#print "\nCONNECTION LATENCY IS : " , latencyOfConnection, "\n\n"
					latencyOfConnectionList.append(latencyOfConnection)
				for i in range (0,len(row)):
					rowData.pop()
		
		if len(latencyOfConnectionList) != 0:
			str1 ="\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text3,str1)
			print "List of all Connection Latency:\n"
			str1 = "List of all Connection Latencies:\n"
			utilities.writeOnGUITextBox1(text,str1,"subtitle")
			utilities.writeOnGUITextBox1(text3,str1,"subtitle")
			print latencyOfConnectionList
			utilities.writeOnGUITextBox(text,latencyOfConnectionList)
			utilities.writeOnGUITextBox(text3,latencyOfConnectionList)

			for i in range(0, len(latencyOfConnectionList)):
				sum1=sum1 + latencyOfConnectionList[i]
				#print sum1
			avgConnection= sum1/len(latencyOfConnectionList)
			list.sort(latencyOfConnectionList)
			#print "Sorted CL:",latencyOfConnectionList
			str1 ="\n\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text3,str1)
			print "MINIMUM CONNECTION LATENCY IS:", latencyOfConnectionList[0]
			str1 = "MINIMUM CONNECTION LATENCY IS:"+str(latencyOfConnectionList[0])+"\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text3,str1)
			print "\nMAXIMUM CONNECTION LATENCY IS:", latencyOfConnectionList[len(latencyOfConnectionList)-1]
			str1 = "MAXIMUM CONNECTION LATENCY IS:"+ str(latencyOfConnectionList[len(latencyOfConnectionList)-1]) + "\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text3,str1)
			
			if avgConnection > dt.timedelta(seconds=8):
				print "\nAVERAGE CONNECTION TIME IS ", avgConnection
				str1 = "AVERAGE CONNECTION TIME IS "+str(avgConnection)+"\n"
				utilities.writeOnGUITextBox1(text,str1,"error")
				utilities.writeOnGUITextBox1(text3,str1,"error")
				print "more than 8 seconds"
				str1="Average Connection time is MORE than 8 seconds"
				utilities.writeOnGUITextBox1(text,str1,"error")
				utilities.writeOnGUITextBox1(text4,str1,"error")
			else:
				print "\nAVERAGE CONNECTION TIME IS ", avgConnection
				str1 = "AVERAGE CONNECTION TIME IS "+str(avgConnection)+"\n"
				utilities.writeOnGUITextBox(text,str1)
				utilities.writeOnGUITextBox(text3,str1)
				print "less than 8 seconds"
		if len(latencyOfInquiryList) !=0:
			str1 ="\n"
			utilities.writeOnGUITextBox(text,str1)
			print "List of all Inquiry Latency :\n"
			str1 = "List of all Inquiry Latency :\n"
			utilities.writeOnGUITextBox1(text,str1,"subtitle")
			utilities.writeOnGUITextBox1(text4,str1,"subtitle")

			print latencyOfInquiryList
			utilities.writeOnGUITextBox(text,latencyOfInquiryList)
			utilities.writeOnGUITextBox(text4,latencyOfInquiryList)
			sum1 = dt.timedelta(seconds=0)
			
			for i in range(0, len(latencyOfInquiryList)):
				sum1=sum1 + latencyOfInquiryList[i]
				#print sum1
			avgInquiry= sum1/len(latencyOfInquiryList)
			list.sort(latencyOfInquiryList)
			#print "Sorted IL:",latencyOfInquiryList
			str1 ="\n\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text4,str1)
			print "\nMINIMUM INQUIRY LATENCY IS:", latencyOfInquiryList[0]
			str1 = "MINIMUM INQUIRY LATENCY IS:"+str(latencyOfInquiryList[0])+"\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text4,str1)
			print "\nMAXIMUM INQUIRY LATENCY IS:", latencyOfInquiryList[len(latencyOfInquiryList)-1]
			str1 = "MAXIMUM INQUIRY LATENCY IS:"+ str(latencyOfInquiryList[len(latencyOfInquiryList)-1]) + "\n"
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text4,str1)
			
			if avgInquiry > dt.timedelta(seconds=8):
				print "\nAVERAGE INQUIRY TIME IS : ", avgInquiry
				str1 = "AVERAGE INQUIRY TIME IS : "+ str(avgInquiry)+"\n"
				utilities.writeOnGUITextBox1(text,str1,"error")
				utilities.writeOnGUITextBox1(text4,str1,"error")
				print "more than 8 seconds"
				str1="Average Inquiry time is MORE than 8 seconds"
				utilities.writeOnGUITextBox1(text,str1,"error")
				utilities.writeOnGUITextBox1(text4,str1,"error")
			else:
				print "\nAVERAGE INQUIRY TIME IS : ", avgInquiry
				str1 = "AVERAGE INQUIRY TIME IS : "+ str(avgInquiry)+"\n"
				utilities.writeOnGUITextBox(text,str1)
				utilities.writeOnGUITextBox(text4,str1)
				print "less than 8 seconds"
		if inquiryEndDone == 0:
			str1 ="\n"
			utilities.writeOnGUITextBox(text,str1)
			print "\nNO INQUIRY MESSAGES ENCOUNTERED"
			str1 = "NO INQUIRY MESSAGES ENCOUNTERED"
			utilities.writeOnGUITextBox1(text,str1,"subtitle")
			utilities.writeOnGUITextBox1(text4,str1,"subtitle")

		elif connectionEndDone == 0:
			str1 ="\n"
			utilities.writeOnGUITextBox(text,str1)
			print "\nNO CONNECTION MESSAGES ENCOUNTERED"
			str1 = "NO CONNECTION MESSAGES ENCOUNTERED\n"
			utilities.writeOnGUITextBox1(text,str1,"subtitle")
			utilities.writeOnGUITextBox1(text4,str1,"subtitle")
		#responseTime = rowData[int(fieldNames.index('Timestamp'))]		
				#print "Poped"
		#print "Final"	

