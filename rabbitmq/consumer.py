import pika
exchangeName = 'testfanaut'
queueName = 'queue_test'

def onConsuming(ch, method, properties, body):
    print(" [x] Received %r" % body)


credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                     port=5672,
                                     virtual_host="/",
                                     credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=queueName)
channel.queue_bind(exchange=exchangeName,queue = queueName)
channel.basic_consume(onConsuming,
                      queue=queueName
                      )

channel.start_consuming()

