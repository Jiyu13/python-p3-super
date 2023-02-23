from user import User


class Student(User):

    def __init__(self, name, grade):
        print("Student.log_in() called.")

        # call User.__init__ method with that name that is required by method defined in User
        super().__init__(name)
        self.grade = grade


    def log_in(self):
        print("Stuednt.log_in() called.")

        #  super() calls the log_in() as defined in the superclass
        super().log_in()

        # supercharge with new attribute that only for Student class
        self.in_class = True


# oneil = Student()
# oneil.log_in()
# print(oneil.in_class)

# Stuednt.log_in() called.
# User.log_in() called.
# True

marley = Student("Marley", 6)
# Student.log_in() called.
# User.__init__() called.

print(marley.__dict__)
# {'name': 'Marley', 'grade': 6}