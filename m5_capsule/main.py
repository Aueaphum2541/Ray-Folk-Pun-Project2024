# GUI Lib
from PyQt5 import QtWidgets
from application import Ui_Application
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QMessageBox
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
import numpy as np

# MQTT Lib
import paho.mqtt.client as mqtt

# HTTP Lib
import requests

# Google Drive Lib
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json

# OS Lib
import os

raw_mqtt_message = "contain raw data"
# example topic: thammasat/chakapat/sensor
# example data: 1000, 0.25, 0.5, 0.75, 1, 1.25, 1.5
raw_data = {"timestamp":[], "accel_x":[], "accel_y":[], "accel_z":[], "gyro_x":[], "gyro_y":[], "gyro_z":[]}
processed_data = {"distance":[], "velocity":[]}
loaded_data = {"timestamp":[], "accel_x":[], "accel_y":[], "accel_z":[], "gyro_x":[], "gyro_y":[], "gyro_z":[], "distance":[], "velocity":[]}

# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

cumulative_dist = 0

class MainWindow(QtWidgets.QMainWindow, Ui_Application):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1400, 1200)
        self.setupUi(self)
        self.setFont(QtGui.QFont("Cordia New", 14))

        # set default tab
        self.menu_tab.setCurrentIndex(0)

        # set linked function
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset_graph)

        # set visible
        self.reset_button.setVisible(False)
        self.stop_button.setDisabled(True)
        self.send_to_line_button.setVisible(False)

        # set check box linked function
        self.check_box_show_graph.setChecked(True)
        self.check_box_show_graph.stateChanged.connect(lambda: self.show_graph(logic=self.check_box_show_graph.isChecked()))
        self.raw_data_option.setChecked(True)
        self.raw_data_option.stateChanged.connect(lambda: self.show_graph_2(logic=self.raw_data_option.isChecked()))
        self.processed_data_option.setChecked(True)
        self.processed_data_option.stateChanged.connect(lambda: self.show_graph_3(logic=self.processed_data_option.isChecked()))
        self.show_result_option.setChecked(True)
        self.show_result_option.stateChanged.connect(lambda: self.show_result(logic=self.show_result_option.isChecked()))

        # load data file
        self.load_button.clicked.connect(self.load_data)

        # setup graph
        # accel X
        self.figure_raw_ax = Figure()
        self.canvas_raw_ax = FigureCanvas(self.figure_raw_ax)
        self.graph_ax_raw = QtWidgets.QVBoxLayout(self.graph_ax)
        self.graph_ax_raw.addWidget(self.canvas_raw_ax)
        # accel y
        self.figure_raw_ay = Figure()
        self.canvas_raw_ay = FigureCanvas(self.figure_raw_ay)
        self.graph_ay_raw = QtWidgets.QVBoxLayout(self.graph_ay)
        self.graph_ay_raw.addWidget(self.canvas_raw_ay)
        # accel z
        self.figure_raw_az = Figure()
        self.canvas_raw_az = FigureCanvas(self.figure_raw_az)
        self.graph_az_raw = QtWidgets.QVBoxLayout(self.graph_az)
        self.graph_az_raw.addWidget(self.canvas_raw_az)
        # gyro x
        self.figure_raw_gx = Figure()
        self.canvas_raw_gx = FigureCanvas(self.figure_raw_gx)
        self.graph_gx_raw = QtWidgets.QVBoxLayout(self.graph_gx)
        self.graph_gx_raw.addWidget(self.canvas_raw_gx)
        # gyro y
        self.figure_raw_gy = Figure()
        self.canvas_raw_gy = FigureCanvas(self.figure_raw_gy)
        self.graph_gy_raw = QtWidgets.QVBoxLayout(self.graph_gy)
        self.graph_gy_raw.addWidget(self.canvas_raw_gy)
        # gyro z
        self.figure_raw_gz = Figure()
        self.canvas_raw_gz = FigureCanvas(self.figure_raw_gz)
        self.graph_gz_raw = QtWidgets.QVBoxLayout(self.graph_gz)
        self.graph_gz_raw.addWidget(self.canvas_raw_gz)
        # distance
        self.figure_dist = Figure()
        self.canvas_dist = FigureCanvas(self.figure_dist)
        self.graph_dist = QtWidgets.QVBoxLayout(self.graph_dist)
        self.graph_dist.addWidget(self.canvas_dist)
        # velocity
        self.figure_vel = Figure()
        self.canvas_vel = FigureCanvas(self.figure_vel)
        self.graph_vel = QtWidgets.QVBoxLayout(self.graph_vel)
        self.graph_vel.addWidget(self.canvas_vel)

        # setup loaded graph
        # accel X
        self.figure_raw_ax_2 = Figure()
        self.canvas_raw_ax_2 = FigureCanvas(self.figure_raw_ax_2)
        self.graph_ax_raw_2 = QtWidgets.QVBoxLayout(self.graph_ax_2)
        self.graph_ax_raw_2.addWidget(self.canvas_raw_ax_2)
        # accel y
        self.figure_raw_ay_2 = Figure()
        self.canvas_raw_ay_2 = FigureCanvas(self.figure_raw_ay_2)
        self.graph_ay_raw_2 = QtWidgets.QVBoxLayout(self.graph_ay_2)
        self.graph_ay_raw_2.addWidget(self.canvas_raw_ay_2)
        # accel z
        self.figure_raw_az_2 = Figure()
        self.canvas_raw_az_2 = FigureCanvas(self.figure_raw_az_2)
        self.graph_az_raw_2 = QtWidgets.QVBoxLayout(self.graph_az_2)
        self.graph_az_raw_2.addWidget(self.canvas_raw_az_2)
        # gyro x
        self.figure_raw_gx_2 = Figure()
        self.canvas_raw_gx_2 = FigureCanvas(self.figure_raw_gx_2)
        self.graph_gx_raw_2 = QtWidgets.QVBoxLayout(self.graph_gx_2)
        self.graph_gx_raw_2.addWidget(self.canvas_raw_gx_2)
        # gyro y
        self.figure_raw_gy_2 = Figure()
        self.canvas_raw_gy_2 = FigureCanvas(self.figure_raw_gy_2)
        self.graph_gy_raw_2 = QtWidgets.QVBoxLayout(self.graph_gy_2)
        self.graph_gy_raw_2.addWidget(self.canvas_raw_gy_2)
        # gyro z
        self.figure_raw_gz_2 = Figure()
        self.canvas_raw_gz_2 = FigureCanvas(self.figure_raw_gz_2)
        self.graph_gz_raw_2 = QtWidgets.QVBoxLayout(self.graph_gz_2)
        self.graph_gz_raw_2.addWidget(self.canvas_raw_gz_2)
        # distance
        self.figure_dist_2 = Figure()
        self.canvas_dist_2 = FigureCanvas(self.figure_dist_2)
        self.graph_dist_2 = QtWidgets.QVBoxLayout(self.distance_graph)
        self.graph_dist_2.addWidget(self.canvas_dist_2)
        # velocity
        self.figure_vel_2 = Figure()
        self.canvas_vel_2 = FigureCanvas(self.figure_vel_2)
        self.graph_vel_2 = QtWidgets.QVBoxLayout(self.velocity_graph)
        self.graph_vel_2.addWidget(self.canvas_vel_2)

        self.send_to_line_button.clicked.connect(self.send_to_line)

    def start(self):
        self.status_label.setText("Status: On")
        self.start_button.setDisabled(True)
        self.stop_button.setDisabled(False)
        self.reset_button.setVisible(True)
        self.subscribe()
        print("-----Start-----")

    def stop(self):
        self.status_label.setText("Status: Off")
        self.start_button.setDisabled(False)
        self.stop_button.setDisabled(True)
        self.reset_button.setVisible(False)
        self.client.loop_stop()
        
        print("-----Stop-----")
    
    def reset_graph(self):
        global raw_data, processed_data, cumulative_dist
        raw_data = {"timestamp":[], "accel_x":[], "accel_y":[], "accel_z":[], "gyro_x":[], "gyro_y":[], "gyro_z":[]}
        processed_data = {"distance":[], "velocity":[]}
        cumulative_dist = 0
        self.total_dist_label.setText("Total Distance: 0 m")
        self.plot_raw_graph()
        print("-----Reset-----")

    def show_graph(self, logic):
        for i in range(self.raw_data_graph_layout.count()):
            self.raw_data_graph_layout.itemAt(i).widget().setVisible(logic)

    def show_graph_2(self, logic):
        for i in range(self.raw_data_graph_layout_2.count()):
            self.raw_data_graph_layout_2.itemAt(i).widget().setVisible(logic)

    def show_graph_3(self, logic):
        for i in range(self.processed_graph_layout.count()):
            self.processed_graph_layout.itemAt(i).widget().setVisible(logic)

    def show_result(self, logic):
        for i in range(self.result_layout.count()):
            self.result_layout.itemAt(i).widget().setVisible(logic)

    def load_data(self):
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path != "":
            print("File path = ", file_path)
            with open(file_path, 'r') as file:
                # Read the contents of the file
                contents = file.read()

            # Split the contents of the file by newline characters
            text_data = contents.split('\n')
            loaded_timestamp, loaded_accel_x, loaded_accel_y, loaded_accel_z, loaded_gyro_x, loaded_gyro_y, loaded_gyro_z = [],[],[],[],[],[],[]
            
            # append data to list
            for idx_sample in range(len(text_data)):
                temp_sample = text_data[idx_sample].split(', ')
                # Check if the sample has 7 elements (as expected)
                if len(temp_sample) == 7:
                    loaded_timestamp.append(float(temp_sample[0]))
                    loaded_accel_x.append(float(temp_sample[1]))
                    loaded_accel_y.append(float(temp_sample[2]))
                    loaded_accel_z.append(float(temp_sample[3]))
                    loaded_gyro_x.append(float(temp_sample[4]))
                    loaded_gyro_y.append(float(temp_sample[5]))
                    loaded_gyro_z.append(float(temp_sample[6]))
            
            loaded_data["timestamp"] = loaded_timestamp
            loaded_data["accel_x"] = loaded_accel_x
            loaded_data["accel_y"] = loaded_accel_y
            loaded_data["accel_z"] = loaded_accel_z
            loaded_data["gyro_x"] = loaded_gyro_x
            loaded_data["gyro_y"] = loaded_gyro_y
            loaded_data["gyro_z"] = loaded_gyro_z
        
            self.cal_loaded_data()
            self.plot_loaded_graph(loaded_data)
            self.distance_label.setText("Distance: " + str(round(loaded_data["distance"][-1], 2)) + " m")
            self.average_velocity_label.setText("Average Velocity: " + str(round(np.mean(loaded_data["velocity"]), 2)) + " m/s")
            self.send_to_line_button.setVisible(True)

    def save_graph(self, figure, figure_path):
        os.makedirs(os.path.dirname(figure_path), exist_ok=True)
        figure.savefig(figure_path)

    def create_credentials(self, credentials_path):
        with open(credentials_path, 'r') as file:
            credentials = json.load(file)
        # Accept authorization
        flow = InstalledAppFlow.from_client_config(credentials, ['https://www.googleapis.com/auth/drive'])
        credentials = flow.run_local_server(port=0)
        return credentials

    def upload_to_google_drive(self, image_path, creds, file_type):
        drive_service = build('drive', 'v3', credentials=creds)

        if file_type == 'image':
            file_metadata = {
                'name': image_path.split('\\')[-1],
                'mimeType': 'image/jpeg'
            }
            media = MediaFileUpload(image_path, mimetype='image/jpeg')
        elif file_type == 'text':
            file_metadata = {
                'name': image_path.split('/')[-1],
                'mimeType': 'text/plain'
            }
            media = MediaFileUpload(image_path, mimetype='text/plain')

        # Upload the file to Google Drive
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = file.get('id')

        # Define request body for permission
        new_permission = {
            'type': 'anyone',
            'role': 'reader'
        }
        drive_service.permissions().create(fileId=file_id, body=new_permission).execute()

        return file_id
    
    def send_to_line(self):
        # Create a text message to send to Line
        text_message = "Distance: " + str(round(loaded_data["distance"][-1], 2)) + " m" + "\n" + "Average Velocity: " + str(round(np.mean(loaded_data["velocity"]), 2)) + " m/s"
        
        # Path to the distance image file
        dist_path = 'D:\\Download\\dist.png'
        self.save_graph(self.figure_dist_2, dist_path)
        
        # Path to the velocity image file
        vel_path = 'D:\\Download\\vel.png'
        self.save_graph(self.figure_vel_2, vel_path)

        # Path to the credentials file ** NEED TO MODIFY  **
        credentials_path = 'D:\Download\client_secret_155036317222-jpt6af4eliqe1odvpml9nife8u5arvbc.apps.googleusercontent.com.json'
        credentials = self.create_credentials(credentials_path)

        # Call the function to upload "distance" image to google drive and get file ID
        dist_file_id = self.upload_to_google_drive(dist_path, credentials, "image")
        dist_url = f"https://drive.google.com/uc?export=download&id={dist_file_id}"

        # Call the function to upload "velocity" image to google drive and get file ID
        vel_file_id = self.upload_to_google_drive(vel_path, credentials, "image")
        vel_url = f"https://drive.google.com/uc?export=download&id={vel_file_id}"

        # Call the function to upload raw data to google drive and get file ID
        data_file_id = self.upload_to_google_drive(file_path, credentials, "text")
        # data_url = f"https://drive.google.com/uc?export=download&id={data_file_id}"

        # Send a message to Line
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 1CTdQTPxdsLPekcTUoPolFn2UCtpsHvFg1ntA5IsSDJFjIbiCAviCIGBU6zvLOGfKWnxvQia9J2bN2eZ09MF8n1YKuKUoXofdXCIc3y4SlRkPNzZ9yobx0b0sndA0h7bsCzAs9Q7o/aeC0B1oY9nXwdB04t89/1O/w1cDnyilFU="
        }

        data = {
            "to": "Uf652f2e71d592091ced8215c06ef6d41",
            "messages": [
                {
                    "type": "text",
                    "text": text_message
                },
                {
                    "type": "text",
                    "text": "Distance Graph"
                },
                {
                    "type": "image",
                    "originalContentUrl": dist_url,
                    "previewImageUrl": dist_url
                },
                {
                    "type": "text",
                    "text": "Velocity Graph"
                },
                {
                    "type": "image",
                    "originalContentUrl": vel_url,
                    "previewImageUrl": vel_url
                }
            ]
        }

        # Send a POST request to the LINE API
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            QMessageBox.information(None, "Success", "Message sent to Line successfully!")
        else:
            QMessageBox.critical(None, "Error", f"Failed to send message to Line. Error: {response.text}")

    # Callback function when the client receives a CONNACK response from the server
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribe to the topic upon successful connection
        client.subscribe("thammasat/chakapat/sensor")

    # Callback function when a message is received from the subscribed topic
    def on_message(self, client, userdata, msg):
        raw_mqtt_message = msg.payload.decode()
        print("Received message: "+raw_mqtt_message)
        raw_mqtt_message = eval(raw_mqtt_message)
        # self.temp_timestamp, self.temp_accel_x, self.temp_accel_y, self.temp_accel_z, self.temp_gyro_x, self.temp_gyro_y, self.temp_gyro_z = raw_mqtt_message.split(", ")
        self.temp_timestamp = raw_mqtt_message['time']
        self.temp_accel_x = raw_mqtt_message['accelX']
        self.temp_accel_y = raw_mqtt_message['accelY']
        self.temp_accel_z = raw_mqtt_message['accelZ']
        self.temp_gyro_x = raw_mqtt_message['gyroX']
        self.temp_gyro_y = raw_mqtt_message['gyroY']
        self.temp_gyro_z = raw_mqtt_message['gyroZ']
        raw_data["timestamp"].append(float(self.temp_timestamp))
        raw_data["accel_x"].append(float(self.temp_accel_x))
        raw_data["accel_y"].append(float(self.temp_accel_y))
        raw_data["accel_z"].append(float(self.temp_accel_z))
        raw_data["gyro_x"].append(float(self.temp_gyro_x))
        raw_data["gyro_y"].append(float(self.temp_gyro_y))
        raw_data["gyro_z"].append(float(self.temp_gyro_z))
        # get previous data
        try:
            prev_deg_data = np.arctan2(raw_data["accel_x"][-2], raw_data["accel_y"][-2])
        except:
            prev_deg_data = 0
        # calculate distance & velocity
        self.cal_processed_data(float(self.temp_accel_x), float(self.temp_accel_y), prev_deg_data)
        self.total_dist_label.setText("Total Distance: " + str(round(cumulative_dist, 2)) + " m")
        self.average_vel_label.setText("Average Velocity: " + str(round(np.mean(processed_data["velocity"]), 2)) + " m/s")
        
        # processed_data['velocity'].append(vel)
        # plot graph
        self.plot_raw_graph()

    def subscribe(self):
        # Create an MQTT client instance
        self.client = mqtt.Client()

        # Set up callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to the MQTT broker
        # self.client.connect("broker.hivemq.com", 1883, 60)  # Connect with default MQTT version
        self.client.connect("broker.emqx.io", 1883, 60)  # Connect with default MQTT version

        # Start the network loop to handle incoming messages
        self.client.loop_start()

    def plot_raw_graph(self):
        try:
            self.figure_raw_ax.clear()
            self.figure_raw_ay.clear()
            self.figure_raw_az.clear()
            self.figure_raw_gx.clear()
            self.figure_raw_gy.clear()
            self.figure_raw_gz.clear()
            self.figure_dist.clear()
            self.figure_vel.clear()

        except:
            pass
        ax = self.figure_raw_ax.add_subplot(111)
        ax.plot(raw_data["accel_x"])
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=6)
        self.canvas_raw_ax.draw()

        ay = self.figure_raw_ay.add_subplot(111)
        ay.plot(raw_data["accel_y"])
        ay.tick_params(axis='x', labelsize=6)
        ay.tick_params(axis='y', labelsize=6)
        self.canvas_raw_ay.draw()

        az = self.figure_raw_az.add_subplot(111)
        az.plot(raw_data["accel_z"])
        az.tick_params(axis='x', labelsize=6)
        az.tick_params(axis='y', labelsize=6)
        self.canvas_raw_az.draw()

        gx = self.figure_raw_gx.add_subplot(111)
        gx.plot(raw_data["gyro_x"])
        gx.tick_params(axis='x', labelsize=6)
        gx.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gx.draw()

        gy = self.figure_raw_gy.add_subplot(111)
        gy.plot(raw_data["gyro_y"])
        gy.tick_params(axis='x', labelsize=6)
        gy.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gy.draw()

        gz = self.figure_raw_gz.add_subplot(111)
        gz.plot(raw_data["gyro_z"])
        gz.tick_params(axis='x', labelsize=6)
        gz.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gz.draw()

        dist = self.figure_dist.add_subplot(111)
        dist.plot(processed_data["distance"])
        dist.tick_params(axis='x', labelsize=6)
        dist.tick_params(axis='y', labelsize=6)
        self.canvas_dist.draw()

        vel = self.figure_vel.add_subplot(111)
        vel.plot(processed_data["velocity"])
        vel.tick_params(axis='x', labelsize=6)
        vel.tick_params(axis='y', labelsize=6)
        self.canvas_vel.draw()

    def plot_loaded_graph(self, loaded_data):
        try:
            self.figure_raw_ax_2.clear()
            self.figure_raw_ay_2.clear()
            self.figure_raw_az_2.clear()
            self.figure_raw_gx_2.clear()
            self.figure_raw_gy_2.clear()
            self.figure_raw_gz_2.clear()
            self.figure_dist_2.clear()
            self.figure_vel_2.clear()

        except:
            pass
        ax_2 = self.figure_raw_ax_2.add_subplot(111)
        ax_2.plot(loaded_data["accel_x"])
        ax_2.tick_params(axis='x', labelsize=6)
        ax_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_ax_2.draw()

        ay_2 = self.figure_raw_ay_2.add_subplot(111)
        ay_2.plot(loaded_data["accel_y"])
        ay_2.tick_params(axis='x', labelsize=6)
        ay_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_ay_2.draw()

        az_2 = self.figure_raw_az_2.add_subplot(111)
        az_2.plot(loaded_data["accel_z"])
        az_2.tick_params(axis='x', labelsize=6)
        az_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_az_2.draw()

        gx_2 = self.figure_raw_gx_2.add_subplot(111)
        gx_2.plot(loaded_data["gyro_x"])
        gx_2.tick_params(axis='x', labelsize=6)
        gx_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gx_2.draw()

        gy_2 = self.figure_raw_gy_2.add_subplot(111)
        gy_2.plot(loaded_data["gyro_y"])
        gy_2.tick_params(axis='x', labelsize=6)
        gy_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gy_2.draw()

        gz_2 = self.figure_raw_gz_2.add_subplot(111)
        gz_2.plot(loaded_data["gyro_z"])
        gz_2.tick_params(axis='x', labelsize=6)
        gz_2.tick_params(axis='y', labelsize=6)
        self.canvas_raw_gz_2.draw()

        dist_2 = self.figure_dist_2.add_subplot(111)
        dist_2.plot(loaded_data["distance"])
        dist_2.set_xlabel("Time (s)")
        dist_2.set_ylabel("Distance (m)")
        dist_2.tick_params(axis='x', labelsize=6)
        dist_2.tick_params(axis='y', labelsize=6)
        self.canvas_dist_2.draw()

        vel_2 = self.figure_vel_2.add_subplot(111)
        vel_2.plot(loaded_data["velocity"])
        vel_2.set_xlabel("Time (s)")
        vel_2.set_ylabel("Velocity (m/s)")
        vel_2.tick_params(axis='x', labelsize=6)
        vel_2.tick_params(axis='y', labelsize=6)
        self.canvas_vel_2.draw()

    def cal_processed_data(self, accel_x, accel_y, prev_deg_data):
        global cumulative_dist
        # calculate degree
        delta = abs(abs(np.arctan2(accel_x, accel_y)) - abs(prev_deg_data)) * 0.3 # 0.3 is the radius of the wheel
        if delta > 0.01:    # 0.01 is the threshold for noise removal
            cumulative_dist += delta
            processed_data['distance'].append(cumulative_dist)
        else:
            processed_data['distance'].append(cumulative_dist)
        # calculate velocity
        processed_data['velocity'].append(processed_data['distance'][-1] - processed_data['distance'][-2] if len(processed_data['distance']) > 1 else 0)

    def cal_loaded_data(self):
        global loaded_data
        cumulative_value = 0
        deg_data = np.arctan2(loaded_data["accel_x"], loaded_data["accel_y"])
        for idx in range(1, len(deg_data)):
            # collect cumulative radians data
            delta = abs(abs(deg_data[idx]) - abs(deg_data[idx-1]))
            if delta > 0.01:
                cumulative_value += delta
                loaded_data['distance'].append(cumulative_value * 0.3)
        loaded_data['velocity'] = np.diff(loaded_data['distance'])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()  # Create an instance of your MainWindow class
    main_window.show()  # Show the main window
    sys.exit(app.exec_())