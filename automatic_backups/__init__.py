import requests
import datetime
import os
from config import load_env
import smbprotocol.connection 

load_env('.env')

# Construct the data payload for the HTTP request
data = {
    'master_pwd': os.environ['PASSWORD'] , 'name':os.environ['DBNAME'], 'backup_format':os.environ['FILE_FORMAT']
    }

# Get the current date and time
day = datetime.datetime.now()

# Construct the filename for the backup file
filename = day.strftime("backup_%d_%m_%y.zip")

# Send the HTTP request to the server
response = requests.post(os.environ['URL'], data = data)

if response.status_code == 200:
    # If the response status code is 200 OK, save the backup file to disk     
    file_path=os.environ['FILE_PATH'] + filename
    with open(file_path , 'wb') as f:
        f.write(response.content)
    
# Print the URL and response status code for debugging purposes
print(os.environ['URL'])
print(response.status_code)
                        