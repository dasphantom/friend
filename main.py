import _mysql
import credentials

db=_mysql.connect("localhost",credentials.login['username'],credentials.login['password'], "friend")




