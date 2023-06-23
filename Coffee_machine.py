class CoffeeOption:
    def __init__(self, name, size, price, ingredients, addons=None):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients
        self.addons = addons if addons else []

    def __str__(self):
        return f"{self.name} | Size: {self.size} | Price: ${self.price:.2f} | Add-ons: {', '.join(self.addons) if self.addons else 'None'}"


class CoffeeMachine:
    def __init__(self):
        self.options = []
        self.inventory = {"Coffee Beans": 100, "Water": 100, "Milk": 50, "Sugar": 50, "Cups": 100}
        self.sales = 0

    def add_option(self, name, size, price, ingredients, addons=None):
        option = CoffeeOption(name, size, price, ingredients, addons)
        self.options.append(option)

    def display_options(self):
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def select_option(self, option_number):
        if option_number <= len(self.options):
            return self.options[option_number-1]
        else:
            print("Invalid option.")

    def check_inventory(self, option):
        for ingredient, amount in option.ingredients.items():
            if self.inventory.get(ingredient, 0) < amount:
                print(f"Sorry, we're out of {ingredient}.")
                return False
        return True

    def brew_coffee(self, option):
        if self.check_inventory(option):
            print(f"Brewing your {option.size} {option.name}...")
            # Update inventory
            for ingredient, amount in option.ingredients.items():
                self.inventory[ingredient] -= amount
            print("Done! Enjoy your coffee.")
        else:
            print("Unable to brew the coffee due to insufficient inventory.")

    def accept_payment(self, option, amount_given):
        if amount_given >= option.price:
            print("Payment accepted. Brewing coffee...")
            self.sales += option.price
            self.brew_coffee(option)
        else:
            print("Not enough money given. Please try again.")

    def report(self):
        print(f"Total sales: ${self.sales:.2f}")
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")


def run_coffee_machine():
    # Create coffee machine
    coffee_machine = CoffeeMachine()

    # Add options
    coffee_machine.add_option("Espresso", "Small", 2.50, {"Coffee Beans": 2, "Water": 1, "Cups": 1}, addons=["Milk"])
    coffee_machine.add_option("Cappuccino", "Medium", 3.50, {"Coffee Beans": 2, "Water": 2, "Milk": 1, "Cups": 1}, addons=["Sugar"])
    coffee_machine.add_option("Latte", "Large", 4.50, {"Coffee Beans": 2, "Water": 3, "Milk": 1, "Cups": 1})

    while True:
        # Display options
        print("\nWelcome to our coffee shop! Please select an option:")
        coffee_machine.display_options()
        print(f"{len(coffee_machine.options) + 1}. Report")
        print(f"{len(coffee_machine.options) + 2}. Exit")

        user_choice = int(input("Enter option number: "))

        if 1 <= user_choice <= len(coffee_machine.options):
            selected_option = coffee_machine.select_option(user_choice)
            amount = float(input(f"Enter payment for ${selected_option.price:.2f}: "))
            coffee_machine.accept_payment(selected_option, amount)
        elif user_choice == len(coffee_machine.options) + 1:
            coffee_machine.report()
        elif user_choice == len(coffee_machine.options) + 2:
            break
        else:
            print("Invalid option.")


run_coffee_machine()

