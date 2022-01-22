import pandas as pd
import string

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

splits = data.split("\n")

splitsAgain = []


#Working solution but not pretty
for s in splits:
    temp = s.split(';')
    splitsAgain.append(temp)

splitsAgain.pop()

for i in range(len(splitsAgain)):
    
    if i != 0:
        splitsAgain[i][0] = splitsAgain[i][0].translate(str.maketrans('', '', string.punctuation)).strip()
        splitsAgain[i][0] = splitsAgain[i][0].translate(str.maketrans('', '', string.digits)).strip()
        
        if splitsAgain[i][2] == '':
            splitsAgain[i][2] = 20015 + ((i-1)*10)
        else:
            splitsAgain[i][2] = int(splitsAgain[i][2][:5])
        
        
    toFrom = splitsAgain[i][3].split("_")
    splitsAgain[i][3] = toFrom[0].capitalize()
    if 'NEW' in toFrom[1]:
        toFrom[1] = 'New York'
        splitsAgain[i].append(toFrom[1])
    else:
        splitsAgain[i].append(toFrom[1].capitalize())

dataDict = {}
headers = splitsAgain.pop(0)
indexes = []

for index in range(len(headers)):
    dataDict[headers[index]] = [x[index] for x in splitsAgain]
    indexes.append(f"Flight {index}")

table = pd.DataFrame(dataDict, index=indexes)

print(table)



print(dataDict)
#test.translate(str.maketrans('', '', string.punctuation))
#print(splitsAgain)
