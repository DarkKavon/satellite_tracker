import sys
sys.path.append('.')
import json
import ephem
import requests
from src.coordniates.dms_coordinates import DMSCoordinate, DMSCoordinates


if __name__ == "__main__":
    # r = requests.get("http://tle.ivanstanojevic.me/api/tle")
    # rj = json.loads(r.text)['member']
    # print(rj[0])

    i = {'@id': 'https://tle.ivanstanojevic.me/api/tle/25544', '@type': 'Tle', 'satelliteId': 25544, 'name': 'ISS (ZARYA)', 'date': '2023-08-05T03:25:09+00:00', 'line1': '1 25544U 98067A   23217.14246826  .00016091  00000+0  28811-3 0  9997', 'line2': '2 25544  51.6413  85.9742 0000967 156.2280 348.3613 15.50120840409381'}


    tle_rec = ephem.readtle(i['name'], i['line1'], i['line2'])
    tle_rec.compute()

    dms = DMSCoordinates(DMSCoordinate(tle_rec.sublong), DMSCoordinate(tle_rec.sublat))
    print(dms[0])
    print(dms)


    print(dms.convert_to_dd())
