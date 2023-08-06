import sys
sys.path.append('.')
from kafka import KafkaConsumer
from data_consumer.src.connectors.mongo_connector import MongoDBConnector


if __name__ == "__main__":

    TOPIC = "SATELLITE_TRACKER"
    mongo_url = "mongodb://localhost:27017"
    mongo_db = "db"
    mongo_collection = "satellites"

    consumer = KafkaConsumer(TOPIC, bootstrap_servers = "localhost:29092")
    mdb = MongoDBConnector(mongo_url, mongo_db)

    for record in consumer:
        print(record)

