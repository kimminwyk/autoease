# autoease 1.1

pymysql 모듈을 이용해 조금 더 간략하고 조금더 쉽게 사용할수있게 만들어보았습니다.

<br>

+ ##### MySQL Connect
 
    ```py
    db_auto(mysql_host = "host", mysql_port = "port", mysql_user = "user", mysql_passwd = "password", type_decision = "dict")

    ex) db_auto(mysql_host = "localhost",mysql_user = "root",mysql_passwd = "toor", type_decision = "dict")
    ```
<br>

+ ##### MySQL Command execute
    ```py
    mysql_query("SQL Command")

    ex) mysql_query("select * from member")
    ```

<br>

+ ##### MySQL DATABASE Connect

    ```py
    connect_db(db_name)

    ex) connect_db("test")
    ```

<br>

+ ##### MySQL TABLE CREATE
  
    ```py
    table_insert(table_name,column_name = [])
    
    ex) table_insert("testtable", [["id","varchar(100)","NOT NULL"],["pw","varchar(100)","NOT NULL"]])
    ```

<br>

+ ##### MySQL TABLE DATA INSERT

    ```py
    solumn_insert(table_name,solunm_name = [],solumn_value = [])
    
    ex) solumn_insert("testtable",['id','pw'], ["guest","password"])
    ```

<br>

+ ##### MySQL DATA Update

    ```py
    column_update(table_name,column_return = [],if_column = [])

    ex) column_update("testtable", ["id","testid"], ["id": "id"])
    ```

<br>

+ ##### MySQL DATA DELETE

    ```py
    column_delect(table_name,delete_data = [],data_if=None,asksend = None)

    ex ) column_delete("testtable",["columnname","testdata"],"and_or","")
    ```

<br> 

+ ##### MySQL TABLE In Column DELETE

    ```py
    solumn_delete(table_name,solunm_name)

    ex) solumn_delete("testtable","columnonename")
    ```

<br> 

+ ##### MySQL database 조회

    ```py
    databases(type_double)

    ex) databases("")
    ```

<br> 

+ ##### MySQL TABLE 조회
    
    ```py
    table_select(type_double)

    ex) table_select("")
    ```

<br> 

+ ##### MySQL TABLE data 조회

    ```py
    solumn_select(select , table_name , type_double)

    ex) solumn_select("*", "testtable","")
    ```
