#!/usr/bin/python3
import ephem
from datetime import datetime
from dateutil.tz import tzlocal

def next_halloween_full_moon(d=None, hour=20, illumination=98.0):
    return halloween_full_moon(100, d, hour, illumination)

def prev_halloween_full_moon(d=None, hour=20, illumination=98.0):
    return halloween_full_moon(-100, d, hour, illumination)

def halloween_full_moon(finalyear, d, hour, illumination):
    if d is None:
        d = datetime.utcnow()
    results = []
    if finalyear < 0:
        step = -1
    else:
        step = 1
    thisyear = datetime.now().year
    for year in range(thisyear, thisyear + finalyear, step):
        dt = datetime(year, 10, 31, hour, tzinfo=tzlocal())
        m = ephem.Moon(dt)
        if m.phase >= illumination:
            results.append(year)
    return results

if __name__ == '__main__':
    print("Halloween Full Moons")
    print (f"Next:     {next_halloween_full_moon()[0]}")
    print (f"Prev:     {prev_halloween_full_moon()[0]}")
