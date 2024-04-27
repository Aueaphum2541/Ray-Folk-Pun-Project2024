# ICT720-project-2024
# Group [Yes Wheelchair](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024)
## Development of System to Evaluate Wheelchair User Capability
![419119466_727492066142562_5958509345109420164_n](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/e5daaaf6-a96d-479f-8115-b71499980b1d)

![image](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/5db47476-e9c5-4a91-936e-4eaef0677feb)

## Objectives
1. **Enhance User Independence:**
   - **Objective:** Improve the self-reliance of wheelchair users by providing a comprehensive evaluation system.
   - **Key Results:** Users should be able to assess their wheelchair usage abilities independently.

2. **Facilitate Proper Wheelchair Selection:**
   - **Objective:** Assist users in selecting the most suitable wheelchair based on their physical abilities and preferences.
   - **Key Results:** Provide personalized recommendations for wheelchair types that align with the user's physical fitness.

3. **Ensure Mobility and Health:**
   - **Objective:** Minimize mobility barriers and promote the overall physical health of wheelchair users.
   - **Key Results:** Evaluate and enhance the efficiency of wheelchair usage to prevent negative impacts on physical health.

4. **Utilize IMU Technology:**
   - **Objective:** Incorporate Inertial Measurement Unit (IMU) technology for accurate and real-time movement data collection.
   - **Key Results:** Enable precise tracking of wheelchair movements, contributing to the evaluation process.

5. **Create User-Friendly GUI:**
   - **Objective:** Develop a Graphical User Interface (GUI) that is easy to use and understand, catering to both wheelchair users and physical therapists.
   - **Key Results:** Ensure information received from IMU sensors is displayed in a user-friendly format for effective evaluation.


## Stakeholder
1. Matsunaga Wheelchair Company
2. Physical Therapy
3. Wheelchair Coach

**User Stories:**

1. As a **Wheelchair User**, I want to **receive feedback on my wheelchair usage abilities for continuous improvement** so that **I can enhance my skills and overall well-being.**
   - Scenario: **User's Feedback for Improvement**, given **a completed evaluation by a Wheelchair User**, when **the system processes the data, then it generates a summary of the user's performance and suggests areas for improvement**.

2. As a **Wheelchair Coach**, I want to **evaluate the user's strength and mobility to recommend suitable wheelchairs** so that **users can have personalized and comfortable mobility solutions.**
   - Scenario:**Wheelchair Coach's Evaluation**, given **an ongoing evaluation**, when **the system, as requested by a Wheelchair Coach, conducts strength tests, anaerobic performance assessments, and evaluates nimbleness**, then **it processes the data and generates parameters (distance, speed, time) for each test, indicating suitability**.

3. As a **Matsunaga Wheelchair Company**, I want to **enhance the detection of movement within the home of an elderly person using a wheelchair. The emphasis is on collecting long-term data and utilizing indicators of activity type rather than physical performance**. so that **to be ensure accurate and reliable assessment results, fostering user trust in the evaluation outcomes**.
   - Scenario: **Movement Detection and Assessment, given movement data received from IMU sensors during the evaluation**, when **the system processes the data**, then **it generates accurate and reliable evaluation results, ensuring the maximum error percentage for distance and time measurements is within acceptable limits. The focus is on capturing long-term data and distinguishing between various types of activities to provide a comprehensive understanding of the user's mobility patterns. This approach enhances the overall assessment and promotes trust in the evaluation results among wheelchair users.**

## Project Brief

## Members
### TAIST AIoT 
1. Ms. Sitaporn Anektanarojkul ID:6622040274 [(sitaporn.anek@gmail.com)](mailto:sitaporn.anek@gmail.com)

2. Mr. Chakapat Chokchaisiri ID:6622040308 [(chakapat.chokchaisiri@gmail.com)](mailto:chakapat.chokchaisiri@gmail.com)

3. Mr. Aueaphum Aueawatthanaphisut ID:6622040662 [(aueawatth.aue@gmail.com)](mailto:aueawatth.aue@gmail.com)

## Hardware

![image](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/616693fe-8d8d-425b-be37-f53045735ad9)


[ M5Stack Capsule Kit w/ M5StampS3]([https://docs.m5stack.com/en/core/m5stickc](https://shop.m5stack.com/products/m5stack-capsule-kit-w-m5stamps3)) ( M5Stack Capsule Kit w/ M5StampS3)
- [FTDI USB serial](https://docs.m5stack.com/en/core/m5stickc)
- [6-axis IMU BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf) 

## State Diagram
![wheelchair state diagram (1)](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/156740150/c0b54d8c-5d9e-4d31-8af0-5142a6a35948)

## Sequence Diagram
![Sequence Diagram](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/6d3b1bc1-1bc5-4c7d-834f-106a5fae904f)

## System Architecture
![System Architecture](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/151521992/4996583f-a365-47e3-91be-79404838435a)

## Data Flow Process
![image](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/156740150/62fc35d7-c05b-43e4-9123-29fec1face5b)

## Data Modeling
![Data_Modeling1](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/151521992/ad0b5fa2-40d1-45d7-a7a7-f84eaa7d5ceb)

## Wheelchair User Detection with Grove Vision AI Module V2 using YOLO V8 getting started with SenseCraft AI

The operation of the Grove Vision AI v2 board is also convenient with a live preview on Seeed Studio's own SenseCraft AI website, detecting people using wheelchairs using YOLO V8.

![IMG_3110](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/1118c332-4153-4270-84a7-3fd7812893f3)
![grove 7732776a](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/46f5bed3-291f-48a4-8b59-3ce33e431962)

Front and side images of a wheelchair user were used as the data set.
![IMG_3169](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/7ba19537-b8e8-4362-a21b-80b43da757de)
![IMG_3128](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/9150187a-a75e-4c97-b33f-bc32670ab4d4)

Deploy Person Detection--YOLOV8 Model
Supported Devices
The model can be deployed on the following devices that is Grove-Vision AI V2

Connect Device
1. Connect Grove - Vision AI V2 to the camera via the CSI connection cable.
2. Connect the Grove - Vision AI V2 to your computer via USB. 
3. Select USB Single/Serial debug unit to connect.

![image](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/f3f74ab1-b685-4857-949b-bc5289c07564)

The solution that can detect a wheelchair user all view such as front view, side view, and so on.
![Screenshot 2024-04-27 161734](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/c3745822-b425-47da-9fd0-a7c5bfcf6c80)
![Screenshot 2024-04-27 161757](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/dd9237b4-18de-4175-b0f9-a7f7be76e5d7)

and that have a data in logger such as preprocess, inference, postprocess and have bounding box for checking for detection
![Screenshot 2024-04-27 161816](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/abbae8e2-e2bf-4a51-baf5-63551215f8ad)










