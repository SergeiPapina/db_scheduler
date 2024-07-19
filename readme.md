
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

## way don't work
sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<compDIC54#@>" \  
-p 1433:1433 --name sql1 --hostname sql1    -d    mcr.microsoft.com/mssql/server:2022-latest  
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P compDIC54#@  
sudo docker start ID|nameContainer       for example sql1  
sudo docker exec -it sql1 "bash"  
sudo docker exec -t sql1 cat /var/opt/mssql/log/errorlog | grep connection  

