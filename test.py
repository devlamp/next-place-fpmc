from operator import itemgetter
from datetime import datetime
from dateutil import parser
import subprocess

count = 0
#locFilter = ["Bridge", "Train Station", "Subway", "Road", "Bus Station", "Airport", "Ferry", ""]

categories = {
    "Arts & Crafts Store" : "Shop & Service",
    "Bridge" : "Outdoors & Recreation",
    "Home (private)" : "Residence",
    "Medical Center" : "Professional & Other Places",
    "Food Truck" : "Food",
    "Food & Drink Shop" : "Food",
    "Coffee Shop" : "Food",
    "Bus Station" : "Travel & Transport",
    "Bank" : "Shop & Service",
    "Gastropub" : "Food",
    "Electronics Store" : "Shop & Service",
    "Mobile Phone Shop" : "Shop & Service",
    "Cafe" : "Food",
    "Automotive Shop" : "Shop & Service",
    "Restaurant" : "Food",
    "American Restaurant" : "Food",
    "Government Building" : "Food",
    "Airport" : "Travel & Transport",
    "Ferry" : "Travel & Transport",
    "Office" : "Professional & Other Places",
    "Other Great Outdoors" : "Outdoors & Recreation",
    "Building" : "Professional & Other Places",
    "Mexican Restaurant" : "Food",
    "Music Venue" : "Arts & Entertainment",
    "Subway" : "Travel & Transport",
    "Student Center" : "College & University",
    "Park" : "Outdoors & Recreation",
    "Road" : "Travel & Transport",
    "Burger Joint" : "Food",
    "Sporting Goods Shop" : "Shop & Service",
    "Pizza Place" : "Food",
    "Jewelry Store" : "Shop & Service",
    "Sandwich Place" : "Food",
    "Clothing Store" : "Shop & Service",
    "Neighborhood" : "Outdoors & Recreation",
    "Ice Cream Shop" : "Food",
    "Soup Place" : "Food",
    "College Academic Building" : "College & University",
    "Department Store" : "Shop & Service",
    "Playground" : "Outdoors & Recreation",
    "Tattoo Parlor" : "Shop & Service",
    "Mall" : "Shop & Service",
    "Deli / Bodega" : "Food",
    "University" : "College & University",
    "Diner" : "Food",
    "Music Store" : "Shop & Service",
    "Light Rail" : "Travel & Transport",
    "Salon / Barbershop" : "Shop & Service",
    "General College & University" : "College & University",
    "Animal Shelter" : "Professional & Other Places",
    "Laundry Service" : "Shop & Service",
    "Residential Building (Apartment / Condo)" : "Residence",
    "Drugstore / Pharmacy" : "Shop & Service",
    "Cuban Restaurant" : "Food",
    "BBQ Joint" : "Food",
    "Other Nightlife" : "Nightlife Spot",
    "Gym / Fitness Center" : "Outdoors & Recreation",
    "Italian Restaurant" : "Food",
    "Stadium" : "Arts & Entertainment",
    "Church" : "Professional & Other Places",
    "Train Station" : "Travel & Transport",
    "Tanning Salon" : "Shop & Service",
    "Hotel" : "Travel & Transport",
    "Miscellaneous Shop" : "Shop & Service",
    "Bar" : "Nightlife Spot",
    "Spanish Restaurant" : "Food",
    "Moving Target" : "Travel & Transport",
    "Asian Restaurant" : "Food",
    "Factory" : "Professional & Other Places",
    "School" : "Professional & Other Places",
    "General Travel" : "Travel & Transport",
    "Burrito Place" : "Food",
    "Fast Food Restaurant" : "Food",
    "Dumpling Restaurant" : "Food",
    "Cupcake Shop" : "Food",
    "Wings Joint" : "Food",
    "Caribbean Restaurant" : "Food",
    "Hardware Store" : "Shop & Service",
    "Performing Arts Venue" : "Arts & Entertainment",
    "Convenience Store" : "Shop & Service",
    "French Restaurant" : "Food",
    "Bookstore" : "Shop & Service",
    "Bike Shop" : "Shop & Service",
    "Campground" : "Outdoors & Recreation",
    "Gas Station / Garage" : "Shop & Service",
    "Parking" : "Professional & Other Places",
    "Salad Place" : "Food",
    "Art Gallery" : "Arts & Entertainment",
    "Video Game Store" : "Shop & Service",
    "Toy / Game Store" : "Shop & Service",
    "Event Space" : "Professional & Other Places",
    "Vegetarian / Vegan Restaurant" : "Food",
    "Sushi Restaurant" : "Food",
    "Convention Center" : "Professional & Other Places",
    "Chinese Restaurant" : "Food",
    "Latin American Restaurant" : "Food",
    "Spa / Massage" : "Shop & Service",
    "Paper / Office Supplies Store" : "Shop & Service",
    "Candy Store" : "Food",
    "Camera Store" : "Shop & Service",
    "Breakfast Spot" : "Food",
    "Southern / Soul Food Restaurant" : "Food",
    "Cosmetics Shop" : "Shop & Service",
    "Community College" : "College & University",
    "Fried Chicken Joint" : "Food",
    "Plaza" : "Outdoors & Recreation",
    "Dessert Shop" : "Food",
    "Cemetery" : "Outdoors & Recreation",
    "Museum" : "Arts & Entertainment",
    "Bagel Shop" : "Food",
    "Arcade" : "Arts & Entertainment",
    "Concert Hall" : "Arts & Entertainment",
    "Athletic & Sport" : "Outdoors & Recreation",
    "Middle Eastern Restaurant" : "Food",
    "Theater" : "Arts & Entertainment",
    "Medical School" : "College & University",
    "Tea Room" : "Food",
    "Movie Theater" : "Arts & Entertainment",
    "Comedy Club" : "Arts & Entertainment",
    "Post Office" : "Professional & Other Places",
    "Seafood Restaurant" : "Food",
    "Scenic Lookout" : "Outdoors & Recreation",
    "Housing Development" : "Residence",
    "Synagogue" : "Professional & Other Places",
    "Donut Shop" : "Food",
    "General Entertainment" : "Arts & Entertainment",
    "Pool" : "Arts & Entertainment",
    "Japanese Restaurant" : "Food",
    "Arts & Entertainment" : "Arts & Entertainment",
    "Pet Store" : "Shop & Service",
    "German Restaurant" : "Food",
    "Indian Restaurant" : "Food",
    "Garden" : "Outdoors & Recreation",
    "Hot Dog Joint" : "Food",
    "Steakhouse" : "Food",
    "Bowling Alley" : "Arts & Entertainment",
    "Smoke Shop" : "Shop & Service",
    "Pool Hall" : "Arts & Entertainment",
    "Harbor / Marina" : "Travel & Transport",
    "Thai Restaurant" : "Food",
    "Bakery" : "Food",
    "Food" : "Food",
    "Ramen /  Noodle House" : "Food",
    "College Theater" : "College & University",
    "Mediterranean Restaurant" : "Food",
    "Beer Garden" : "Nightlife Spot",
    "African Restaurant" : "Food",
    "Outdoors & Recreation" : "Outdoors & Recreation",
    "River" : "Outdoors & Recreation",
    "Sorority House" : "College & University",
    "Beach" : "Outdoors & Recreation",
    "Casino" : "Arts & Entertainment",
    "Malaysian Restaurant" : "Food",
    "High School" : "College & University",
    "Snack Place" : "Food",
    "Taxi" : "Travel & Transport",
    "College & University" : "College & University",
    "Record Shop" : "Shop & Service",
    "Temple" : "Professional & Other Places",
    "Historic Site" : "Arts & Entertainment",
    "Rest Area" : "Travel & Transport",
    "Furniture / Home Store" : "Shop & Service",
    "History Museum" : "Arts & Entertainment",
    "Recycling Facility" : "Shop & Service",
    "Bridal Shop" : "Shop & Service",
    "Library" : "Professional & Other Places",
    "Nail Salon" : "Shop & Service",
    "Professional & Other Places" : "Professional & Other Places",
    "Nursery School" : "Professional & Other Places",
    "Sculpture Garden" : "Arts & Entertainment",
    "Antique Shop" : "Shop & Service",
    "Taco Place" : "Food",
    "South American Restaurant" : "Food",
    "Law School" : "College & University",
    "Thrift / Vintage Store" : "Shop & Service",
    "Brazilian Restaurant" : "Food",
    "Winery" : "Professional & Other Places",
    "Greek Restaurant" : "Food",
    "Falafel Restaurant" : "Food",
    "Tapas Restaurant" : "Food",
    "City" : "Professional & Other Places",
    "Eastern European Restaurant" : "Food",
    "Korean Restaurant" : "Food",
    "Ski Area" : "Outdoors & Recreation",
    "Rental Car Location" : "Shop & Service",
    "Spiritual Center" : "Professional & Other Places",
    "Science Museum" : "Arts & Entertainment",
    "Car Dealership" : "Shop & Service",
    "Flea Market" : "Shop & Service",
    "Art Museum" : "Arts & Entertainment",
    "Gift Shop" : "Shop & Service",
    "Portuguese Restaurant" : "Food",
    "Flower Shop" : "Shop & Service",
    "Hobby Shop" : "Shop & Service",
    "Car Wash" : "Shop & Service",
    "Board Shop" : "Shop & Service",
    "Brewery" : "Nightlife Spot",
    "Cajun / Creole Restaurant" : "Food",
    "Mac & Cheese Joint" : "Food",
    "Shop & Service" : "Shop & Service",
    "Vietnamese Restaurant" : "Food",
    "Video Store" : "Shop & Service",
    "Travel & Transport" : "Travel & Transport",
    "Dim Sum Restaurant" : "Food",
    "Racetrack" : "Arts & Entertainment",
    "Elementary School" : "Professional & Other Places",
    "Zoo" : "Arts & Entertainment",
    "Design Studio" : "Shop & Service",
    "Gaming Cafe" : "Shop & Service",
    "Swiss Restaurant" : "Food",
    "Travel Lounge" : "Travel & Transport",
    "Trade School" : "College & University",
    "Australian Restaurant" : "Food",
    "Funeral Home" : "Professional & Other Places",
    "Shrine" : "Professional & Other Places",
    "Peruvian Restaurant" : "Food",
    "College Stadium" : "College & University",
    "Fraternity House" : "College & University",
    "Bike Rental / Bike Share" : "Shop & Service",
    "Filipino Restaurant" : "Food",
    "Arepa Restaurant" : "Food",
    "Turkish Restaurant" : "Food",
    "Embassy / Consulate" : "Professional & Other Places",
    "Aquarium" : "Arts & Entertainment",
    "Scandinavian Restaurant" : "Food",
    "Middle School" : "Professional & Other Places",
    "Financial or Legal Service" : "Shop & Service",
    "Fish & Chips Shop" : "Food",
    "Mosque" : "Professional & Other Places",
    "Afghan Restaurant" : "Food",
    "Motorcycle Shop" : "Shop & Service",
    "Fair" : "Professional & Other Places",
    "Ethiopian Restaurant" : "Food",
    "Distillery" : "Professional & Other Places",
    "Gluten-free Restaurant" : "Food",
    "Argentinian Restaurant" : "Food",
    "Moroccan Restaurant" : "Food",
    "Nightlife Spot" : "Nightlife Spot",
    "Planetarium" : "Arts & Entertainment",
    "Storage Facility" : "Shop & Service",
    "Molecular Gastronomy Restaurant" : "Food",
    "Internet Cafe" : "Shop & Service",
    "Military Base" : "Professional & Other Places",
    "Newsstand" : "Shop & Service",
    "Public Art" : "Arts & Entertainment",
    "Market" : "Shop & Service",
    "Photography Lab" : "Shop & Service",
    "Garden Center" : "Shop & Service",
    "Music School" : "Professional & Other Places",
    "Castle" : "Outdoors & Recreation",
    "Pet Service" : "Shop & Service",
}

