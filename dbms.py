import csv
import sys
import subprocess



def show(table):
	print "\nRelational table \n"
	with open(table,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			print row
	subprocess.call(["libreoffice",table])	
	
def printT(table):
	subprocess.call(["libreoffice",table])
		
def union(tab1,tab2):
	print "\nAfter Union of table 1 and table 2: \n\n"
	
	unique=[]
	with open(tab1,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			unique.append(row)
		
	with open(tab2,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			if len(unique[0]) != len(row):
				print "arity not same! Union not possible"
			if row not in unique:
				unique.append(row)
	for row in unique:
		print row			
	with open("output.csv", 'wb') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		for row in unique:
			wr.writerow(row)
	printT("output.csv")
	

def selection(table):
	print "available operations - >, <, =, <=, >= "
	fi=int(input("first operand: "))
	opertr=input("operator: ")
	si=int(input("second operand: "))
	with open(table,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			if opertr=="<" and row[fi]<row[si]:
				print row
			elif opertr==">" and row[fi]>row[si]:
				print row
			elif opertr=="<=" and row[fi]<=row[si]:
				print row
			elif opertr==">=" and row[fi]>=row[si]:
				print row
			elif opertr== "=" and row[fi]==row[si]:
				print row
		

def projection(table):
	col=[]	
	
	listIn=raw_input('Enter column number')
	l = listIn.split(',')
	col = [int(x) for x in l]
	with open(table,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			for i in col:
				sys.stdout.write(row[i]+" ")
			print ""
			
def cartesian(tab1,tab2):
	print "\nAfter cartesian product of table 1 and table 2: \n\n"
	with open(tab1,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			with open(tab2,'rb') as t:
				reader2= csv.reader(t)
				for row2 in reader2:
					print row+row2
				
				
def setDifference(tab1,tab2):
	print "\n After set difference table1-table2 \n"
	with open(tab1,'rb') as f:
		reader= csv.reader(f)
		for row in reader:
			with open(tab2,'rb') as t:
				reader2= csv.reader(t)
				if row not in reader2:
					print row
	
	

	
while True:
	print "\n\n*************Relational Algebra Implementation*************"
	print "\nAvailable tables - sample1.csv\n"
	print "Available operations- \n 0. Show table\n 1. Union \n 2. Selection \n 3. Projection \n 4. Catesian product\n 5. Set Difference"
	str1= raw_input('Enter your choice : ')
	try:
		choice =int(str1)
	except:
		pass
	if choice==0:
		toShow=raw_input('table to show: ')
		show(toShow)
	
	elif choice==1:
		table1=raw_input('enter 1st table: ')
		table2=raw_input('enter 2nd table: ')
		union(table1,table2)
	
	elif choice==2:
		table1=raw_input('enter table: ')
		selection(table1)

	elif choice==3:
		table1=raw_input('enter 1st table: ')
		projection(table1)
	
	elif choice==4:
		table1=raw_input('enter 1st table: ')
		table2=raw_input('enter 2nd table: ')
		cartesian(table1,table2)
	elif choice==5:
		table1=raw_input('enter 1st table: ')
		table2=raw_input('enter 2nd table: ')
		setDifference(table1,table2)
	elif choice==-1:
		break
		


