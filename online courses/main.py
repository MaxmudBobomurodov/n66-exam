from menu import teacher_menu , student_menu
from auth import register , login

def main():
    print("""
    1.Register
    2.Login
    3.exit
    """)
    choice = input("enter your choice :")
    if choice == "1":
        email, role = register()
    elif choice == "2":
        email, role = login()
    elif choice == "3":
        print("good bye")
        return
    else:
        print("something went wrong!")
        return

    if role == "teacher":
        teacher_menu(email)
    elif role == "student":
        student_menu(email)
    else:
        print("invalid role")
    main()



if __name__ == "__main__":
    main()
