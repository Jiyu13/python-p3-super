from user import User


class Student(User):

    def __init__(self, name, grade):
        print("Student.log_in() called.")
        self.name = name
        self.grade = grade


    def log_in(self):
        print("Stuednt.log_in() called.")

        #  super() calls one the log_in() as defined in the superclass
        super().log_in()

        # supercharge with new attribute that only for Student class
        self.in_class = True


oneil = Student()
oneil.log_in()
print(oneil.in_class)

# Stuednt.log_in() called.
# User.log_in() called.
# True


