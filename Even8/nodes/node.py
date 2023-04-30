import random # import random module
import paho.mqtt.client as mqtt # import mqtt client from paho mqtt module to use mqtt protocol
import time # import time module for processing time to add to seed curation

# Create the Node class that describes a node 
class Node(): 
    # Constructor, takes the id of a node as a parameter
    def __init__(self, id, clientID): 
        self.id = id # Set id to given param id
        self.clientID = clientID # Set clientID to given param clientID
        self.location = "RGU" # Set location to RGU, change if location changes
        self.required = True # Set required to True, change if node is not required or optional
        self.project = "Mystify" # Set project to Mystify, change if project changes
        self.owner = "Even8" # Set owner to Even8, change if owner changes
        self.user_name = "s.macdonald41@rgu.ac.uk" # Set user_name to, change if user_name changes
        self.password = "Uy21GUrz-3RaEQE3o" # Set password to, change if password changes
    
    # Get id of this sensor    
    def get_id(self):
        # Return sensor id
        return self._id 
    
    # Get reading of this sensor, aka get sensor data
    def get_reading(self):
        # import the sense-hat module for programmatically getting the sensor data for the sense-hat
        import sense_hat 

        # Sensor data from the Sense HAT
        sense = Sensehat() # create sense-hat object for getting the sensor data for use in each node
        temperature = sense.get_temperature() # get temperature of node
        humidity = sense.get_humidity() # get humidity of node
        pressure = sense.get_pressure() # get pressure of node
        orientation = sense.get_orientation() # get orientation of node
        acceleration = sense.get_accelerometer_raw() # get acceleration of node
        magnetometer = sense.get_compass() # get magnetometer of node
        gyroscope = sense.get_gyroscope_raw() # get gyroscope of node
    
        # create empty list for raw data storage
        raw_data = []
        # append all data to raw_data list
        raw_data.append(temperature, humidity, pressure, orientation, acceleration, magnetometer, gyroscope)
    
        # return raw_data list to node
        return raw_data 
    
    # Method to calibrate sensor node
    def calibrate(self): 
        # return calibration message
        return "Calibrating Node" + self._id 
        
    # Method to observe a node sensor    
    def observe(self): 
        # return observation message
        return "Observing Node" + self._id 
    
    # Method to process data from the sensors
    def process(self): 
        #data = process_data(get_reading()) # get data from the sensors and process it
        # permute the data and return it
        # return random integer between 0 and 999999
        return random.randint(0, 999999)
    
    # Method to process data from the sensors in serial
    def process_data(raw_input): 
        # set total to 0
        total = 0
        
        # for each data in raw_input
        for data in raw_input:
            # do something with the data
            # add data to total
            total += data
            
        # return total
        return total
    
    # Method to complete the currents node seed valuation contribution
    def seed_step_formulation():
        # combine process and process_data methods
        # more advanced computations
        pass # empty


    # MQTT relations
    def on_message(client, userdata, message): # function to send message to node
        # connect to broker
        # subscribe to seedData topic
        # publish seedfragmentData to topic
        # close connection
        pass # empty
    
    # method to invoke after connection to broker
    def on_connect(self, client, userdata, flags, rc):
        # if connection is successful
        if(rc == 0):
            # subscribe to seedData topic
            client.subscribe("seedData")
        else:
            # print connection failed message
            print(self.clientID + " connection failed")