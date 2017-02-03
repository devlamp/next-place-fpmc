# coding: utf8
import numpy
from datetime import datetime
import operator
from operator import itemgetter
from dateutil import parser
import pickle
import os.path

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

 

class DatasetParser:
    def __init__(self, path, categories, n):
        self.I = []
        self.H = []
        self.n = n
        self.__parseFile(path, categories)
        self.L = self.__locationCombination(self.I, n)
        self.D, self.T = self.__flattenHistory(self.H)


    def __parseFile(self, path, categories):
        with open(path) as f:
            USERS = {}
            count = 0
            for line in f:
                values = line.split('\t')
                uid = int(values[0])
                location = values[3]
        
                if categories:
                    location = categories[location]

                time = parser.parse(values[7])
                if not USERS.has_key(uid):
                    USERS[uid]=count
                    count = count + 1

                u = USERS[uid]

                if location not in self.I:
                    self.I.append(location)

                l = self.I.index(location)

                if u >= len(self.H):
                    self.H.append([])
                self.H[u].append((l,time))
            f.close()
    
    def __locationCombination(self, I, n):
        L = I

        for i in xrange(n-1):
            L = self.__combinateLists(L, I)
        return L
    
    def __combinateLists(self, A, B):
        C = []
        for a in A:
            for b in B:
                C.append(a+"-"+b)
        return C

    def __last_location(self, I, L, user, eid):
        if (eid - self.n >= 0):
            #t1 = user[eid][1]
            #t2 = user[eid-1][1]
            valid = True
            loc = I[user[eid-1][0]]
            for i in xrange(1, self.n + 1):
                #print i
                if i > 1:
                    loc = I[user[eid-i][0]] + "-" + loc
                    
                if user[eid-i+1][1].day != user[eid-i][1].day:
                    valid = False

            if (valid):
                l = L.index(loc)
                return l
            else:
                return -1
        else:
             return -1
    
    def __flattenHistory(self, H): # This function will flatten the UserHistories to a Dataset and a Testdataset consisting of (u, l, i)-Tuples
        O = []
        T = []
        C = 0
        uid = 0
        for u in H:
            eid = 0
            for i in xrange(0,len(u)):
                t = u[i]
                l = self.__last_location(self.I,self.L,u,eid)
                if not l == -1:
                    if i < 0.9 * len(u):
                        O.append((uid, l, t[0]))
                    else:
                        T.append((uid, l, t[0]))
                C+=1
                eid+=1
            uid+=1
        print "shrinked dataset from " + str(C) + " to " + str(len(O)) + " and testdata: " + str(len(T))  
        print "Users: " + str(uid)
        return O, T

