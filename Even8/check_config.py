import os

if not os.path.exists("config.yaml"):
    print("config.yaml not found")
    quit()
    
else:
    print("config.yaml found")
    
# read config.yaml
with open("config.yaml") as f:
    config = f.read()
    
    # get profile name
    profile = config.split("profile: ")[1].split("\n")[0]
    # if config.yaml profile is default 
    if "profile: default" in config:
        print("profile is " + profile)
        os.system("python3 Even8/main.py clear")
        
    create = input("Do you want to create a new profile? (y/n): ")
    if create == "y":
        # change profile name in config.yaml
        new_profile = input("Enter new profile name: ")
        config = config.replace(profile, new_profile)
        with open("config.yaml", "w") as f:
            f.write(config)
        print("profile changed to " + new_profile)
        
    if profile != "default":
        print("profile is " + profile)
        os.system("python3 Even8/main.py clear")
    
    f.close()