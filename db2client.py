import os
import datetime
import json
import ibm_db

# CREATE TABLE Statement
'''
CREATE TABLE OSWTRAFFIC (
                            CATEGORY CHAR(1) NOT NULL, 
                            LINK VARCHAR(255) NOT NULL,
                            TRAFFIC_TIMESTAMP TIMESTAMP NOT NULL
                            );
'''

class db2Access:
    db2conn = ""

    def __init__ (self):

        # read the db2.cred file with json content describing the db2 connection parameter
        #{
        #"db_name": "BLUEDB",
        #"db_hostname": "dashdb-...",
        #"db_port": "50000",
        #"db_uid": "xxx",
        #"db_pwd": "yyy"
        #}

        data = os.environ['db2-cred']
        #print('data:',data)

        # parse file
        obj = json.loads(data)

        DB_NAME     = obj["db_name"]
        DB_HOSTNAME = obj["db_hostname"]
        DB_PORT     = obj["db_port"]
        DB_UID      = obj["db_uid"]
        DB_PWD      = obj["db_pwd"]

        print(">",DB_NAME,"<")

        self.db2conn = ibm_db.connect("DATABASE="+DB_NAME+";HOSTNAME="+DB_HOSTNAME+";PORT="+DB_PORT+";UID="+DB_UID+";PWD="+DB_PWD+";","","")

    def close(self):
        ibm_db.close(self.db2conn)
    
    def get_categorized_images(self, category):
        get_images_stmt = "SELECT CATEGORY, LINK, TRAFFIC_TIMESTAMP FROM OSWTRAFFIC\
             WHERE CATEGORY = '"+category+"' AND (TRAFFIC_TIMESTAMP > NOW() - 24 HOURS);"
        stmt = ibm_db.prepare(self.db2conn, get_images_stmt) 
        ibm_db.execute(stmt)
        result = {}
        imageList = []
        result["imageList"] = imageList 
        dbresult = ibm_db.fetch_assoc(stmt)
        while dbresult != False:
            record = {}
            record['url'] = dbresult['LINK']
            record['time'] = (dbresult['TRAFFIC_TIMESTAMP']).strftime('%d.%m.%Y %H:%M')
            imageList.append(record)
            dbresult = ibm_db.fetch_assoc(stmt)    
        return result
        
if __name__ == '__main__':
    
    mydb2 = db2Access()    
    mydb2.get_car_images()
    mydb2.close()

