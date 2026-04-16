#1- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#2- Change the last_name of the first student from 'Jordan' to 'Bryant'
#3- In the sports_directory, change 'Messi' to 'Andres'
#4- Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x [1][0] = 15 # 1
# print(x)

print(sports_directory['basketball'][-1])

students[0]['last_name'] = "Bryant" #2
# print(students)

sports_directory['soccer'][0] = "Andres" #3
# print(sports_directory)

z[0]['y'] = 30 #4
# print(z)


#first_name - Michael, last_name - Jordan
def iterateDictionary(lista):
    for dictionary in lista:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


def iterateDictionary2(key_name, lista):
    for dictionary in lista:
        if key_name in dictionary:
            print(dictionary[key_name])

print('--- first_name ---')
iterateDictionary2('first_name', students)
print('--- last_name ---')
iterateDictionary2('last_name', students)

print('------')
def printInfo (dict):
    for key in dict:
        print(f"{len(dict[key])} {key.upper()}")
        for item in dict[key]:
            print(item)
        print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)