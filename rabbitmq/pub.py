import pika
exchangeName = 'testfanaut'
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                     port=5672,
                                     virtual_host="/",
                                     credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange=exchangeName,exchange_type='fanout')
channel.basic_publish(exchange=exchangeName,
                      routing_key='',
                      body='hi')