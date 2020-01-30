# Oracle Machine Learning for Python Client on Windows

Below are the steps to install OML4Py client for Windows 64-bit 

### Pre Requisites

  * Oracle InstaClient
  * Python 3.7.3 +
  * Perl 5.0 +

## Installation steps 

Make sure you have a Python and Perl on your machine before procceding with installtion 

### Step 1 : Oracle InstaClient 

  * Download the Oracle InstaClient basic/basiclite for Windows 64-bit
  
        Assuming you downloaded and unzipped the content to C:\Oracle\Instaclient_19_5
        add this directory to the PATH variable in Environment Variables
        
### Step 2 : Python Packages 

  * Install python packages which are pre requisites as per documentation
  
         pip install numpy pandas scipy matplotlib cx_Oracle scikit-learn pyreadline
 
### Step 3 : OML4Py Client Installtion

  * Download and unzip the OML4Py windows client package to a folder 
      
         Assuming your folder to be D:\Programs\OML4Py
         
  * From command line navigate to the path where we have the unzipped client software and run the below code. 
  This will install the oml package in default site-packages folder of Python
  
        perl -Iclient client/client.pl 
  
  * If you want to install in a specific folder use below code. As an additional step we will have to add a PYTHONPATH with this location for python to pickup installed packages here.
  
        perl -Iclient client/client.pl --target C:\Programs\oml4py
        
      ![alt text](https://github.com/prampradeep/oml4py/blob/master/images/oml4pyclient.png)
        
 ### Step 4 : Testing OML4Py Install
 
  * Open Python from command line and type below commands. If this runs fine then oml is installed properly.
        
         import oml
         om.__path__
    ![alt text](https://github.com/prampradeep/oml4py/blob/master/images/oml4pyclienttest.png)
