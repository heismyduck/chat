import sqlite3
import json

class db():
    
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        print("Opened database successfully")

    def readJson(self):
        f = open('dbCommand.json')
        self.data = json.load(f)
        self.retrieveDict ={}
        for i in self.data['retrieve']:
            for key, val in i.items():
                self.retrieveDict[key] = val

    def createTable(self):
        if self.conn is None: return
        f = open('dbCommand.json')
        data = json.load(f)
        for i in data['create_table']:
            for key, a in i.items():
                self.conn.execute(key)
                print(key)
        
        f.close()
        print("create table success")

    def closeDB(self):
        if self.conn is None: return
        self.conn.close()
    
    def insertHistory(self):
        if self.conn is None: return
        self.conn.execute(self.retrieveDict['insert_history'])
        print(self.retrieveDict['insert_history'])
        

d = db()
d.readJson()
d.insertHistory()
d.closeDB()

