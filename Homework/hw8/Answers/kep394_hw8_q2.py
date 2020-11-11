'''

Kiersten Page
CS 1114
kep394

The purpose of this program is to create a method to organize weather data efficiently. It also allows
for temperatures and length measurements to be converted from imperial values to metric values. Another
purpose of the program is to retrieve the average high and low temperatures for each city.
'''

# Part A

def clean_data(complete_weather_filename, cleaned_weather_filename):
    fileIn = open(complete_weather_filename, "r")
    fileOut = open(cleaned_weather_filename, "w")
    line = fileIn.readline().split(",")
    print(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[8],file=fileOut)
    for i in fileIn:
        line = i.split(",")
        cleanLine = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + ","
        if line[8].isalpha():
            cleanLine += "0"
        else:
            cleanLine += line[8]
        print(cleanLine, file=fileOut)

    fileIn.close()
    fileOut.close()

    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.

# Part B
def f_to_c(f_temperature):
    c_temperature = ((f_temperature - 32) * (5 / 9))
    return c_temperature

def in_to_cm(inches):
    cm = (inches * 2.54)
    return cm

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    # Similar to clean_data() - read in the file and make a new file with metric values.
    fileIn = open(imperial_weather_filename, "r")
    fileOut = open(metric_weather_filename, "w")
    print(fileIn.readline(),file=fileOut)
    for i in fileIn:
        line = i.split(",")
        convertedTemp1 = f_to_c(float(line[2]))
        convertedTemp2 = f_to_c(float(line[3]))
        convertedPrecipitation = in_to_cm(float(line[4]))
        print(line[0] + "," + line[1] + "," + str(convertedTemp1) + "," + str(convertedTemp2) + "," + str(convertedPrecipitation), file=fileOut)

    fileIn.close()
    fileOut.close()

# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
    fileIn = open(weather_filename, "r")
    monthsList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    highSums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lowSums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    header = fileIn.readline()
    month = 0
    for i in fileIn:
        line = i.split(",")
        if line[0] == city:
            date = line[1].split("/")
            month = (int(date[0])-1)
            highSums[month] += float(line[2])
            lowSums[month] += float(line[3])
            countList[month] += 1
    if unit_type == "imperial":
        type = "F"
    else:
        type = "C"
    print("Average temperatures for", city)
    for k in range(12):
        print(monthsList[k], ": ", round(highSums[k]/countList[k]), type, " High, ", round(lowSums[k]/countList[k]), type, " Low", sep="")
    print() #printed just to make reading the averages for each city easier later on

    fileIn.close()


    # prints average highs and lows in each month for the given city
# Part D
# Write your question (as a comment), and implement a function to answer it

# According to the data given, what is the highest recorded temperature for each city? Round to the nearest whole number

def highest_temp(city, weather_filename, unit_type):
    fileIn = open(weather_filename, "r")
    tempList = []
    for i in fileIn:
        line = i.split(",")
        if line[0] == city:
            tempList.append(line[2])
    lengthOfList = len(tempList)
    highestTemp = 0
    currentTemp = 0
    for j in range(lengthOfList):
        currentTemp = float(tempList[j])
        if currentTemp > highestTemp:
            highestTemp = currentTemp
    if unit_type == "metric":
        type = "C"
    else:
        type = "F"

    print("The highest recorded temperature for ", city, " is ", round(highestTemp), type, sep="")

    fileIn.close()

def main():
    print ("Running Part A")
    clean_data("hw8 - weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    highest_temp("San Francisco", "weather in imperial.csv", "imperial")
    highest_temp("New York", "weather in metric.csv", "metric")
    highest_temp("San Jose", "weather in imperial.csv", "imperial")
    highest_temp("Los Angeles", "weather in metric.csv", "metric")
    highest_temp("Seattle", "weather in imperial.csv", "imperial")

main()
