#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install mysql-connector


# In[5]:


#import require libraries 

import mysql.connector
from mysql.connector import Error


# In[12]:


#make connection with database from python
try:
    connection = mysql.connector.connect(
            host = "127.0.0.1",
            user = "rahuldb",
            password = "rahul@1889",
            database = "analytics_info",
            auth_plugin='mysql_native_password',
            autocommit=True

    )
    print('connected to mysql database')

except Error as e:
    print(f'Error connecting to MySQL: {e}')


# In[13]:


#create a cursor object

try:
    cursor = connection.cursor()
except Error as e:
    print("Error: cursor is not active")
    print(e)


# In[31]:


#CREATING TABLES IN DATABASE

try:
    cursor.execute("CREATE TABLE IF NOT EXISTS Reports(Report_id INT, Report_Name VARCHAR(255), Report_Date DATE, Description VARCHAR(255), Project_ID INT, Analysis_method_ID INT);")
except Error as e:
    print("Error: issue occured while creating table")
    print(e)


# In[37]:


from datetime import datetime


# In[41]:


#INSERT DATA INTO TABLE

report_date = datetime.strptime("1/15/2022", "%m/%d/%Y").date()

try:
    cursor.execute("INSERT INTO Reports(Report_id, Report_Name, Report_Date, Description, Project_ID, Analysis_method_ID) VALUES(%s, %s, %s, %s, %s, %s)", (3001, "Sales Analysis", report_date,"Analyzing sales trends", 2001, 2046))
except Error as e:
    print("Error: Inserting Rows")
    print(e)


# In[42]:


#VALIDATE THE INSERTED DATA

try:
    cursor.execute("SELECT * FROM Reports;")
except Error as e:
    print("Error: select *")
    print(e)

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()


# In[43]:


# CLOSE THE CURSOR AND CONNECTION

cursor.close()
connection.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