class FPMC(object):
    lambdaUI = 0.02
    lambdaIU = 0.02
    lambdaIL = 0.02
    lambdaLI = 0.02
    alpha = 0.002
    def __init__(self, D, T, I, L, kui, kil, n, dataset):
        self.D = D
        self.I = I
        self.T = T
        self.n = n
        self.dataset = dataset
        self.kui = kui
        self.kil = kil
        self.VUI = numpy.random.rand(len(D),kui)
        self.VIU = numpy.random.rand(len(I),kui)
        self.VIL = numpy.random.rand(len(I),kil)
        self.VLI = numpy.random.rand(len(L),kil)
    
    
    def sigma(self, x):
        return 1 / (1 + numpy.exp(-numpy.abs(x)))

    def x(self, u,l,i):
        return numpy.dot(self.VUI[u], self.VIU[i]) + numpy.dot(self.VIL[i], self.VLI[l])

    def train(self, steps):
        for step in xrange(steps):
            if (step % 1000 == 0):
                pass
                #print str(int(float(step) / float(steps) * 100))+'%'

            dataid = numpy.random.randint(0,len(self.D))
            data = self.D[dataid]

            u = data[0]
            l = data[1]
            i = data[2]
            j = numpy.random.randint(0, len(self.I))
            delta = 1 - self.sigma(self.x(u,l,i)- self.x(u,l,j)) # should the second l be j specific?

            for f in xrange(self.kui):
                self.VUI[u,f] = self.VUI[u,f] + self.alpha * (delta * (self.VIU[i, f] - self.VIU[j,f]) - self.lambdaUI * self.VUI[u,f])
                self.VIU[i,f] = self.VIU[i,f] + self.alpha * (delta * self.VUI[u,f] - self.lambdaIU * self.VIU[i,f])
                self.VIU[j,f] = self.VIU[j,f] + self.alpha * (-delta * self.VUI[u,f] - self.lambdaIU * self.VIU[j,f])

            for f in xrange(self.kil):
                eta = self.VLI[l,f]

                self.VIL[i,f] = self.VIL[i,f] + self.alpha * (delta * eta - self.lambdaIL * self.VIL[i,f])
                self.VIL[j,f] = self.VIL[j,f] + self.alpha * (-delta * eta - self.lambdaIL * self.VIL[j,f])
                self.VLI[l,f] = self.VLI[l,f] + self.alpha * (delta * (self.VIL[i,f] - self.VIL[j,f]) - self.lambdaLI * self.VLI[l,f])
    
    def fmeasure(self, iteration):
        positives = 0
        falsepositives = 0
        distances = 0
        LP = {}
        LFP = {}
        LFN = {}
        for d in self.T:
            u = d[0]
            l = d[1]
            i = d[2]
        
            K = {}
            for c in xrange(len(self.I)):
                K[c] = self.x(u,l,c)
                #print "MF:" + str(numpy.dot(self.VUI[u], self.VIU[i]))
                #print "FMC:" + str(numpy.dot(self.VIL[i], self.VLI[l]))
            O = sorted(K.items(), key=itemgetter(1), reverse=True)
        
            k = O[0]
            predicted_i = k[0]

            if (i == predicted_i):
                #print k
                if not LP.has_key(i):
                    LP[i] = 0
                LP[i]+=1
                positives += 1
            else:
                if not LFP.has_key(predicted_i):
                    LFP[predicted_i] = 0
                LFP[predicted_i] += 1
                if not LFN.has_key(i):
                    LFN[i] = 0
                LFN[i] += 1
            
                distance = 0
                for a in O:
                    distance+=1
                    if a[0] == i:
                        break
                    
                distances+=distance
                falsepositives += 1
        accuracy = float(positives) / float(positives + falsepositives)

        fp = 0
        re = 0
        i_count = 0
        for i in xrange(len(self.I)):
            if not LP.has_key(i):
                LP[i] = 0
            if not LFP.has_key(i):
                LFP[i] = 0
            if not LFN.has_key(i):
                LFN[i] = 0
            
            if (LFP[i] + LP[i]) != 0:
                i_count+=1
                fp += float(LP[i]) / float(LFP[i] + LP[i])
        fp = fp / float(i_count) 

        i_count = 0
        for i in xrange(len(self.I)):         
            if (LP[i] + LFN[i]) != 0:
                i_count+=1
                #print self.I[i] + ":" + str(LFN[i])
                re += float(LP[i])/ float(LFN[i] + LP[i])
        re = re / float(i_count)



        f_measure = 0
        if (fp+re!=0):
            f_measure = 2 * (fp * re) / (fp + re)
        
        avgdistance = 0
        if (falsepositives!=0):
            avgdistance= float(distances) / float(falsepositives)
        sum = 0

        for i in xrange(len(self.I)):
            sum += LFN[i]
        
        
        output = ""
        output+= self.__class__.__name__+"\t"
        output+= self.dataset+"\t"
        output+= str(self.n)+"\t"
        output+= str(self.kil)+"\t"
        output+= str(self.kui)+"\t"
        output+= str(iteration)+"\t"
        output+= str(avgdistance)+"\t" #avg. distance
        output+= str(fp)+"\t" #precision
        output+= str(accuracy)+"\t"
        output+= str(re)+"\t" #recall
        output+= str(f_measure)+"\t"

        with open("result.txt", "a") as o:
            o.write(output+"\n")

        print "Datapoints: " + str(len(self.T))
        print "LFN: " + str(sum)
        #print "Avg. Distance" + str(float(distances) / float(falsepositives))
        print "Precision: " + str(fp)
        print "Accuracy: " + str(accuracy)
        print "Recall: " + str(re)
        print "F-Measure:" + str(f_measure)

