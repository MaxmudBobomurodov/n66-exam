from teacher_func import Teacher
from student_func import Student

def student_menu(email: str):
    student = Student(email)
    print("""
    1.show course lists
    2.buy course
    3.show bought courses
    4.send message to teacher
    5.exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student.show_course_lists()
    elif choice == 2:
        student.buy_course()
    elif choice == 3:
        student.show_purchased_courses()
    elif choice == 4:
        receiver_email = input("Enter receiver email: ")
        message = input("Enter message: ")
        student.send_message(receiver_email,message)
    elif choice == 5:
        print("Good bye")
        return
    else:
        print("Invalid choice")
    student_menu(email)

def teacher_menu(email: str):
    teacher = Teacher("data/courses.csv")
    print("""
    1.show all courses
    2.create new course
    3.show student bought courses
    4.change course price
    5.show messages
    6.exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        teacher.show_all_courses()
    elif choice == 2:
        teacher.creating_new_course()
    elif choice == 3:
        teacher.show_my_students(email)
    elif choice == 4:
        teacher.change_course_price()
    elif choice == 5:
        teacher.read_messages(email)
    elif choice == 6:
        print("Thank you for using this program")
        return
    else:
        print("Invalid choice")
    teacher_menu(email)