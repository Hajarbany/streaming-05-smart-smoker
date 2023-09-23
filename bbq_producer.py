"""
    This program sends a message to a queue on the RabbitMQ server.
    Make tasks harder/longer-running by adding dots at the end of the message.
    this program also sends an offer to open the rabbitMQ admin website.
    the CSV used for this file is called "smoker-temp.csv 

    Author: Hajar Banyalmarjeh
    Date: September 22nd, 2023

"""

import pika
import sys
import webbrowser
import csv
import time
import logging


# set up basic configuration for logging: 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# our program constants: 
HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
FILE_NAME = "smoker-temps.csv"
SHOW_OFFER = True 


# Now, we add an offer to open the rabbitMQ admin site: 
def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters(HOST))
# use the connection to create a communication channel
ch = conn.channel()

def main():
    try:
        # use the channel to delete the three queues
        ch.queue_delete(queue="01-smoker")
        ch.queue_delete(queue="02-food-A")
        ch.queue_delete(queue="03-food-B")

        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        ch.queue_declare(queue="01-smoker", durable=True)
        ch.queue_declare(queue="02-food-A", durable=True)
        ch.queue_declare(queue="03-food-B", durable=True)


        with open(FILE_NAME, "r") as input_file:
            reader = csv.reader(input_file, delimiter=",")
            for row in reader:
                # the row variables: 
                Time, Channel1, Channel2, Channel3 = row

                # Now, we can choose which messages to send to our queue
                first = f"[{Time}, {Channel1}]"
                second = f"[{Time}, {Channel2}]"
                third = f"[{Time}, {Channel3}]"

                # next, we make sure all three messages will send: 
                send_message("01-smoker", first)
                send_message("02-food-A", second)
                send_message("03-food-B", third)
                    # except, in the event of an error OR user stops the process, do this

    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

def send_message(queue_name, message):
    """
      Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """

    print(" [*] Messages being sent to the queues. To exit press CTRL+C")

    # Read one value every half minut
    time.sleep(0.5)



