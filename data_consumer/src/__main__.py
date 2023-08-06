import sys
sys.path.append('.')
import json
import logging
from kafka import KafkaConsumer
from data_consumer.src.connectors.mongo_connector import MongoDBConnector


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    logger = logging.getLogger()

    TOPIC = "SATELLITE_TRACKER"
    mongo_url = "mongodb://localhost:27017"
    mongo_db = "db"
    mongo_collection = "satellites"

    consumer = KafkaConsumer(TOPIC, bootstrap_servers = "localhost:29092")
    logger.info("Kafka consumer registered...")
    
    mdb = MongoDBConnector(mongo_url, mongo_db)
    logger.info("Connection with MongoDB established...")

    logger.info("Start reading records...")
    for record in consumer:
        mdb.insert(mongo_collection, decoded := json.loads(record.value.decode()))
        logger.info(f"Record about {decoded['satellite_name']} inserted to database...")
