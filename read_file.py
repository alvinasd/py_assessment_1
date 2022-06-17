import csv 
import pandas as pd
import mysql.connector as mysql

#open csv file
data = open("random_txt.csv", encoding = "utf-8")

#read the csv file
csv_data = csv.reader(data)

#reformat data
rand_data = list(csv_data)

#put csv data into a DF 
df = pd.DataFrame(rand_data)
df.rename(columns={0: 'id', 1: 'first_name', 2: 'last_name'}, inplace=True)

#connect to mysql, password deleted for privacy
connection = mysql.connect(host = "localhost", user = "root", password = "")

cursor = connection.cursor()
#select DB, drop table if made, create table
cursor.execute("USE py_assessment_1;")
cursor.execute("DROP TABLE IF EXISTS random_data;")
cursor.execute("CREATE TABLE random_data(id VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255));")

#insert DF into mysql table
for i, row in df.iterrows():
	query = "INSERT INTO random_data (id, first_name, last_name) VALUES (%s,%s,%s);"
	cursor.execute(query, tuple(row))

connection.commit()

#create final table to insert values in the requested format
cursor.execute("DROP TABLE IF EXISTS final;")
cursor.execute("CREATE TABLE final (id varchar(255), name varchar(255));")

#call and insert data from random_data
#into a dataframe - to be sent into the "final" table
random_data_table = pd.read_sql_query("SELECT id, first_name AS name FROM random_data UNION ALL SELECT id, last_name AS name FROM random_data ORDER BY id;", connection)
df2 = pd.DataFrame(random_data_table)
df.rename(columns={0: 'id', 1: 'name'}, inplace=True)
print(df2)

#used to send data into "final" table
for i, row in df2.iterrows():
	query = "INSERT INTO final (id, name) VALUES (%s, %s);"
	cursor.execute(query, tuple(row))

#used to commit changes to db
connection.commit()

#close connection to mysql
connection.close()