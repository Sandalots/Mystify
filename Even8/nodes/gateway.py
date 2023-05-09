from nodes.node import Node # import Node class from node module from within the nodes directory
import hashlib # for hashing passwords
import datetime # for getting time for encryption

# Describe a Gateway class that inherits from Node class that controls the other nodes
class Gateway(Node):
    # MQTT on connection method
    def on_connect(): # or on_message
        # connect to broker
        # subscribe to seedData topic
        # read seedData from topic
        # get seed fragments from nodes
        # close connection
        # compose seed
        return None
    
    # Method to diagnose the gateway
    def diagnostics():
        # return simple diagnostics message
        return "Gateway is online"
    
    # Method to process data from given nodes
    def process_next(self, node_gateway, node1, node2, node3):
        # Declare variables
        # create empty list for future inputs storage
        input_chain = []
        
        # create empty variable for a future seed computation, initial type is None
        seed = None 
        
        # Add nodes processation to the input_chain
        input_chain.append(node_gateway.process())
        input_chain.append(node1.process())
        input_chain.append(node2.process())
        input_chain.append(node3.process())
        
        # Compose seed from the input_chain
        seed = input_chain[0] + input_chain[1] + input_chain[2] + input_chain[3]
        
        # print seed to user
        print(seed)
        # write seed to output.csv file
        self.write(seed) 
        
        # return seed
        return seed 
    
    # Method for encrypting given passwords
    def encrypt_passwd(self, passwd):
        import main # include main for seed
        
        # Get seed from main source file
        seed = main.main()
        
        # Get time for encryption
        encryption_time_int = int(datetime.datetime.now().strftime("%H%M%S")) 
    
        # Advanced encryption method needed.
        # Below needs to be removed and modified with advanced encryption method
        passwd_encrypted = passwd + str(seed) + str(encryption_time_int)
        passwd_encrypted = hashlib.sha256(passwd_encrypted.encode()).hexdigest()
        
        # return the encrypted password to the caller
        return passwd_encrypted