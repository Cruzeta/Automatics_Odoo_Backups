import os

def load_env(filename):

    # Load configuration from file and store as dictionary
    with open(filename, 'r') as f:
        for line in f.readlines():
            key, value = line.strip().split('=')
            os.environ[key]=value
