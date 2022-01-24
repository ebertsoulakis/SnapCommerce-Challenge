import pandas as pd
import string

#Data that needs to be cleaned
data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

#Split data into individual entries
splits = data.split("\n")
splitsAgain = []
for s in splits:
    temp = s.split(';')
    splitsAgain.append(temp)

#Remove last empty element
splitsAgain.pop()

#Perform data cleaning
for i in range(len(splitsAgain)):
    
    #First entry is headers and don't need to be cleaned except for last column
    if i != 0:
        #Remove all punctuation, numbers and extra spaces from Airline Codes
        splitsAgain[i][0] = splitsAgain[i][0].translate(str.maketrans('', '', string.punctuation))
        splitsAgain[i][0] = splitsAgain[i][0].translate(str.maketrans('', '', string.digits)).strip()
        
        #If Flight Code doesn't exist, add it
        if splitsAgain[i][2] == '':
            splitsAgain[i][2] = 20015 + ((i-1)*10)
        #Convert Flight Code to integer
        else:
            splitsAgain[i][2] = int(splitsAgain[i][2][:5])
        
    #Split last data entry into two different columns, "To" and "From"    
    toFrom = splitsAgain[i][3].split("_")
    #Correctly capitalize "To" column
    splitsAgain[i][3] = toFrom[0].capitalize()
    #Special case for 'New York' since it is entered as "NEWyork"
    if 'NEW' in toFrom[1]:
        toFrom[1] = 'New York'
        splitsAgain[i].append(toFrom[1])
    #If not 'New York', correctly capitalize "From" column
    else:
        splitsAgain[i].append(toFrom[1].capitalize())

dataDict = {}
headers = splitsAgain.pop(0)
indexes = []

#Create dictionary to be used in pandas data frame
for index in range(len(headers)):
    dataDict[headers[index]] = [x[index] for x in splitsAgain]
    indexes.append(f"Flight {index+1}")

#create data frame
table = pd.DataFrame(dataDict, index=indexes)
pd.set_option('display.colheader_justify', 'center')
print(table)


