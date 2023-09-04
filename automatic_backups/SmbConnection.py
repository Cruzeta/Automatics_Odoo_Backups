import smbclient
import os

class SmbConnection:
    def __init__(self, server=os.environ['SERVER'] , workgroup=os.environ['WORKGROUP'] , user=os.environ['SERVERUSER'] , password=os.environ['SERVERPASSWORD']) -> None:
        
        self.user = os.environ['SERVERUSER'] 
        self.password = os.environ['SERVERPASSWORD'] 
        self.workgroup = os.environ['WORKGROUP'] 
        self.smb = smbclient
        
    def start_connection(self):
        
        self.smb.register_session()