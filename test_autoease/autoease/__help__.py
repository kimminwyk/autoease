"""
auto.py 사용법

db_auto(mysql 호스트,mysql 네임,mysql 패스워드,mysql db 네임,type_decision -> dict or tuple)
-> mysql 연결

mysql_query(sql 쿼리)
-> mysql 쿼리 전송

connect_db(연결할 mysql db 네임)
->해당 db에 연결

special_characters(테이블 네임,검사에 제외시킬 특수문자,특수문자 나타내기)
->해당 테이블네임에있는 모든 컬럼의 데이터들을 특수문자가있는지 검사 (단 검사에 제외시킬 특수문자는 삭제)

table_insert(생성할 table 네임,생성할 컬럼 이름과 컬럼 속성)
->지정한 테이블과 컬럼 생성

db_insert(생성할 db 이름)
->해당 db로 생성

solumn_insert(컬럼생성할 테이블네임 , 컬럼 네임,컬럼 값)
->원하는 테이블의 컬럼에 값 추가

column_update(테이블 네임,변경할 컬럼이름와 컬럼값,조건을걸 컬럼이름과 컬럼값)
->원하는 조건으로 되는 행의 데이터를 업데이트(변경)

"""