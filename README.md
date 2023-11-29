# Shared Vehicle Manager with IOT

# Table of Contents
1. [Project Overview](#project-overview)
2. [Current Market Situation of Shared Vehicle Management](#current-market-situation-of-shared-vehicle-management)
3. [Project Description](#project-description)
    - [Project Architecture](#project-architecture)
    - [Shared Vehicle Management System](#shared-vehicle-management-system)
    - [User-Customized HUD Application](#user-customized-hud-application)
4. [Potential Improvement](#potential-improvement)

## Team “Millennium”

Team Leader: Minchan Jung

Team Members: Dahyun Ko, Hokyung Park, Junho Kim, Sujong Ha

<a href="https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement" />
</a>

## Project Overview

This project aims to provide a customized management solution for the shared vehicle industry, enhancing the experience for both vehicle providers and users. To achieve this, we developed a shared vehicle management system utilizing the latest digital twin technology, along with a user-customized application.

## Current Market Situation of Shared Vehicle Management

<div align="center">
    <img src="https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/73748884/e70e1a66-3b8e-450c-ad53-7a9f024bf339" width="500" height="300">
</div>

The future of the automotive industry demands Sofware Defined Vehicle (SDV), requiring changes in the shared vehicle market. With the growing shared vehicle market, there is an urgent need to improve vehicle management and user experience. The diverse needs of customers are increasing, and providing efficient vehicle management and enhanced user experiences has become a key factor in market competition.

## Project Description

### Project Architecture

#### Ideal Structure
![ideal](https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/138571365/c46a4a88-5ef1-44f0-b1ed-bb11705a35d5)

#### For Hackathon
![hack](https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/138571365/b457784f-d16c-4fc0-9664-339c3b83e59c)

### Shared Vehicle Management System

<div align="center">
    <img src="https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/73748884/f97aa38a-16dd-457a-85af-b1ae7b787b54" width="500" height="300">
</div>

- Overview
    
    The shared vehicle management system utilizes digital twin technology to monitor and manage aspects such as the vehicle's battery life, consumable status, and accident occurrences in real-time. New vehicles, when introduced, are efficiently managed centrally through cloud connection, enabling cost reduction in maintenance and quicker response to accidents.
    
- Features
    1. Monitors and manages shared vehicles in real-time, including battery life, consumable status, and accident occurrences, using digital twin technology.
    2. When new vehicles are connected our ECU(with custom Leda image), they automatically connect to fleet management system.
    3. Without hardware change, can connect to ECU via eCAL, SOME/IP, CAN
    4. Allows for real-time assessment of vehicle condition, reducing maintenance costs.
    5. Shortens response time to car accidents.
    6. Shared vehicle companies can transparently provide the vehicle's condition to customers.

### User-Customized HUD Application

<div align="center">
    <img src="https://github.com/Eclipse-SDV-Hackathon-Accenture/Millennium_FleetManagement/assets/73748884/8120ae4d-de6c-4050-9479-c70093c0a745" width="500" height="300">
</div>

- Overview
    
    The user-customized application provides personalized HUD and vehicle settings, ensuring a consistent user experience regardless of the shared vehicle used. The ability to control and set up vehicles through smartphones and customization features based on user accounts contribute to increasing customer satisfaction and loyalty.
    
- Features
    1. Provides customized HUDs as desired by customers.
    2. Users enjoy a consistent, personalized experience with any shared vehicle, without the need for adaptation to new vehicles, contributing to increased customer loyalty and satisfaction.
    3. Offers vehicle operation and custom HUD through smartphones, including seat adjustments, air conditioning settings, and audio profiles, from anywhere.
    4. When users login to the vehicle application with their accounts, personalized settings stored in their accounts are applied to the vehicle, allowing customization across different types of shared vehicles.
    5. Supports customization of the dashboard through the Head Up Display, encouraging users to choose the same shared vehicle provider to maintain familiar dashboard settings and configurations.
    6. Updates for the app and firmware are possible through Leda's OTA (Over-The-Air).
    7. There is No need for companies to provide hardware for HUD.

## Potential Improvement

1. Beyond HUD, the possibility of providing customized Head Units and Instrument Clusters.
2. Emphasizing scalability for integration with future vehicle technologies.
3. Expanding service scope through continuous technological innovation.


--- 

- Change MonitorIP in forwarder-setting.env
- Send influxdb.token to /etc/forwarder/influxdb.token

# on the (local) host that you have started the back end components on
docker exec -it influxDB cat /tmp/out/fms-demo.token > /tmp/influxdb.token

# The FMS Forwarder needs to read the token required for authenticating to influxdb.
scp -P 2222 /tmp/influxdb.token root@127.0.0.1:/data/usr/fms/forwarder
