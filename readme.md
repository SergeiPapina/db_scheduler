
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
