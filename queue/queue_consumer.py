import os
from dotenv import load_dotenv
import pika

load_dotenv()
host = os.getenv("RABBIT_MQ_HOST", default="localhost")
port = os.getenv("RABBIT_MQ_PORT", default="5672")
params = pika.URLParameters(f"amqp://{host}:{port}")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")

channel.start_consuming()

channel.close()
