import os
from dotenv import load_dotenv
import pika

load_dotenv()
host = os.getenv("RABBIT_MQ_HOST", default="")
port = os.getenv("RABBIT_MQ_PORT", default="")

params = pika.URLParameters(f"amqp://{host}:{port}")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
