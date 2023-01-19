from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import smtplib
from email.mime.text import MIMEText
import random
import datetime


class Registration:

	def __init__(self,root):
		
		self.__opt=None
		self.__conf=0

		self.root=root
		self.root.title("Registration window")
		self.root.geometry("1350x900+0+0")
		#Login().__init__()
        #Configuration

		self.root.config(bg='green')
		#Python bg Image

		self.bg=ImageTk.PhotoImage(file="img//bg.jpg")
		bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
         
		#self.bg=ImageTk.PhotoImage(file="img//bgImage.jpg")
		#bg=Label(self.root,image=self.bg).place(x=0,y=0,width=1350,height=900)
		
         #Left image  ,relwidth=1,relheight=1

		self.left=ImageTk.PhotoImage(file='img//Guessing-Game-Pic-full.jpg')
		left=Label(self.root,image=self.left).place(x=0,y=90,height=720)

		#Registration Frame

		frame1=Frame(self.root,bg='white')
		frame1.place(x=680,y=90,width=700,height=720)

		title=Label(frame1,text='REGISTER HERE',font=("times new roman",20,'bold'),bg='white',fg='#F88017').place(x=50,y=30)

		first_name_label=Label(frame1,text='first_name',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=100)
		self.first_name=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.first_name.place(x=50,y=130,width=200)

		last_name_label=Label(frame1,text='Last name',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=100)
		self.last_name=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.last_name.place(x=370,y=130,width=200)


		address_label=Label(frame1,text='Address',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=170)
		self.address=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.address.place(x=50,y=200,width=200)

		DOB_label=Label(frame1,text='Date of Birth (e.g: 01-12-2000)',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=170)
		self.DOB=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.DOB.place(x=370,y=200,width=200)

		country_label=Label(frame1,text='Country',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=240)
		self.country=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.country.place(x=50,y=270,width=200)

		town_label=Label(frame1,text='Town',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=250)
		self.town=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.town.place(x=370,y=270,width=200)

		profession_label=Label(frame1,text='Profession',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=310)
		self.profession=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.profession.place(x=50,y=340,width=200)

		username_label=Label(frame1,text='Username',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=310)
		self.username=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.username.place(x=370,y=340,width=200)

		password_label=Label(frame1,text='Password',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=380)
		self.password=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black',show='*')
		self.password.place(x=50,y=410,width=200)

		conf_password_label=Label(frame1,text='Confirm your password',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=380)
		self.conf_password=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black',show='*')
		self.conf_password.place(x=370,y=410,width=200)

		email_label=Label(frame1,text='Email (in lower case)',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=50,y=450)
		self.email=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.email.place(x=50,y=480,width=200)

		number_label=Label(frame1,text='Mobile Number',font=("times new roman",12,'bold'),bg='white',fg='black').place(x=370,y=450)
		self.number=Entry(frame1,font=("times new roman",12),bg='#E5E4E2',fg='black')
		self.number.place(x=370,y=480,width=200)

		pin_code_label_label=Label(frame1,text='Enter your pin code',font=('times new roman',12,'bold'),bg='white',fg='black').place(x=370,y=510)
		self.pin_code=Entry(frame1,font=('times new roman',12),bg='#E5E4E2',fg='black',show='*')
		self.pin_code.place(x=370,y=540,width=200)



		gender_label=Label(frame1,text='Gender',font=('times new roman',12,'bold'),bg='white',fg='black').place(x=50,y=510)

		#Create a combobox we import ttk module from tkinter lybrary
		#if you dont want the combobox to be modify we use 'state='readonly''

		#gender=ttk.Combobox(frame1,font=('times new roman',12),state='readonly',justify=CENTER)
		self.gender=ttk.Combobox(frame1,font=('times new roman',12),state='readonly')
		self.gender['value']=('Select','Male','Female','Transgender')
		self.gender.place(x=50,y=540)
		self.gender.current(0)

		#answer_label=Label(frame1,text='answer',font=('times new roman',12,'bold'),bg='white',fg='black').place(x=370,y=510)
		#answer=Entry(frame1,font=('times new roman',12),bg='#E5E4E2',fg='black').place(x=370,y=540,width=200)

		#check condition button (check button)
		self.check=IntVar()
		check=Checkbutton(frame1,text='I agree the terms & condition',font=('times new roman',12),variable=self.check,onvalue=1,offvalue=0,bg='white',bd=0,cursor='hand2').place(x=50,y=580)

		self.button_img=ImageTk.PhotoImage(file='img//button_re.jpeg')
		button=Button(frame1,image=self.button_img,bd=0,cursor='hand2',command=self.Registration_db).place(x=150,y=610)


		#exit button

		self.exit=Button(self.root,text='Exit',font=('times new roman',18,'bold'),bg='red',fg='white',width=10,bd=5,cursor='hand2',command=self.exit)
		self.exit.grid(row=1300,column=700,padx=1210,pady=850)


		#Create a Login button in case you you already have an account

		#Login=Button(self.root,text='Login',font=('times new roman',15),bg='green',fg='white',bd=6,cursor='hand2',command=self.new_window).place(x=210,y=675,width=150,height=60)

	def OtpsBut(self):
			self.otp_button=Entry(self.root,font=("times new roman",12),bg='white',fg='black',show='*')
			self.otp_button.place(x=225,y=800,width=200,height=30)

			self.OTP=Button(self.root,text='Confirm Otp ',font=('times new roman',15),bg='green',fg='white',bd=6,cursor='hand2',command=self.__submit_data).place(x=250,y=850,width=150,height=30)




	def mailcheck(self,email):
		import re
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		if(re.search(regex,email)):
			return 1
		else:
			return 0


	def exit(self):

		self.exits=messagebox.askyesno("Login System",'Confirm if you want to exit??')

		if self.exits>0:
			self.root.destroy()


	def Registration_db(self):

		#Message box is used to display whether an error occurs or not


		import sqlite3

		conn=sqlite3.connect('db//tkinter1.db')

		c=conn.cursor()

		mail=self.email.get()

		c.execute("SELECT * FROM Guessing_db WHERE email=?",[mail])

		info=c.fetchone()

		conn.close()



		special_characters = '"!@#$%^&*().\-+?_=,<>/;'
		

		if self.first_name.get()=='' or self.last_name.get()==''or self.address.get()==''or self.DOB.get()==''or self.country.get()==''or self.town.get()==''or self.profession.get()=='' or self.username.get()=='' or self.password.get()==''or self.conf_password.get()=='' or self.email.get()==''or self.number.get()=='' or self.pin_code.get()=='' or self.gender.get()=='' or self.gender.get()=="Select": 
			messagebox.showerror('error','All the features are required',parent=self.root)

		elif self.password.get() != self.conf_password.get() :

			messagebox.showerror('Error',' Both password are not equal',parent=self.root)
			self.password.delete(0,END)
			self.conf_password.delete(0,END)

		elif any(c in special_characters for c in self.password.get())==False or len(self.password.get())<=8:

			messagebox.showerror('Error',' Your password should contain special_characters and the lenght shouldbe more than 9',parent=self.root)
			self.password.delete(0,END)
			self.conf_password.delete(0,END)

		elif self.mailcheck(self.email.get())==0:

			messagebox.showerror('Error','This email id is incorrect')
			self.email.delete(0,END)


		elif self.check.get()==0:
			messagebox.showerror('Error','Please agree our terms before register')

		#else:

			#messagebox.showinfo("Success",'Gongratualtion your Registration has been processed Successfully')

		elif len(self.pin_code.get())>4 or len(self.pin_code.get())<4 or (self.pin_code.get()).isdigit()!=True:

			messagebox.showerror('Error','Make sure that your pin code is an integer value and equal to 4 digit number')
			self.pin_code.delete(0,END)




		elif info!=None:

			messagebox.showinfo("Existed","This email Id has already an account , please try to login")
			self.message=messagebox.askyesno("Success",'Do you want to login now??')

			if self.message>0:
				self.root.destroy()
				logs()


		else:

			try:

				conf=self.__regis_conf()


				if conf==1:

					messagebox.showinfo("Success",'Please check your email account for your otp confirmation')

					self.OtpsBut()

				else:
					messagebox.showerror("Error",'An error occur try again')
				


			except Exception as es:
				messagebox.showerror("Error","Error due to  {} ".format(str(es)))
				self.email.delete(0,END)




	def __submit_data(self):

		if self.__opt==self.otp_button.get():

			try:


					conn=sqlite3.connect("db//tkinter1.db")
					c=conn.cursor()

					c.execute("INSERT INTO Guessing_db VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.first_name.get(),self.last_name.get(),self.address.get(),
																							self.DOB.get(),self.country.get(),self.town.get(),
																							self.profession.get(),self.username.get(),self.password.get(),
																							int(self.pin_code.get()),self.email.get().lower(),self.number.get(),self.gender.get()
																							))

					c.execute("INSERT INTO Baccount VALUES (?,?,?)",(0,self.username.get(),self.email.get()))
					conn.commit()

					conn.close()

					messagebox.showinfo("Success",'Gongratualtion your Registration has been processed Successfully ')

					self.message=messagebox.askyesno("Success",'Do you want to login now??')

					if self.message>0:
						self.root.destroy()
						logs()

					self.clear()

					#self.OTP.destroy()
					#self.otp_button.destroy()
					


			except Exception as es:

				messagebox.showerror("Error","Error due to  {} ".format(str(es)))

		else:

			messagebox.showerror("Error","Make sure you have submit all your infomation or You have entered a wrong opt try again")



		
	def clear(self):

		self.first_name.delete(0,END)
		self.last_name.delete(0,END)
		self.address.delete(0,END)
		self.DOB.delete(0,END)
		self.country.delete(0,END)
		self.town.delete(0,END)
		self.profession.delete(0,END)
		self.username.delete(0,END)
		self.password.delete(0,END)
		self.pin_code.delete(0,END)
		self.email.delete(0,END)
		self.number.delete(0,END)
		self.gender.delete(0,END) 
		self.conf_password.delete(0,END)
		self.gender.current(0)




	def __regis_conf(self):
		a=list(range(0,10))
		otp=random.choices(a,k=6)
		otps=''
		for i in otp:
			otps+=str(i)


		self.__opt=otps
		body=f"""This is your OTP for your registration confirmation in our guessing Game OTP : {otps}"""
		message=MIMEText(body)

		fromAddr="yateassekeronald@gmail.com"

		toAddr=self.email.get()
		message['From'] =fromAddr
		message['To'] = toAddr
		message["Subject"]=f"Registration confirmation"
		
		server=smtplib.SMTP('smtp.gmail.com',587)

		server.starttls()

		password='yate1999Y,'
		server.login(fromAddr,password)

		server.send_message(message)

		server.quit()
        
		return 1



	def new_window(self):
		self.newwindow=Toplevel()
		self.app=Login(self.newwindow)



