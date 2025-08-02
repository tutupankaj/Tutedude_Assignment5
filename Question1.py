dict1 = {'Pankaj':81.88,'Alice':85,'Alok':40}
name = str(input('Enter the student\'s name: '))
variable1= str(dict1.get(name,'Student not found.'))
if (variable1.isnumeric()):
    print('{0}\'s marks: {1}'.format(name,variable1))
else:
    print('{0}'.format(variable1))