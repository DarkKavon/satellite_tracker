import sys
sys.path.append('.')
from data_producer.src.utils.serializer import serializer
from data_producer.src.utils.prepare_data import prepare_data
from kafka import KafkaProducer
from time import sleep
import requests
import logging
import json


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    stream_handler = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(stream_handler)

    SLEEP_MINUTES = 60
    TOPIC = "SATELLITE_TRACKER"
    last_sent_records = {}

    producer = KafkaProducer(bootstrap_servers = "localhost:29092", value_serializer = serializer)
    logger.info("Kafka producer registered...")

    while True:
        logger.info("Start sending info...")

        response = requests.get("http://tle.ivanstanojevic.me/api/tle")
        response = json.loads(response.text)['member']
        
        for record in response:
            if record['name'] not in last_sent_records.keys() or last_sent_records[record['name']] != record['date']:
                logging.info(f"Info about {record['name']}: {record}")
                producer.send(TOPIC, prepare_data(record))
                last_sent_records[record['name']] = record['date']
                logging.info(f"Info about {record['name']} sent...")
            else:
                logger.info(f"Skipping sending for {record['name']}...")
        
        logger.info(f"Sleeping {SLEEP_MINUTES} minutes...")
        sleep(60 * SLEEP_MINUTES)