class Login:


	global mail
	global get_inf

	def __init__(self,root):
		
		self.root=root
		self.root.title("Login Page")
		self.root.geometry('800x600+0+0')

		self.bgI=ImageTk.PhotoImage(file='img//bg-1.png')
		self.Imgbg=Label(self.root,image=self.bgI).place(x=0,y=0.5)

		self.leftIm=ImageTk.PhotoImage(file='img//Login.jpg')
		self.leftI=Label(self.root,image=self.leftIm,bg='#E5E4E2').place(x=0,y=100,width=300,height=400)

		self.frame=Frame(self.root,bg='white')
		self.frame.place(x=250,y=100,width=600,height=400)

		self.Titles=Label(self.frame,text="Welcom to the Guessing Game  Login Page",font=('times new roman',15),fg='#2B65EC',bg='white',justify=CENTER).place(x=110,y=10)


		self.Title=Label(self.frame,text="Login to start play now!!!",font=('times new roman',25),fg='#EE9A4D',bg='white',justify=CENTER).place(x=120,y=50)

		self.Username_label=Label(self.frame,text='E-mail',font=('times news roman',15,'bold'),bg='white',fg='black',bd=1,relief='ridge').place(x=190,y=130)
		self.Username=Entry(self.frame,font=('times new roman',12),bg='#E5E4E2',fg='black',bd=4,relief='ridge')
		self.Username.place(x=90,y=180,width=300,height=30)

		self.Password_label=Label(self.frame,text='Password',font=('times news roman',15,'bold'),bg='white',fg='black',bd=1,relief='ridge').place(x=170,y=220)
		self.Password=Entry(self.frame,font=('times new roman',12),bg='#E5E4E2',fg='black',show='*',bd=4,relief='ridge')
		self.Password.place(x=90,y=260,width=300,height=30)

		self.LogI=ImageTk.PhotoImage(file='img//log.jpg')
		self.Login_but=Button(self.frame,image=self.LogI,bd=0,cursor='hand2',command=self.__login).place(x=130,y=320,height=80)
		self.__get_inf=None
		self.__Binf=None
		self.__em=self.Username.get()
		self.__otp=None
		self.__Amount=0

	def	__Pinconf(self):

		self.pin_conf=Entry(self.root,font=('times news roman',12),bg='#E5E4E2',fg='black',bd=10,show='*')
		self.pin_conf.place(x=300,y=510,width=200)

		self.cod_but_conf=Button(self.root,text='Enter Pin_code',font=('times news roman',15) ,bg='green',fg='white',command=self.__verification)
		self.cod_but_conf.place(x=312,y=560)


	def __verification(self):

		if self.__Permission()==False:

			messagebox.showerror("Error","Your age does not allow you to play this game , This game is for those people whore have more than 18 year old")


		elif int(self.pin_conf.get())==self.__get_inf[9]: #code pin check
			log_conf=1
								#print('Thank for login , can play your game\n')

			messagebox.showinfo('Success',"You have Successfully login into your account")

			self.root.destroy()

			self.__Game()

		else:
			

			messagebox.showerror('Error',"Pin code incorrect")
			self.pin_conf.delete(0,END)
			
										#entry=int(input(""))


    
	def __login(self):

		global mail
		global log_conf
		log_conf=0

		try :

				
				import sqlite3

				conn=sqlite3.connect('db//tkinter1.db')

				c=conn.cursor()
				cur=conn.cursor()

				mail=self.Username.get()

				password=self.Password.get()

				c.execute("SELECT * FROM Guessing_db WHERE email=?",[mail])
				cur.execute("SELECT * FROM Baccount WHERE email=? ",[mail])

				self.__Binf=cur.fetchone()

				self.__get_inf=c.fetchone()
				#print(self.__get_inf)
				get_inf=self.__get_inf

				if self.Password.get()=='' or self.Username.get()=='':
					messagebox.showerror("Error","Email or password should not be blank")

				elif self.__get_inf!=None:

					if (self.__get_inf[8]==password) and (self.__get_inf[10]==mail): #mail and password check

						#self.con
						self.__Pinconf()
						

					else:

						messagebox.showerror("Error","Password or Email is incorrect")
						self.Password.delete(0,END)




				else:
					
					messagebox.showerror('Error',"This email is not register in our DataBase please try to register")
					self.message=messagebox.askyesno("Success",'Do you want to Register??')

					if self.message>0:
						self.root.destroy()
						regists()

					

		except Exception as er:

			messagebox.showerror("Error" ," An error occur dur to ' {} '".format(str(er)))










	def  __Game (self):

		import tkinter
		from tkinter import ttk,messagebox
		from PIL import Image,ImageTk

		

		self.root1=tkinter.Tk()
		self.root1.title('Game interface')
		self.root1.geometry('900x700+0+0')
		self.root1.config(bg='#64E986')

		self.frame1=Frame(self.root1,bg='cadet blue',width=900,height=100,relief='ridge',bd=10)
		self.frame1.place(x=0,y=5)

		self.frame1_label=Label(self.frame1,text=" Welcome to our Guessing Game interface ",fg='white',bg='cadet blue',font=('times new roman',20,'bold'))
		self.frame1_label.place(x=150,y=10,width=550,height=50)



		#self.textinfo=Text(self.root,bg='white',width=36,height=15,relief='ridge',bd=10,font=('times new roman',15,'bold'))
		#self.textinfo.place(x=907,y=150)

		self.frame2=Frame(self.root1,width=700,height=500,relief='ridge',bd=5)
		self.frame2.place(x=100,y=180)

		self.frame2_img=ImageTk.PhotoImage(file='img//bg-1.png')
		frame2_img=Label(self.frame2,image=self.frame2_img).place(x=0,y=0,height=500,width=700)


		self.text=Text(self.frame2,bg='white',width=67,height=10,relief='ridge',bd=10,font=('times new roman',15,'bold'))
		self.text.place(x=0,y=20)

		self.question=('''WELCOM TO THE GUESS GAME!!!!!!!
	here are many options
1-Guess a number between 0-10 ("Your profile will be your bet*10 ")
2-Guess a number between 0-5 ("Your profile will be your bet*5 ")
3-Guess a vowel ("Your profile will be your bet*5 ")
4-Guess consonant ("Your profile will be your bet*10 ")
5-Add Money in your account
6-View detail

					 ''')
		self.text.insert(END,self.question)




		#self.entry=Entry(self.frame2,bg='white',width=15,relief='ridge',bd=10,font=('times new roman',15,'bold'))
		#self.entry.place(x=245,y=310)

		self.sub_img=ImageTk.PhotoImage(file='img//submit.jpg')
		self.Submit=Button(self.frame2,image=self.sub_img,bg='green',relief='ridge',bd=0,font=('times new roman',15,'bold'),command=self.__PlayGame,cursor='hand2')
		self.Submit.place(x=215,y=390)


		self.headerinfo=Label(self.root1,text=f'Name : {self.__get_inf[0] + " " + self.__get_inf[1]}',font=('times new roman',12,'bold'),bg='white').place(x=30,y=130)

		self.headerinfo=Label(self.root1,text=f'Username : {self.__get_inf[7]}',font=('times new roman',14,'bold'),bg='white').place(x=400,y=130)

		self.headerinfo=Label(self.root1,text='Balance: ',font=('times new roman',12,'bold'),bg='white').place(x=700,y=131)
		self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
		#self.headerinfo_=Entry(self.root1,font=('times new roman',12,'bold'),bg='white',fg='green')
		#self.headerinfo_.place(x=770,y=131,width=90)
		#self.headerinfo_.insert(0,self.__Binf[0])
        

        # Game set frame
		self.style = ttk.Style()
		self.choice=ttk.Combobox(self.frame2,font=('times new roman',14),state='readonly',width=7)
		self.choice['value']=('Choice',1,2,3,4,5,6)
		self.style.map('TCombobox', selectbackground=[('readonly', 'black')])
		self.choice.place(x=111,y=310)
		self.choice.current(0)

		self.Choice=Label(self.frame2,text='Bet Choice : ',font=('times new roman',14,'bold'),bg='white').place(x=5,y=310)


		self.Bet_amount=Label(self.frame2,text='Bet_amount ',font=('times new roman',14,'bold'),bg='white').place(x=230,y=310)
		self.Bet_amount_=Entry(self.frame2,font=('times new roman',14,'bold'),bg='white',fg='green',bd=1)
		self.Bet_amount_.place(x=335,y=310,width=70)

		self.Guess_v=Label(self.frame2,text='Guess_value',font=('times new roman',14,'bold'),bg='white').place(x=450,y=310)
		self.Guess_v_=Entry(self.frame2,font=('times new roman',14,'bold'),bg='white',fg='green',bd=1)
		self.Guess_v_.place(x=557,y=310,width=70)



	def reset_butt(self):

		self.reset=Button(self.root1,text='Reset',font=('times new roman',20,'bold'),bg='red',cursor='hand2',bd=6,command=self.__reset_data)
		self.reset.place(x=630,y=580,width=100)

	
	def __reset_data(self):
		self.reset.destroy()
		self.text.delete('1.0',END)
		self.text.insert(END,self.question)
		self.reset.destroy()
		self.MoneyAdd.destroy()
		self.MoneyAdd_B.destroy()
		self.conf_opt_B.destroy()
		self.conf_opt.destroy()




	def getDetail(self):

		return('Personal Details\nFull_Name : {}\nAddress : {}\nDOB : {}\nCountry : {}\nTown : {}\nProfession : {}\nE-mail : {}\nMobile Phone : {}\nGender : {}'.format(self.__get_inf[0] + ' ' + (self.__get_inf[1]),
																																				self.__get_inf[2],self.__get_inf[3],
																																				self.__get_inf[4],self.__get_inf[5],
																																				self.__get_inf[6],self.__get_inf[10],self.__get_inf[11],self.__get_inf[-1]))



	def __Guess_10(self):

		a=list(range(0,11))
		return random.choice(a) 

	def __Guess_5(self):
		a=list(range(0,6))
		return random.choice(a)     

	def __Guess_vowel(self):
		vowel='aieuo'
		guess=random.choice(vowel)
		return str(guess)
	def __Guess_consonant(self):
		consonant='qwrtpsdfghjklmnbvcxyz'
		guess=random.choices(consonant,k=3)
		return guess 
 
	def __Permission(self):
		try:
			year=datetime.datetime.now()
			age=int(year.strftime("%Y"))-int(self.__get_inf[3][6:])
			if age>18:
				return True
			else:
				return False

		except Exception as er:

			messagebox.showerror('Error',f'This error occur due to {str(er)}')



    
	def __Update_Bal_win(self,prof):
		
		conn=sqlite3.connect('db//tkinter1.db')
		cur = conn.cursor()
		email = self.__get_inf[10]
		cur.execute(""" UPDATE Baccount SET balance = balance + ?  WHERE email= ?
			""",(prof,email))
		conn.commit()
        
	def __Update_Bal_los(self,bet):
		
		conn=sqlite3.connect('db//tkinter1.db')
		cur=conn.cursor()
		email=self.__get_inf[10]
		cur.execute(" UPDATE Baccount SET balance = balance - ?  WHERE email= ?"
			,(bet,email))
		conn.commit()
        
    
	def getBalance(self):
		
		email=self.__get_inf[10]
		conn=sqlite3.connect('db//tkinter1.db')
		cur=conn.cursor()
		cur.execute("SELECT * FROM Baccount WHERE email=? ",[email])
		info=cur.fetchone()
		return info[0]

	
	def __addmoney(self,money) :

		conn=sqlite3.connect('db//tkinter1.db')
		cur=conn.cursor()
		email=self.__get_inf[10]
		cur.execute(""" UPDATE Baccount SET balance = balance + ?  WHERE email= ?
			""",(money,email))
		conn.commit()

	def __data_conf(self,money):
		a=list(range(0,10))
		otp=random.choices(a,k=6)
		otps=''
		for i in otp:
			otps+=str(i)


		self.__otp=otps
		user=self.__get_inf[10]
		body=f"""The user {user} want to add {money} in his account this is it otp confirmation {otps}"""
		message=MIMEText(body)

		fromAddr="yateassekeronald@gmail.com"

		toAddr='yateronald@gmail.com'
		message['From'] =fromAddr
		message['To'] = toAddr
		message["Subject"]=f"Registration confirmation"
		
		server=smtplib.SMTP('smtp.gmail.com',587)

		server.starttls()

		password='yate1999Y,'
		server.login(fromAddr,password)

		server.send_message(message)

		server.quit()
        
		return 1




	def __addMonAmont(self):

		self.__Amount=self.MoneyAdd.get()
		self.__data_conf(self.__Amount)
		messagebox.showinfo('Verification',"Please wait the Admistrator will contact to give you the otp ")

		self.MoneyAdd.destroy()
		self.MoneyAdd_B.destroy()

		self.reset_butt()

		self.conf_opt=Entry(self.frame2,font=('times new roman',14,'bold'),bg='white',fg='green',bd=1,show='*')
		self.conf_opt.place(x=70,y=390,width=90)

		self.conf_opt_B=Button(self.frame2,text='Confirm otp',bg='green',relief='ridge',bd=0,font=('times new roman',15,'bold'),command=self.__Validation,cursor='hand2')
		self.conf_opt_B.place(x=50,y=430)


	def __Validation(self):
		try:

			if int(self.__otp)==(int(self.conf_opt.get())):

				self.__addmoney(int(self.__Amount))
				messagebox.showinfo('Congratulation',"Your money has been added Successfully ")

				
				self.conf_opt.destroy()
				self.conf_opt_B.destroy()
				self.headerinfoB=Label(self.root1,text=f' {self.getBalance()}',font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
				

			else:
				messagebox.showerror('error','Otp incorect')



		except Exception as er:

			messagebox.showerror('error',f'error du to {str(er)}')



	def __PlayGame(self):

		Vowel='aieuo'
		special_characters = '"!@#$%^&*().\-+?_=,<>;/'

		try:

			if int(self.choice.get())==1:

				if self.Bet_amount_.get()=='' or self.Guess_v_.get()=='':

					messagebox.showerror('error','Bet Amount and Guess value should not be blank')
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Bet_amount_.get().isdigit()==False:

					messagebox.showerror('error',"The Amount should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Guess_v_.get().isdigit()==False:

					messagebox.showerror('error',"The guessing should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif int(self.Guess_v_.get())>=11:

					messagebox.showerror('error',"The guessing should be a number between 0-10 ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.getBalance()<float(self.Bet_amount_.get()):

					messagebox.showerror('error',"You don't have enough credit in you account please recharge your account ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				else:

					real_num=self.__Guess_10()

					bet=float(self.Bet_amount_.get())
					print(real_num)

					if real_num==int(self.Guess_v_.get()):

						messagebox.showinfo('Congratulation',"Congratulation you have won!!!!!!!!!! ")

						self.__Update_Bal_win((bet*10))
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)

					else:

						messagebox.showerror('Lost','Sorry!!! you have lost ,Please try again')
						messagebox.showerror('Lost','the guess number was : {}'.format(real_num))
						self.__Update_Bal_los(bet)
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)


			elif int(self.choice.get())==2:

				if self.Bet_amount_.get()=='' or self.Guess_v_.get()=='':

					messagebox.showerror('error','Bet Amount and Guess value should not be blank')
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Bet_amount_.get().isdigit()==False:

					messagebox.showerror('error',"The Amount should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Guess_v_.get().isdigit()==False:

					messagebox.showerror('error',"The guessing should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif int(self.Guess_v_.get())>=6:

					messagebox.showerror('error',"The guessing should be a number between 0-5 ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.getBalance()<float(self.Bet_amount_.get()):

					messagebox.showerror('error',"You don't have enough credit in you account please recharge your account ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				else:

					real_num=int(self.__Guess_5())
					bet=float(self.Bet_amount_.get())
					print(real_num)

					if real_num==int(self.Guess_v_.get()):

						messagebox.showinfo('Congratulation',"Congratulation you have won!!!!!!!!!! ")
						#self.__Update_Bal_los(bet)
						self.__Update_Bal_win((bet*5))
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)

					else:

						messagebox.showerror('Lost','Sorry!!! you have lost ,Please try again')
						messagebox.showerror('Lost','the guess number was : {}'.format(real_num))
						self.__Update_Bal_los(bet)
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)


			elif int(self.choice.get())==3:

				Vowel='aieuo'
				

				if self.Bet_amount_.get()=='' or self.Guess_v_.get()=='':

					messagebox.showerror('error','Bet Amount and Guess value should not be blank')
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Bet_amount_.get().isdigit()==False:

					messagebox.showerror('error',"The Amount should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.getBalance()<float(self.Bet_amount_.get()):

					messagebox.showerror('error',"You don't have enough credit in you account please recharge your account ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)


				elif len(self.Guess_v_.get())>=2 :

					messagebox.showerror('error'," You have to choose a single vowel ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)


				elif any(c in self.Guess_v_.get() for c in Vowel)==False or self.Guess_v_.get().isdigit()==True:

					messagebox.showerror('error'," You have to choose only a vowel")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif any(c in self.Guess_v_.get() for c in special_characters)==True:

					messagebox.showerror('error'," You have to choose only a Vowel")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)




				else:

					real_num=self.__Guess_vowel()
					bet=float(self.Bet_amount_.get())	
					print(real_num)			

					if (real_num==self.Guess_v_.get().lower())==True:

						messagebox.showinfo('Congratulation',"Congratulation you have won!!!!!!!!!! ")
						#self.__Update_Bal_los(bet)
						self.__Update_Bal_win((bet*5))
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)

					else:

						messagebox.showerror('Lost','Sorry!!! you have lost ,Please try again')
						messagebox.showerror('Lost','the guess number was : {}'.format(real_num))
						self.__Update_Bal_los(bet)
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)


			elif int(self.choice.get())==4:

				if self.Bet_amount_.get()=='' or self.Guess_v_.get()=='':

					messagebox.showerror('error','Bet Amount and Guess value should not be blank')
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif self.Bet_amount_.get().isdigit()==False:

					messagebox.showerror('error',"The Amount should be a number ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)


				elif self.getBalance()<float(self.Bet_amount_.get()):

					messagebox.showerror('error',"You don't have enough credit in you account please recharge your account ")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)


				elif len(self.Guess_v_.get())>=2:

					messagebox.showerror('error'," You have to choose a single consonant")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif any(c in self.Guess_v_.get() for c in Vowel)==True or self.Guess_v_.get().isdigit()==True:

					messagebox.showerror('error'," You have to choose only a Consonant")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)

				elif any(c in self.Guess_v_.get() for c in special_characters)==True:

					messagebox.showerror('error'," You have to choose only a Consonat")
					self.choice.current(0)
					self.Bet_amount_.delete(0,END)
					self.Guess_v_.delete(0,END)


				else:

					real_num=self.__Guess_consonant()
					bet=float(self.Bet_amount_.get())
					print(real_num)

					if (self.Guess_v_.get().lower() in real_num)==True:

						messagebox.showinfo('Congratulation',"Congratulation you have won!!!!!!!!!! ")
						messagebox.showinfo('info','All the possible consonant was  : {}'.format(real_num))
						#self.__Update_Bal_los(bet)
						self.__Update_Bal_win((bet*10))
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)

					else:

						messagebox.showerror('Lost','Sorry!!! you have lost ,Please try again')
						messagebox.showerror('Lost','the guess number was : {}'.format((real_num)))
						#messagebox.showerror('Lost','the guess number was : {}'.format(self.Guess_v_.get()))
						self.__Update_Bal_los(bet)
						self.headerinfoB=Label(self.root1,text=' {:.2f}'.format(self.getBalance()),font=('times new roman',12,'bold'),bg='white',fg='green').place(x=760,y=131,width=70)
						self.choice.current(0)
						self.Bet_amount_.delete(0,END)
						self.Guess_v_.delete(0,END)





			elif int(self.choice.get())==5:

				self.reset_butt()

				self.MoneyAdd=Entry(self.frame2,font=('times new roman',14,'bold'),bg='white',fg='green',bd=1)
				self.MoneyAdd.place(x=70,y=390,width=90)

				self.MoneyAdd_B=Button(self.frame2,text='Add Amount',bg='green',relief='ridge',bd=0,font=('times new roman',15,'bold'),command=self.__addMonAmont,cursor='hand2')
				self.MoneyAdd_B.place(x=50,y=430)


			elif int(self.choice.get())== 6:
				self.text.delete('1.0',END)
				self.text.insert(END,self.getDetail())
				self.reset_butt()



				

		except Exception as er:

			messagebox.showerror('error',f'error du to {str(er)}')

#Main part of the program

def log():
	menu.destroy()
	root=Tk()
	objt=Login(root)
	root.mainloop()		

def regist():
	menu.destroy()
	root=Tk()
	objt=Registration(root)
	root.mainloop()	


def main():
	global menu
	


	menu = Tk()
	menu.title('Guessing Game Menu')
	menu.geometry('800x600+0+0')
	c = Canvas(menu, width=800, height=600, bg='blue')

	c.grid(row=0, column=3)
	# the image
	image = PhotoImage(file="img//main_1_800x600.gif")
	c.create_image(400, 300, image=image)

	c.create_text(400, 100, text="WELCOM TO OUR GUESSING  GAME ", fill="#FF0202",font=("Purisa", 20))

	c.create_text(400, 200, text="Register if you are new on our Guessing game application ", fill="#1600A4",font=("Purisa", 20))
	c.create_text(400, 250, text="OR ", fill="red",font=("Purisa", 25))
	c.create_text(400, 300, text="Login if you have an account", fill="#1600A4",font=("Purisa", 25))


	Login_image=ImageTk.PhotoImage(file='img//log1.jpg')
	Login=Button(menu,image=Login_image,font=('times new roman',12,'bold'),bd=4,bg='#33FF8A',fg='black',cursor='hand2',command=log)
	Login.place(x=559,y=390)

	register_image=ImageTk.PhotoImage(file='img//buttmain_1_230x200.png')
	register=Button(menu,image=register_image,font=('times new roman',12,'bold'),bd=4,fg='black',cursor='hand2',command=regist,width=150,height=100,bg='#FF3333')
	register.place(x=0,y=400,width=230,height=200)

	menu.mainloop()
def logs():
	root=Tk()
	objt=Login(root)
	root.mainloop()		

def regists():
	root=Tk()
	objt=Registration(root)
	root.mainloop()


if __name__ == '__main__':
	main()