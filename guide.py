def main():
    print("Hello world!")


def data_types():
    integer = 15
    print(integer, type(integer))

    binary = bin(integer)
    print("The number", integer, "in binario =====>", binary)

    hexadecimal = hex(integer)
    print("The number", integer, "in hexadecimal =>", hexadecimal)

    octal = oct(integer)
    print("The number", integer, "in octal =======>", octal)

    pi = 3.141595
    print(pi, type(pi))

    imaginary = 1j
    print(imaginary, type(imaginary))

    square = imaginary ** 2
    print(square, type(square))


def print_five(p=0, w=0, x=0, y=0, z=0):
    print(p, w, x, y, z)


def operations_tuples():
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (6, 7, 8, 9, 10)
    super_tuple = tuple1 + tuple2
    tuple3 = tuple1 * 3
    7 in tuple3
    tuple3.count(67)
    tuple3.count(1)
    # to find the position where it is stored
    tuple3.index(4)
    tuple3[4]
    # it raise an error
    tuple3[1] = 0


def operations_dictionaries():
    dict([("brand", "Lamborghini"), ("model", "LP 570-4")])
    dict(brand="Lamborghini", model="LP 570-4")
    car = {"brand": "Lamborghini", "model": "LP 570-4"}
    car["year"] = 2012
    car.get("brand")
    car.items()
    car.keys()
    "brand" in car.keys()
    car.pop("brand")

    dict_comprehensions = {x: x ** 2 for x in (2, 4, 6)}
    dict_comprehensions[2]
    dict_comprehensions.get(2)


def operations_list():
    a = [66.25, 333, 333, 1, 1234.5]
    a.count(333)
    a.count(66.25)
    a.count('x')
    # get the index where the value is stored
    a.index(333)
    a.remove(333)
    a.reverse()
    a.sort()
    a.pop()
    a.append(-1)
    # list comprehensions
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    squares = [x ** 2 for x in range(10)]
    squares_odd = [x ** 2 for x in range(10) if x & 1]
    squares_even = [x ** 2 for x in range(10) if not x & 1]


def conditionals():
    a = 3
    b = 7
    c = 9
    if a < b:
        print("a is less than b")
    if a < c:
        print("a is less than c")
    if a < b and b < c:
        print("b is between a and c")
    if a < b < c:
        print("b is between a and c")

    if a < 1:
        print("a is less than one")
    elif a == 3:
        print("a is equal to three")
    else:
        print("a is not one and neither three")


def tree(branches):
    for i in range(1, branches + 1):
        print(' ' * (branches - i), '*' * i if i != 1 else '*' * i, '*' * (i - 1) if i > 1 else '', sep='')
    for i in range(1, branches - 1):
        print(' ' * (branches - 1), '*', sep='')


"""
Ejercicio tree(5)
0 <= n < 20
Crear un árbol con n pisos de '*',
con un tronco de longitud n-2 y por último
cada uno de los niveles deberá ser impar comenzando con el 1
    *
   ***
  *****
 *******
*********
    *
    *
    *
"""


def data_structures():
    print_five(1, 2, z=15)

    ordered_tuple = (1, 2, 3, 4, 5)
    print_five(*ordered_tuple)

    dict_as_params = {"p": 1, 'x': 3, "z": 5, 'w': 2, 'y': 4}
    print_five(**dict_as_params)

    other_five = {'a': 1, 'b': 3, 'c': 5, 'd': 2, 'y': 5555}
    # python3
    merged_dict = {**ordered_tuple, **other_five}
    # python 2.7
    merged_dict = dict_as_params.copy()
    merged_dict.update(other_five)
    print(dict_as_params)
    print(other_five)
    print(merged_dict)


def error():
    integer = 15
    binary = bin(integer)

    variable = integer + binary
    print(variable)


class Person:

    def __init__(self, name=None, last_name=None, age=None):
        self.__name = name
        self.__last_name = last_name
        self.age = int(age)

    def __call__(self, name=None, last_name=None, age=None):
        print("I'm at the call method")
        self.__name = name
        self.__last_name = last_name
        self.age = int(age)

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name


class Employee(Person):
    def __init__(self, name=None, last_name=None, age=None, job=None):
        super().__init__(name, last_name, age)
        self.job = job

    def get_full_name(self):
        return super().get_name() + " " + super().get_last_name()

    def get_age(self):
        return self.age

    @staticmethod
    def do_nothing():
        print("static method xD xD")


if __name__ == '__main__':
    # main()
    # data_types()
    # data_structures()
    # error()
    # tree(5)
    persona = Person("Fulano", "Perez", 12)
    print(persona.get_name())
    # print(persona.__name)
    print(persona.age)
    persona(last_name="Otro", age=10)
    print(persona.__dict__)
    employee = Employee("Mickey", "Mouse", 8, "Developer")
    print(employee.__dict__)
    employee(name="Minnie", last_name="Mouse", age=10)
    print(employee.get_last_name())
    print(employee.__dict__)
    print(employee.get_age())
    print(employee.get_full_name())
    Employee.do_nothing()