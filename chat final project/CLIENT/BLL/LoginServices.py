#LOGIN SERVICES
import sys
sys.path.append('..')
from DL.DBconnection import DBconnection
class loginServices():
	@staticmethod
	def login(usrname,passwd):
		db=DBconnection.connect()
		cursor=db.cursor()
		query='select * from usermaster'
		cursor.execute(query)
		for row in cursor:
			if row[1]==usrname and row[2]==passwd:
				return row[0],row[1]
		return -1,'0'
	@staticmethod	
	def forgotPassword():
		pass
	@staticmethod
	def changePassword(usr,old,new):
		db=DBconnection.connect()
		cursor=db.cursor()
		query='select password from usermaster where username=%s'
		cursor.execute(query,(usr,))
		cur=cursor.fetchall()
		for row in cur:
			if row[0]==old:
				qry='update usermaster set password=%s where username=%s'
				cursor.execute(qry,(new,usr))
				db.commit()
				cursor.close()
				return True
		return False
				
	@staticmethod
	def logout(uid):
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		q="update usermaster set online='inactive' where userid=%s"
		cur.execute(q,(uid,))
		cnx.commit()
		cur.close()
		cnx.close()