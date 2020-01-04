#dbconnection
import mysql.connector
class DBconnection:
	host='127.0.0.1'
	port=3306
	un='root'
	pd=''
	db='chat'
	
	@staticmethod
	def connect():
		return mysql.connector.connect(host=DBconnection.host,port=DBconnection.port,user=DBconnection.un,passwd=DBconnection.pd,database=DBconnection.db)