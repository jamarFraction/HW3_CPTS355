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

    # Run Tests
    if addDictN(testInput1) != {'355': 16, '360': 24, '451': 6}:
        return False
    if addDictN(testInput2) != {'350': 5, '355': 2, '360': 4, '479': 8}:
        return False

    # all tests passed!
    return True

def searchDicts(L,k): 

    revList = list(L)

    revList.reverse()

    for subList in revList:
        
        if subList.get(k, None) != None:

            return subList[k]

    return None

def testsearchDicts(): 

    # Test Input
    testInput1 = [{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}]
    testInput2 = [{"t": 1, "e": "soup"}, {"z": "found"}, {"e": 80}, {"q": True, "t": 15}]

    # Run Tests
    if searchDicts(testInput1, "x") != 2:
        return False
    if searchDicts(testInput1,"y") != False:
        return False
    if searchDicts(testInput1,"z") != "found":
        return False
    if searchDicts(testInput1,"t") != None:
        return False
    if searchDicts(testInput2, "z") != "found":
        return False
    if searchDicts(testInput2, "e") != 80:
        return False
    if searchDicts(testInput2, "t") != 15:
        return False
    
    # all tests passed!
    return True

def searchDicts2Helper(index, L, k):

    valueFound = L[index][1].get(k, None)

    if index == 0:
        return valueFound

    elif valueFound == None:
        newIndex = L[index][0]
        return searchDicts2Helper(newIndex, L, k)

    else:
        return L[index][1][k] 

def searchDicts2(L,k):

    valueFound = searchDicts2Helper(len(L) - 1, L, k)

    return valueFound

def testsearchDicts2(): 

    testInput1 = [(0, {"x": 0, "y": True, "z": "zero"}),
                  (0, {"x": 1}),
                  (1, {"y": False}),
                  (1, {"x": 3, "z": "three"}),
                  (2, {})]

    testInput2 = [(0, {"x": 0, "y": True, "z": "yikes"}),
                  (0, {"z": 1}),
                  (5, {"y": 77}),
                  (0, {"d": 8, "q": "deez"}),
                  (2, {}),
                  (3, {"x": 3, "p": "three"}),
                  (2, {"x": 3})]

    if searchDicts2(testInput1, "x") != 1:
        return False
    if searchDicts2(testInput1, "y") != False:
        return False
    if searchDicts2(testInput1, "z") != "zero":
        return False
    if searchDicts2(testInput1, "t") != None:
        return False
    if searchDicts2(testInput2, "d") != 8:
        return False
    if searchDicts2(testInput2, "z") != "yikes":
        return False
    if searchDicts2(testInput2, "y") != 77:
        return False
    
    return True


testFunctions = {"busStops": testbusStops, "addDict": testaddDict,
                "addDictN": testaddDictN, "searchDicts": testsearchDicts,
                "searchDicts2": testsearchDicts2}

# MAIN, not gucci
if __name__ == '__main__':

    for testName, testFunc in testFunctions.items():
        print(testName, ': ', testFunc())
        print('---------------------')
    
