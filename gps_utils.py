from gpsprint import printLocationData
from gpsprint import printSatelliteData

def reportHasLocationData(report):
    try:
        report['lat']
        return True
    except KeyError:
        return False

def reportHasSatelliteData(report):
    try:
        report['satellites']
        return True
    except KeyError:
        return False

def readAndOutputData(session):
    for report in session:
        if reportHasLocationData(report):
            #Does this report have location data?
            latitude = float(report['lat'])
            longitude = float(report['lon'])

            printLocationData(report, latitude, longitude)
        elif reportHasSatelliteData(report):
            #If report doesn't contain location data, check if it has satellite data
            for satellite in report['satellites']:
               printSatelliteData(satellite)

            print ""

        else:
            print "No fix acquired"