class FMC(FPMC):
    def __init__(self, D, T, I, L, kui, kil, n, dataset):
        super(FMC, self).__init__(D,T,I,L,0,kil, n, dataset)
    
    def x(self, u,l,i):
        return numpy.dot(self.VIL[i], self.VLI[l])

class MF(FPMC):
    def __init__(self, D, T, I, L, kui, kil, n, dataset):
        super(MF, self).__init__(D,T,I,L,kui,0, n, dataset)
    
    def x(self, u,l,i):
        return numpy.dot(self.VUI[u], self.VIU[i])


class TEST(FPMC):
    def __init__(self, D, T, I, L, kui, kil, n, dataset):
        super(TEST, self).__init__(D,T,I,L,kui,kil, n, dataset)

    def x(self, u,l,i):
        return numpy.dot(self.VUI[u], self.VIU[i])
    
    def y(self, u,l,i):
        return numpy.dot(self.VIL[i], self.VLI[l])

    def train(self, steps):
        for step in xrange(steps):
            if (step % 1000 == 0):
                pass
                #print str(int(float(step) / float(steps) * 100))+'%'

            dataid = numpy.random.randint(0,len(self.D))
            data = self.D[dataid]

            u = data[0]
            l = data[1]
            i = data[2]

            j = numpy.random.randint(0, len(self.I))
            while j == i:
                j = numpy.random.randint(0, len(self.I))
            
            delta = 1 - self.sigma(self.x(u,l,i)- self.x(u,l,j)) # should the second l be j specific?

            for f in xrange(self.kui):
                self.VUI[u,f] = self.VUI[u,f] + self.alpha * (delta * (self.VIU[i, f] - self.VIU[j,f]) - self.lambdaUI * self.VUI[u,f])
                self.VIU[i,f] = self.VIU[i,f] + self.alpha * (delta * self.VUI[u,f] - self.lambdaIU * self.VIU[i,f])
                self.VIU[j,f] = self.VIU[j,f] + self.alpha * (-delta * self.VUI[u,f] - self.lambdaIU * self.VIU[j,f])

            delta = 1 - self.sigma(self.y(u,l,i)- self.y(u,l,j)) 

            for f in xrange(self.kil):
                eta = self.VLI[l,f]

                self.VIL[i,f] = self.VIL[i,f] + self.alpha * (delta * eta - self.lambdaIL * self.VIL[i,f])
                self.VIL[j,f] = self.VIL[j,f] + self.alpha * (-delta * eta - self.lambdaIL * self.VIL[j,f])
                self.VLI[l,f] = self.VLI[l,f] + self.alpha * (delta * (self.VIL[i,f] - self.VIL[j,f]) - self.lambdaLI * self.VLI[l,f])
    
    def fmeasure(self, iteration):
        positives = 0
        falsepositives = 0
        distances = 0
        LP = {}
        LFP = {}
        LFN = {}
        for d in self.T:
            u = d[0]
            l = d[1]
            i = d[2]
        
            K = {}
            for c in xrange(len(self.I)):
                K[c] = numpy.dot(self.VUI[u], self.VIU[c])
                #print "MF:" + str(numpy.dot(self.VUI[u], self.VIU[i]))
                #print "FMC:" + str(numpy.dot(self.VIL[i], self.VLI[l]))

            J = {}
            for c in xrange(len(self.I)):
                J[c] = numpy.dot(self.VIL[c], self.VLI[l])

            O = sorted(K.items(), key=itemgetter(1), reverse=True)
            N = sorted(J.items(), key=itemgetter(1), reverse=True)
        
            P = {}
            for c in xrange(len(self.I)):
                o_pos = 0
                n_pos = 0
                for a in xrange(len(O)):
                    b = O[a]
                    if b[0] == c:
                        o_pos = a
                for a in xrange(len(N)):
                    b = N[a]
                    if b[0] == c:
                        n_pos = a
                P[c] = (o_pos + n_pos) / float(2)
                
            M = sorted(P.items(), key=itemgetter(1))

            k = M[0]
            #print k
            predicted_i = k[0]
        
            if (i == predicted_i):
                #print k
                if not LP.has_key(i):
                    LP[i] = 0
                LP[i]+=1
                positives += 1
            else:
                if not LFP.has_key(predicted_i):
                    LFP[predicted_i] = 0
                LFP[predicted_i] += 1
                if not LFN.has_key(i):
                    LFN[i] = 0
                LFN[i] += 1
            
                distance = 0
                for a in O:
                    distance+=1
                    if a[0] == i:
                        break
                    
                distances+=distance
                falsepositives += 1
        accuracy = float(positives) / float(positives + falsepositives)

        fp = 0
        re = 0
        i_count = 0
        for i in xrange(len(self.I)):
            if not LP.has_key(i):
                LP[i] = 0
            if not LFP.has_key(i):
                LFP[i] = 0
            if not LFN.has_key(i):
                LFN[i] = 0
            
            if (LFP[i] + LP[i]) != 0:
                i_count+=1
                fp += float(LP[i]) / float(LFP[i] + LP[i])
        fp = fp / float(i_count) 

        i_count = 0
        for i in xrange(len(self.I)):         
            if (LP[i] + LFN[i]) != 0:
                i_count+=1
                #print self.I[i] + ":" + str(LFN[i])
                re += float(LP[i])/ float(LFN[i] + LP[i])
        re = re / float(i_count)

        f_measure = 0
        if (fp+re!=0):
            f_measure = 2 * (fp * re) / (fp + re)
        
        avgdistance = 0
        if (falsepositives!=0):
            avgdistance= float(distances) / float(falsepositives)
        sum = 0

        for i in xrange(len(self.I)):
            sum += LFN[i]
        
        
        output = ""
        output+= self.__class__.__name__+"\t"
        output+= self.dataset+"\t"
        output+= str(self.n)+"\t"
        output+= str(self.kil)+"\t"
        output+= str(self.kui)+"\t"
        output+= str(iteration)+"\t"
        output+= str(avgdistance)+"\t" #avg. distance
        output+= str(fp)+"\t" #precision
        output+= str(accuracy)+"\t"
        output+= str(re)+"\t" #recall
        output+= str(f_measure)+"\t"

        with open("result.txt", "a") as o:
            o.write(output+"\n")

        print "Datapoints: " + str(len(self.T))
        print "LFN: " + str(sum)
        #print "Avg. Distance" + str(float(distances) / float(falsepositives))
        print "Precision: " + str(fp)
        print "Accuracy: " + str(accuracy)
        print "Recall: " + str(re)
        print "F-Measure:" + str(f_measure)

