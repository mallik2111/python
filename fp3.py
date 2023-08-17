while True:
    n = int(input("Enter a number: "))
    if n>0:
        break

for _ in range(n):
    print("Hello")


students =["Vachu", "Samu", "Sneha", "Sanjana","Souparnika"]
i=1
for student in students:
    print(i, student)
    i+=1

for i in range(len(students)):
    print(i+1, students[i])

students = {"Vachu":"BNG",
             "Sneha":"BNG",
             "Sanjana":"Dwd",
             "Souparnika":"Hyd" 
}
for student in students:
    print(student, students[student], sep=",")

student1 = [{"name": "Vachan", "place":"BNG", "school": "SRS"},
            {"name": "Sneha", "place":"BNG", "school": "LMF"},
            {"name": "Sanjana", "place":"DWD", "school": "classic"},
            {'name':'Souparnika', "place": "Hyd", "school": None} 
]

for student in student1:
    print(student["name"], student["school"], student['place'], sep = )
