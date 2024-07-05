class Registration:
    """class for registring for sports event"""

    def decorator_gender(func):
        """decorator which will add gender based welcome message"""

        def wrapper(self):
            match self.gender.lower():
                case "male":
                    print("Welcome, Sir!")
                case "female":
                    print("Welcome, Madam!")
                case _:
                    print("Welcome!")
            return func(self)
        return wrapper

    @staticmethod
    def sports_venue_map():
        """mapping to show whether particular sports is indoor or outdoor"""
        venue_map = {
            "tennis": "outdoor",
            "badminton": "indoor",
            "chess": "indoor",
            "carrom": "indoor",
        }
        return venue_map

    def __init__(self, name, gender, age, sports_category) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.sports_category = sports_category

    def _determine_games_venue(self):
        """private method to determine whether sports event is indoor or outdoor"""
        venue_map = self.sports_venue_map()
        return venue_map[self.sports_category]

    # @decorator_gender
    def registration_confirmation(self):
        """confirm registration to user"""
        if (
            all([self.name, self.gender, self.age, self.sports_category])
            and self.sports_category in self.sports_venue_map()
        ):
            venue = self._determine_games_venue()
            return f"Congratulations {self.name}! You have successfully registered for the {self.sports_category} sports event. It's an {venue} event."
        else:
            return "Please check your inputs"


if __name__ == "__main__":
    reg = Registration("Rahul", "Male", 23, "carrom")  # success case
    # reg=Registration("Rahul","Male",23,"billiards") #failing case
    print(reg.registration_confirmation())