locFilter = []
for k,v in categories.items():
    if v == "Travel & Transport":
        locFilter.append(k)

users = []

locations = []
history ={}
usersWithHome={}
usersWithOffice={}
uwithoffice=0
uwithhome = 0
U = {}
dataset = "NY/dataset.txt"
lasttime = {}
lastloc = {}
doubles = 0


with open(dataset) as f:
    for line in f:
        values = line.split('\t')
        uid = int(values[0])
        location = values[3]
        time = parser.parse(values[7])
        if not lastloc.has_key(uid):
            lastloc[uid] = ""
        if not lasttime.has_key(uid):
            lasttime[uid] = datetime.now()
        if location == lastloc[uid] and time.day == lasttime[uid].day and time.month == lasttime[uid].month and time.year == lasttime[uid].year:
            doubles+=1
            continue
        if location in locFilter:
            continue
        lasttime[uid] = time
        lastloc[uid] = location

        #location = categories[location]
        if location not in locations:
            locations.append(location)



lastday = -99
dayc = -1
print "Duplicates:" + str(doubles)
with open(dataset) as f:
    for line in f:
        count = count + 1
        values = line.split('\t')
        location = values[3]
        uid = int(values[0])
        time = parser.parse(values[7])
        if not lastloc.has_key(uid):
            lastloc[uid] = ""
        if not lasttime.has_key(uid):
            lasttime[uid] = datetime.now()
        if location == lastloc[uid] and time.day == lasttime[uid].day and time.month == lasttime[uid].month and time.year == lasttime[uid].year:
            doubles+=1
            continue
        if location in locFilter:
            continue
        lasttime[uid] = time
        lastloc[uid] = location
        if uid not in users:
            users.append(uid)
        
        if not history.has_key(uid):
            history[uid] = 0

        history[uid] = history[uid] + 1
        time = parser.parse(values[7])
        if not time.day == lastday:
            dayc+=1
            lastday = time.day


        
        #location = categories[location]
        lid = locations.index(location)

        if not U.has_key(uid):
            U[uid] = {}

        if not U[uid].has_key(dayc):
            U[uid][dayc] = []

        U[uid][dayc].append(lid)
        
        #if (uid == 525):
        #    print location

