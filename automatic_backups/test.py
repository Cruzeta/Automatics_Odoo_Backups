s={}

with open('.env', 'r') as f:
    for line in f.readlines():
        key, value = line.strip().split('=')
        s[key]= value
        
print(s)
