from kafka import KafkaProducer
count = 100
p = KafkaProducer(bootstrap_servers = '127.0.0.1:9092')
topic = 'test'
for data in range(20, count):
    print(str(data).encode('utf-8'))
    p.send(topic,str(data).encode('utf-8'))
