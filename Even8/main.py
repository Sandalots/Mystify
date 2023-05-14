from nodes import node, gateway # import node and gateway modules from nodes directory to use their classes
from interfaces import gui # import gui module from interfaces directory to use the gui interface
from web import webserver # import webserver module from web directory to use the webserver interface
from multiprocessing import Process # import Process class from multiprocessing module to run multiple calls in parallel, e.g. make gui and webserver run in parallel
import sys, os # import sys and os modules to use command line arguments and file deletion

# Declare the nodes we are going to use
node_gateway = gateway.Gateway(0, "nodeGateway")
node1 = node.Node(1, "node1") 
node2 = node.Node(2, "node2")
node3 = node.Node(3, "node3")

# Declare list of nodes assigned above
nodes = [node_gateway, node1, node2, node3]

def main():
    # call node_gateway's process_next function on each declared node object 
    return node_gateway.process_next(node_gateway,node1, node2, node3)

# Test encyption function
def testEncryption():
    # print encrypted password using encrypt module on a test string
    print("Encrypted password is: " + node_gateway.encrypt_passwd("testpasswordstring"))

# function for testing mqtt broker
def testBroker(): 
    # import the test source file to test each node
    from testing import test_broker_connection
    # for each node in nodes
    for node in nodes:
        # test the node with the nodes client id
        test_broker_connection.test_a_node(node.client_id)
    
# Method to ask user if they would like to encrypt a password or not
def password_invokation():
    # try to run an infinite loop to ask user for a password to encrypt
    try:
        # loop forever
        while True:
            # ask user for a password to encrypt
            password = input("Please enter a password you would like to encrypt: ctrl-C to exit to interfaces: ")
            # check if password is empty
            while password == "":
                # if password is empty, ask user to try again
                print("Password cannot be empty, please try again")
                # repeat input prompt
                password = input("Please enter a password you would like to encrypt: ctrl-C to exit to interfaces: ")
                
            # print the encrypted password output
            print(node_gateway.encrypt_passwd(password))
            # write the encrypted password to the output file
            node.write_password(node_gateway.encrypt_passwd(password))
            
    # if the user presses ctrl+c to exit the program
    except KeyboardInterrupt:
        # break out of the loop and continue to the interfaces
        pass

# for webserver requesting, a webserver optimised version of the above function
def small_password_encrypt(recieved_input):
    # write the encrypted password to the output file
    node.write_password(node_gateway.encrypt_passwd(recieved_input))
    # return the encrypted password
    return node_gateway.encrypt_passwd(recieved_input)
    

# function to run both the main function, gui and websever in parallel, takes in any number of given functions
def run_parallel(*functions):
    # create empty list for processes, to be processed in parallel 
    processes = []
    
    # for each function in functions
    for function in functions:
        # create new process object
        proc = Process(target=function)
        # start the process
        proc.start()
        # append the process to processes list
        processes.append(proc)
        
    # for each process in processes
    for proc in processes:
        # join the process
        proc.join()
        
# run the main function
if __name__ == "__main__": 
    # check if there is no command line argument
    if len(sys.argv) == 1:
         # print error message
        print("Please enter a command line argument, either gateway or node.")
    
    # Now check if the argument passed is either gateway or node.
    else:
    # check if the first argument is gateway
        if sys.argv[1] == "gateway":
            # ask user if they would like to encrypt a password or not
            password_invokation()
            # run main, gui and webserver in parallel so all interfaces are available to the end user
            run_parallel(main, gui.startGUI, webserver.host, testEncryption) 
            # This will run all the interfaces, terminal, gui and web as well as test the encyption function, to be removed in the future when encryption is implemented
   
         # check if the first argument is node
        elif sys.argv[1] == "node":
            # create new node object with the node number and client id passed in the command line
            parsed_node = node.Node(1, 'node1')
            # import the test source file to test each node
            from testing import test_broker_connection
            # test the node with the nodes client id
            test_broker_connection.test_a_node(parsed_node.clientID)
            # call the node mqtt function, that will generate a fragment of the seed, push and close.
            # return a standard out of it's success or failure

            # success output message
            print("This Node has successfully generated a fragment of the seed and pushed it to the broker.")
            # further instructions to user
        
        # check for clear argument
        elif sys.argv[1] == "clear":
            # check if ../output.csv exists using os
            if os.path.exists("output.csv"):
                # delete the file
                os.remove("output.csv")
                # print success message
                print("Successfully deleted output.csv")
            else:
                # print error message
                print("The file does not exist or is yet to be created.")
                sys.exit()