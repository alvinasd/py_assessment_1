import csv 
import pandas as pd
import mysql.connector as mysql

#open csv file
data = open("random_txt.csv", encoding = "utf-8")

#read the csv file
csv_data = csv.reader(data)

#reformat data
rand_data = list(csv_data)
print(rand_data)

#connect to mysql
connection = mysql.connect(host = "localhost", user = "root", password = "3171998Aa")

cursor = connection.cursor()
#select DB, drop table if made, create table
cursor.execute("USE py_assessment_1;")
cursor.execute("DROP TABLE IF EXISTS random_data;")
cursor.execute("CREATE TABLE random_data(id VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255));")

row = list["","",""]
entry = "INSERT INTO random_data VALUES ('%s', '%s', '%s');"
cursor.execute(entry, list(row))
connection.commit()
print(cursor.execute("SELECT * FROM random_data;"))