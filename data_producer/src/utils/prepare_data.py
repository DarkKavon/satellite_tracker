import os
import sys
sys.path.append(os.getcwd())
from data_producer.src.coordniates.dms_coordinates import DMSCoordinates, DMSCoordinate
from collections.abc import MutableMapping
import ephem



def prepare_data(input: MutableMapping) -> MutableMapping:
    satellite_id = input['satelliteId']
    satellite_name = input['name']
    timestamp = input['date']
    timestamp_split = input['date'].split('T')
    date = timestamp_split[0]
    time = timestamp_split[1]
    tle_line1 = input['line1']
    tle_line2 = input['line2']

    tle_coordniates = ephem.readtle(satellite_name, tle_line1, tle_line2)
    tle_coordniates.compute()

    dms = DMSCoordinates(DMSCoordinate(tle_coordniates.sublong),
                         DMSCoordinate(tle_coordniates.sublat))
    dd = dms.convert_to_dd()

    return {
        "satellite_id": satellite_id,
        "satellite_name": satellite_name,
        "timestamp": timestamp,
        "date": date,
        "time": time,
        "tle_line1": tle_line1,
        "tle_line2": tle_line2,
        "dms_coordinates": dms.to_json(),
        "dd_coordinates": dd.to_json()
    }
