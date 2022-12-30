import math


def get_numeric_input(count):
    numbers = []

    for i in range(count):
        number = input("Enter {} number: ".format(i + 1))
        try:
            number = int(number)
            print(number)
            numbers.append(number)
        except:
            print("You should enter numeric input")
            return []
    return numbers


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


if __name__ == '__main__':
    inputs = get_numeric_input(2)

    if len(inputs):
        print("Least common multiple of entered numbers is {}".format(lcm(inputs[0], inputs[1])))
    else:
        print("Invalid inputs received !")