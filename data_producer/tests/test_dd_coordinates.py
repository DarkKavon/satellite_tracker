import os
import sys
sys.path.append(os.getcwd())
from data_producer.src.coordniates.dd_coordinates import DDCoordinates



def test_to_json():
    ddc = DDCoordinates(44.2, 12.2)
    assert {"long": 44.2, "lat": 12.2} == ddc.to_json()
