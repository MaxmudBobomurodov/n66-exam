from file_manager import read, write, append
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Student:
    def __init__(self, email):
        self.email = email

    def show_course_lists(self):
        reader = read("data/courses.csv")
        if not reader:
            print("there are no courses available .")
            return

        for row in reader:
            print(f"course id: {row[0]} , course name: {row[1]}, field :{row[2]}, price: {row[3]}")
        return


    def buy_course(self):
        reader = read("data/courses.csv")
        course_id = input("Enter course id that you want to buy: ")
        for row in reader:
            if course_id == row[0]:
                print(f"you buy this course successfully : {row[1]}")
                append("data/purchases.csv", [self.email, row])

    def show_purchased_courses(self):
        purchased_courses = []
        reader = read("data/purchases.csv")
        for row in reader:
            if row[0] == self.email:
                purchased_courses.append(row[1])

        if not purchased_courses:
            print("you don't have any courses yet")
            return

        print(f"you purchased {len(purchased_courses)} courses")
        with open("data/purchases.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] in purchased_courses:
                    print(f"{row[1]} | {row[2]} | {row[3]}")



    def send_message(self, receiver_email, message):
        subject = "Message from your student"
        password = input("Enter your password: ")


        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))


        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, password)
                server.sendmail(self.email, receiver_email, msg.as_string())
                print("✅ Email sent successfully!")
        except Exception as e:
            print(f" Failed to send email. Error: {e}")


        try:
            with open("data/messages.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.email, receiver_email, message])
                print("Message saved to messages.csv")
        except Exception as e:
            print(f" Failed to save message to CSV. Error: {e}")
