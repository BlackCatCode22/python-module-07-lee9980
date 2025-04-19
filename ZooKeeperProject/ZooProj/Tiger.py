
# Import Animal to allow tiger to inherit functions from Animal
from Animal import Animal

class Tiger(Animal):
    # Tiger count
    numOfTigers = 0

    # List of possible tigers sounds
    list_of_tiger_sounds = ["Mew", "Meowww", "Mrrrrew!", "Mew! Mew!"]

    # List of tiger names
    list_of_tiger_names = []

    file_path = "animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num==15:
                list_of_tiger_names.extend(line.strip().split(","))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex", weight="a_weight", originating_zoo="a_zoo", arrival_date="2099-01-01"):

        # Increment the created tiger count
        Tiger.numOfTigers += 1

        # Call the constructor of the parent class (Animal) with 'tiger' as the species
        super().__init__("tiger",name,animal_id,birth_date, color, sex, weight, originating_zoo, arrival_date)

    def make_sound(self):
        return self.list_of_tiger_sounds

    # Get an unused tiger name
    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)
