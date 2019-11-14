import json 
from geopy import distance

with open('airports.json') as j:
    airports = json.load(j)

FAA_input = input('Enter FAA code: ')

def find_airport(value,key):
    for a in airports:
        if value == a[key]:
            return a
    
airport = find_airport(FAA_input,'IATA/FAA')  
lat1 = airport["Latitude"]
long1 = airport['Longitude']

destinations = []
for ID in airport['destinations']:
    dest = find_airport(ID,'Airport ID')
    lat2 = dest['Latitude']
    long2 = dest['Longitude']
    destinations.append([dest['IATA/FAA'],dest['Name'],distance.distance([lat1,long1],[lat2,long2]).km])
    
def sorted_dict(val):
    return val[2]

destinations.sort(key = sorted_dict)

for d in destinations:
    print(str(d[0]) + ' ' + str(d[1]) + ' {:,.0f} km'.format(d[2]))
    