with open('locations.txt', 'a') as f:
    for l in locations:
        f.write("\t\"" + l + "\" : \"\",\n")      

print 'Users:' + str(len(users))
print 'Locations:' + str(len(locations))
print 'Data:' + str(count)
print 'Average:' + str(float(count) / float(len(users)))
print 'Users with home:' + str(uwithhome)
print 'Users with office:' + str(uwithoffice)

uwithhomeoffice = 0

for uid in users:
    if usersWithHome.has_key(uid) and usersWithOffice.has_key(uid):
        uwithhomeoffice+=1

print 'User with home and office:' + str(uwithhomeoffice)


O = sorted(history.items(), key=itemgetter(1), reverse=True)

S = {}

for i in xrange(0,100):
    uid = O[i][0]
    with open(str(uid) + '.txt', 'w') as f:
        h = U[uid]
        for d in h.items():
            line = ""
            for c in d[1]:
                line += str(c) + " -1 "
            line += "-2\n"
            f.write(line)
    count = 0
    #p = subprocess.Popen('java -jar spmf.jar run PrefixSpan ' + str(uid) + ".txt output.txt 10%", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen('java -jar spmf.jar run SPAM ' + str(uid) + ".txt output.txt 0.1 2 99", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        if count == 3: #6
            S[uid] = [int(s) for s in line.split() if s.isdigit()][0]
        count += 1
    retval = p.wait()

B = sorted(S.items(), key=itemgetter(1), reverse=True)



uidFilter = []

for i in xrange(0,50):
    b = B[i]
    uidFilter.append(b[0])
    print str(b[0]) + " : " + str(b[1])

with open(dataset) as f:
    with open('filtered_dataset_NY_final.txt', 'w') as o:
        for line in f:
            values = line.split('\t')
            uid = int(values[0])
            location = values[3]
            time = parser.parse(values[7])
            if not lastloc.has_key(uid):
                lastloc[uid] = ""
            if not lasttime.has_key(uid):
                lasttime[uid] = datetime.now()
            if location == lastloc[uid] and time.day == lasttime[uid].day and time.month == lasttime[uid].month and time.year == lasttime[uid].year:
                doubles+=1
                continue
            if location in locFilter:
                continue
            lasttime[uid] = time
            lastloc[uid] = location
            uid = int(values[0])
            if uid in uidFilter:
                o.write(line)

