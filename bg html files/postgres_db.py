import postgresql
import re

db = postgresql.open("pq://postgres:root@localhost/postgres")
get_records = db.prepare("SELECT * from test.verse_content") 
mylist=[]
i=0
for row in get_records:
   
    if row['c1title']:
         chap=row['c1title'].split('.')[0]
##         
##         if chap.isdigit():
##              
####               mylist[chap]=mylist[chap]+1
##         else:
##              
####         if chap.isdigit():
####             mylist[chap]=mylist[chap]+1


f=open("hello.txt",'w')
f.write("hello")
     
   
    
