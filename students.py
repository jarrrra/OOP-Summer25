def add_student(students, first_name, last_name, index_number, nationality, starting_date, courses):
  students.append({'first_name' : first_name, 'last_name' : last_name, 'index_number' : index_number, 'nationality' : nationality, 'starting_date' : starting_date,'courses' : courses})

def get_students(students):
  for student in students[:-1]:
    print(student['first_name'], ' ', student['last_name'], ' ', student['index_number'], end = ', ')
  print(students[-1]['first_name'], ' ', students[-1]['last_name'], ' ', students[-1]['index_number'])

students = [{
  'first_name' : 'John',
  'last_name' : 'Doe',
  'index_number' : 10013,
  'nationality' : 'undisclosed',
  'starting_date' : 'September 1st',
  'courses' : ['Math', 'Economics'] 
},
{
  'first_name' : 'Jane',
  'last_name' : 'Doe',
  'index_number' : 10012,
  'nationality' : 'undisclosed',
  'starting_date' : 'September 1st',
  'courses' : ['Managment', 'Economics'] 
},
{
  'first_name' : 'Robert',
  'last_name' : 'Sponge',
  'index_number' : 10014,
  'nationality' : 'american(?)',
  'starting_date' : 'October 7th',
  'courses' : ['Milkshakes class'] 
}]

get_students(students)
add_student(students, 'Leo', 'Brown', 10015, 'unknown', 'September 2nd', ['Math', 'Computer Science'])
get_students(students)
