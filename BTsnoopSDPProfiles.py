import csv
import sys
from array import *
from sets import Set
import utilities
def code(text,text2,filepath):
	print filepath
	fieldNames=[]
	rowData=[]
	lineInCSV =1
	searchResponse =0
	masterProfiles=[]
	masterProfilesVersion=[]
	slaveProfiles=[]
	slaveProfilesVersion=[]
	file= str(filepath)
	print "BT SNOOP SDP CSV\n"
	str1 ="\n"
	utilities.writeOnGUITextBox(text,str1)
	utilities.writeOnGUITextBox(text2,str1)
	str1 = "\t\tBTsnoop Log SDP Layer Analysis for file " + file +"\n\n"
	str11 = "\t\tBTSNOOP LOG SDP LAYER ANALYSIS \n\n"
	utilities.writeOnGUITextBox1(text,str11,"title")
	utilities.writeOnGUITextBox1(text2,str11,"title")
	with open(filepath, 'rb') as csvFile:
		csvReader = csv.reader(csvFile, quoting=csv.QUOTE_ALL)
		
		for row in csvReader:
			if lineInCSV == 1:
				for i in range (0,len(row)):
					fieldNames.append(row[i])
				print fieldNames
			lineInCSV= lineInCSV + 1
			if lineInCSV > 2:
				for i in range (0,len(row)):
					rowData.append(row[i])
				#print rowData
				if rowData[int(fieldNames.index('Role'))] == 'Master' : ## eNTER AND CONDITION FOR REPEATED PROFILES
					if rowData[int(fieldNames.index('UUID'))] not in masterProfiles and rowData[int(fieldNames.index('UUID'))] != '':
						masterProfiles.append(rowData[int(fieldNames.index('UUID'))])
						masterProfilesVersion.append(rowData[int(fieldNames.index('Version'))])
				if rowData[int(fieldNames.index('Role'))] == 'Slave' : ## eNTER AND CONDITION FOR REPEATED PROFILES
					if rowData[int(fieldNames.index('UUID'))] not in slaveProfiles and rowData[int(fieldNames.index('UUID'))] != '':
						slaveProfiles.append(rowData[int(fieldNames.index('UUID'))])		
						slaveProfilesVersion.append(rowData[int(fieldNames.index('Version'))])
				for i in range (0,len(row)):
					rowData.pop()
	print "---------------Master Supported Profiles---------"
	str1 = "---------------Master Supported Profiles---------\n"
	utilities.writeOnGUITextBox1(text,str1,"subtitle")
	utilities.writeOnGUITextBox1(text2,str1,"subtitle")
	for i in range(0,len(masterProfiles)):
		if len(str(masterProfilesVersion[i])) == 0:
			print masterProfiles[i]," ",masterProfilesVersion[i],'\n'
			str1 = masterProfiles[i] + " " + masterProfilesVersion[i]+'\n'
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text2,str1)
		else:
			print masterProfiles[i]," ",masterProfilesVersion[i],'\n'
			str1 = masterProfiles[i] + "\t\tVersion  :" + masterProfilesVersion[i]+'\n'
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text2,str1)
	print "-------------Slave Supported Profiles-----------"
	str1 = "-------------Slave Supported Profiles-----------\n"
	utilities.writeOnGUITextBox1(text,str1,"subtitle")
	utilities.writeOnGUITextBox1(text2,str1,"subtitle")
	for i in range(0,len(slaveProfiles)):
		if len(str(slaveProfilesVersion[i])) == 0:
			print '\n',slaveProfiles[i]," ",slaveProfilesVersion[i],'\n'
			str1 = slaveProfiles[i] + " " + slaveProfilesVersion[i]+'\n'
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text2,str1)
		else:
			print '\n',slaveProfiles[i]," ",slaveProfilesVersion[i],'\n'
			str1 = slaveProfiles[i] + "\t\tVersion :" + slaveProfilesVersion[i]+'\n'
			utilities.writeOnGUITextBox(text,str1)
			utilities.writeOnGUITextBox(text2,str1)