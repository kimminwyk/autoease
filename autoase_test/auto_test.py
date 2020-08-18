import sys
sys.path.insert(0,"../")
from auto import *

#test_mysql_connect = db_auto(mysql_host="localhost",mysql_user="root",mysql_passwd="autoset",mysql_db="autoease",type_decision="dict")
#####
test_mysql_connect = db_auto(mysql_host="localhost",mysql_user="root",mysql_passwd="autoset",type_decision="dict")

test_mysql_connect.db_insert("autoease")#create pymysql db

test_mysql_connect.connect_db("autoease")#connect to pymysql db

table_insert_array = [["test1","longtext not null"],["test2","varchar(100) not null"]]#Array for table creation

test_mysql_connect.table_insert("autoease_test",table_insert_array)#Create table

insert_solumn = ["test1","test2"]#Column name


insert_value = ["auto test","insert"]#Column value to be added

test_mysql_connect.solumn_insert("autoease_test",insert_solumn,insert_value)#Add column function

query_result = test_mysql_connect.mysql_query("SELECT * FROM autoease_test")#sql statement transfer
#####
#query_result = test_mysql_connect.mysql_query("SELECT test1,test2 FROM autoease_test")
for i in query_result:
    print(i)

