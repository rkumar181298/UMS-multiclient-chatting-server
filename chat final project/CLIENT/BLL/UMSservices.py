#UMS SERVICES
import sys
sys.path.append('..')
from DL.DBconnection import DBconnection
from DL.User import user
class UMSservices:
	@staticmethod
	def add(user):
		try:
			db=DBconnection.connect()
			cursor=db.cursor()
			query='insert into usermaster(username,password,usertype,userstatus,name,email,contact,address,gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
			values=[]
			values.append(user.getUsername())
			values.append(user.getPassword())
			values.append(user.getUsertype())
			values.append(user.getUserstatus())
			values.append(user.getName())
			values.append(user.getEmail())
			values.append(user.getContact())
			values.append(user.getAddress())
			values.append(user.getGender())
			cursor.execute(query,values)
			if(cursor.rowcount==1):
				db.commit()
				cursor.close()
				return True
		except:
			cursor.close()
			db.commit()
			return False
	@staticmethod
	def view():
		list=[]
		db=DBconnection.connect()
		cursor=db.cursor()
		query='select * from usermaster'
		cursor.execute(query)
		cur=cursor.fetchall()
		for row in cur:
			usr=user()
			usr.setUserid(int(row[0]))
			usr.setUsername(row[1])
			usr.setPassword(row[2])
			usr.setUsertype(row[3])
			usr.setUserstatus(bool(row[4]))
			usr.setName(row[5])
			usr.setEmail(row[6])
			usr.setContact(row[7])
			usr.setAddress(row[8])
			usr.setGender(bool(row[9]))
			list.append(usr)
		cursor.close()
		db.close()
		return list
		
	@staticmethod
	def searchbyid(id):
		db=DBconnection.connect()
		cursor=db.cursor()
		q='select * from usermaster where userid=%s'
		data=[]
		data.append(id)
		cursor.execute(q,data)
		cur=cursor.fetchall()
		if (cursor.rowcount==1):
			for row in cur:
				usr=user()
				usr.setUserid(int(row[0]))
				usr.setUsername(row[1])
				usr.setPassword(row[2])
				usr.setUsertype(row[3])
				usr.setUserstatus(bool(row[4]))
				usr.setName(row[5])
				usr.setEmail(row[6])
				usr.setContact(row[7])
				usr.setAddress(row[8])
				usr.setGender(bool(row[9]))
			cursor.close()
			db.close()
			return usr
		else:
			cursor.close()
			db.close()
			return None
			
	@staticmethod
	def update(user):		
		db=DBconnection.connect()
		cursor=db.cursor()
		query='update usermaster set usertype=%s,userstatus=%s,name=%s,email=%s,contact=%s,address=%s,gender=%s where userid=%s'
		values=[]
		values.append(user.getUsertype())
		values.append(user.getUserstatus())
		values.append(user.getName())
		values.append(user.getEmail())
		values.append(user.getContact())
		values.append(user.getAddress())
		values.append(user.getGender())
		values.append(user.getUserid())
		cursor.execute(query,values)
		if(cursor.rowcount==1):
			db.commit()
			cursor.close()
			return True
		else:
			db.commit()
			cursor.close()
			return False

	@staticmethod
	def updateprofile(user):		
		db=DBconnection.connect()
		cursor=db.cursor()
		query='update usermaster set name=%s,email=%s,contact=%s,address=%s,gender=%s where userid=%s'
		values=[]
		values.append(user.getName())
		values.append(user.getEmail())
		values.append(user.getContact())
		values.append(user.getAddress())
		values.append(user.getGender())
		values.append(user.getUserid())
		cursor.execute(query,values)
		if(cursor.rowcount==1):
			db.commit()
			cursor.close()
			return True
		else:
			db.commit()
			cursor.close()
			return False
	
	@staticmethod
	def online_user():
		list=[]
		db=DBconnection.connect()
		cursor=db.cursor()
		query='select username from usermaster where online=%s'
		list.append('active')
		cursor.execute(query,list)
		cur=cursor.fetchall()
		cursor.close()
		db.close()
		return cur			
		
	@staticmethod
	def Active(user):
		db=DBconnection.connect()
		cursor=db.cursor()
		values=[]
		query='update usermaster set online=%s where username=%s'
		values.append('active')
		values.append(user)
		cursor.execute(query,values)
		cursor.close()
		db.commit()
		
	@staticmethod
	def InActive(user):
		db=DBconnection.connect()
		cursor=db.cursor()
		values=[]
		query='update usermaster set online=%s where username=%s'
		values.append('inactive')
		values.append(user)
		cursor.execute(query,values)
		cursor.close()
		db.commit()
		
		
	@staticmethod
	def GetPortno():
		db=DBconnection.connect()
		cursor=db.cursor()
		query='select * from portno'
		cursor.execute(query)
		for i in cursor:
			prt=int(i[0])
			break
		cursor.close()
		db.close()
		return prt