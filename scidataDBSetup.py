# Science Data DB Setup script
# Object for setting up database
# Author: Emma Farrell

import mysql.connector
import glob
if glob.glob("db_config.py"):
    print(True)
    import db_config as cfg
else:
    import db_configpa as cfg


conn = ""
cursor = ""
host = cfg.sql["host"]
user = cfg.sql["user"]
pw = cfg.sql["password"]
db = ""

def getcursor():
    global conn
    conn = mysql.connector.connect(
        host = host,
        user = user,
        password = pw,
        database = db,
    )
    global cursor
    cursor = conn.cursor()
    return cursor

def closeAll():
    conn.close()
    cursor.close()

def dropDB():
    # drop DB
    global cursor
    cursor = getcursor()
    cursor.execute("DROP DATABASE IF EXISTS science_measurements")
    closeAll()
    return True

def dropCollectionTable():
    # drop table
    global db
    db = cfg.sql["database"]
    global cursor
    cursor = getcursor()
    cursor.execute("DROP TABLE IF EXISTS collection")
    closeAll()
    return True

def dropCollectionTypeTable():
    # drop table
    global db
    db = cfg.sql["database"]
    global cursor
    cursor = getcursor()
    cursor.execute("DROP TABLE IF EXISTS collection_type")
    closeAll()
    return True

def dropDataTable():
    # drop table
    global db
    db = cfg.sql["database"]
    global cursor
    cursor = getcursor()
    cursor.execute("DROP TABLE IF EXISTS data")
    closeAll()
    return True

def createDB():
    # create DB
    dropDB()
    global cursor
    cursor = getcursor()
    cursor.execute("CREATE DATABASE science_measurements")
    closeAll()
    return True

def createCollectionTable():
    # create collection table
    # USE DATABASE
    dropCollectionTable()
    global cursor
    cursor = getcursor()
    cursor.execute("""CREATE TABLE collection (
                            id int NOT NULL AUTO_INCREMENT,
                            name varchar(50) NOT NULL,
                            collectiontypeid int,
                            startdate datetime,
                            enddate datetime,
                            location varchar(50),
                            measurement varchar(20),
                            units varchar(10),
                            PRIMARY KEY (id)
                        )""")
    closeAll()
    return True

def createCollectionTypeTable():
    # create collection type table
    dropCollectionTypeTable()
    global cursor
    cursor = getcursor()
    cursor.execute("""CREATE TABLE collection_type (
                            id int NOT NULL AUTO_INCREMENT,
                            collectiontype varchar(50) NOT NULL,
                            PRIMARY KEY (id)
                        )""")
    closeAll()
    return True

def createDataTable():
    # create data table
    dropDataTable()
    global cursor
    cursor = getcursor()
    cursor.execute("""CREATE TABLE data (
                        id int NOT NULL AUTO_INCREMENT,
                        collectionid int NOT NULL,
                        datum varchar(50) NOT NULL,
                        latitude decimal(38,7),
                        longitude decimal(38,7),
                        datecollected datetime,
                        PRIMARY KEY (id)
                    )""")
    closeAll()
    return True  

if __name__ == "__main__":
    createDB()
    createCollectionTable()
    createCollectionTypeTable()
    createDataTable()