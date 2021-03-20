import MySQLdb
def adduser(xuehao,mima):
	db = MySQLdb.connect("127.0.0.1", port=3306,user= "XXXX",passwd= "XXXXX",db="XXXX", charset='utf8' )
	cursor=db.cursor()
	try:
		cursor.execute("INSERT INTO `xsb`(`xuehao`, `mima`) VALUES ("+"\""+str(xuehao)+"\",\""+str(mima)+"\")")
		db.commit()
		db.close()
		return 0
	except:
		db.close()
		return 1
def banuser(xuehao):
        db =  MySQLdb.connect("127.0.0.1", port=3306,user= "XXXX",passwd= "XXXXX",db="XXXX", charset='utf8' )
        cursor=db.cursor()
        cursor.execute("UPDATE `xsb` SET `isdel`=1 WHERE xuehao="+str(xuehao))
        db.commit()
        db.close()
        selectall()
        return 0
def selectall():
	db =  MySQLdb.connect("127.0.0.1", port=3306,user= "XXXX",passwd= "XXXXX",db="XXXX", charset='utf8' )
	cursor=db.cursor()
	cursor.execute("select * from xsb")
	db.commit()
	b=cursor.fetchall()
	db.close()
	#for i in b:
	#	print(i[0],i[1],i[2])

	return b
#adduser(12,2)
banuser(999)
selectall()

