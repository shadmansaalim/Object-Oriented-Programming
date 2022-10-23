from this import d


class School:
    def __init__(self, school_name) -> None:
        self.school_name = school_name
        print("School Class init called")


class Grade:
    def __init__(self, grade_name) -> None:
        self.grade_name = grade_name
        print("Grade Class init called")


class SportsTeam:
    def __init__(self, sport_name) -> None:
        self.sport_name = sport_name
        self.team = []
        print("SportsTeam Class init called")

    def add_player(self, player_name):
        self.team.append(player_name)


# Inheriting multiple classes
class Student(School, Grade, SportsTeam):
    def __init__(self, name, grade_name, school_name, sport_name) -> None:
        print("Student Init Called")
        self.name = name
        Grade.__init__(self, grade_name)
        School.__init__(self, school_name)
        SportsTeam.__init__(self, sport_name)


sam = Student("Sammy", 10, "RMIT", "Cricket")
print(sam.name, sam.grade_name, sam.school_name)
print(sam.team)
sam.add_player("Sam")
sam.add_player("Henry")
print(sam.team)