#dataset = DatasetParser("filtered_dataset_TY_2.txt", False, 3)
#datasetCategories = DatasetParser("filtered_dataset.txt", categories, 1)
K = [8, 16, 32, 64, 128]
N = [1, 2, 3]
SETS = {"filtered_dataset_TY_final.txt", "filtered_dataset_NY_final.txt"}
#E3 = FMC(dataset.D, dataset.T, dataset.I, dataset.L, 128, 256)
#for i in xrange(100):
#    print i
#    E3.train(100000)
#    E3.fmeasure()

for k in K:
    for n in N:
        for s in SETS:
            dataset = DatasetParser(s, False, n)
            print k
            print s
            print n

            E1 = TEST(dataset.D, dataset.T, dataset.I, dataset.L, k, k, n, s)
            E1.fmeasure(-1)
            for i in xrange(50):
                print i
                E1.train(100000)
                E1.fmeasure(i)

            E1 = MF(dataset.D, dataset.T, dataset.I, dataset.L, k, k, n, s)
            E1.fmeasure(-1)
            for i in xrange(50):
                print i
                E1.train(100000)
                E1.fmeasure(i)

            E1 = FMC(dataset.D, dataset.T, dataset.I, dataset.L, k, k, n, s)
            E1.fmeasure(-1)
            for i in xrange(50):
                print i
                E1.train(100000)
                E1.fmeasure(i)

            E1 = FPMC(dataset.D, dataset.T, dataset.I, dataset.L, k, k, n, s)
            E1.fmeasure(-1)
            for i in xrange(50):
                print i
                E1.train(100000)
                E1.fmeasure(i)

#E2 = MF(dataset.D, dataset.T, dataset.I, dataset.L, 128*16, 128)
#for i in xrange(10):
#    print i
#    E2.train(100000)
#    E2.fmeasure()

