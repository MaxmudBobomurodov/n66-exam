from file_manager import  read , write , generate_id , append
import csv
class Teacher:
    def __init__(self,filepath):
        self.filepath = filepath
        
    def creating_new_course(self):
        course_id = generate_id(self.filepath)
        course_name = input("Enter course name: ")
        field = input("Enter field name: ")
        price = input("Enter price: ")
        data = [course_id,course_name,field,price]
        append(self.filepath, data)
        print("New course created!")

    def show_all_courses(self):
        reader = read("data/courses.csv")
        courses = []
        for row in reader:
            courses.append(row)
            print(f"course id: {row[0]} , course name: {row[1]}, field: {row[2]}, price: {row[3]}")
        if not courses:
            print("No courses available.")

    def show_my_students(self, teacher_email):
            my_courses = []
            with open("data/courses.csv") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2].strip() == teacher_email.strip():
                        my_courses.append((row[0], row[1]))

            if not my_courses:
                print("you do not have any courses.")
                return

            for course_id, course_name in my_courses:
                print(f"\n course: {course_name}")
                found = False
                with open("data/purchases.csv") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] == course_id:
                            print(f"   👤 {row[0]}")
                            found = True
                if not found:
                    print("this course did not buy yet.")

    def change_course_price(self):
        reader = read(self.filepath)
        if not reader:
            print("you do not have any courses.")
            return

        for row in reader:
            print(f"course id: {row[0]}, course name: {row[1]}, old price: {row[3]}")

        course_id = input("Enter course id: ")
        changed_price = input("Enter changed price: ")

        found = False
        for row in reader:
            if row[0] == course_id:
                row[3] = changed_price
                found = True
                break

        if found:
            write(self.filepath, reader)
            print(f" Price has been changed to {changed_price}")
        else:
            print(" There is no such course.")

    @staticmethod
    def read_messages(teacher_email):
        print("messages sent to you : \n")
        try :
            reader = read("data/messages.csv")
            count = 0
            for row in reader:
                if len(row) != 3:
                    continue

                sender = row[0]
                receiver = row[1]
                message = row[2]

                if receiver.strip() == teacher_email.strip():
                    count += 1
                    print(f"from : {sender} , message : {message}")

            if count == 0:
                print("no messages sent to you")

        except FileNotFoundError:
            print("file not found !.")

