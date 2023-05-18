import os

if not os.path.exists("config.yaml"):
    print("config.yaml not found")
    quit()
    
else:
    print("config.yaml found")