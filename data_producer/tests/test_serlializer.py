import os
import sys
sys.path.append(os.getcwd())
from data_producer.src.utils.serializer import serializer



def test_serializer():
    assert b'{"a": 1, "b": 2}' == serializer({"a": 1, "b": 2})