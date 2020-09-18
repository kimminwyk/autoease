"""mysql management auto"""
import sys,os
from .try_result import *
#sys.path.insert(0,"c:\python38\lib\site-packages")
import pymysql
class db_auto:
    def __init__(self,mysql_host = None,mysql_port = None,mysql_user = None,mysql_passwd = "",mysql_db= None,type_decision=None):
        """
        mysql_host = 연결할려는 mysql 의 호스트

        mysql_port = 연결할려는 mysql 의 포트

        mysql_user = 연결할려는 mysql 의 name

        mysql_passwd = 연결할려는 mysql 의 비밀번호

        mysql_db = 연결할려는 database 의 이름

        type_decision = dict 일시에 딕셔너리로 반환 dict 가 아닐시에는 튜블로 mysql 반환 

        """
        """mysql host user passwd db connect"""
        if mysql_port != "":

            if mysql_db != "":

                if type_decision == "dict":

                    """mysql return trpe dict"""
                    self.mysql_new = pymysql.connect(host=mysql_host,port=mysql_port, user=mysql_user, passwd=mysql_passwd, db=mysql_db,cursorclass=pymysql.cursors.DictCursor)

                else:
                    
                    """mysql return type tuple"""
                    self.mysql_new = pymysql.connect(host=mysql_host,port=mysql_port, user=mysql_user, passwd=mysql_passwd, db=mysql_db)

            else:

                if type_decision == "dict":

                    """mysql return trpe dict"""
                    self.mysql_new = pymysql.connect(host=mysql_host,port=mysql_port, user=mysql_user, passwd=mysql_passwd,cursorclass=pymysql.cursors.DictCursor)

                else:

                    """mysql return type tuple"""
                    self.mysql_new = pymysql.connect(host=mysql_host,port=mysql_port, user=mysql_user, passwd=mysql_passwd)
        else:

            if mysql_db != "":

                if type_decision == "dict":

                    """mysql return trpe dict"""
                    self.mysql_new = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db,cursorclass=pymysql.cursors.DictCursor)

                else:

                    """mysql return type tuple"""
                    self.mysql_new = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)

            else:

                if type_decision == "dict":
                        
                    """mysql return trpe dict"""
                    self.mysql_new = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,cursorclass=pymysql.cursors.DictCursor)

                else:

                    """mysql return type tuple"""
                    self.mysql_new = pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd)


    def mysql_query(self,sql_dict):
        """

        sql_dict = 실행하고싶은 sql 명령어

        """


        """mysql code injection"""
        mysql_result = self.mysql_new.cursor()
        try:
            """result sql injection """
            mysql_result.execute(sql_dict)
            self.mysql_new.commit()
            self.mysql_result = mysql_result
            print(1)
            return mysql_result
        except:
            
            mysql_result.execute("SELECT DATABASE()")

            for i in mysql_result:
                if i['DATABASE()'] == None:
                    #데이터베이스 접근 안되있음
                    print(not_db)
                else:
                    print(syntax_insert_sentence)

    def connect_db(self,db_name):
        sql_db = self.mysql_new.cursor()
        try:
            sql_db.execute(f"use {db_name}")

            print(connect_db)
        except:
            #잘못된 데이터베이스 이름
            print(not_value_key_db)
        

    def special_characters(self,table,not_column = [],special_check = None):
        """
        table = 연결할려는 테이블

        

        column_special = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','\\','|',']','}','[','{',"'",'"',';',':','?','/','>','.',',','<']
        ↑
        해당 특수문자로 검사
        
        not_column = 만약에 허용하는 특수문자가있다면 [] 리스트로 선언한후 주입

        그러면 해당 특수문자는 무시하고 나머지를 검사한다.
        """
        
        table_mysql = self.mysql_new.cursor()
        """select * from table name"""
        table_mysql.execute(f"SELECT * FROM {table}")

        """special characters remove"""
        column_special = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','\\','|',']','}','[','{',"'",'"',';',':','?','/','>','.',',','<']

        special_column = list(not_column)


        execute_list = []

        for special in special_column:
            column_special.remove(special)

        for execute in table_mysql:

            for list_special in execute:

                execute_list.append(list_special)

            for key_value in execute_list:

                for check_list in column_special:

                    if str(execute[str(key_value)]).find(check_list) > 0:
                        print(str(execute[str(key_value)]))
        if special_check == "special":
            print("special :[",end="")
            for i in column_special:
                print(i,end=' ')
            print(" ] ")
        elif special_check == "not_special":
            print("not_special :[ ",end='')
            for i in special_column:
                print(i,end=' ')
            print(" ]")
        else:
            print("special :[ ",end='')
            for i in column_special:
                print(i,end=' ')
            
            print(" ] ")
            print("not_special :[ ",end='')
            for i in special_column:
                print(i,end=' ')
            print(" ]")
    def table_insert(self,table_name,column_name = []):
        """
        column_array = [["hello","varchar(100) not null"]]

        table_insert("table",column_array)

        SQL = select hello from table;
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |       hello      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        not data 


        table_insert() = 테이블 생성

        table_name = 원하는 테이블 이름

        column_name = 원하는 컬럼 이름과 속성
        ↑
        [["hello","longtext not null"]]
            ↑                 ↑
        원하는 컬럼이름      원하는 컬럼의 속성


        """

        result_execut = self.mysql_new.cursor()
        i = 0
        sql = f"CREATE TABLE {table_name} ("
        
        for j in column_name:
            i +=1
        for num in range(i):
            if num == i-1:
                sql = sql + f"{column_name[num][0]} {column_name[num][1]})"
            else:
                sql = sql + f"{column_name[num][0]} {column_name[num][1]},"
        try:
            result_execut.execute(sql)

            self.mysql_new.commit()

            print(sql)

        except:
            #잘못된 sql 구문
            print(syntax_insert_sentence)

    def db_insert(self,db_name):
        db = self.mysql_new.cursor()
        try:
            db.execute(f"CREATE DATABASE {db_name}")

            print(insertdb)
        except:
            #잘못된 데이터베이스 구문
            print(not_db)

    def solumn_insert(self,table_name,solunm_name = [],solumn_value = []):
        """
        예) 
        array_name = ["hello"]

        array_value = ["world"]

        solum_insert("test_table",array_name,array_value)

        SQL = select test_table from test_table;

        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |      hello       |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |      world       |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        
        
        
        
        solumn_insert() = 컬럼 데이터 추가

        table_name = 컬럼 추가할 테이블 이름

        solunm_name = 추가할려는 컬럼이름 
        예) -> ["test1","test2"]

        solumn_value = 추가할려는 컬럼의 값
        예) -> ["hello! test1","world! test2"]

        test1 -> hello! test1 추가

        test2 -> world! test2 추가

        순서대로 처리

        """
        mysql_sql = self.mysql_new.cursor()
        
        #print(table_name)
        name = 0
        value = 0
        sql = f"insert into {table_name} ("
        for i in solunm_name:
            #print(i,end="")
            name +=1
        #print()
        for j in solumn_value:
            #print(j,end="")
            value +=1
        print()
        if name == value:
            
            for check_name in range(name):
                if check_name != name-1:

                    sql = sql + f"{solunm_name[check_name]},"
                else:
                    sql = sql + f"{solunm_name[check_name]})"

            sql = sql + " values("

            for check_value in range(value):
                if check_value != name-1:

                    sql = sql + f'"{solumn_value[check_value]}",'
                else:
                    sql = sql + f'"{solumn_value[check_value]}")'
            #print(sql)
            mysql_sql.execute(sql)
            self.mysql_new.commit()


        else:
            print(input_value_exc)

    def column_update(self,table_name,column_return = [],if_column = []):
        """
        SQL = select test1 from table_name;
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |      test1       | 
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |      HELLO       |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        예)
        update_array = [["test1","world"]]

        update_return = [["test1","HELLO"]]

        column_update("table_name",update_array,update_return)
        
        
        컬럼 업데이트

        [[]]
        이중 배열을 이용해야됨

        table_name = 업데이트 하고자하는 테이블 이름

        column_return = 변경할려는 컬럼과 값
        -> type = list
        예 ) array =[[변경할려는 컬럼,변경할려는 컴럼의 값],[변경할려는 컬럼,변경할려는 컬럼의값]]
        예 ) -> "update table_name set hello = "world" where 변경할려는 컬럼의 조건"
                                        ↑          ↑
                            변경할려는 컬럼 이름    변경할려는 컬럼의 값

        if_column = 변경할려는 컬럼값의 조건
        -> type = list
        예 ) array_if = [[변경할려는 조건 컬럼의 이름,변경할려는 조건 컬럼의 값]]
        예 -> "update table_name set 변경할려는 컬럼값 where hello = 'hello'" ← 조건 컬럼의 값
                                                            ↑               
                                                            조건 컬럼의 이름
        column_update(컬럼 변경할려는 테이블,변경할려는 컬럼과 컬럼값이 들어있는 리스트 변수,변경할려는 행의 컬럼과 값이있는 조건의 리스트 변수 )


        """
        mysql_update = self.mysql_new.cursor()

        sql = f"UPDATE {table_name} SET "

        column = 0
        if_clu = 0

        for i in column_return:
            column += 1
        for j in if_column:
            if_clu += 1
        for column_name in range(column):
            
            if str(type(column_return[column_name][1])) == "<class 'str'>":
                if column_name != column-1:
                    sql = sql + f'{column_return[column_name][0]} = "{column_return[column_name][1]}",'
                else:
                    sql = sql + f'{column_return[column_name][0]} = "{column_return[column_name][1]}"'

            else:
                if column_name != column-1:
                    sql = sql + f'{column_return[column_name][0]} = {column_return[column_name][1]},'
                else:
                    sql = sql + f'{column_return[column_name][0]} = {column_return[column_name][1]}'

        sql += ' where '
        
        for if_column_else in range(if_clu):

            if len(if_column) >= 2:
                if str(type(if_column[if_column_else][1])) == "<class 'str'>":
                    if if_column_else != if_clu-1:
                        if len(if_column[if_column_else])-1 >= 2:
                            if if_column[if_column_else][2] == "and" or if_column[if_column_else][2] == "or":
                                sql = sql + f'{if_column[if_column_else][0]} = "{if_column[if_column_else][1]}" {if_column[if_column_else][2]} '
                            else:
                                print(syntax_insert_sentence[0])
                        else:
                            print("fuck")
                            break
                    else:
                        sql = sql + f'{if_column[if_column_else][0]} = "{if_column[if_column_else][1]}"'
                else:
                    if if_column_else != if_clu-1:
                        if len(if_column[if_column_else])-1 >= 2:
                            if if_column[if_column_else][2] == "and" or if_column[if_column_else][2] == "or":
                                sql = sql + f'{if_column[if_column_else][0]} = {if_column[if_column_else][1]} {if_column[if_column_else][2]} '
                            else:
                                print(syntax_insert_sentence[0])
                            
                        else:
                            print("fuck")
                            break
                    else:
                        sql = sql + f'{if_column[if_column_else][0]} = {if_column[if_column_else][1]}'

            else:
                if str(type(if_column[if_column_else][1])) == "<class 'str'>":
                    if if_column_else != if_clu-1:
                        sql = sql + f'{if_column[if_column_else][0]} = "{if_column[if_column_else][1]}"'
                    else:
                        sql = sql + f'{if_column[if_column_else][0]} = "{if_column[if_column_else][1]}"'

                else:
                    if if_column_else != if_clu-1:
                        sql = sql + f'{if_column[if_column_else][0]} = {if_column[if_column_else][1]}'
                    else:
                        sql = sql + f'{if_column[if_column_else][0]} = {if_column[if_column_else][1]}'



        #print(sql)
        try:
            mysql_update.execute(sql)
            self.mysql_new.commit()
        except:
            print(syntax_insert_sentence)

    def column_delect(self,table_name,delete_data = [],data_if=None,asksend = None):
        
        """
        예) 현 데이터 형식 
        SQL = SELECT email,password FROM member;
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |         email         |      password    |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |       a@gmail.com     |        NULL      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |     world@gmail.com   |        NULL      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |     hello@gmail.com   |        NULL      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |  helloworld@gmail.com |        NULL      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |         NULL          |       @c#fs#     |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        |         NULL          |       2hTg$      |
        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        함수 사용 예) data_if 를 하지않을경우

        not_data_if = [["email","a@gmail.com","hello@gmail.com","world@gmail.com","helloworld@gmail.com"],["password","@c#fs#","2hTg$"]]        
        
        column_delect("member",not_data_if,asksend="")

        예) data_if 를 하용할경우

        yes_data_if = [["email","a@gmail.com","or"],["email","world@gmail.com","or"],["email","hello@gmail.com","or"],["email","helloworld@gmail.com","or"],["password","@c#fs#","or"],["password","2hTg$"]]

        column_delect("member",yes_data_if,data_if="and_or",asksend="")
        
         data_if = and or 형식 아니면 in() 형식 선택 

        asksend = 데이터 손실 안전을 위해 묻는다.

        """
        mysql_delete = self.mysql_new.cursor()

        sql = f"DELETE FROM {table_name} WHERE "
        data_delete = 0
        a = 0
        for delete in delete_data:
            data_delete+=1
        for ran in range(data_delete):
            if data_if == "and_or":
                if str(type(delete_data[ran][1])) == "<class 'str'>":
                    if ran+1 == data_delete:
                        sql = sql + f'{delete_data[ran][0]} = "{delete_data[ran][1]}"'
                    else:
                        sql = sql + f'{delete_data[ran][0]} = "{delete_data[ran][1]}" {delete_data[ran][2]} '
                else:
                    if ran+1 == data_delete:
                        sql = sql + f"{delete_data[ran][0]} = {delete_data[ran][1]}"
                    else:
                        sql = sql + f"{delete_data[ran][0]} = {delete_data[ran][1]} {delete_data[ran][2]} "
                    
                
                
                    

            else:

                if str(type(delete_data[ran][1])) == "<class 'str'>":
                    if len(delete_data[ran])-1 >= 2:
                        sql = sql + f"{delete_data[ran][0]} in ("
                        for i in range(1,len(delete_data[ran])):

                            if len(delete_data[ran])-1 == i:
                                if str(type(delete_data[ran][i])) == "<class 'str'>":
                                    sql = sql + f'"{delete_data[ran][i]}"'
                                else:
                                    sql = sql + f'{delete_data[ran][i]}'
                            else:
                                if str(type(delete_data[ran][i])) == "<class 'str'>":
                                    sql = sql + f'"{delete_data[ran][i]}",'
                                else:
                                    sql = sql + f'{delete_data[ran][i]},'
                        sql = sql + ")" 
                    else:
                        sql = sql + f'{delete_data[ran][0]} = "{delete_data[ran][1]}"'
                else:
                    #sql = sql + f"{delete_data[ran][0]} = {delete_data[ran][1]}"
                    if len(delete_data[ran])-1 >= 2:
                        
                        sql = sql + f"{delete_data[ran][0]} in ("
                        for i in range(len(delete_data[ran])):

                            if len(delete_data[ran])-1 == i:
                                if str(type(delete_data[ran][i])) == "<class 'str'>":
                                    sql = sql + f'"{delete_data[ran][i]}"'
                                else:
                                    sql = sql + f'{delete_data[ran][i]}'
                            else:
                                if str(type(delete_data[ran][i])) == "<class 'str'>":
                                    sql = sql + f'"{delete_data[ran][i]}",'
                                else:
                                    sql = sql + f'{delete_data[ran][i]},'
                        sql = sql + ")" 
                    else:
                        sql = sql + f'{delete_data[ran][0]} = {delete_data[ran][1]}'
                if asksend:
                    if a == 0:
                        print("처리할 쿼리 >> ",len(delete_data[ran]))
                        a +=1
                    while True:
                        print()
                        print("전송 or 취소 : ",sql)
                        send_ask = input("c/s >>>")
                        if send_ask == "s" or send_ask == "S":
                            print("전송됨  :",sql)
                            mysql_delete.execute(sql)
                            self.mysql_new.commit()
                            break
                        elif send_ask == "c" or send_ask == "C":
                            print("ok cancel")
                            break
                        elif send_ask == "exit":
                            return True
                        else:
                            pass
                sql = f"DELETE FROM {table_name} WHERE "
        if data_if == "and_or":
            if asksend:#cancel send
                while True:
                    print(sql)
                    send_ask = input("c/s >>>")
                    if send_ask == "s" or send_ask == "S":
                        print(sql)
                        mysql_delete.execute(sql)
                        self.mysql_new.commit()
                        break
                    elif send_ask == "c" or send_ask == "C":
                        print("ok cancel")
                        break
                    else:
                        pass
            else:
                print(sql)
                mysql_delete.execute(sql)
                self.mysql_new.commit()


    def db_delete(self,db_name):
        mysql_db = self.mysql_new.cursor()
                
        if db_name:
            sql = f"DROP  DATABASE {db_name}"
            #print(sql)
            try:
                mysql_db.execute(sql)
                self.mysql_new.commit()
            except:
                print("not database name")
        else:
            return False
    def table_delete(self,table_name):
        mysql_table = self.mysql_new.cursor()

        if table_name:
            try:
                sql = f"DROP TABLE {table_name}"
                
                mysql_table.execute(sql)
                self.mysql_new.commit()
            except:
                mysql_table.execute("SELECT DATABASE()")

                for i in mysql_table:
                    if i['DATABASE()'] == None:
                        #데이터베이스 접근 안되있음
                        print(not_db)
                    else:
                        print(syntax_insert_sentence)

    def solumn_delete(self,table_name,solunm_name):
        mysql_solumn = self.mysql_new.cursor()

        if table_name and solunm_name:
            sql = f"ALTER TABLE {table_name} DROP {solunm_name}"
            try:
                mysql_solumn.execute(sql)

                self.mysql_new.commit()
            except:
                print("not table name or solunm_name")
    def solumn_select(self,select,table_name,type_double = None):
        mysql_select = self.mysql_new.cursor()
        print(f"SELECT {select} FROM {table_name}")
        mysql_select.execute(f"SELECT {select} FROM {table_name}")
        self.mysql_new.commit()
        if type_double is not None:
            result = [i for i in mysql_select]
            return result
        else:
            return mysql_select

    def table_select(self,table_name,type_double = None):
        mysql_table = self.mysql_new.cursor()
        mysql_table.execute("SHOW TABLES")
        if type_double is not None:
            result = [i for i in mysql_table]
            return result
        else:
            return mysql_table

    def databases(self,type_double= None):
        mysql_db = self.mysql_new.cursor()

        mysql_db.execute("SHOW DATABASES")

        if type_double is not None:
            result = [i for i in mysql_db]
            return result
        else:
            return mysql_db
        

    def file_remove(file_location):
        """
        file_remove() -> 삭제할려는 파일 또는 디렉터리

        file_location = 원하는 파일이나 디렉터리의 위치

        """
        try:
            """import os file_name remove"""
            if os.path.isfile(file_location):
                """if file -> remove"""
                os.remove(file_location)
            else:
                """if file -> dir rmdir"""
                os.rmdir(file_location)

            return True

        except FileNotFoundError:
            #잘못된 파일 또는 잘못된 위치
            print(syntax_not_Filename)
            

