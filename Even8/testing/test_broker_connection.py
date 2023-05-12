import paho.mqtt.client as mqttClient # import mqtt client from paho mqtt module to use mqtt protocol
import time # import time module

# Broker connect and client details
host          = "node02.myqtthub.com"
port          = 1883
client_id     = "nodeGateway"
user_name     = "s.macdonald41@rgu.ac.uk"
password      = "Uy21GUrz-3RaEQE3o"

# Define what happens when client gets a connect
def on_connect(client, userdata, flags, rc):
    # if response code is 0, connection is successful
    if rc == 0:
        # output connection message to user
        print("Connected to broker at " + host + " with client id " + client_id)
        # create global var for connected
        global Connected     
        # set connected to true       
        Connected = True
    # If connection failed, print error message
    else:
        print("Connection failed")

# Set connected initially to false
Connected = False

# Create a client
client = mqttClient.Client(client_id)         
client.username_pw_set(user_name, password=password)
client.on_connect= on_connect
client.connect(host, port=port)   

# Start the client loop
client.loop_start()

# While the client is not connected, wait
while Connected != True:
    # Wait for 0.1 seconds
    time.sleep(0.1)
    
# While the client is connected, attempt to publish a message
try:
    # While the client is connected
    while True:
        # Get value from user
        value = input('Enter the message:')
        # Publish the value to the seedData topic
        client.publish("seedData", value)
        client.disconnect()
        client.loop_stop()
 
# If the users keyboard intterupts close the client connenction and stop the client loop       
except KeyboardInterrupt:
    # disconnect from the client
    client.disconnect()
    # stop the client loop
    client.loop_stop()
    
# Function for testing each node
def test_a_node(clientID):
    # Set connected initially to false
    Connected = False
    
    # Create a client and configure it
    client = mqttClient.Client(clientID)
    client.username_pw_set(user_name, password=password)
    client.on_connect= on_connect
    client.connect(host, port=port)
    
    # Start the client's loop
    client.loop_start()
    
    # If the client is not connected, wait
    if Connected != True:
        # Wait for 0.1 seconds
        time.sleep(0.1)
        # Tell the user that the client is trying to connect
        print("Trying to connect to broker at " + host + " with client id " + client_id)
    # If the client connects
    else:
        # Make a test value 
        value = '3219'
        # Publish the value to the seedData topic
        client.publish("seedData", value)
        
        # Disconnect the client and stop the client's loop
        client.disconnect()
        client.loop_stop()
        # Tell the user that the client has disconnected, and that the test has been completed with the value returned
        print("published to seedData topic with value " + value)
            