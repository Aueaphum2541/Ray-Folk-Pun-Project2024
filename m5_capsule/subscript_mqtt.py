import paho.mqtt.client as mqtt

# Global variable to store the message
received_message = ""

# Callback function when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to the topic upon successful connection
    client.subscribe("thammasat/chakapat/sensor")

# Callback function when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    global received_message  # Access the global variable
    received_message = msg.payload.decode()  # Assign the received message to the variable
    print("Received message: "+received_message)

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Set up callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("broker.hivemq.com", 1883, 60)  # Connect with default MQTT version

# Start the network loop to handle incoming messages
client.loop_start()
