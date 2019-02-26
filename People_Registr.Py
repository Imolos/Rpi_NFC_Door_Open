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
   cursor.execute('''INSERT into list(Firstname,Lastname)
                   SELECT Firstname,Lastname FROM students WHERE UID = %s ''',
                  (P))
     # Odeslání změn na server
   db.commit()

# Close Connection
db.close()
