import os
import shutil 
import logging
logging.debug('----------------------------------------------------------------->')
path= r'C:\MyEclipse 2017 CI\Workspaces\chinauip.mobile\WebRoot\WEB-INF\classes'  
os.path.exists(path) 
shutil.rmtree(path)
logging.debug('----------------------------------------------------------------->')
path1= r'C:\MyEclipse 2017 CI\Workspaces\chinauip.cfc5\WebRoot\WEB-INF\classes'
os.path.exists(path1)
shutil.rmtree(path1)
logging.debug('----------------------------------------------------------------->')
path2= r'C:\MyEclipse 2017 CI\Workspaces\chinauip.sso\WebRoot\WEB-INF\classes'
os.path.exists(path2)
shutil.rmtree(path2)
logging.debug('----------------------------------------------------------------->')
path_file =r'D:\Apache_Tomcat\apache-tomcat-6.0.48\work'
os.path.exists(path_file)
shutil.rmtree(path_file)

logging.debug('----------------------------------------------------------------->')