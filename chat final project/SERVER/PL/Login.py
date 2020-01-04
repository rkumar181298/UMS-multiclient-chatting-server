#LOGIN PL
import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append('..')
from BLL.LoginServices import loginServices
from DL import User,DBconnection
from Mainframe import *



class Login:
	def __init__(self):
		self.root=tk.Tk()
		self.root.geometry('')
		self.root.title('LOGIN')
		tk.Label(self.root,text='AUTHENTICATION').grid(row=0,column=0,padx=20,pady=10)
		tk.Label(self.root,text='USER_NAME').grid(row=2,column=0,padx=20,pady=10)
		tk.Label(self.root,text='PASSWORD ').grid(row=3,column=0,padx=20,pady=10)
		self.user=tk.Entry(self.root)
		self.user.grid(row=2,column=1,padx=20,pady=10)
		self.passwd=tk.Entry(self.root,show='*')
		self.passwd.grid(row=3,column=1,padx=20,pady=10)
		self.clear=tk.Button(self.root,text='CLEAR',width=10,command=self.btn_clear_clicked)
		self.clear.grid(row=4,column=0,padx=20,pady=10)
		self.login=tk.Button(self.root,text='LOGIN',width=10,command=self.btn_login_clicked)
		self.login.grid(row=4,column=1)
		self.root.mainloop()
	def btn_login_clicked(self):
		l,u=loginServices.login(self.user.get(),self.passwd.get())
		if(l!=-1):
			self.root.destroy()
			m=Mainframe(l,u)
		else:
			messagebox.showinfo('Login Error','INVALID USERNAME AND PASSWORD \nTRY AGAIN')
			self.btn_clear_clicked()
	def btn_clear_clicked(self):
		self.user.delete(0,'end')
		self.passwd.delete(0,'end')

if __name__=='__main__':
	l=Login()
