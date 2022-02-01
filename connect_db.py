import mysql.connector as connector

# Connection to Database:

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                               port = '3306',
                               user='root',
                               password='',
                               database='staff database')

# Creating Table :

        query = 'create table if not exists user_details(user_name varchar(100),contact int(20) primary key,email varchar(100),location varchar(100))'
        cur = self.con.cursor()
        cur.execute(query)

# Data Insertion :

    def insert_user_details(self,user_name,contact,email,location):
        query = "insert into user_details(user_name,contact,email,location) values('{}','{}','{}','{}')".format(user_name,contact,email,location)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data is saved to database")

# Fetching Data :

    def civil(self):

        # query = "SELECT * FROM organisational_details"
        # cur = self.con.cursor()
        # cur.execute(query)
        # rows = cur.fetchall()
        # self.con.commit()
        # print(rows)
        # self.con.close()

        query = "SELECT * FROM organisational_details WHERE Department = 'Civil Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def mech(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Mechanical Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def elec(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Electrical Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def instru(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Instrumentation Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def comp(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Computer Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def infotec(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Information Engineering'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def moha(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Home Affairs'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def moj(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Justice'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def mol(self):

        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Labour'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def mos(self):
        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Science'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def mosa(self):
        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Social Affairs'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

    def mosp(self):
        query = "SELECT * FROM organisational_details WHERE Department = 'Ministry of Sports'"
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        self.con.commit()
        print(rows)
        self.con.close()

helper = DBHelper()
