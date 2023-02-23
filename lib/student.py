from use import User


class Student(User):
    def log_in(self):
        super().log_in()
        self.in_class = True