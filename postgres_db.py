import postgresql
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
db = postgresql.open("pq://postgres:root@localhost/postgres")
get_records = db.prepare("SELECT * from test.verse_content") 

f=open("C:\\Users\\I308830\\log.txt","w")

for row in get_records:
##    f=open(row['c1title']+'.html','w')
##    f.write(row['c2ptext'])
    logging.debug('row no : %s ' %(row['c1title']))   
    f.write(row['c1title'])
