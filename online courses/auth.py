import csv , os
users_file = "data/users.csv"

def check_users():
    if not os.path.exists(users_file):
        with open(users_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["username", "password", "role"])

def register():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    role = input("Enter your role: ")

    if role not in ["teacher", "student"]:
        print("Invalid role")
        return

    with open(users_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                print("Email already registered")
                return

    with open(users_file, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email, password, role])
        print("Registered successfully")
    return email, role





def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open(users_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email and row[1] == password:
                print("Login successfully")
                return email, row[2]
    print("Login failed")
    return None