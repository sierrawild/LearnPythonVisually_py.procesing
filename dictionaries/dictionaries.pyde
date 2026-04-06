student = {'name': 'Sam', 'age': 24,}

print(student['name'])

if 'gender' in student:
    print(student['age'])
else:
    print('There is no key you are asking for')
    
student['id'] = 123
del student['age']

print(student)

students = [
    {'name': 'Sam', 'id': 123},
    {'name': 'Al', 'id': 124},
]
print(students[1]['name'])

courses = {
  'game development': 'Prof. Smith',
'web design': 'Prof. Ncube',
'code art': 'Prof. Sato'
}
