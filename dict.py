student_courses={}
n=int(input("How students to enter:"))
m = int(input("how many courses:"))
while True:
# Menu for user interaction
    print("Menu:")
    print("1. Add Registration")
    print("2. Display Registrations")
    print("3. Query Student Courses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        for _ in range(n):
            key = input("Student Reg No:")
            courses=[]
            for _ in range(m):
                value = input("Student Courses:")
                courses.append(value)
            student_courses[key]= courses
    elif choice == '2':
        student_courses.items()
    elif choice == '3':
        print(student_courses)


"""student_courses = {}

n = int(input("How many students to enter: "))
m = int(input("How many courses per student: "))

for _ in range(n):
    key = input("Student Reg No: ")
    courses = []
    for _ in range(m):
        course = input("Enter course for student: ")
        courses.append(course)
    student_courses[key] = courses

print(student_courses)
"""