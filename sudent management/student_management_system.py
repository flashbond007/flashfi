import getpass
path=r'C:\Users\flash\Desktop\ethans\hey_flash.txt'
path1=r'C:\Users\flash\Desktop\credential.txt'
width="*"*50
rno=''
dict11={}
new_rno={}

name=''
father=''
maths=''
eng=''
science=''
hindi=''
percentage=''

def get_last_no():
	fh=open(path)
	total=len(fh.readlines())
	fh.close()
	return total


def add_info():    
	print(width)
	sname=input("Enter student name:")
	fname=input("Enter father name:")
	mmarks=int(input("enter marks for maths:"))
	hmarks=int(input("enter marks for hindi:"))
	emarks=int(input("enter marks for english:"))
	smarks=int(input("enter marks for science:"))
	percent=((mmarks+emarks+smarks+hmarks)/400)*100
	global dict11,rno,name,father,maths,eng,science,hindi,percentage
	rno=get_last_no()+1
	temp_dict={rno:{'name':sname,'fname':fname,'marks':{'maths':mmarks,'hindi':hmarks,'english':emarks,'science':smarks,'percent':percent}}}
	name=sname
	father=fname
	maths=mmarks
	eng=emarks
	hindi=hmarks
	science=smarks
	percentage=percent
	dict11.update(temp_dict)	
	print('data entered succesfully')
	print('*'*50)
	return teacher_menu()

def read_parser(file_name):
	global dict11
	fh = open(file_name)
	for line in fh:
		rno,sname,fname,mmarks,emarks,hmarks,smarks,percent = line.split(',')
		if '#' not in rno:
			dict11[rno] = {'name':sname,'father_name':fname,
						  'marks' : {'maths':mmarks,'english':emarks,'hindi':hmarks,'science':smarks,'percent':percent}}
	fh.close()
	return dict11



def get_student_data(name):
	fh=open(path)
	r_no=[]
	for line in fh:
		if name in line:
			data=line.split(',')
			r_no.append(data)			
	return r_no


def view_result():
	name=input('Enter name to view result::')
	data=get_student_data(name)
	if data:
		print(width)
		print(f"name:  					{data[0][1]}")
		print(f"Father name:   		    {data[0][2]}")
		print(width)
		print("Marks::")
		print(f"Marks in hindi:  		{data[0][3]}")
		print(f"Marks in maths:  		{data[0][4]}")
		print(f"Marks in english:  		{data[0][5]}")
		print(f"Marks in science: 		{data[0][6]}")
		print(f"Total percentage:  		{data[0][7]}")
		print(width)
		print(width)
	return teacher_menu()


def search_with_name():
	print(width)
	name=input('Enter name of the student: ')
	data=get_roll(name)
	if data:
		print(f"Roll no of {name} is {data}")
		print(width)
		return teacher_menu()


def get_roll(name):
	fh=open(path)
	r_no=[]
	for line in fh:
		if name in line:
			data=line.split(',')[:1]
			r_no.append(data)			
	return r_no



def teacher_menu():
	print(width)
	print('1.Add information about students')
	print('2.view results by entering roll no')
	print('3.search student by name')
	print('4.exit')
	tchoice=int(input('enter your choice to perform operations::'))
	print('*'*50)
	if tchoice==1:
		return add_info()
	elif tchoice==2:
		return view_result()
	elif tchoice==3:
		return search_with_name()
	elif tchoice==4:
		return main()
	else:
		print('Wrong choice')


def student_menu():
	print(width)
	print("1.View student Roll no")
	print("2.View result")
	choice=int(input("enter yr choice from above meunu"))
	if choice==1:
		return search_with_name()
	elif choice==2:
		return view_result()
	elif chocie==3:
		return main()
	else:
		print("Invalid choice ")

def teacher_login():
	print(width)
	uname=input('Pls Enter Yr username: ')
	passw=input('Pls Enter Yr password: ')
	fh=open(path1,'r')
	for line in fh:
		login=line.split(',')
		if uname==login[0] and passw==login[1]:
			print("Login successfull")
			return teacher_menu()
		else:
			print("wrong username and password")


def main():
	print('-'*121)
	print('*****************************Flash & Zak School***********************************')
	print('-'*121)
	print('*'*50)
	print('1.Teacher Login')
	print('2.Student Login')
	print('*'*50)
	choice=int(input('Enter Yr choice::'))
	if choice==1:
		return teacher_login()
	elif choice==2:
		return student_menu()
	else:
		print('incorrect choice')
main()


def write_parser(file_name,rno,name,father_name,maths,english,hindi,science,percent):
	d = read_parser(file_name)
	fh = open(file_name,'a')
	fh.write(f'\n{rno},{name},{father_name},{maths},{english},{hindi},{science},{percent}')
	fh.close()
	return 'New data added'

write_parser(path,rno,name,father,maths,eng,hindi,science,percentage)