#User
class user:
	def __init__(self,id=0,un='',paswd='',name='',em='',cn='',ad=''):
		self.__userid=id
		self.__username=un
		self.__password=paswd
		self.__usertype='admin'
		self.__userstatus=1
		self.__name=name
		self.__email=em
		self.__contact=cn
		self.__address=ad
		self.__gender=1
	
	
	def __str__(self):
		return (str(self.__userid)+' '+self.__username+' '+self.__password+' '+str(self.__usertype)+' '+self.__userstatus+' '+self.__name+' '+self.__email+' '+self.__contact+' '+self.__address+' '+str(self.__gender))
		
		
	def getUserid(self):
		return self.__userid
	def getUsername(self):
		return self.__username
	def getPassword(self):
		return self.__password
	def getUsertype(self):
		return self.__usertype
	def getUserstatus(self):
		return self.__userstatus
	def getName(self):
		return self.__name
	def getEmail(self):
		return self.__email
	def getContact(self):
		return self.__contact
	def getAddress(self):
		return self.__address
	def getGender(self):
		return self.__gender
		
	def setUserid(self,id):
		self.__userid=id
	def setUsername(self,un):
		self.__username=un
	def setPassword(self,pd):
		self.__password=pd
	def setUsertype(self,ut):
		self.__usertype=ut
	def setUserstatus(self,us):
		self.__userstatus=us
	def setName(self,name):
		self.__name=name
	def setEmail(self,em):
		self.__email=em
	def setContact(self,cn):
		self.__contact=cn
	def setAddress(self,ad):
		self.__address=ad
	def setGender(self,g):
		self.__gender=g
		