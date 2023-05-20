# run the program
import os

# check if config.yaml exists
if not os.path.exists("config.yaml"):
    print("config.yaml not found")
    quit()
    
# check if output.csv exists
if os.path.exists("output.csv"):
    # delete output.csv
    os.remove("output.csv")

# check if Even8/main.py exists
if not os.path.exists("Even8/main.py"):
    print("Even8/main.py not found")
    quit()
    
os.system("python3 Even8/main.py gateway")
quit()