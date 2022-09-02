# quetion-1
ages = [19,22,19,24,20,25,26,24,25,24]
# sorting the list 
ages.sort()
# finding the minimum age from the list ages
minimum = ages[0]
# finding the maximum age from the list ages
maximum = ages[-1]
# printing the sorted list and minimum and maximum values in the list
print(ages)
print(minimum)
print(maximum)
length = len(ages)
# finding the median 
if length%2 == 1:
	median = ages[length//2]
else:
	median = (ages[length//2-1]+ages[length//2])/2
# printing the median
print(median)
# finding the average
average = sum(ages)/len(ages)
# printing the average
print(average)
# since the range is the keyword in python, variable name should not be the same
rangee = maximum-minimum
print(rangee)




# question-2
# creating an empty dictionary called dog
dog = {}
# adding name to dog dictionary
dog['name'] = 'gimmy'
# adding color to dog dictionary
dog['color'] = 'white'
# adding breed to the dog dictionary
dog['breed'] = 'german'
# adding legs to the dog dictionary
dog['legs'] = 4
# adding age to the dog dictionary
dog['age'] = 6
# printing the dog dictionary
print(dog)

# creating the student dictionary
student = {'first_name':'Alekhya','last_name':'bhimereddy','gender':'Female','age':23,'marital_status':'single','skills':['python','c','sql','mongoDB'],'country':'India','city':'Guntur','address':'Kothapet'}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('flask')
print(student.keys())
print(student.values())


# question-3
brothers = ('Sai','Guna')
sisters = ('yamini','Vidya','Joshnika')
siblings = brothers + sisters
print(len(siblings))

family_members = siblings + ('Nagi reddy','Madhavi')
print(family_members)



# question-4
it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
age = [22,19,24,25,26,24,25,24]
# fiding the length of it companies
print(len(it_companies))
# adding twitte to it_companies
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Netflix','ussa','Salesforce'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

# remove method will remove the specified element from the set. if the specified element is not present in the set, it will give keyerror
# discard method will also remove the specified element from the set. if the specifed element is not present it wont raise any keyerror

C = A.union(B)
print(C)
C = A.intersection(B)
print(C)
print(A.issubset(B))
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del(A)
del(B)
ages_set = set(ages)
print(len(ages))
print(len(ages_set))

# question-5
radius = 30
_area_of_circle_ = 3.14*radius**2
print(_area_of_circle_)
_circum_of_circle_ = 2*3.14*radius
print(_circum_of_circle_)
radius = int(input('Enter radius: '))
_area_of_circle_ = 3.14*radius**2
print(_area_of_circle_)

# question-6
string = 'I am teacher and I love to inspire and teach people'
print(set(string.split()))

# question-7
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# question-8
radius = 10
area = 3.14*radius**2
print('The area of a circle with radius {} is {} meters square'.format(radius,area))

# question-9
n = int(input('Enter no of students : '))
weights_in_lb = []
for i in range(n):
	weights_in_lb.append(int(input('Enter weight of student-{} : '.format(i+1))))
print(weights_in_lb)
weights_in_kg = []
for i in weights_in_lb:
	weights_in_kg.append(i*0.453592)
print(weights_in_kg)