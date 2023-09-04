import smbclient
import os

#Create connection smb
class SmbConnection:
    def __init__(self, server=os.environ['SERVER'] , workgroup=os.environ['WORKGROUP'] , user=os.environ['SERVERUSER'] , password=os.environ['SERVERPASSWORD']) -> None:
        
        self.server = os.environ['SERVER']
        self.user = os.environ['SERVERUSER'] 
        self.password = os.environ['SERVERPASSWORD'] 
        self.workgroup = os.environ['WORKGROUP'] 
        self.smb = smbclient
        
    def _get_connection_parameters(self):
        
        return self._server, self._user , self._password
        
    def start_connection(self):
        
        return self.smb.register_session(self._get_connection_parameters)