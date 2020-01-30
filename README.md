# oml4py

Below are the steps to install OML4Py on a Oracle Database 18c 

### Software Pre Requisites
  * Oracle Linux 7.7
  * Oracle Database 18c, 19c 
  * Python 3.7.3 +
  * Perl 

### Necessary DB options
  * Atleast One PDB is needed. We can find the available PDB's in the database using the below query. Connect as SYS user to run the query
  
        select NAME from v$pdbs where OPEN_MODE = 'READ WRITE';
      
  * Advanced Analytics option enabled. The below query should result **TRUE**
        
        select * from v$option where PARAMETER like 'Advanced Analytics';
 
 ## Installtion Steps
 
 ### Step 1 : Installing OS packages
 
  * For the Server to be installed we need some system packages to be installed like c compiler etc. Below command will install all the necessary packages at once
 
        sudo yum install gcc libffi libffi-devel zlib-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel xz-devel zlib-devel bzip2-devel perl-Env -y --skip-broken
        
  * This is optional
   
        sudo yum update -y
        
  * switch to oracle user
  
        sudo su oracle
        cd $HOME

 ### Step 2 : Python Installtion
 
  * Installtion of Python is mandatory for the server installtion. Prefreed version is 3.7.3 and above.
  
        wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
        tar -xvf Python-3.7.3.tgz
        /home/oracle/Python-3.7.3
        
  * Configure and Install python
  
        ./configure --enable-shared --prefix=/home/oracle/Python-3.7.3
        make clean; make
        make altinstall
        
  * Set paths for Python and Lib
  
        export PYTHONHOME=/home/oracle/Python-3.7.3
        export PATH=$PATH:$PYTHONHOME/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PYTHONHOME/lib
        
  * Soft links for Python, PIP
  
        cd /home/oracle/Python-3.7.3/bin
        ln -s python3.7 python3
        ln -s pip3.7 pip3
    
  * Install Python packages 
        
        pip3 install numpy pandas scipy matplotlib cx_Oracle scikit-learn
        
  
### Step 3 : OML4Py Installtion 

OML4Py Server setup file to be downloaded from Oracle site before we proceed with installtion.

  * Create Folder and Move setup files
  
        mkdir $ORACLE_HOME/oml4py
        cd $ORACLE_HOME/oml4py
        # My Server Setup is available in /tmp 
        cp /tmp/oml4py-server-linux-x86_64-1.0.zip $ORACLE_HOME/oml4py
        unzip oml4py-server-linux-x86_64-1.0.zip
  
  * Installtion of OML4Py
  
        perl -Iserver server/server.pl
       
       When prompted for PDB enter your PDB name, Tablespace PERMANENT tablespace USERS, TEMPORARY table space TEMP
       
         Procced ? [yes] yes 
        
    
      ![alt text](https://github.com/prampradeep/oml4py/blob/master/oml4py.png)
      
 ### Step 4 : Create a PYQUSER 
 
  * Connect to PDB as SYS user 
  
        #IF CDB service name is 
        OML4PYDB_fra2sp.sub02220907041.analyticsvcn.oraclevcn.com
        #And your PDB name is PDB then PDB service name will be 
        PDB.sub02220907041.analyticsvcn.oraclevcn.com
  
  * Create a user pyquser 
  
        create user pyquser identified by WelCome#123#
        default tablespace USERS
        temporary tablespace TEMP 
        quota unlimited on USERS;

        begin
          execute immediate 
            'grant create session, create table, create view, ' ||
            'create procedure, create mining model to pyquser';
          commit;
          IF lower('pyqadmin') = 'pyqadmin' THEN
            execute immediate 'grant PYQADMIN to pyquser';
            commit;
          END IF;
        end;
        /
  
  * Grant permissions for pyquser 
  
        GRANT CREATE SESSION, CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE MINING MODEL to pyquser;
        GRANT EXECUTE ON CTXSYS.CTX_DDL to pyquser; 
        GRANT PYQADMIN to pyquser;

  * Connect as pyquser user run below query
  
        SELECT * FROM sys.pyq_config;
       
       ![alt text](https://github.com/prampradeep/oml4py/blob/master/pyquser.png)
       
       
        
        





 
 
