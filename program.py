import Tkinter as tk
from Tkinter import *
import datetime
from sql_connect import *
from password import *

LARGE_FONT = ("Verdana", 12)

#create the GUI window of the application
class first(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		first_page = tk.Frame(self)
		first_page.pack(side="top", fill="both", expand=True)
		first_page.grid_rowconfigure(0, weight=1)
		first_page.grid_columnconfigure(0, weight=1)
		self.frames = {}
		#let the frame can be choose from it
		for F in (login, instruction_page, Email_practice_page, Shopping_practice_page, Banking_practice_page, prepare_page, real_email_page, real_shopping_page, real_banking_page, end_page):
			frame = F(first_page, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame(login)
	#function to move to next frame
	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

#login page for the tester to enter their username, and it will be collect into the database
class login(tk.Frame):
	#helper function to input username into the database, and then switch to the next page.
	def get_username(self):
		username_info = self.username_entry.get()
		insert_username(username_info)
		self.controller.SomeVar = username_info
		#send the username to the next frame as a variable
		self.controller.frames[instruction_page].name_label()

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller = controller
		tk.Label(self, text="Please enter your username", pady=10, padx=10, font=LARGE_FONT).pack()
		#get the username from the user's input
		username_label = Label(self, text="Username")
		username_label.pack()
		self.username_entry = Entry(self)
		self.username_entry.pack()
		#button to go to next page	
		next = tk.Button(self, text="Enter", fg="white", bg="#263D42", command=lambda:[self.get_username(), controller.show_frame(instruction_page)]).pack()
		
		
#Testing Email password
class instruction_page(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		#label to give enough instruction for the user.
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		tk.Label(self, text="Before the practice,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="In the following pages, you need to remember the face which will be shown on the left side,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Press CHECK button to check if you entered the right password.", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Press Back button to go to the last page.", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Press CONTINUE button to go to the next page.", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Press submit button on right side to coloured the face.", pady=5, padx=10, font=LARGE_FONT).pack()
		
		tk.Label(self, text="To contnue, press the NEXT PAGE button below", pady=5, padx=10, font=LARGE_FONT).pack()

		#Back button to return to the three_mode page, and continue button to go the login page.
		Next = tk.Button(self, text="NEXT PAGE", fg="white", bg="#263D42", command=lambda: controller.show_frame(Email_practice_page)).pack(side=BOTTOM)
		
	def name_label(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[Email_practice_page].name_label2()
		
#Pracetice page for the Email password
class Email_practice_page(tk.Frame):
	def name_label2(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[Shopping_practice_page].name_label3()
	
	#get colours from the input and changes the colour of the clown face
	def colouring(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(basic, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	#get the username
	def get(self):
		x = self.name["text"]
		return x
	#record the assigned password into database
	def get_name(self, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh, p):
		array = ['', '', '', '', '', '', '', '', '', '', '', '']
		array[0] = h
		array[1] = f
		array[2] = n
		array[3] = lc
		array[4] = rc
		array[5] = m
		array[6] = le
		array[7] = re
		array[8] = lew
		array[9] = rew
		array[10] = ha
		array[11] = coh
		str = ""
		for i in array:
			str += i + " "
		user = self.get()
		insert_password(user, str, p)
	
	#compare the input password and the assigned password
	def check(self, lst, p):
		user = self.get()
		str = ""
		for i in lst:
			str+= i + " "
		assigned_array = get_password(user, p)
		str2 = ""
		for j in assigned_array:
			str2+= j + " " 
		if str == str2:
			window = tk.Tk()
			tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
		else:
			window2 = tk.Tk()
			tk.Label(window2, text="Wrong password, try again.").pack(side=TOP)
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		global left, right, selection, basic, assigned
		self.page = tk.Label(self, text="Email_practice_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		#username
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		self.label = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.label.pack()
		canvas = Canvas(self, height=370, width=1000, bg="#263D42")
		canvas.pack()
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		left = Frame(canvas, bg="white")
		right = Frame(canvas, bg="white")
		selection = Frame(canvas, bg ="white")
		left.place(x=10, y=10, height=330, width=300, anchor='nw')
		right.place(x=320, y=10, height=330, width=300, anchor='nw')
		selection.place(x=630, y=10, height=330, width=350, anchor='nw')
		Label(left, text="Here is your assigned password", font=("Times", "8")).pack(side=TOP)
		Label(right, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(selection, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the assigned password on left frame
		hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat = random_colour()
		assigned = clown_face(left, hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat)
		assigned.pack()

		#show the basic password you have on right frame
		basic = clown_face(right, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		basic.pack()
		
		#option menu
		list = dropbox(selection)
		Submit = tk.Button(selection, text="Submit", command=lambda:self.colouring(list)).pack(side=RIGHT)
		
		#Back button to return to the instruction_page, and continue button to go the next page.
		Back = tk.Button(self, text="Back", fg="white", bg="#263D42", command=lambda: controller.show_frame(instruction_page)).pack(side=LEFT, expand=YES)
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "email_password"), self.check(list, "email_password")]).pack(side=LEFT, expand=YES)
		Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "email_password"), controller.show_frame(Shopping_practice_page)]).pack(side=LEFT, expand=YES)
	

#Pracetice page for the Shopping password
class Shopping_practice_page(tk.Frame):
	def name_label3(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[Banking_practice_page].name_label4()
		
	def colouring2(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(basic_2, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	def get(self):
		x = self.name["text"]
		return x
		
	def get_name(self, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh, p):
		array = ['', '', '', '', '', '', '', '', '', '', '', '']
		array[0] = h
		array[1] = f
		array[2] = n
		array[3] = lc
		array[4] = rc
		array[5] = m
		array[6] = le
		array[7] = re
		array[8] = lew
		array[9] = rew
		array[10] = ha
		array[11] = coh
		str = ""
		for i in array:
			str += i + " "
		user = self.get()
		insert_password(user, str, p)
	
	def check(self, lst, p):
		user = self.get()
		str = ""
		for i in lst:
			str+= i + " "
		assigned_array = get_password(user, p)
		str2 = ""
		for j in assigned_array:
			str2+= j + " " 
		if str == str2:
			window = tk.Tk()
			tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
		else:
			window2 = tk.Tk()
			tk.Label(window2, text="Wrong password, try again.").pack(side=TOP)
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.page = tk.Label(self, text="Shopping_practice_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		canvas = Canvas(self, height=370, width=1000, bg="#263D42")
		canvas.pack()
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		global left_2, right_2, selection_2, basic_2, assigned_2
		left_2 = Frame(canvas, bg="white")
		right_2 = Frame(canvas, bg="white")
		selection_2 = Frame(canvas, bg ="white")
		left_2.place(x=10, y=10, height=330, width=300, anchor='nw')
		right_2.place(x=320, y=10, height=330, width=300, anchor='nw')
		selection_2.place(x=630, y=10, height=330, width=350, anchor='nw')
		Label(left_2, text="Here is your assigned password", font=("Times", "8")).pack(side=TOP)
		Label(right_2, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(selection_2, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the assigned password on left frame
		hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat = random_colour()
		assigned_2 = clown_face(left_2, hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat)
		assigned_2.pack()
		
		#show the basic password you have on right frame
		basic_2 = clown_face(right_2, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		basic_2.pack()
		
		#option menu
		list = dropbox(selection_2)
		Submit = tk.Button(selection_2, text="Submit", command=lambda: self.colouring2(list)).pack(side=RIGHT)
		
		#Back button to return to the instruction_page, and continue button to go the next page.
		Back = tk.Button(self, text="Back", fg="white", bg="#263D42", command=lambda: controller.show_frame(Email_practice_page)).pack(side=LEFT, expand=YES)
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "shopping_password"), self.check(list, "shopping_password")]).pack(side=LEFT, expand=YES)
		Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "shopping_password"), controller.show_frame(Banking_practice_page)]).pack(side=LEFT, expand=YES)
		
	
#Pracetice page for the Shopping password
class Banking_practice_page(tk.Frame):
	def name_label4(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[prepare_page].name_label5()
		
	def colouring3(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(basic_3, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	def get(self):
		x = self.name["text"]
		return x
		
	def get_name(self, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh, p):
		array = ['', '', '', '', '', '', '', '', '', '', '', '']
		array[0] = h
		array[1] = f
		array[2] = n
		array[3] = lc
		array[4] = rc
		array[5] = m
		array[6] = le
		array[7] = re
		array[8] = lew
		array[9] = rew
		array[10] = ha
		array[11] = coh
		str = ""
		for i in array:
			str += i + " "
		user = self.get()
		insert_password(user, str, p)
	
	def check(self, lst, p):
		user = self.get()
		str = ""
		for i in lst:
			str+= i + " "
		assigned_array = get_password(user, p)
		str2 = ""
		for j in assigned_array:
			str2+= j + " " 
		if str == str2:
			window = tk.Tk()
			tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
		else:
			window2 = tk.Tk()
			tk.Label(window2, text="Wrong password, try again.").pack(side=TOP)
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.page = tk.Label(self, text="Banking_practice_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		canvas = Canvas(self, height=370, width=1000, bg="#263D42")
		canvas.pack()
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		global left_3, right_3, selection_3, basic_3, assigned_3
		left_3 = Frame(canvas, bg="white")
		right_3 = Frame(canvas, bg="white")
		selection_3 = Frame(canvas, bg ="white")
		left_3.place(x=10, y=10, height=330, width=300, anchor='nw')
		right_3.place(x=320, y=10, height=330, width=300, anchor='nw')
		selection_3.place(x=630, y=10, height=330, width=350, anchor='nw')
		Label(left_3, text="Here is your assigned password", font=("Times", "8")).pack(side=TOP)
		Label(right_3, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(selection_3, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the assigned password on left frame
		hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat = random_colour()
		assigned_3 = clown_face(left_3, hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat)
		assigned_3.pack()
		
		#show the basic password you have on right frame
		basic_3 = clown_face(right_3, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		basic_3.pack()
		
		#option menu
		list = dropbox(selection_3)
		Submit = tk.Button(selection_3, text="Submit", command=lambda: self.colouring3(list)).pack(side=RIGHT)
		
		#Back button to return to the instruction_page, and continue button to go the next page.
		Back = tk.Button(self, text="Back", fg="white", bg="#263D42", command=lambda: controller.show_frame(Shopping_practice_page)).pack(side=LEFT, expand=YES)
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "banking_password"), self.check(list, "banking_password")]).pack(side=LEFT, expand=YES)
		Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_name(hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat, "banking_password"), controller.show_frame(prepare_page)]).pack(side=LEFT, expand=YES)

class prepare_page(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		#label to give enough instruction for the user.
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		tk.Label(self, text="Before the real test,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="make sure you are ready,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="once you press continue,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="you can not go back to check your assigned password.", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Good luck!!!!!", pady=5, padx=10, font=LARGE_FONT).pack()

		#Back button to return to the password practice page, and continue button to go the login page.
		Next = tk.Button(self, text="NEXT PAGE", fg="white", bg="#263D42", command=lambda: controller.show_frame(real_email_page)).pack(side=BOTTOM)
		Back = tk.Button(self, text="Back", fg="white", bg="#263D42", command=lambda: controller.show_frame(Banking_practice_page)).pack(side=BOTTOM)
		
	def name_label5(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[real_email_page].name_label6()

#Real testing page for emai;
class real_email_page(tk.Frame):
	def name_label6(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[real_shopping_page].name_label7()
		
	def email_colouring(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(email_basic, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	def get(self):
		x = self.name["text"]
		return x
	
	def get_e(self):
		a = datetime.datetime.now()
		return a
	
	#get the current time and insert it into the database
	def get_time_e(self, t):
		time = datetime.datetime.now()
		user = self.get()
		self.controller.end_time = time
		count_time(user, t, time, "email_password")
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		start_e = self.get_e()
		self.controller = controller
		self.page = tk.Label(self, text="Real_Email_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		self.count = tk.Label(self, text="0", pady=5, padx=10, font=LARGE_FONT)
		canvas = Canvas(self, height=370, width=700, bg="#263D42")
		canvas.pack()
		
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		global email_pass, email_selection, email_basic
		email_pass = Frame(canvas, bg="white")
		email_selection = Frame(canvas, bg ="white")
		email_pass.place(x=10, y=10, height=330, width=300, anchor='nw')
		email_selection.place(x=320, y=10, height=330, width=350, anchor='nw')
		Label(email_pass, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(email_selection, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the basic password you have on right frame
		email_basic = clown_face(email_pass, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		email_basic.pack()
		
		#option menu
		list = dropbox(email_selection)
		Submit = tk.Button(email_selection, text="Submit", command=lambda: self.email_colouring(list)).pack(side=RIGHT)
		#check function
		def check(lst, p):
			user = self.get()
			str = ""
			#entered password
			for i in lst:
				str+= i + " "
			#get the assigned password from the database
			assigned_array = get_password(user, p)
			str2 = ""
			for j in assigned_array:
				str2+= j + " " 
			#compare the two password
			if str == str2:
				window = tk.Tk()
				tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
				Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_time_e(start_e), controller.show_frame(real_shopping_page)]).pack(side=BOTTOM)
			else:
				email_allow = self.count["text"]
				counter = int(email_allow)
				window2 = tk.Tk()
				tk.Label(window2, text="Wrong password").pack(side=TOP)
				if counter == 2:
					self.get_time_e(start_e)
					controller.show_frame(real_shopping_page)
				counter += 1
				count_failure(user, counter, "email_password")
				self.count.config(text=counter)
				
		#Back button to return to the instruction_page, and continue button to go the next page.
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: check(list, "email_password")).pack(side=LEFT, expand=YES)

#Real testing page for shopping;
class real_shopping_page(tk.Frame):
	def name_label7(self):
		self.name.config(text=self.controller.SomeVar)
		self.controller.frames[real_banking_page].name_label8()
		
	def shopping_colouring(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(shopping_basic, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	def get(self):
		x = self.name["text"]
		return x
	
	def get_s(self):
		a = datetime.datetime.now()
		return a
	
	def get_time_s(self):
		t = self.controller.end_time
		time = datetime.datetime.now()
		user = self.get()
		self.controller.end_time = time
		count_time(user, t, time, "shopping_password")
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		start_s = self.get_s()
		self.page = tk.Label(self, text="Real_Shopping_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		self.count = tk.Label(self, text="0", pady=5, padx=10, font=LARGE_FONT)
		canvas = Canvas(self, height=370, width=700, bg="#263D42")
		canvas.pack()
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		global shopping_pass, shopping_selection, shopping_basic
		shopping_pass = Frame(canvas, bg="white")
		shopping_selection = Frame(canvas, bg ="white")
		shopping_pass.place(x=10, y=10, height=330, width=300, anchor='nw')
		shopping_selection.place(x=320, y=10, height=330, width=350, anchor='nw')
		Label(shopping_pass, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(shopping_selection, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the basic password you have on right frame
		shopping_basic = clown_face(shopping_pass, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		shopping_basic.pack()
		
		#option menu
		list = dropbox(shopping_selection)
		Submit = tk.Button(shopping_selection, text="Submit", command=lambda: self.shopping_colouring(list)).pack(side=RIGHT)
		#check function
		def check(lst, p):
			user = self.get()
			str = ""
			for i in lst:
				str+= i + " "
			assigned_array = get_password(user, p)
			str2 = ""
			for j in assigned_array:
				str2+= j + " " 
			if str == str2:
				window = tk.Tk()
				tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
				Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_time_s(), controller.show_frame(real_banking_page)]).pack(side=BOTTOM)
			else:
				email_allow = self.count["text"]
				counter = int(email_allow)
				window2 = tk.Tk()
				tk.Label(window2, text="Wrong password").pack(side=TOP)
				if counter == 2:
					self.get_time_s()
					controller.show_frame(real_banking_page)
				counter += 1
				count_failure(user, counter, "shopping_password")
				self.count.config(text=counter)
		
		
		#Back button to return to the instruction_page, and continue button to go the next page.
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: check(list, "shopping_password")).pack(side=LEFT, expand=YES)

#Real testing page for shopping;
class real_banking_page(tk.Frame):
	def name_label8(self):
		self.name.config(text=self.controller.SomeVar)
		
	def banking_colouring(self, list):
		colors = list
		h = colors[0]
		f = colors[1]
		n = colors[2]
		lc = colors[3]
		rc = colors[4]
		m = colors[5]
		le = colors[6]
		re = colors[7]
		lew = colors[8]
		rew = colors[9]
		ha = colors[10]
		coh = colors[11]
		change_color(banking_basic, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh)
	
	def get(self):
		x = self.name["text"]
		return x
		
	def get_b(self):
		a = datetime.datetime.now()
		return a
		
	def get_time_b(self):
		t = self.controller.end_time
		time = datetime.datetime.now()
		user = self.get()
		self.controller.end_time = time
		count_time(user, t, time, "banking_password")
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		start_b = self.get_b()
		self.page = tk.Label(self, text="Real_Banking_page", pady=5, padx=10, font=LARGE_FONT)
		self.page.pack()
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		self.count = tk.Label(self, text="0", pady=5, padx=10, font=LARGE_FONT)
		canvas = Canvas(self, height=370, width=700, bg="#263D42")
		canvas.pack()
		#building left frame for showing the assigned password, and the right frame to show the entered password, and the selection frame is for the user to enter their password.
		global banking_pass, banking_selection, banking_basic
		banking_pass = Frame(canvas, bg="white")
		banking_selection = Frame(canvas, bg ="white")
		banking_pass.place(x=10, y=10, height=330, width=300, anchor='nw')
		banking_selection.place(x=320, y=10, height=330, width=350, anchor='nw')
		Label(banking_pass, text="Here is the graph you have coloured", font=("Times", "8")).pack(side=TOP)
		Label(banking_selection, text ="Please select the colour for each part, then press submit", font=("Times", "8")).pack(side=TOP)
		
		#show the basic password you have on right frame
		banking_basic = clown_face(banking_pass, "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white")
		banking_basic.pack()
		
		#option menu
		list = dropbox(banking_selection)
		Submit = tk.Button(banking_selection, text="Submit", command=lambda: self.banking_colouring(list)).pack(side=RIGHT)
		#check function
		def check(lst, p):
			user = self.get()
			str = ""
			for i in lst:
				str+= i + " "
			assigned_array = get_password(user, p)
			str2 = ""
			for j in assigned_array:
				str2+= j + " " 
			if str == str2:
				window = tk.Tk()
				tk.Label(window, text="You have entered the correct password.").pack(side=TOP)
				Continue = tk.Button(self, text="Continue", fg="white", bg="#263D42", command=lambda: [self.get_time_b(), controller.show_frame(end_page)]).pack(side=BOTTOM)
			else:
				email_allow = self.count["text"]
				counter = int(email_allow)
				window2 = tk.Tk()
				tk.Label(window2, text="Wrong password").pack(side=TOP)
				if counter == 2:
					self.get_time_b()
					controller.show_frame(end_page)
				counter += 1
				count_failure(user, counter, "banking_password")
				self.count.config(text=counter)

		#Back button to return to the instruction_page, and continue button to go the next page.
		Check = tk.Button(self, text="Check", fg="white", bg="#263D42", command=lambda: check(list, "banking_password")).pack(side=LEFT, expand=YES)

class end_page(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		#label to give enough instruction for the user.
		self.name = tk.Label(self, text="", pady=5, padx=10, font=LARGE_FONT)
		self.name.pack()
		tk.Label(self, text="Thank you for the testing,", pady=5, padx=10, font=LARGE_FONT).pack()
		tk.Label(self, text="Well done!!!!!", pady=5, padx=10, font=LARGE_FONT).pack()
		
def main():
	app = first()
	app.mainloop()
main()
	
	
