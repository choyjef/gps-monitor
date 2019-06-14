def convertSnrDBToSnr(SnrDB):
    return 10 ** (SnrDB / 10)

def printLocationData(report, latitude, longitude):
    print "Time : %s" % report['time']
    print "Latitude : %3.6f" % latitude
    print "Longitude : %3.6f\n" % longitude

def printSatelliteData(satellite):
    print "PRN : %3d" % int(satellite['PRN']),
    print "Elevation : %2d" % int(satellite['el']),
    print "Azimuth : %3d" % int(satellite['az']),
    print "SNR dB : %2d" % int(satellite['ss']),
    print "SNR : %3.3f" % convertSnrDBToSnr(float(satellite['ss'])),

    used = "Y" if satellite['used'] else "N"

    print "Used : %s\n" % used,
