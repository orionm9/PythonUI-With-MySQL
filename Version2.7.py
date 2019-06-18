#!/usr/bin/env python
# coding=utf-8
import datetime
import time
import warnings
import pymysql
import csv
import sys

from tkinter import *
import tkinter as tk
import tkinter.messagebox 

from faker import Faker

warnings.filterwarnings('ignore')
hostname = "localhost"
username = "root"
password = "way520520"
wait = "Please wait...\n\n"

window = tk.Tk()
window.title('Group1 Version2.7')
window.geometry('600x300')

image_file = tk.PhotoImage(file='main.png') 
# lable=tk.Label(window,image=image_file)

canvas = tk.Canvas(window, bg='green', width=600, height=800)
image = canvas.create_image(300, 0, anchor='n',image=image_file) 
canvas.grid(row=0,rowspan=70,column=1,columnspan=4)

on_hit = False  
var = tk.StringVar()    




# def hit1():
#     global on_hit
#     if on_hit == False:     
#         on_hit = True
#         var.set('you hit me')  
#     else:       
#         on_hit = False
#         var.set('') # 
def DBA():



    def CreateDBA():
        clean()
        
        # connect DBA
        try:
            starttime = time.time()
            print('connect mysql DBA...')
            conn = pymysql.connect(hostname, username,password)
            cursor = conn.cursor()
            # run SQL, create DBA.
            #cursor.execute("""drop database if exists DBA """)
            cursor.execute("""CREATE DATABASE IF NOT EXISTS DBA""")
            # close connection
            cursor.close()
            conn.commit()
            conn.close()

            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)

            cursor = db.cursor()
            # Create table if not exists student
            sql1 = """CREATE TABLE IF NOT EXISTS `Players`(
                    Name VARCHAR(64),
                    PlayerID INT NOT NULL,
                    Team_name VARCHAR(64),
                    Position CHAR(2) CHECK (Position IN ('QB' , 'RB', 'WR')),
                    Touchdowns INT,
                    Total_Yards INT,
                    Salary INT,
                    PRIMARY KEY (PlayerID)
                    )"""
            # create table if not exists Games
            sql2 = """CREATE TABLE IF NOT EXISTS `Games`(
                    GameID INT NOT NULL,
                    Date DATE,
                    Stadium VARCHAR(64),
                    Result CHAR(1) CHECK (Result IN ('W' , 'L', 'T')),
                    Attendance INT,
                    Ticket_Revenue INT,
                    PRIMARY KEY (GameID)
                    )"""
            # create table if not exists Play
            sql3 = """CREATE TABLE IF NOT EXISTS `Play`(
                    PlayerID INT NOT NULL,
                    GameID INT NOT NULL,
                    PRIMARY KEY (PlayerID , GameID)
                    )"""
            #create table Run Mysql
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)

            endtime = time.time()
            print('DBA Connection successful!')
            result = "DBA Connection successful!!\nCreate tables successful!!!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Database Connection False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))
    
    def createtable():
        db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
        # cursor()
        cursor = db.cursor()

        # Drop table if exists student
        #cursor.execute("DROP TABLE IF EXISTS Players")
        sql1 = """CREATE TABLE IF NOT EXISTS `Players`(
                Name VARCHAR(64),
                PlayerID INT NOT NULL,
                Team_name VARCHAR(64),
                Position CHAR(2) CHECK (Position IN ('QB' , 'RB', 'WR')),
                Touchdowns INT,
                Total_Yards INT,
                Salary INT,
                PRIMARY KEY (PlayerID)
                )"""

        sql2 = """CREATE TABLE IF NOT EXISTS `Games`(
                GameID INT NOT NULL,
                Date DATE,
                Stadium VARCHAR(64),
                Result CHAR(1) CHECK (Result IN ('W' , 'L', 'T')),
                Attendance INT,
                Ticket_Revenue INT,
                PRIMARY KEY (GameID)
                )"""

        sql3 = """CREATE TABLE IF NOT EXISTS `Play`(
                PlayerID INT NOT NULL,
                GameID INT NOT NULL,
                PRIMARY KEY (PlayerID , GameID)
                )"""
        # sql4 = "SELECT PlayerID, Team_name, Salary FROM Players"
        #create table
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        #  print(cursor.execute(sql4))

    def insertAPlayers():
        deleteAPlayers()
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            # cursor()
            cursor = db.cursor()
            filename= txt1.get()
            starttime = time.time()
            # sql1 = "LOAD DATA local INFILE %s INTO TABLE DBA.Players fields terminated BY ',' lines terminated BY '\n';", filename
            sql1 = "LOAD DATA local INFILE '" + filename + "'INTO TABLE DBA.Players fields terminated BY ',' lines terminated BY '\n';"
            cursor.execute(sql1)
            cursor.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBA.Players successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBA.Players data False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def insertAGames():
        deleteAGames()
        clean()
        db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
        # cursor()
        cursor = db.cursor()
        filename= txt1.get()
        starttime = time.time()
        try:
            # sql1 = "LOAD DATA local INFILE %s INTO TABLE DBA.Players fields terminated BY ',' lines terminated BY '\n';", filename
            sql1 = "LOAD DATA local INFILE '" + filename + "'INTO TABLE DBA.Games fields terminated BY ',' lines terminated BY '\n';"
            cursor.execute(sql1)
            cursor.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBA.Games successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            txt4.insert(END, result)
            # print(tk.messagebox.showinfo(title='Result', message=result))
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBA.Games False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def insertAPlay():
        deleteAPlay()
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            # cursor()
            cursor = db.cursor()
            filename= txt1.get()
            starttime = time.time()
            # sql1 = "LOAD DATA local INFILE %s INTO TABLE DBA.Players fields terminated BY ',' lines terminated BY '\n';", filename
            sql1 = "LOAD DATA local INFILE '" + filename + "'INTO TABLE DBA.Play fields terminated BY ',' lines terminated BY '\n';"
            cursor.execute(sql1)
            cursor.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBA.Play successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBA.Play False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def destroy():
        window_DBA.destroy()
    
    def queryDBA():
        empty()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            starttime = time.time()
            # cursor()
            print("")
            # sql1 = input("Please write MYSQL statement: \n")
            sql1 = txt2.get("0.0", "end")
            cursor = db.cursor()
            cursor.execute(sql1)

            f = open('result.txt','w')
            for num in range(1,101):
                data = cursor.fetchone()
                result = str(data) + "\n"
                if result != 'None\n':
                    f.write(result)
                elif result=='None\n' and num==1:
                    f.write("No result")
            f.close()
            db.commit()
            db.close()
            endtime = time.time()

            qury = ""
            f2 = open("result.txt","r")
            lines = f2.readlines()
            for line in lines:
                qury = qury + line
            f2.close()

            print("Run successful!")
            result = "Run successful!\n" "Run time: %.7f Second\n\nResult(Limation:100):\n\n"%(endtime-starttime) +qury
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(0.0, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteAPlayers():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()

            # SQL delete
            sql = "DELETE FROM Players"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete Players data successful!')
            endtime = time.time()
            result = "Delete DBA.Players successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBA.Players False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteAGames():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()
            # SQL delete
            sql = "DELETE FROM Games"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete Games data successful!')
            endtime = time.time()
            result = "Delete DBA.Games successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBA.Games False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteAPlay():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBA",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()
            # SQL delete
            sql = "DELETE FROM Play"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete DBA.Play data successful!')
            endtime = time.time()
            # print ('Time: ' + str(endtime - starttime))
            result = "Delete DBA.Play successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBA.Play False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def clean():
        txt4.delete('1.0','end')
        txt4.insert(END, wait)

    def empty():
        txt4.delete('1.0','end')
   


    window_DBA = tk.Toplevel(window)
    window_DBA.geometry('600x800')
    window_DBA.title('Bulk insertion(DBA)')

    canvas = tk.Canvas(window_DBA, bg='green', width=600, height=800)
    image = canvas.create_image(300, 0, anchor='n',image=image_file) 
    canvas.grid(row=0,rowspan=70,column=1,columnspan=3)


    b10 = tk.Button(window_DBA, 
        text='Create database DBA and tables(Optional)',      
        font=('Arial', 12),
        width=40, height=3, 
        command=CreateDBA)  

    b0 = tk.Button(window_DBA, 
        text='Exit',
        fg= 'red',
        font=('Arial', 12),
        width=20, height=2, 
        command=exit)  

    l2 = tk.Button(window_DBA, 
        text='←Before you do insert, you need to input the file name on the textbox.↓↓',
        bg='white', font=('Arial', 12), width=60, height=1,fg = "Blue")
    # l1.grid() 

    txt1 = tk.Entry(window_DBA,width = 45, show = None)
    txt1.insert(END,'1000Players.txt')

    b11 = tk.Button(window_DBA, 
        text='insert  into Players',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertAPlayers)     


    b12 = tk.Button(window_DBA, 
        text='insert into Games',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertAGames)     

    b13 = tk.Button(window_DBA, 
        text='insert into Play',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertAPlay)

    l3 = tk.Button(window_DBA, 
        text='←Before you do query, you need to input the statement on the textbox.↓↓',
        bg='white', font=('Arial', 12), width=60, height=1,fg = "Blue")
    # l1.grid() 

    txt2 = tk.Text(window_DBA,width = 55, height= 6, relief= "sunken", borderwidth= 2)
    txt2.insert(END,'Select * from Players')

    b14 = tk.Button(window_DBA, 
        text='query the data',      
        font=('Arial', 12),
        width=20, height=3, 
        command=queryDBA)     

    b15 = tk.Button(window_DBA, 
        text='Delete Players',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteAPlayers)    


    b16 = tk.Button(window_DBA, 
        text='Delete Games',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteAGames)     


    b17 = tk.Button(window_DBA, 
        text='Delete Play',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteAPlay)  

    b104 = tk.Button(window_DBA, 
        text='Empty the output',     
        font=('Arial', 12),
        width=20, height=2, 
        command=empty)  


    b105 = tk.Button(window_DBA, 
        text='Back',     
        font=('Arial', 12),
        width=20, height=2, 
        command=destroy)  

    l5 = tk.Button(window_DBA, 
        text='↓↓↓Output↓↓↓',
        bg='white', font=('Arial', 20), width=10, height=1)

    scroll = tk.Scrollbar()

    txt4 = tk.Text(window_DBA,height=25,relief= "ridge", borderwidth= 6)
    scroll.config(command=txt4.yview)
    txt4.config(yscrollcommand=scroll.set)

    b10.grid(row=0,column=1, columnspan=2)
    b0.grid(row=0,column=3)

    l2.grid(row=1,column=2,columnspan=3)
    txt1.grid(row=2,column=2,columnspan=3)

    b11.grid(row=1,column=1)
    b12.grid(row=2,column=1)
    b13.grid(row=3,column=1)

    b14.grid(row=4,column=1)
    l3.grid(row=4,column=2,columnspan=3)
    txt2.grid(row=5,rowspan=8,column=2,columnspan=3)

 
    b15.grid(row=6,column=1)
    b16.grid(row=7,column=1)
    b17.grid(row=8,column=1)




    l5.grid(row=17,column=1)
    b104.grid(row=17, column = 2)
    b105.grid(row=17, column = 3)
    txt4.grid(row=18,rowspan = 28,column=1,columnspan=3)

    window_DBA.mainloop()



def DBB():



    def CreateDBB():
        clean()
        
        # connect DBB
        try:
            starttime = time.time()
            print('connect mysql DBB...')
            conn = pymysql.connect(hostname, username,password)
            cursor = conn.cursor()
            # run SQL, create DBB.
            #cursor.execute("""drop database if exists DBB """)
            cursor.execute("""CREATE DATABASE IF NOT EXISTS DBB""")
            # close connection
            cursor.close()
            conn.commit()
            conn.close()

            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)

            cursor = db.cursor()
            # Create table if not exists student
            sql1 = """CREATE TABLE IF NOT EXISTS `Players`(
                    Name VARCHAR(64),
                    PlayerID INT NOT NULL,
                    Team_name VARCHAR(64),
                    Position CHAR(2) CHECK (Position IN ('QB' , 'RB', 'WR')),
                    Touchdowns INT,
                    Total_Yards INT,
                    Salary INT,
                    PRIMARY KEY (PlayerID)
                    )"""
            # create table if not exists Games
            sql2 = """CREATE TABLE IF NOT EXISTS `Games`(
                    GameID INT NOT NULL,
                    Date DATE,
                    Stadium VARCHAR(64),
                    Result CHAR(1) CHECK (Result IN ('W' , 'L', 'T')),
                    Attendance INT,
                    Ticket_Revenue INT,
                    PRIMARY KEY (GameID)
                    )"""
            # create table if not exists Play
            sql3 = """CREATE TABLE IF NOT EXISTS `Play`(
                    PlayerID INT NOT NULL,
                    GameID INT NOT NULL,
                    PRIMARY KEY (PlayerID , GameID)
                    )"""
            #create table Run Mysql
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)

            endtime = time.time()
            print('DBB Connection successful!')
            result = "DBB Connection successful!!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Database Connection False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))
    
    def createtable():
        db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
        # cursor()
        cursor = db.cursor()

        # Drop table if exists student
        #cursor.execute("DROP TABLE IF EXISTS Players")
        sql1 = """CREATE TABLE IF NOT EXISTS `Players`(
                Name VARCHAR(64),
                PlayerID INT NOT NULL,
                Team_name VARCHAR(64),
                Position CHAR(2) CHECK (Position IN ('QB' , 'RB', 'WR')),
                Touchdowns INT,
                Total_Yards INT,
                Salary INT,
                PRIMARY KEY (PlayerID)
                )"""

        sql2 = """CREATE TABLE IF NOT EXISTS `Games`(
                GameID INT NOT NULL,
                Date DATE,
                Stadium VARCHAR(64),
                Result CHAR(1) CHECK (Result IN ('W' , 'L', 'T')),
                Attendance INT,
                Ticket_Revenue INT,
                PRIMARY KEY (GameID)
                )"""

        sql3 = """CREATE TABLE IF NOT EXISTS `Play`(
                PlayerID INT NOT NULL,
                GameID INT NOT NULL,
                PRIMARY KEY (PlayerID , GameID)
                )"""
        # sql4 = "SELECT PlayerID, Team_name, Salary FROM Players"
        #create table
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        #  print(cursor.execute(sql4))

    def insertBPlayers():
        deleteBPlayers()
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            cur = db.cursor()
            cur.execute("SET SQL_SAFE_UPDATES = 0;")
            cur.execute("delete from Players;")

            filename= txt1.get()
            starttime = time.time()
            f = open(filename, "r")
            while True:
                line = f.readline()
                if line:
                    line = line.strip('\n')
                    line = line.split(",")
                    #print (line)
                    cur.execute(
                        "insert into Players values(%s,%s,%s,%s,%s,%s,%s)",
                        [line[0], line[1], line[2], line[3], line[4], line[5], line[6]])
                else:
                    break
            f.close()
            cur.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBB.Players data successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBB.Players False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def insertBGames():
        deleteBGames()
        clean()

        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            cur = db.cursor()
            cur.execute("SET SQL_SAFE_UPDATES = 0;")
            cur.execute("delete from Games;")
            filename= txt1.get()
            starttime = time.time()
            f = open(filename, "r")
            while True:
                line = f.readline()
                if line:
                    line = line.strip('\n')
                    line = line.split(",")
                    #print (line)
                    cur.execute(
                        "insert into Games values(%s,%s,%s,%s,%s,%s)",
                        [line[0], line[1], line[2], line[3], line[4], line[5]])
                else:
                    break
            f.close()
            cur.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBB.Games data successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBB.Games False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def insertBPlay():
        deleteBPlay()
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            cur = db.cursor()
            cur.execute("SET SQL_SAFE_UPDATES = 0;")
            cur.execute("delete from Play;")
            filename= txt1.get()
            starttime = time.time()
            f = open(filename, "r")
            while True:
                line = f.readline()
                if line:
                    line = line.strip('\n')
                    line = line.split(",")
                    #print (line)
                    cur.execute(
                        "insert into Play values(%s,%s)",
                        [line[0], line[1]])
                else:
                    break
            f.close()
            cur.close()
            db.commit()
            print ('Insert data successful!')
            endtime = time.time()
            result = "Insert into DBB.Play successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Insert into DBB.Play False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

            deleteBPlay()
            clean()
            try:
                db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
                # cursor()
                cursor = db.cursor()
                filename= txt1.get()
                starttime = time.time()
                # sql1 = "LOAD DATA local INFILE %s INTO TABLE DBB.Players fields terminated BY ',' lines terminated BY '\n';", filename
                sql1 = "LOAD DATA local INFILE '" + filename + "'INTO TABLE DBB.Play fields terminated BY ',' lines terminated BY '\n';"
                cursor.execute(sql1)
                cursor.close()
                db.commit()
                print ('Insert data successful!')
                endtime = time.time()
                result = "Insert into DBB.Play successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
                # print(tk.messagebox.showinfo(title='Result', message=result))
                txt4.insert(END, result)
            except Exception as e:
                print("False")
                print('Reason:', e)
                result = "Insert into DBB.Play False!\n" + "\nReason: " + str(e)
                print(tk.messagebox.showinfo(title='Result', message=result))

    def destroy():
        window_DBB.destroy()
    
    def queryDBB():
        empty()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            starttime = time.time()
            # cursor()
            print("")
            # sql1 = input("Please write MYSQL statement: \n")
            sql1 = txt2.get("0.0", "end")
            cursor = db.cursor()
            cursor.execute(sql1)

            f = open('result.txt','w')
            for num in range(1,101):
                data = cursor.fetchone()
                result = str(data) + "\n"
                if result != 'None\n':
                    f.write(result)
                elif result=='None\n' and num==1:
                    f.write("No result")
            f.close()
            db.commit()
            db.close()
            endtime = time.time()

            qury = ""
            f2 = open("result.txt","r")
            lines = f2.readlines()
            for line in lines:
                qury = qury + line
            f2.close()

            print("Run successful!")
            result = "Run successful!\n" "Run time: %.7f Second\n\nResult(Limation:100):\n\n"%(endtime-starttime) +qury
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(0.0, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteBPlayers():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()

            # SQL delete
            sql = "DELETE FROM Players"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete Players data successful!')
            endtime = time.time()
            result = "Delete DBB.Players successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBB.Players False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteBGames():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()
            # SQL delete
            sql = "DELETE FROM Games"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete Games data successful!')
            endtime = time.time()
            result = "Delete DBB.Games successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBB.Games False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def deleteBPlay():
        clean()
        try:
            db = pymysql.connect(hostname,username,password,"DBB",local_infile=1)
            starttime = time.time()
            # cursor()
            cursor = db.cursor()
            # SQL delete
            sql = "DELETE FROM Play"
            cursor.execute(sql)
            db.commit()
            db.close()
            print ('Delete DBB.Play data successful!')
            endtime = time.time()
            # print ('Time: ' + str(endtime - starttime))
            result = "Delete DBB.Play successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
            # print(tk.messagebox.showinfo(title='Result', message=result))
            txt4.insert(END, result)
        except Exception as e:
            print("False")
            print('Reason:', e)
            result = "Delete DBB.Play False!\n" + "\nReason: " + str(e)
            print(tk.messagebox.showinfo(title='Result', message=result))

    def clean():
        txt4.delete('1.0','end')
        txt4.insert(END, wait)

    def empty():
        txt4.delete('1.0','end')

    window_DBB = tk.Toplevel(window)
    window_DBB.geometry('600x800')
    window_DBB.title('Single insertion(DBB)')

    canvas = tk.Canvas(window_DBB, bg='green', width=600, height=800)
    image = canvas.create_image(300, 0, anchor='n',image=image_file) 
    canvas.grid(row=0,rowspan=70,column=1,columnspan=3)

    b10 = tk.Button(window_DBB, 
        text='Create database DBB and tables(Optional)',      
        font=('Arial', 12),
        width=40, height=3, 
        command=CreateDBB)  

    b0 = tk.Button(window_DBB, 
        text='Exit',
        fg= 'red',
        font=('Arial', 12),
        width=20, height=2, 
        command=exit) 

    # l2 = tk.Label(window_DBB, 
    #     text='←Before you do insert, you need to input the file name on the textbox.↓↓',
    #     bg='white', font=('Arial', 12), width=60, height=2,fg='blue')
    # # l1.grid() 
    l2 = tk.Button(window_DBB, 
        text='←Before you do insert, you need to input the file name on the textbox.↓↓',      
        font=('Arial', 12),
        width=60, height=1,fg='blue') 

    txt1 = tk.Entry(window_DBB,width = 45, show = None)
    txt1.insert(END,'1000Players.txt')

    b11 = tk.Button(window_DBB, 
        text='insert  into Players',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertBPlayers)     


    b12 = tk.Button(window_DBB, 
        text='insert into Games',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertBGames)     

    b13 = tk.Button(window_DBB, 
        text='insert into Play',      
        font=('Arial', 12),
        width=20, height=2, 
        command=insertBPlay)

    # l3 = tk.Label(window_DBB, 
    #     text='←Before you do query, you need to input the statement on the textbox.↓↓',
    #     bg='white', font=('Arial', 12), width=60, height=1,fg='blue')
    # l1.grid() 

    l3 = tk.Button(window_DBB, 
        text='←Before you do query, you need to input the statement on the textbox.↓↓',      
        font=('Arial', 12),
        width=60, height=1,fg='blue') 

    txt2 = tk.Text(window_DBB,width = 55, height= 7, relief= "sunken", borderwidth= 2)
    txt2.insert(END,'Select * from Players')

    b14 = tk.Button(window_DBB, 
        text='query the data',      
        font=('Arial', 12),
        width=20, height=3, 
        command=queryDBB)     

    b15 = tk.Button(window_DBB, 
        text='Delete Players',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteBPlayers)    


    b16 = tk.Button(window_DBB, 
        text='Delete Games',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteBGames)     


    b17 = tk.Button(window_DBB, 
        text='Delete Play',      
        font=('Arial', 12),
        width=20, height=2, 
        command=deleteBPlay)  

    b104 = tk.Button(window_DBB, 
        text='Empty the output',     
        font=('Arial', 12),
        width=30, height=2, 
        command=empty)  


    b105 = tk.Button(window_DBB, 
        text='Back',     
        font=('Arial', 12),
        width=30, height=2, 
        command=destroy)  

    l5 = tk.Button(window_DBB, 
        text='↓↓↓Output↓↓↓',
        bg='white', font=('Arial', 20), width=10, height=1)

    scroll = tk.Scrollbar()

    txt4 = tk.Text(window_DBB,height=25,relief= "ridge", borderwidth= 6)
    scroll.config(command=txt4.yview)
    txt4.config(yscrollcommand=scroll.set)



    b10.grid(row=0,column=1, columnspan=2)
    b0.grid(row=0,column=3)

    l2.grid(row=1,column=2,columnspan=3)
    txt1.grid(row=2,column=2,columnspan=3)

    b11.grid(row=1,column=1)
    b12.grid(row=2,column=1)
    b13.grid(row=3,column=1)

    b14.grid(row=4,column=1)
    l3.grid(row=4,column=2,columnspan=3)
    txt2.grid(row=5,rowspan=8,column=2,columnspan=3)

 
    b15.grid(row=6,column=1)
    b16.grid(row=7,column=1)
    b17.grid(row=8,column=1)




    l5.grid(row=17,column=1)
    b104.grid(row=17, column = 2)
    b105.grid(row=17, column = 3)
    txt4.grid(row=18,rowspan = 28,column=1,columnspan=3)

    window_DBB.mainloop()



def CreatePlayers():
 
    #start time
    starttime = time.time()
    #loop = how many rows. size intger.
    #row = int(sys.argv[1])
    print("dataset size: (example 10000)")
    size = txt3.get()
    row = int(size)
    #open file
    File = open( str(row) + "Players" + ".txt", "w")

    PlayerID1 = 0 #PlayerID from 0
    space = ','
    f = Faker()

    for i in range(row):
        #Random Name
        name1 = f.name()
        Name = name1.replace(" ", "_")
        #PlayerID = 1,2,3...
        PlayerID1 += 1
        PlayerID2 = str(PlayerID1)
        PlayerID = PlayerID2.zfill(8)
        #Random Team Name = State + Team
        Team_name1 = f.state()
        Team_name = Team_name1.replace(" ", "_") +"_Team"
        #Random Position = QB or RB or WR
        Position1 = str(f.random_int(1,3))
        Position2 = Position1.replace("1", "QB")
        Position3 = Position2.replace("2", "RB")
        Position = Position3.replace("3", "WR")
        #Random Touchdowns, from 0 to 300
        Touchdowns = str(f.random_int(0,300))
        #Random Total Yards, from 0 to 500
        Total_Yards = str(f.random_int(0,500))
        #Random Salary, from 100000.99 to 999999.99
        Salary1 = f.random_int(100000,999999)
        Salary2 = f.pyfloat(left_digits = 0, right_digits = 2)
        Salary = str(Salary1 + Salary2)
        # print (Name + ' ' + PlayerID + ' ' + Team_name + ' ' + Position + ' ' + Touchdowns + ' ' + Total_Yards + ' ' + Salary)
        #Row
        data = (Name + space + PlayerID + space + Team_name + space + Position + space + Touchdowns + space + Total_Yards + space + Salary)
        #write row
        File.write(str(data) + "\n")
    #Close the file
    File.close()
    #Read file
    # with open("datax.txt") as f:
    #     for line in f.readlines():
    #         print(line)
    #End time
    endtime = time.time()
    #Run time
    result = "Create \""+ str(row) + "Players" + ".txt" + "\" successful\n" "\nRun time: %.7f Second"%(endtime-starttime)
    print(tk.messagebox.showinfo(title='Result', message=result))

def CreateGames():

    #start time
    starttime = time.time()
    #loop = how many rows. size intger.
    #row = int(sys.argv[1])
    print("dataset size: (example 10000)")
    size = txt3.get()
    row = int(size)
    #open file
    File = open(str(row) +"Games"+".txt", "w")

    GameID1 = 0 #PlayerID from 0
    space = ','
    f = Faker()

    for i in range(row):

        #GameID = 1,2,3...
        GameID1 += 1
        GameID2 = str(GameID1)
        GameID = GameID2.zfill(8)

        #data
        Date = f.date(pattern="%Y-%m-%d")

        #Stadium = state + center
        Stadium1 = f.state()
        Stadium = Stadium1.replace(" ", "_") +"_Center"

        #Random Result = W or L or T
        Result1 = str(f.random_int(1,3))
        Result2 = Result1.replace("1", "W")
        Result3 = Result2.replace("2", "L")
        Result = Result3.replace("3", "T")

        #Random Attendance, from 0 to 300
        Attendance = str(f.random_int(0,150000))
    
        #Random Ticket_Revenue, from 1000.99 to 9999999.99
        Ticket_Revenue1 = f.random_int(1000,9999999)
        Ticket_Revenue2 = f.pyfloat(left_digits = 0, right_digits = 2)
        Ticket_Revenue = str(Ticket_Revenue1 + Ticket_Revenue2)
  
        # print (Name + ' ' + PlayerID + ' ' + Team_name + ' ' + Result + ' ' + Attendance + ' ' + Total_Yards + ' ' + Ticket_Revenue)
        #Row
        data = (GameID + space + Date + space + Stadium + space + Result + space + Attendance + space + Ticket_Revenue)
        #write row
        File.write(str(data) + "\n")
    #Close the file
    File.close()
    #Read file
    # with open("datax.txt") as f:
    #     for line in f.readlines():
    #         print(line)
    #End time
    endtime = time.time()
    #Run time
    result = "Create \""+ str(row) + "Games" + ".txt" + "\" successful\n" "\nRun time: %.7f Second"%(endtime-starttime)
    print(tk.messagebox.showinfo(title='Result', message=result))

def CreatePlay():
 
    #start time
    starttime = time.time()
    #loop = how many rows. size intger.
    #row = int(sys.argv[1])
    print("dataset size: (example 10000)")
    size = txt3.get()
    row = int(size)
    #open file
    File = open(str(row) + "Play" + ".txt", "w")

    PlayerID1 = 0 #PlayerID from 0
    GameID1 = 0
    space = ','
    f = Faker()

    for i in range(row):

        #PlayerID = 1,2,3...
        PlayerID1 += 1
        PlayerID2 = str(PlayerID1)
        PlayerID = PlayerID2.zfill(8)        
        
        #PlayerID = 1,2,3...
        GameID1 += 1
        GameID2 = str(GameID1)
        GameID = GameID2.zfill(8)

        #Row
        data = (PlayerID + space + GameID)
        #write row
        File.write(str(data) + "\n")
    #Close the file
    File.close()
    #Read file
    # with open("datax.txt") as f:
    #     for line in f.readlines():
    #         print(line)
    #End time
    endtime = time.time()
    #Run time
    result = "Create \""+ str(row) + "Play" + ".txt" + "\" successful\n" "\nRun time: %.7f Second"%(endtime-starttime)
    print(tk.messagebox.showinfo(title='Result', message=result))

def exit():
    print(tk.messagebox.showinfo(title='Have a nice day!', message="Thanks"))

    window.destroy()

# l1 = tk.Label(window, 
#     text='Before do insert, query, and delete, you need choose the database.',
#     font=('Arial', 12), width=60, height=2, fg = "Blue")

l1 = tk.Button(window, 
    text='Before do insert, query, and delete, you need choose the database.',      
    font=('Arial', 12),
    width=60, height=1,fg = "Blue", 
    ) 

b1 = tk.Button(window, 
    text='Bulk-loading(In database DBA)',      
    font=('Arial', 12),
    width=50, height=2, 
    command=DBA
    ) 

b2 = tk.Button(window, 
    text='Single insertion(In database DBB)',      
    font=('Arial', 12),
    width=50, height=2, 
    command=DBB) 




 


# l4 = tk.Label(window, 
#     text='Before you create data, you need to input the data set size on the textbox.',
#     bg='white', font=('Arial', 12), width=60, height=1,fg='Blue')

l4 = tk.Button(window, 
    text='Before you create data, you need to input the data set size on the textbox.',      
    font=('Arial', 12),
    width=60, height=1,fg = "Blue", 
    ) 

txt3 = tk.Entry(window,width = 30, show = None)
txt3.insert(END,'1000')

b101 = tk.Button(window, 
    text='Create x Players',      
    font=('Arial', 12),
    width=20, height=2, 
    command=CreatePlayers)     

b102 = tk.Button(window, 
    text='Create x Games',      
    font=('Arial', 12),
    width=20, height=2, 
    command=CreateGames)     


b103 = tk.Button(window, 
    text='Create x Play',     
    font=('Arial', 12),
    width=20, height=2, 
    command=CreatePlay)    

b0 = tk.Button(window, 
    text='Exit',
    fg='red',     
    font=('Arial', 12),
    width=40, height=2, 
    command=exit) 






l1.grid(row=1,column=1,columnspan=3)
b2.grid(row=2,column=1,columnspan=3)
b1.grid(row=3,column=1,columnspan=3)






l4.grid(row=4,column=1,columnspan=3)
txt3.grid(row=5,column=1,columnspan=3)
b101.grid(row=6,column=1)
b102.grid(row=6,column=2)
b103.grid(row=6,column=3)


b0.grid(row=7,column=1,columnspan=5)




# window.attributes("-alpha", 0.3)

window.mainloop()