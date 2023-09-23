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




