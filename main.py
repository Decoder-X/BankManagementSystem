import os,time,sys
import random

#version check
def version():
  ver_py = sys.version_info[:2]
  return ver_py

#input data
def inp_data(data):
  if version() < (3,0):
    inp = raw_input(data)
  else:
    inp = input(data)
  return inp


#random number create
def create_number():
  n = random.randint(100000000000000,999999999999999)
  return n

#money Add
def money_add(balance,a,loan,acc_pass):
	new_balance = inp_data("\033[1;32;40mHow much money do you add? \033[0m")
	balance = int(balance)+int(new_balance)
	n_w = open(a,"w")
	n_w.write(str(balance)+"|"+loan+"|"+acc_pass)
	n_w.close()
	print("\033[1;33;40m[ + ] Money added successfully\033[0m")
	

#Check Password correction
def pass_check(acc_pass,balance,p,state):
	     if p == acc_pass:
	     	print(state+ balance)
	     else:
	     	print("\n\t\033[1;31;40m[ !!! ] Wrong password\033[0m")
	     	time.sleep(2)
	     	options()
      

#Create an account
def creating_account(acc_num,file):
  acc_name = inp_data("Enter Your Name: ")
  acc_pass =inp_data("Create a password: ")
  file.write(acc_name+"|"+str(acc_num))
  file.write("\n")
  print("\033[1;32;40m[ * ]Account create successfully\033[0m")
  ac_file= "accounts/"+str(acc_num)
  f_w= open(ac_file,"w")
  f_w.write("1000"+"|"+"0"+"|"+str(acc_pass))
  f_w.close()
  print("\033[1;33;40mYour Account Name :\033[1;35;40m"+acc_name+"\033[0m")
  print("\033[1;33;40mYour Account Number :\033[1;35;40m"+str(acc_num)+"\033[0m")


#Overwrite the account
def set_acc():
  file = open("accounts/account.txt", "r+")
  for i in file:
    a, b= i.split("|")
    acc_num = create_number()
    if str(acc_num) in file:
      exit()
      print("Accounts full")
    else:
      creating_account(acc_num,file)
  file.close()
  return acc_num


#Balance Check
def check_balance(acc_num,acc_pass):
  a = "accounts/"+acc_num
  try:
    with open(a,"r+") as f:
      lis = f.read().split("|")
      balance = lis[0]
      p = lis[2]
      state = "Your balance is "
      pass_check(acc_pass,balance,p,state)
      	
  except:
    print("\033[1;31;40m[ ! ]No accounts Found\033[0m")


#Add Balance in Account
def add_balance(acc_num,acc_pass):
	a = "accounts/"+acc_num
	try:
	   with open(a,"r+") as f:
	   	b_l = f.read().split("|")
	   	balance = b_l[0]
	   	loan = b_l[1]
	   	p = b_l[2]
	   	state = "Your current balance is "
	   	pass_check(acc_pass,balance,p,state)
	   	money_add(balance,a,loan,acc_pass)
	   	
	except:
		print("\033[1;31;40m[ ! ]No accounts Found\033[0m")



#Take A Loan
def take_loan(acc_num,acc_pass):
	a = "accounts/"+acc_num
	try:
	   with open(a,"r+") as f:
	   	b_l = f.read().split("|")
	   	balance = b_l[0]
	   	loan = b_l[1]
	   	p = b_l[2]
	   	if p == acc_pass:
	   		print("\033[1;35;40mYour current loan is "+loan+"\033[0m")
	   		if int(loan) <= 20:
	   			take_loan = inp_data("\033[1;32;40mHow much money do you take loan? \033[0m")
	   			loan = int(loan)+int(take_loan)
	   			balance = int(balance)+int(take_loan)
	   			n_w = open(a,"w")
	   			n_w.write(str(balance)+"|"+str(loan)+"|"+acc_pass)
	   			n_w.close()
	   		else:
	   			print("\033[1;31;40m[ ! ]You have to complete previous loan\033[0m\n")
	   	else:
	   		print("\033[1;31;40m[ !!! ] Wrong Password\033[0m")
	   		time.sleep(2)
	   	
	except Exception as e:
		print("\033[1;31;40m[ ! ]No accounts Found\033[0m")



