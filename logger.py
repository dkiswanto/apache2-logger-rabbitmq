import pika
from util import log_generator

# Initialization rabbit-mq connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
queue_name = 'apache-logger'

# Make a rabbit-mq queue (Channel)
channel.queue_declare(queue=queue_name)

# Apache log file locations
# (Apache2 installation using apt package manager in Ubuntu 16.04)
apache_log_location = "/var/log/apache2/access.log"


def main():
    try:
        # Open log file
        file_log = open(apache_log_location, "r")

        # generate logs file
        logs = log_generator(file_log)

        # process the log
        for log in logs:

            # print out the log
            print("sent to pak budi {}".format(log))

            # make a delivery mode object option 2 (persistent message)
            deliv_mode = pika.BasicProperties(delivery_mode=2)

            # publish to rabbit-mq broker
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  properties=deliv_mode,
                                  body=log)

    # Close rabbit-mq connection when CTRL + C
    except KeyboardInterrupt:
        connection.close()
        print("Connection close")

if __name__ == "__main__":
    print("Logger running, will send a message to '{}' queue\n"
          "CTRL + C to Stop".format(queue_name))
    main()