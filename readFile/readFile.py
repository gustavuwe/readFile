
fO = input('Insert here the path to the file: ')

try:
    fOpen = open(fO)
except:
    print('Cannot Open the file: ',fO)
    quit()

chooseType = input('What you want to do? Read, or Get the emails?')

if chooseType == 'Read':
    for eachLine in fOpen:
        print(eachLine)
elif chooseType == 'Get the emails':
    for eachLine in fOpen:
        eachLine = eachLine.strip()
        if eachLine.startswith('From:') :
            print(eachLine)
else:
    print('Error: digit a type available!')git init
    
