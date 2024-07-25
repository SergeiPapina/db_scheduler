
### first install postgresql
sudo apt install postgresql
### add user with password
sudo -u postgres psql template1
ALTER USER postgres with encrypted password 'your_password';
\q
### restart postgresql.service
sudo systemctl restart postgresql.service
### install client
sudo apt install postgresql-client

### configure peer authentication
sudo vim /etc/postgresql/16/main/pg_hba.conf  
edit peer line  
TYPE  DATABASE      USER        ADDRESS       METHOD  
local   all           all                       peer map=foransible

sudo vim /etc/postgresql/16/main/pg_ident.conf  
MAPNAME       SYSTEM-USERNAME         PG-USERNAME  
foransible      ansible                 postgres  
foransible      postgres                postgres

### connect to postgresql
psql -U postgres  
then use   
\l  
\c db_name;  
\dt  
\q  

### now application ready to use
set correct username and password in db_connect.py  
run  
python3 db_proc.py




## better way to use docker image throw sqlcmd
/////////////////////////////////////////////////////////////////////////////////////  
sudo sqlcmd create mssql --tag 2022-latest --hostname sql_oim --name sql_oim --port 1433 --accept-eula  
sudo sqlcmd config view --raw  
sudo docker exec -t sql_oim cat /var/opt/mssql/log/errorlog | grep connection  
sudo sqlcmd config connection-strings
export 'SQLCMDPASSWORD=9IkX1u#O%A$0z9P1f$Q3PGG0@LM2$WuDjY@SLSM54Z**G$w826'  
sqlcmd -S 127.0.0.1,1433 -U root -d master  (or db_name)   

## sudo sqlcmd config connection-strings
install ODBC driver with ./odbc_install.sh

## unfortunately bad way
sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<compDIC54#@>" \  
-p 1433:1433 --name sql1 --hostname sql1    -d    mcr.microsoft.com/mssql/server:2022-latest  
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P compDIC54#@  
sudo docker start ID|nameContainer       for example sql1  
sudo docker exec -it sql1 "bash"  
sudo docker exec -t sql1 cat /var/opt/mssql/log/errorlog | grep connection  

## import DB from *.mdf files
chmod 666 file
sudo docker cp ComponentDB.mdf sqltest:/var/opt/mssql/data/ComponentDB.mdf  
sudo docker cp ComponentDB_log.ldf sqltest:/var/opt/mssql/data/ComponentDB_log.ldf  
CREATE DATABASE ComponentDB ON (FILENAME='/var/opt/mssql/input_data/ComponentDB.mdf')  
LOG ON (FILENAME='/var/opt/mssql/input_data/ComponentDB_log.ldf') FOR ATTACH;

## some SQL queries
USE 'dbname'
SELECT * FROM INFORMATION_SCHEMA.TABLES  
GO  
SELECT * FROM authors;    
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='Resistors';  

SELECT COLUMN_NAME AS ColumnName, DATA_TYPE AS DataType, CHARACTER_MAXIMUM_LENGTH AS CharacterLength
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Manufacturers'

SELECT 
    sc.name AS [Columne Name], 
    st1.name AS [User Type],
    st2.name AS [Base Type]
FROM dbo.syscolumns sc
    INNER JOIN dbo.systypes st1 ON st1.xusertype = sc.xusertype
    INNER JOIN dbo.systypes st2 ON st2.xusertype = sc.xtype
-- STEP TWO: Change OurTableName to the table name
WHERE sc.id = OBJECT_ID('Resistors')
ORDER BY sc.colid;

SELECT 
    sc.name AS [Columne Name], 
    st1.name AS [User Type],
    st2.name AS [Base Type]
FROM dbo.syscolumns sc
    INNER JOIN dbo.systypes st1 ON st1.xusertype = sc.xusertype
    INNER JOIN dbo.systypes st2 ON st2.xusertype = sc.xtype
-- STEP TWO: Change OurTableName to the table name
WHERE sc.id = OBJECT_ID('Manufacturers')
ORDER BY sc.colid;

exec sp_help 'Manufacturers';
EXEC sp_fkeys 'TableName'
