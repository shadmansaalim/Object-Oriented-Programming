class Student:
    def __init__(self, name, id, marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


saalim = Student("Saalim Shadman", 16, 99)

print(saalim.student_id)

# You cannot set it
# saalim.student_id = 1

print(saalim.student_id)

print(saalim.name)
del saalim.name
print(saalim.name)
