import os

if not os.path.exists("config.yaml"):
    print("config.yaml not found")
    quit()
    
else:
    print("config.yaml found")
    
# read config.yaml
with open("config.yaml") as f:
    config = f.read()
    
    # if config.yaml profile is default 
    if "profile: default" in config:
        print("profile is " + "default")
        os.system("python3 Even8/main.py clear")