### install requirements:  
docker-desktop  
sqlcmd(Go)  
SQL Server management studio(SSMS-Setup-ENU.exe)   
msodbcsql.msi

### run container  
sqlcmd create mssql --tag 2022-latest --hostname localhost --name sql_oim --port 1433 --accept-eula    
sudo sqlcmd config view --raw   
sudo docker exec -t sql_oim cat /var/opt/mssql/log/errorlog | grep connection    
sudo sqlcmd config connection-strings  

### test access to container  
export 'SQLCMDPASSWORD=fromConnectionStringsPassword'  
sqlcmd -S 127.0.0.1,1433 -U root -d master  (or db_name)  
sudo docker exec -it sql1 "bash"  

### import DB from *.mdf files  
chmod 666 file  
sudo docker cp ComponentDB.mdf sqltest:/var/opt/mssql/data/ComponentDB.mdf  
sudo docker cp ComponentDB_log.ldf sqltest:/var/opt/mssql/data/ComponentDB_log.ldf  
CREATE DATABASE ComponentDB ON (FILENAME='/var/opt/mssql/input_data/ComponentDB.mdf')    
LOG ON (FILENAME='/var/opt/mssql/input_data/ComponentDB_log.ldf') FOR ATTACH;  

### fix credentials in db_connect.py  
get actual info from connection-strings  

