import json
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        for subject, mark in self.marks.items():
            print(f"{subject} : {mark}")

    def calculate_total(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        return total

    def calculate_avg(self):
        if not self.marks:
            return 0
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_avg()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def student_report(self):
        print("========== STUDENT REPORT ==========")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

        for subject, mark in self.marks.items():
            print(f"{subject} : {mark}")

        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average: {self.calculate_avg()}")
        print(f"Grade: {self.calculate_grade()}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.roll_number_exists(student.roll_number):
            return False

        
        self.students.append(student)
        return True

    def display_all_students(self):
        if not self.students:
            print("No students available")
            return

        for student in self.students:
            student.student_report()

    def find_student(self, roll_number):
        for student in self.students:
            if roll_number == student.roll_number:
                return student
            
        return None

    def remove_student(self, roll_number):
        for student in self.students:
            if roll_number == student.roll_number:
                self.students.remove(student)
                print("Student removed successfully")
                return

        print("Student not found")
            

    def get_top_student(self):
        top_student = None
        highest_avg = 0
        for student in self.students:
            average = student.calculate_avg()
            if average >= highest_avg:
                highest_avg = average
                top_student = student
        return top_student

    def calculate_class_average(self):
        total = 0
        if not self.students:
            return 0

        for student in self.students:
            average = student.calculate_avg()
            total += average
        class_average = total / len(self.students)
        return class_average

    def grade_distribution(self):
        distribution = {
               "A": 0,
               "B": 0,
               "C": 0,
               "D": 0,
               "F": 0 }

        for student in self.students:
            grade = student.calculate_grade()
            if grade == "A":
                distribution["A"] += 1
            elif grade == "B":
                distribution["B"] += 1
            elif grade == "C":
                distribution["C"] += 1
            elif grade == "D":
                distribution["D"] += 1
            elif grade == "F":
                distribution["F"] += 1
        return distribution

    def class_report(self):
        top_student = self.get_top_student()
        distribution = self.grade_distribution()
        print("========== CLASS REPORT ==========")
        print(f"Total Students: {len(self.students)}")
        print(f"Class Average: {self.calculate_class_average()}")
        if top_student:
           print(f"Top Student: {top_student.name}")
           print(f"Top Student Average: {top_student.calculate_avg()}")
        else:
            print("Top Student: No Students Available")
        for grade, count in distribution.items():
          print(f"{grade}: {count}")

    def roll_number_exists(self, roll_number):
       for student in self.students:
        if student.roll_number == roll_number:
            return True

       return False

    def update_marks(self, roll_number):
        student = self.find_student(roll_number)

        if not student:
           print("Student Not Found")
           return

        while True:
          try:
             python_marks = int(input("Enter New Python Marks: "))

             if 0 <= python_marks <= 100:
              student.marks["PYTHON"] = python_marks
              break
             else:
              print("Marks must be between 0 and 100.")

          except ValueError:
              print("Please enter a valid number.")

        while True:
          try:
             sql_marks = int(input("Enter New SQL Marks: "))

             if 0 <= sql_marks <= 100:
              student.marks["SQL"] = sql_marks
              break
             else:
               print("Marks must be between 0 and 100.")

          except ValueError:
               print("Please enter a valid number.")

        while True:
          try:
             statistics_marks = int(input("Enter New Statistics Marks: "))

             if 0 <= statistics_marks <= 100:
               student.marks["STATISTICS"] = statistics_marks
               break
             else:
               print("Marks must be between 0 and 100.")

          except ValueError:
            print("Please enter a valid number.")
        print("Marks Updated Successfully")

    def update_student(self, roll_number):
        student = self.find_student(roll_number)

        if not student:
           print("Student Not Found")
           return

        while True:
           new_name = input("Enter New Student Name: ").strip()

           if new_name and new_name.replace(" ", "").isalpha():
              break
           else:
              print("Please enter a valid name.")
           

        while True:
           try:
            new_roll_number = int(input("Enter New Roll Number: "))

            if new_roll_number <= 0:
                print("Roll Number must be greater than 0.")
                continue

            if new_roll_number != student.roll_number and self.roll_number_exists(new_roll_number):
                print("Roll Number Already Exists")
                continue

            break

           except ValueError:
            print("Please enter a valid roll number.")

        student.name = new_name
        student.roll_number = new_roll_number

        print("Student Details Updated Successfully")

    def sort_students_by_average(self):
        sorted_students = sorted(
          self.students,
          key=lambda student: student.calculate_avg(),
          reverse=True
        )

        for student in sorted_students:
          print(f"{student.name} : {student.calculate_avg():.2f}")

    def subject_analysis(self):
        if not self.students:
          print("No Students Available")
          return

        subjects = ["PYTHON", "SQL", "STATISTICS"]

        print("========== SUBJECT ANALYSIS ==========")

        for subject in subjects:
          total = 0
          highest_marks = -1
          lowest_marks = 101

          highest_student = None
          lowest_student = None

          for student in self.students:
            marks = student.marks[subject]
            total += marks

            if marks > highest_marks:
                highest_marks = marks
                highest_student = student

            if marks < lowest_marks:
                lowest_marks = marks
                lowest_student = student

          average = total / len(self.students)

          print(f"\n{subject}")
          print(f"Average: {average:.2f}")
          print(f"Highest: {highest_student.name} - {highest_marks}")
          print(f"Lowest: {lowest_student.name} - {lowest_marks}")

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
             return student

        return None

    def sort_students_by_name(self):
        sorted_students = sorted(
         self.students,
         key=lambda student: student.name.lower()
        )

        for student in sorted_students:
            print(f"{student.name} - Roll Number: {student.roll_number}")

    def sort_students_by_roll_number(self):
        sorted_students = sorted(
        self.students,
        key=lambda student: student.roll_number
        )

        for student in sorted_students:
           print(f"{student.name} - Roll Number: {student.roll_number}")

    def save_students(self):
        data = []

        for student in self.students:
            student_data = {
            "name": student.name,
            "roll_number": student.roll_number,
            "marks": student.marks
            }

            data.append(student_data)

        with open("students.json", "w") as file:
             json.dump(data, file, indent=4)

        print("Students saved successfully")

    def load_students(self):
        try:
           with open("students.json", "r") as file:
            data = json.load(file)

           self.students = []

           for student_data in data:
            student = Student(
                student_data["name"],
                student_data["roll_number"],
                student_data["marks"]
            )

            self.students.append(student)

           print("Students loaded successfully")

        except FileNotFoundError:
          print("No saved student data found")
    
manager = StudentManager()

manager.load_students()

while True:
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. ADD STUDENT")
    print("2. Display All Students")
    print("3. Find Student By roll number")
    print("4. Find Student By Name")
    print("5. Remove Student")
    print("6. Show Top Student")
    print("7. Show Class Average")
    print("8. Show Grade Distribution")
    print("9. Show Class Report")
    print("10. Update Student Marks")
    print("11. update student details")
    print("12. Sort Students By Average")
    print("13. Sort Students By Name")
    print("14. Sort Students By Roll Number")
    print("15. Subject-Wise Analysis")
    print("16. Exit")
    
    choice = input("Enter Your Choice:")

    if choice == "16":
        manager.save_students()
        print("Exiting Student Management System...")
        break
    elif choice == "10":
        try:
          roll_number = int(input("Enter Roll Number: "))
          manager.update_marks(roll_number)
        except ValueError:
          print("Please enter a valid roll number")

    elif choice == "11":
        try:
           roll_number = int(input("Enter Roll Number: "))
           manager.update_student(roll_number)
        except ValueError:
           print("Please enter a valid roll number")

    elif choice == "1":
        while True:
           student_name = input("Enter Student Name:").strip()
           if student_name and student_name.replace(" ", "").isalpha():
             break
           else:
             print("please enter a valid name")
        while True:
            try:
               roll_number = int(input("Enter Student Roll Number"))
               break
            except ValueError:
                print("Please enter a valid roll number")

        marks = {}
        while True:
           try:
              python_marks = int(input("Enter Python Marks: "))

              if 0 <= python_marks <= 100:
                marks["PYTHON"] = python_marks
                break
              else:
                  print("Marks must be between 0 and 100.")
           except ValueError:
               print("Please enter a valid number")

        while True:
            try:
                sql_marks = int(input("Enter SQL Marks:"))
                if 0 <= sql_marks <= 100:
                  marks["SQL"] = sql_marks
                  break
                else:
                  print("Marks must be between 0 and 100")

            except ValueError:
                print("Enter a valid number")

        while True:
            try:
              statistics_marks = int(input("Enter Statistics Marks:"))
              if 0 <= statistics_marks <= 100:
                marks["STATISTICS"] = statistics_marks
                break
              else:
                print("Marks must be between 0 and 100")
            except ValueError:
                print("Enter a valid number")

        student = Student(student_name, roll_number, marks)
        if manager.add_student(student):
           print("Student Added Successfully")
        else:
           print("Roll Number Already Exists")
    elif choice == "2":
        manager.display_all_students()
    elif choice == "3":
        try:
          roll_number = int(input("Enter Roll Number:"))
          student = manager.find_student(roll_number)
          if student:
            student.student_report()
          else:
            print("Student Not Found")
        except ValueError:
            print("please enter a valid roll number")
    elif choice == "4":
        student_name = input("Enter Student Name: ").strip()

        student = manager.find_student_by_name(student_name)

        if student:
          student.student_report()
        else:
           print("Student Not Found")

    elif choice == "5":
        try:
            roll_number = int(input("Enter Roll Number"))
            manager.remove_student(roll_number)
        except ValueError:
            print("please enter a valid roll number")
    elif choice == "6":
       top_student = manager.get_top_student()

       if top_student:
          print(f"Top Student: {top_student.name}")
          print(f"Average: {top_student.calculate_avg()}")
       else:
          print("No Students Available")


    elif choice == "7":
        class_average = manager.calculate_class_average()
        print(class_average)

    elif choice == "8":
        grade_distribution = manager.grade_distribution()
        for grade, count in grade_distribution.items():
            print(f"{grade} : {count}")

    elif choice == "9":
        manager.class_report()

    elif choice == "12":
        manager.sort_students_by_average()

    elif choice == "13":
         manager.sort_students_by_name()

    elif choice == "14":
         manager.sort_students_by_roll_number()

    elif choice == "15":
         manager.subject_analysis()

    else:
        print("invalid choice")