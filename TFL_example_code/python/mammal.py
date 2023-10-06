from typing import Any

class Mammal:
    """
    Parent class representing general mammal characteristics.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """
        General method to show a mammal's sound.
        """
        return "Some generic mammal sound"

    def move(self) -> str:
        """
        General method to show how a mammal moves.
        """
        return "Mammal moves"


class Equine(Mammal):
    """
    Intermediate class inheriting from Mammal, 
    representing general characteristics of equines (like horses and zebras).
    """
    def speak(self) -> str:
        """
        Overridden method to provide a general equine sound.
        """
        return "Neigh!"


class Zebra(Equine):
    """
    Child class inheriting from Equine, representing characteristics of a zebra.
    """
    def __init__(self, name: str, stripe_count: int) -> None:
        # Calls the constructor of the parent class (Equine) which itself calls Mammal's constructor
        super().__init__(name)
        self.stripe_count = stripe_count

    def speak(self):
        return "ARGG"
    
    def move(self):
        return super().move()


    def display_stripes(self) -> str:
        """
        Unique method for the Zebra class.
        """
        return f"This zebra has {self.stripe_count} stripes!"


class Horse(Equine):
    """
    Child class inheriting from Equine, representing characteristics of a horse.
    """
    def __init__(self, name: str, breed: str) -> None:
        # Calls the constructor of the parent class (Equine)
        super().__init__(name)
        self.breed = breed

    def display_breed(self) -> str:
        """
        Unique method for the Horse class.
        """
        return f"This horse is a {self.breed}!"


if __name__ == "__main__":
    z = Zebra("Ziggy", 100)
    h = Horse("Harry", "Arabian")
    
    print(z.speak())  # Calls overridden method from Equine class
    print(h.speak())  # Calls overridden method from Equine class
    print(z.display_stripes())  # Calls method unique to Zebra class
    print(h.display_breed())  # Calls method unique to Horse class
    print(z.move())  # Calls method from Mammal (parent) class
