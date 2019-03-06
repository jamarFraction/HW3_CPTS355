# importing functools for reduce() 
import functools as functools

def busStops(b):

    output = {}

    for bus in b:
    
        stopsList = b.get(bus, None)

        for stop in stopsList:
            
            if output.get(stop, None) == None:
                output[stop] = [bus]
            else:
                newStopList = output[stop]
                newStopList.append(bus)
                newStopList.sort()
    
    return output

def testbusStops():

    buses = {
        "Lentil": ["Chinook", "Orchard", "Valley", "Emerald", "Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
        "Wheat": ["Chinook", "Orchard", "Valley", "Maple", "Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
        "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop", "Walmart", "Shopco", "RockeyWay"],
        "Blue": ["TransferStation", "State", "Larry", "TerreView", "Grand", "TacoBell", "Chinook", "Library"],
        "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside", "Crestview", "CityHall", "Stadium", "Colorado"]
    }

    correctOutput = {
        'Chinook': ['Blue', 'Lentil', 'Wheat'],
        'Orchard': ['Lentil', 'Wheat'], 
        'Valley': ['Lentil', 'Wheat'], 
        'Emerald': ['Lentil'], 
        'Providence': ['Lentil'], 
        'Stadium': ['Gray', 'Lentil', 'Silver'], 
        'Main': ['Gray', 'Lentil'], 
        'Arbor': ['Lentil'], 
        'Sunnyside': ['Gray', 'Lentil'], 
        'Fountain': ['Lentil'], 
        'Crestview': ['Gray', 'Lentil'], 
        'Wheatland': ['Lentil'], 
        'Walmart': ['Lentil', 'Silver', 'Wheat'], 
        'Bishop': ['Lentil', 'Silver', 'Wheat'],
        'Derby': ['Lentil'], 'Dilke': ['Lentil'], 
        'Maple': ['Wheat'], 
        'Aspen': ['Wheat'], 
        'TerreView': ['Blue', 'Wheat'], 
        'Clay': ['Wheat'], 
        'Dismores': ['Wheat'], 
        'Martin': ['Wheat'], 
        'PorchLight': ['Silver', 'Wheat'], 
        'Campus': ['Wheat'], 
        'TransferStation': ['Blue', 'Gray', 'Silver'], 
        'Shopco': ['Silver'], 
        'RockeyWay': ['Silver'], 
        'State': ['Blue'], 
        'Larry': ['Blue'], 
        'Grand': ['Blue'], 
        'TacoBell': ['Blue'], 
        'Library': ['Blue'], 
        'Wawawai': ['Gray'], 
        'CityHall': ['Gray'], 
        'Colorado': ['Gray']}

    if busStops(buses) == correctOutput:
        return True
    else:
        return False

def addDict(d):

    output = {}

    for day in d:
        
        loggedHours = d[day]

        for course in loggedHours:
            if output.get(course, None) == None:
                
                output[course] = loggedHours[course]
            else:
                
                output[course] += loggedHours[course]
    

    return output

def testaddDict():

    # Test Input
    testInput1 = {'Mon': {'355': 2, '451': 1, '360': 2}, 'Tue': {'451': 2, '360': 3}, 'Wed': {'451': 12, '360': 8}, 
    'Thu': {'355': 3, '451': 2, '360': 3}, 'Fri': {'355': 2}, 'Sun': {'355': 1, '451': 3, '360': 1}}

    testInput2 = {'Fri': {'355': 10}, 'Sat': {'479': 8, '451': 3, '360': 10}, 'Sun': {'355': 8, '451': 1, '360': 11}}

    # Run Tests
    if addDict(testInput1) != {'355': 8, '360': 17, '451': 20}:
        return False
    if addDict(testInput2) != {'355': 18, '360': 21, '451': 4, '479': 8}:
        return False
    
    # all tests passed!
    return True

def twoCourseReduction(logList1, logList2):

    for course in logList2:
        if logList1.get(course, None) == None:
            logList1[course] = logList2[course]
        else:
            logList1[course] += logList2[course]

    return logList1

def addDictN(L):

    # use map per assignment spec
    # map addDict over each week in the input list
    courseHoursLoggedByWeek = list(map(addDict, L))

    # use redue per assignment spec
    # twoCourseReduction returns the lhs values summed with the rhs values, adding to list if necessary
    output = functools.reduce(twoCourseReduction, courseHoursLoggedByWeek)

    return output

def testaddDictN(): 

    # Test Input
    testInput1 = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}}, {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}}, {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
    testInput2 = [{'Mon': {'355': 2, '360': 2, '479': 8}}, {'Mon': {'360': 2}}, {'Mon': {'350': 5}}]
    testInput3 = []

    # Run Tests
    if addDictN(testInput1) != {'355': 16, '360': 24, '451': 6}:
        return False
    if addDictN(testInput2) != {'350': 5, '355': 2, '360': 4, '479': 8}:
        return False
    if addDictN(testInput3) != {}:
        return False

    # all tests passed!
    return True



testFunctions = {"busStops": testbusStops, "addDict": testaddDict, "addDictN": testaddDictN}

# MAIN, not gucci
if __name__ == '__main__':

    for testName, testFunc in testFunctions.items():
        print(testName, ': ', testFunc())
        print('---------------------')
    
