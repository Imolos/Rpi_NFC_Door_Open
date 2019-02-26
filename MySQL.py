#MySQL Library
import MySQLdb
#regular expression Library
import re
#Library to use Commands in python
import subprocess
#”p” for calling "nfc-poll"
p = subprocess.Popen("nfc-poll", stdout=subprocess.PIPE)
result = p.communicate()[0]
#”seaqrchObj”  is for Regular expresion of „p“ 
searchObj = re.search(r'\s..\s\s..\s\s..\s\s..\s\s',result)
#Make searchObj.group() to something easier to write "P"
P = searchObj.group()
# Database connection
db = MySQLdb.connect("localhost","user","password","database" )

# preparing cursor()
cursor = db.cursor()

   # SQL command
   cursor.execute('''INSERT into students(Firstname,Lastname,UID)
                  values (%s, %s,%s)''',
                  ('John','Doe',P))
   # Commiting insert
   db.commit()

# Close connection
db.close()
