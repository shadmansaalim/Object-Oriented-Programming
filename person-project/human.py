class Human:
    def __init__(self, gender, height, weight) -> None:
        self.gender = gender
        self.height = height
        self.weight = weight


class Police(Human):
    def __init__(self, gender, height, weight, cases_solved, nationality) -> None:
        super().__init__(gender, height, weight)
        self.cases_solved = cases_solved
        self.nationality = nationality


class Engineer(Human):
    def __init__(self, gender, height, weight, position, is_married) -> None:
        super().__init__(gender, height, weight)
        self.position = position
        self.is_married = is_married


police = Police('M', 5.9, 70, 34, "Australian")
police = Engineer('M', 5.9, 70, "Frontend Developer", True)
