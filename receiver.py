import pika


# make an output message callback function
def output_message(ch, method, properties, message_received):
    print("[x] {}".format(message_received))

# Initialization connection & channel rabbit-mq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
queue_name = 'apache-logger'

# declare a channel to subscribing/consuming a queue
channel.queue_declare(queue=queue_name)

# consume the channel with selected queue
channel.basic_consume(output_message,
                      queue=queue_name,
                      no_ack=True)

# Output application message
print('Pak Budi logging an apache server, listening to "{}" queue.\n'
      'CTRL + C to Quit'.format(queue_name))

# loop the channel for getting queue message
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.close()
    print("Connection close")