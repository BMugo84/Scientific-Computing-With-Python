class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far ", self.x)

an = PartyAnimal()

# an.party()
# print(type(an))
# print(dir(an))

class Recipe:
    def __init__(self, name, ingredients, instructions):
        """     
        In Python, self is a reference to the current instance of a class. 
        It is a convention in Python to use self as the first parameter name 
        for instance methods of a class, although any other name can be used.
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def print_recipe(self):
        print("Recipe : ", self.name)
        print("Ingredients: ")
        for ingredient in self.ingredients:
            print("- ", ingredient)
        print("Instructions: ")

        """
        enumerate() is a very useful function when you 
        want to loop through an iterable and also want to keep 
        track of the index of each element.
        """
        for i, instruction in enumerate(self.instructions):
            print(i+1, instruction)

ingredients = ["1 cup flour", "1/2 cup sugar", "2 eggs", "1/4 cup butter", "1/2 cup milk"]
instructions = ["Preheat oven to 350 degrees F.", "Mix all ingredients together in a large bowl.", "Pour batter into a greased baking pan.", "Bake for 30-35 minutes or until a toothpick inserted in the center comes out clean."]
chocolate_cake = Recipe("Chocolate Cake", ingredients, instructions)

chocolate_cake.print_recipe()



    