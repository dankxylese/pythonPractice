class Car:
    def __init__(self, max_speed: int, speed: int = 0):
        self.__max_speed = max_speed  # one underscore hides (gentlemen/'s agreement to avoid modifying directly)
        # Double underscore prevents direct access entirely.
        self.__speed = speed

    def __repr__(self):  # Very useful for (debugging). Have developers in mind when printing data here
        return f"max_speed: {self.__max_speed}\nspeed: {self.__speed} \n"

    def __str__(self):  # For outputting user friendly string (logging)
        return f"Max speed: {self.__max_speed}\nCurrent speed: {self.__speed} \n"

    # When doing print(object), __str__ takes priority, if that is missing, then __repr__.
    # Otherwise, use print(repr(object))

    def get_speed(self):  # Getter
        return self.__speed

    def get_max_speed(self):
        return self.__max_speed

    def do_accelerate(self, speed_inc: int):  # Setter
        if (self.__speed + speed_inc) > self.__max_speed:
            self.__speed = self.__max_speed
        else:
            self.__speed += speed_inc

        # or
        # self.current_speed = min(self.max_speed, self.current_speed + speed_inc)

    def do_break(self, speed_dec: int):
        if (self.__speed - speed_dec) < 0:
            self.__speed = 0
        else:
            self.__speed -= speed_dec


renault = Car(40, 20)
# print(f"Max speed: {renault.get_max_speed()}\nCurrent speed: {renault.get_speed()} \n")
print(renault)

print("Car go vrooom")
renault.do_accelerate(15)
print(f"Current speed: {renault.get_speed()}")

renault.do_accelerate(15)
print(f"Current speed: {renault.get_speed()}")

renault.do_break(35)
print(f"Current speed: {renault.get_speed()}")

renault.do_break(35)
print(f"Current speed: {renault.get_speed()}")
