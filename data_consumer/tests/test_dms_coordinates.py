import os
import sys
sys.path.append(os.getcwd())
from src.coordniates.dms_coordinates import DMSCoordinates, DMSCoordinate
from src.coordniates.dd_coordinates import DDCoordinates


def test_convert_to_dd():
    dms1 = DMSCoordinate("48:23:23.4")
    dms2 = DMSCoordinate("23:12:12.3")
    dmsc = DMSCoordinates(dms1, dms2)
    assert DDCoordinates(48.389833333333335, 23.203416666666666) == dmsc.convert_to_dd()


def test_dms_coordinates_repr():
    dms = DMSCoordinate("48:23:23.4")
    dmsc = DMSCoordinates(dms, dms)
    assert """48° 23' 23.4\"""" == str(dmsc.long)
