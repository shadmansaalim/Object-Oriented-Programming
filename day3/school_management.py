class School:
    # Constructor
    def __init__(self, name, address, principal="") -> None:
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, coordinator):
        new_grade = Grade(name, coordinator)
        self.grades.append(new_grade)

    def remove_grade(self, name):
        for i, grade in enumerate(self.grades):
            if (grade.name == name):
                # This calls Grade class destructor
                del self.grades[i]
                break


class Grade:
    # Constructor
    def __init__(self, name, coordinator) -> None:
        self.name = name
        self.students = []
        self.coordinator = coordinator

    # How an object will be represented if it is printed
    def __repr__(self) -> str:
        return f"{self.name} with coordinator {self.coordinator}"

    # Destructor
    def __del__(self):
        print(f"Deleting {self.name} with coordinator {self.coordinator}")


cambridge = School("Cambridge School", "Melbourne CBD", "Saalim Shadman")
cambridge.add_grade("Grade 7", "Falk Scholar")
cambridge.add_grade("Grade 10", "Ron Van")
cambridge.add_grade("Grade 12", "Emad Alsadi")

print(cambridge.grades)

cambridge.remove_grade("Grade 12")

print(cambridge.grades)
