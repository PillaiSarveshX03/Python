class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I study at {self.school}."


if __name__ == "__main__":
    person = Person("Alice", 30)
    student = Student("Bob", 20, "Greenwood High")

    print(person.introduce())
    print(student.introduce())
