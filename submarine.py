class Submarine:
    __max_deepness = 545 # The meters of ocean's deepnest part
    def __init__(self, name, color, current_deepness, capacity = 20, weapon = ""):
        self.__name = name
        self.__color = color
        self.__current_deepness = current_deepness
        self.__capacity = capacity
        self.__weapon = weapon

    # dunder methods
    def __str__(self):
        description = f"Su submarino {self.__name} es de color {self.__color}, tiene una capacidad para {self.__capacity} personas y se encuentra a una profundidad de {self.__current_deepness} metros."
        if self.__weapon != "":
            description += f" También tiene un {self.__weapon} como arma."
        return description

    # getters
    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_weapon(self):
        return self.__weapon if self.__weapon != "" else "No tiene un arma"

    def get_capacity(self):
        return self.__capacity

    def get_max_deepness(self):
        return self.__max_deepness

    # setters
    def set_name(self, new_name):
        self.__name = new_name

    # class methods
    def go_down(self):
        if self.__current_deepness == self.__max_deepness:
            return f"{self.__name} no puede bajar más, ya está en lo más profundo"
        else:
            if self.__current_deepness + 15 > self.__max_deepness:
                message = f"{self.__name} bajó {self.__max_deepness - self.__current_deepness} metros de profundidad y llegó a lo más profundo."
                self.__current_deepness = self.__max_deepness
                return message
            else:
                self.__current_deepness += 15
                return f"{self.__name} bajó 15 metros de profundidad, ahora está a {self.__current_deepness} metros de profundidad"
    
    def go_up(self):
        if self.__current_deepness == 0:
            return f"{self.__name} no puede subir más, ya está en la superficie"
        else:
            if self.__current_deepness - 15 < 0:
                message = f"{self.__name} subió {self.__current_deepness} metros hacia la superficie y llegó a la misma."
                self.__current_deepness = 0
                return message
            else:
                self.__current_deepness -= 15
                return f"{self.__name} subió 15 metroa hacia la superficie, ahora se encuentra a {self.__current_deepness} metros de profundidad"

    def go_to_surface(self):
        if self.__current_deepness == 0:
            return f"{self.__name} ya se encuentra en la superficie"
        else:
            self.__current_deepness = 0
            return f"{self.__name} llegó a la superficie"
    
    def go_to_deepest(self):  
        if self.__current_deepness == self.__max_deepness:
            return f"{self.__name} ya se encuentra en lo más profundo"
        else:
            self.__current_deepness = self.__max_deepness
            return f"{self.__name} llegó a lo más profundo del mar"
