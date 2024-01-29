# ICT720-project-2024
# Group 1 [Yes Wheelchair](https://www.facebook.com/100066453249785/posts/pfbid02DiEnpRqT1H4SUK5FBEpH5kz9rZoqYkPg4KNShhSsfJ4qUXWBaDWnk1JEBK1ZKjNhl)
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

1. As a **Wheelchair User**, I want to **assess my physical abilities for optimal wheelchair usage** so that **I can enhance my mobility and overall wheelchair experience.**
   - Scenario: **Wheelchair User's Assessment**, given **a Wheelchair User initiating the evaluation process**, when **the system prompts for personal information (name, surname, weight, and height)**, then **the system accurately records and stores the user's information for future evaluations**.

2. As a **Wheelchair User**, I want to **receive feedback on my wheelchair usage abilities for continuous improvement** so that **I can enhance my skills and overall well-being.**
   - Scenario: **User's Feedback for Improvement**, given **a completed evaluation by a Wheelchair User**, when **the system processes the data, then it generates a summary of the user's performance and suggests areas for improvement**.

3. As a **Wheelchair Coach**, I want to **evaluate the user's strength and mobility to recommend suitable wheelchairs** so that **users can have personalized and comfortable mobility solutions.**
   - Scenario:**Wheelchair Coach's Evaluation**, given **an ongoing evaluation**, when **the system, as requested by a Wheelchair Coach, conducts strength tests, anaerobic performance assessments, and evaluates nimbleness**, then **it processes the data and generates parameters (distance, speed, time) for each test, indicating suitability**.

4. As a **Physical Therapist**, I want to **access accurate data for evaluating the user's wheelchair usage abilities** so that **I can provide tailored therapeutic interventions and support.**
   - Scenario: **Physical Therapist's Data Access**, **given a Physical Therapist accessing the system**, when **entering the user's information and observing wheelchair movement during tests**, then **the system accurately records and displays the data, enabling informed assessments**.

5. As a **Matsunaga Wheelchair Company**, I want to **enhance the detection of movement within the home of an elderly person using a wheelchair. The emphasis is on collecting long-term data and utilizing indicators of activity type rather than physical performance**. so that **to be ensure accurate and reliable assessment results, fostering user trust in the evaluation outcomes**.
   - Scenario: **Movement Detection and Assessment, given movement data received from IMU sensors during the evaluation**, when **the system processes the data**, then **it generates accurate and reliable evaluation results, ensuring the maximum error percentage for distance and time measurements is within acceptable limits. The focus is on capturing long-term data and distinguishing between various types of activities to provide a comprehensive understanding of the user's mobility patterns. This approach enhances the overall assessment and promotes trust in the evaluation results among wheelchair users.**

6. As a **Matsunaga Wheelchair Company**, I want to **use the evaluation system to recommend appropriate wheelchair models** so that **users can have a personalized and optimal mobility solution.**
   - Scenario: **Wheelchair Company's Recommendations**, given **evaluation results**, when **the system processes the data**, then **it provides personalized recommendations for Wheelchair types, as required by a Wheelchair Company, based on the user's physical fitness and usage requirements**.

  
## Project Brief

## Members
### TAIST AIoT 
1. Ms. Sitaporn Anektanarojkul ID:6622040274 [(sitaporn.anek@gmail.com)](mailto:sitaporn.anek@gmail.com)

2. Mr. Chakapat Chokchaisiri ID:6622040308 [(chakapat.chokchaisiri@gmail.com)](mailto:chakapat.chokchaisiri@gmail.com)

3. Mr. Aueaphum Aueawatthanaphisut ID:6622040662 [(aueawatth.aue@gmail.com)](mailto:aueawatth.aue@gmail.com)

## Hardware
![image](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/109651869/61ed37ec-3e5c-4cbb-ad19-d9cf908cda47)


[M5StickC](https://docs.m5stack.com/en/core/m5stickc) (M5Stick-C)
- [FTDI USB serial](https://docs.m5stack.com/en/core/m5stickc)
- LCD 80x160
- [6-axis IMU MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)

## State Diagram
![wheelchair state diagram (1)](https://github.com/Aueaphum2541/Ray-Folk-Pun-Project2024/assets/156740150/c0b54d8c-5d9e-4d31-8af0-5142a6a35948)

## Sequence Diagram

## System Architecture
