# excercise 1

students = ["Bob", "Hannah", "John", "Mark", "Nathan", "Elizabeth"]
print(students[1])
print(students[-1])

#Excercise 2

foods = ("rice", "noodles", "soup", "hamburger", "pizza", "salad")
for food in foods:
    print(f"{food} is a good food")

# Excercise 3

print(foods[-2:])

# Exercise 4

home_town = {
    "city": "Victorville",
    "state": "California",
    "population": 135950
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Excercise 5

for key,val in home_town.items():
    print(f"{key} = {val}")

# Excercise 6

cohort = []
for idx, name in enumerate(students):
    cohort.append({
        "student": name,
        "fav_food": foods[idx]
    })
print(cohort)

# Excercise 7

awesome_students = [f"{student} is awesome!" for student in students]
print(awesome_students)

# Excercise 8

foods_a = [food for food in foods if "a" in food]
print(foods_a)