#Make a Payment
def payment(acc_num,acc_pass):
	a = "accounts/"+acc_num
	try:
	   with open(a,"r+") as f:
	   	b_l = f.read().split("|")
	   	balance = b_l[0]
	   	loan = b_l[1]
	   	p = b_l[2]
	   	if p == acc_pass:
	   		print("\033[1;35;40mYour current balance is "+balance+"\033[0m")
	   		payment = inp_data("\033[1;32;40mHow much money do you payment? \033[0m")
	   		balance = int(balance)-int(payment)
	   		if balance >=0:
	   			n_w = open(a,"w")
	   			n_w.write(str(balance)+"|"+loan+"|"+acc_pass)
	   			n_w.close()
	   			print("\033[1;32;40m[ * ]Payments Succesful\033[0m\n")
	   		else:
	   			print("\033[1;34;40m[ - ]No Balance\033[0m")
	   	else:
	   		print("\033[1;31;40m[ !!! ] Wrong Passwoord\033[0m")
	except Exception as e:
		print("\033[1;31;40m[ ! ]No accounts Found\033[0m")


#Withdrawal Money
def withdraw_balance(acc_num,acc_pass):
	a = "accounts/"+acc_num
	try:
	   with open(a,"r+") as f:
	   	b_l = f.read().split("|")
	   	balance = b_l[0]
	   	loan = b_l[1]
	   	p = b_l[2]
	   	if p==acc_pass:
	   		print("\033[1;35;40mYour current balance is "+balance+"\033[0m")
	   		with_draw = inp_data("\033[1;32;40mHow much money you want to withdraw:  \033[0m")
	   		balance = int(balance)-int(with_draw)
	   		if balance >=0:
	   			w_f = open(a,"w")
	   			w_f.write(str(balance)+"|"+loan+"|"+acc_pass)
	   			w_f.close()
	   			print("\033[1;32;40m [ * ]Successfully Withdrawal\033[0m\n")
	   		else:
	   			print("\033[1;34;40m[ - ]No Balance\033[0m")
	   	else:
	   		print("\033[1;31;40m[ !!! ] Wrong Passwoord\033[0m")	   	
	except :
		print("\033[1;31;40m[ ! ]No accounts Found\033[0m")


#A Back Fucntion
def back():
	i = input("\n\033[1;36;40mEnter 0 to go to Menu Or Enter e or E to Exit    :\033[0m")
	if i =="e" or i =="E":
		print("\033[1;37;40m[ ~ ]Thanks for using\033[0m")
		exit()
	elif i=="0":
		options()
	else:
		back()


#Options
def options():
	print("\n\033[1;36;40m------------------\033[0m\033[1;37;40mBANK MANEGMENT SYSTEM\033[0m\033[1;36;40m-----------------\033[0m\n")
	print("\t\033[1;31;40m==============MENU=============\033[0m\n")
	print("\t\033[1;33;40m________1.Create Account________\n")
	print("\t_________2.Check Balance________\n")
	print("\t____________3.Payment___________\n")
	print("\t___________4.Take Loan__________\n")
	print("\t___________5. Add Money_________\n")
	print("\t_______6. Withdrawal Money______\033[0m\n")
	o = inp_data("\033[1;32;40mSelect Option: \033[0m")
	if o == str(1):
		time.sleep(1)
		set_acc()
		time.sleep(1)
		back()
	elif o==str(2):
		acc_num = inp_data("\033[1;31;40mYour Account Number : \033[0m")
		acc_pass = inp_data("\033[1;31;40mYour Account Password : \033[0m")
		check_balance(acc_num,acc_pass)
		time.sleep(1)
		back()
	elif o==str(3):
		acc_num = inp_data("\033[1;31;40mYour Account Number : \033[0m")
		acc_pass = inp_data("\033[1;31;40mYour Account Password : \033[0m")
		payment(acc_num,acc_pass)
		time.sleep(1)
		back()
	elif o==str(4):
		acc_num = inp_data("\033[1;31;40mYour Account Number : \033[0m")
		acc_pass= inp_data("\033[1;31;40mYour Account Password : \033[0m")
		take_loan(acc_num,acc_pass)
		time.sleep(1)
		back()
	elif o==str(5):
		acc_num = inp_data("\033[1;31;40mYour Account Number : \033[0m")
		acc_pass=inp_data("\033[1;31;40mYour Account Password:\033[0m")
		add_balance(acc_num,acc_pass)
		time.sleep(1)
		back()
	elif o==str(6):
		acc_num = inp_data("\033[1;31;40mYour Account Number : \033[0m")
		acc_pass=inp_data("\033[1;31;40mYour Account Password:\033[0m")
		withdraw_balance(acc_num,acc_pass)
		time.sleep(1)
		back()
		
	else:
		print("You need to Enter Currect Input")
		time.sleep(1)
		options()


#Main Function
if __name__=="__main__":
	os.system("clear")
	try:
		os.mkdir("accounts")
		with open("accounts/account.txt","w+")as n:
			n.write("Name|1")
			n.write("\n")
	except FileExistsError:
		pass
	options()
