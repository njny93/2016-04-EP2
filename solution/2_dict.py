# make the dictionary
students = dict()

# store the student info value
students['20161001'] = 'Sherlock Holmes'
students['20161002'] = 'John Watson'
students['20161003'] = 'James Moriarty'

# print the values
for key in students.keys():
    print(key + ': ' + students[key])
