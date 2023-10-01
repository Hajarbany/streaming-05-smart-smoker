# streaming-05-smart-smoker
# Student: Hajar Banyalmarjeh
 The purpose of this module is to be able to learn how to use RabbitMQ to take temperature readings and send over to working channels. In this case, the working channels are 2 food categories. 

## Before You Begin

1. Make sure RabbitMQ server is running
2. Make sure pika is installed in your active environment

## Project explanation

- For this project, I imported pika, webbrowser, csv, logging, sys, and time. 
- I declared all the program constants and set up basic configuration for logging. 
- Then, we wrote a code which allows the user to open the rabbitMQ admin site.  
- I created a blocking connection to the RabbitMQ server and used the connection to create a communication channel
- I used the channel to delete the 3 existing queues and then declare durable queue. 
- In the code, I chose which messages to send to the queue based on the requirements, and then added a code to make sure all the messages will get sent. 
- I also added a "Print" function that allowed me to show the user what is happening in the terminal once we execute the file. 

## Screenshots of the work: 
- RabbitMQ Admin Site: 
<img width="1317" alt="Screenshot 2023-09-23 at 12 19 35 AM" src="https://github.com/Hajarbany/streaming-05-smart-smoker/assets/97689037/90e05ba5-65c5-4961-ad75-c7a53a4efdb6">
- Terminal: 
<img width="870" alt="Screenshot 2023-09-23 at 12 22 05 AM" src="https://github.com/Hajarbany/streaming-05-smart-smoker/assets/97689037/afa4194a-8551-47fe-be2f-a1045361b329">
- Entire page with terminal (Showing my name):
<img width="1126" alt="Screenshot 2023-09-23 at 12 22 17 AM" src="https://github.com/Hajarbany/streaming-05-smart-smoker/assets/97689037/4a1ede87-7709-4d34-a23f-b25c6c409449">

# streaming-05-smart-smoker
# Student: Hajar Banyalmarjeh
# Date: September 30th 2023
    The purpose of this module is to learn to create a script that listens for work messages contiously.
    In the consumer script, we have three queues that are each being used to listen for messages separately about the temperatures of the Smoker, Food A, and Food B. 
    We set up basic logging configuration, and we idenfied our variables. 
    In the consumer file, we wrote in detail how we ran our code. 

## Screenshots of the work: 
s




