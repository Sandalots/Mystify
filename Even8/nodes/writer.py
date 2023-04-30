import csv # import csv module to write in csv file, outputs in root project output.csv 

# define write function, note that a default value is set for b to avoid passing errors
def write(b=None): 
    # open file in write mode
    with open('output.csv', 'a', newline='') as file: 
        # create writer object for file declared above
        writer = csv.writer(file) 
        # writer.writerow(["id", "output"]) # write header row
        # write test data row
        writer.writerow(["Seed", b])
    # close file
    file.close()
    
# writer method for dealing with writing passwords, instead of seeds
def write_password(p=None):
    # open output.csv in append mode
    with open('output.csv', 'a', newline='') as file:
        # create writer object for file declared above
        writer = csv.writer(file)
        # write password to file
        writer.writerow(["Password", p])
    # close file
    file.close()