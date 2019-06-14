from gps import *
from gps_utils import readAndOutputData

session = gps()
session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)

readAndOutputData(session)
