from datetime import datetime
from math import degrees

import ephem

place = ephem.Observer()
place.lat = '31.7754'
place.lon = '76.9861'
place.elevation = 1000
place.date = datetime.now().strftime('%Y/%m/%d')

#print (place.date)
#print (datetime.now().date().strftime('%Y/%m/%d'))

test_place = place

objects_string = ["Polaris", "Vega", "Deneb", "Altair", "Caph", "Schedar",
                  "Scheat",  "Algenib", "Fomalhaut", "Hamal", "Aldebaran", "Atlas",
                  "Capella", "Menkalinan", "Achernar", "Elnath", "Bellatrix",  "Rigel",
                  "Mintaka", "Alnilam", "Betelgeuse", "Alnitak", "Saiph", "Castor", "Sirius", "Dubhe",
                  "Procyon", "Pollux", "Merak", "Canopus", "Megrez", "Phecda", "Alphard", "Algieba",
                  "Regulus", "Alioth", "Mizar", "Denebola", "Alcaid"
                  ]

objects = []
for s in objects_string:
    objects.append(ephem.star(s))


ruchbah = ephem.FixedBody()
ruchbah.name = "Ruchbah"
ruchbah._ra = '0:56:42.0'
ruchbah._dec = '60:43:00.0'

alpheratz = ephem.FixedBody()
alpheratz.name = "Alpheratz"
alpheratz._ra = '0:08:23.0'
alpheratz._dec = '29:05:26.0'

cursa = ephem.FixedBody()
cursa.name = "Cursa"
cursa._ra = '5:07:51.0'
cursa._dec = '-5:05:11.0'

rngc1980 = ephem.FixedBody()
rngc1980.name = "RNGC 1980"
rngc1980._ra = '5:36:27.0'
rngc1980._dec = '-5:54:35.0'

m42 = ephem.FixedBody()
m42.name = "M 42"
m42._ra = '5:35:21.0'
m42._dec = '-5:23:31.0'


m45 = ephem.FixedBody()
m45.name = "M 45"
m45._ra = '3:47:24.0'
m45._dec = '24:7:0.0'

other_objects = [ruchbah, alpheratz,  cursa, rngc1980, m42, m45]

objects.append(ephem.Saturn())
objects.append(ephem.Mars())
objects.append(ephem.Moon())
objects.append(ephem.Jupiter())
objects.append(ephem.Uranus())
objects.append(ephem.Neptune())
objects.append(ephem.Mercury())
objects.append(ephem.Venus())
objects = objects + other_objects
planets = ["Saturn", "Mars", "Moon", "Jupiter",
           "Uranus", "Neptune", "Mercury", "Venus"]

obj_req = input("Enter the name of object: ")
if obj_req not in objects + planets + objects_string:
    print("**Entered object is not in the databse\n**Giving details of Moon by default")
    obj_req = "Moon"

obj = ephem.FixedBody()


x = iter(planets)
for o in objects:
    o.compute(place.date)
    if o.name in planets:
        for x in planets:
            if o.name == x == obj_req:
                obj.name = o.name
                obj._ra = o.ra
                obj._dec = o.dec

    elif o.name == obj_req:
        obj.name = o.name
        obj._ra = o._ra
        obj._dec = o._dec


test_place.date = ephem.now()
obj.compute(test_place)
val1 = degrees(obj.alt)
val2 = degrees(obj.az)

# Checking the status of the object, if it below or above the Horizon


if val1 < degrees(0):
    print("Status:  The Object is below the Horizon!")
elif val1 < 10:
    print("Status:  The Object is just above the Horizon and may not be visible from the current location")
else:
    print("Status:  The Object is above the Horizon")

print("Resultant Altitude: " + str(val1) + " degrees")
print("Resultant Azimuth:  " + str(val2) + " degrees")
