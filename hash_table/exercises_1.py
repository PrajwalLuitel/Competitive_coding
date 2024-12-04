"""nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
"""

# THe best data structure for this problem is a hashmap or a hash table (also known as dictionary in python)

class NYCWeather:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for el in key:
            hash += ord(el)

        return hash % self.MAX 

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for el in self.arr[h]:
            if el[0] == key:
                found = True
                el = (key,value)
        if not found:
            self.arr[h].append((key, value))


    def __getitem__(self, key):
        h = self.get_hash(key)
        for el in self.arr[h]:
            if el[0] == key:
                return el[1]
    

    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] != []:
            for el in self.arr[h]:
                if el[0] == key:
                    self.arr[h].remove(el)
                    return
    

if __name__=="__main__":
    nyc_weather = NYCWeather()
    nyc_weather['january 1'] = -3
    nyc_weather['january 2'] = -6
    nyc_weather['january 3'] = -5
    nyc_weather['january 4'] = -1
    nyc_weather['january 5'] = 0
    nyc_weather['january 6'] = 1
    nyc_weather['january 7'] = 7
    nyc_weather['january 8'] = -7
    nyc_weather['january 9'] = 0
    nyc_weather['january 10'] = -4

    print(f"The hashtable looks like: \n {nyc_weather.arr}")

    sum = 0
    for i in range(1,11):
        sum += nyc_weather[f"january {i}"]
    average = sum/10
    print(f"Average temperature in NYC between JAN 1 and JAN 10 is: {average} degree celcius.") 


    max = -99999
    for i in range(1, 11):
        if nyc_weather[f'january {i}'] > max:
            max = nyc_weather[f'january {i}']
    print(f"The maximum temperature between JAN 1 to JAN 10 in NYC is: {max} degree celcius.")

    """nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?"""

    print(f"The temperature on Jan 9 is: {nyc_weather['january 9']}")
    print(f"The temperature on Jan 4 is: {nyc_weather['january 4']}")