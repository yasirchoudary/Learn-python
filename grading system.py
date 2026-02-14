
classA2 = {
    "Raza": {
        "name": "Raza",
        "age": "21",
        "Roll no": "10",
        "Program": "BSCS",
        "Semester": "5th",
        "Session": "2024-2028",
        "Marks": None
    },
    "Asjad": {
        "name": "Asjad",
        "age": "20",
        "Roll no": "28",
        "Program": "BSCS",
        "Semester": "5th",
        "Session": "2024-2028",
        "Marks": None
    },
    "Yasir": {
        "name": "Yasir",
        "age": "21",
        "Roll no": "21",
        "Program": "BSCS",
        "Semester": "5th",
        "Session": "2024-2028",
        "Marks": None
    },
    "Sipra": {
        "name": "Sipra",
        "age": "22",
        "Roll no": "34",
        "Program": "BSCS",
        "Semester": "5th",
        "Session": "2024-2028",
        "Marks": None
    },
    "Rizwan": {
        "name": "Rizwan",
        "age": "21",
        "Roll no": "23",
        "Program": "BSCS",
        "Semester": "5th",
        "Session": "2024-2028",
        "Marks": None
    }
}
choice= input("Enter 1 to add marks\n 2 to add new student\n 3 to search for a student: \n 4 to display all students: ")
if choice == "1":
    name = input("Enter the name of the student: ")
    if name in classA2:
        if classA2[name].get("Marks") is None:
            automata = int(input("Enter marks of Automata: "))
            oop = int(input("Enter marks of OOP: "))
            coal = int(input("Enter marks of COAL: "))

            total_marks = automata + oop + coal
            percentage = (total_marks / 300) * 100

            classA2[name]["Marks"] = {
                "Automata": automata,
                "OOP": oop,
                "COAL": coal,
                "Total": total_marks,
                "Percentage": percentage
            }

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print(f"{name}, {classA2[name]['Roll no']}, {classA2[name]['Program']}, {classA2[name]['Session']} got {grade} grade with percentage {percentage}%")
        else:
            print(f"{name} already has marks recorded.")
    else:
        print("Student not found in class A2.")
if choice == "2":
    new_student = input("enter the name of new student: ")
    if new_student not in classA2:
        new_student_data = {
            "name": new_student,
            "age": input("enter age of new student: "),
            "Roll no": input("enter roll no of new student: "),
            "Program": input("enter program of new student: "),
            "Semester": input("enter semester of new student: "),
            "Session": input("enter session of new student: ")
        }
        classA2[new_student] = new_student_data
        
if choice == "3":
    search = input("enter the name of student you want to search: ")
    if search in classA2:
        print(f"{classA2[search]['name']}, {classA2[search]['age']}, {classA2[search]['Roll no']}, {classA2[search]['Program']}, {classA2[search]['Semester']}, {classA2[search]['Session']} is present in class A2")
if choice == "4":
    for key, value in classA2.items():
        print(key, value)

