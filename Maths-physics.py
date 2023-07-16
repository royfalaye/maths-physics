import math

choice = input("Please Choose Class \n Math \n Physics \n")


class Math:
    def exponential(self, exponent, power):
        self.exponential = exponent ** power
        return self.exponential

    def squareRoot(self, number):
        self.squareRoot = math.sqrt(number)
        return self.squareRoot

    def modulus(self, num1, num2):
        mod = int(num1) % int(num2)
        return mod

    def twoDimVector(self, num1, num2):
        magnitude = math.sqrt(num1 ** 2 + num2 ** 2)
        return magnitude

    def threeDimVectors(self, num1, num2, num3):
        magnitude = math.sqrt(num1 ** 2 + num2 ** 2 + num3 ** 2)
        return magnitude


class Physics:
    def velocity(self, distance, time):
        self.velocity = int(distance) / int(time)
        return self.velocity

    def energy(self, mass):
        speedOfLight = 3.0 * 10 ** 8
        self.energy = int(mass) * speedOfLight
        return self.energy

    def workDone(self, force, distance):
        self.workDone = force * distance
        return self.workDone

    def power(self, current, volt):
        self.power = current * volt
        return self.power

    def force(self, mass, acceleration):
        self.force = mass * acceleration
        return self.force


maths = Math()
phy = Physics()

if choice.lower() == "math" or choice.lower() == "m":
    func = input(
        "Choose Function \n Exponenetial \n SquareRoot \n Modulus \n Two Dimensional Vector \n Three Dimensional Vector \n")
    if func.lower().replace(" ", "") == "exponential" or func.lower().replace(" ", "") == "e":
        exponent = int(input("Base number: "))
        power = int(input("Power: "))
        print(maths.exponential(exponent, power))
    elif func.lower().replace(" ", "") == "squareroot" or func.lower().replace(" ", "") == "s":
        number = int(input("Number to square: "))
        print(maths.squareRoot(number))
    elif func.lower().replace(" ", "") == "modulus" or func.lower().replace(" ", "") == "m":
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print(maths.modulus(num1, num2))
    elif func.lower().replace(" ", "") == "twodimensionalvector" or func.lower().replace(" ", "") == "2d":
        num1 = int(input("First vector : "))
        num2 = int(input("Second Vector: "))
        print(maths.twoDimVector(num1, num2))
    elif func.lower().replace(" ", "") == "threedimensionalvector" or func.lower().replace(" ", "") == "3d":
        num1 = int(input("First vector : "))
        num2 = int(input("Second Vector: "))
        num3 = int(input("Third Vector: "))
        print(maths.threeDimVectors(num1, num2, num3))

elif choice.lower() == 'physics' or choice.lower() == "p":
    func = input("Choose  Function \n Velocity \n Energy \n Workdone \n Power \n Force ")
    if func.lower().replace(" ", "") == "velocity" or func.lower().replace(" ", "") == "v":
        distance = int(input("distance: "))
        time = int(input("time: "))
        print(f'Velocity is {phy.velocity(distance, time)} m/s')
    elif func.lower().replace(" ", "") == "energy" or func.lower().replace(" ", "") == "e":
        mass = int(input("Mass: "))
        print(f'Energy is {phy.energy(mass)} joules')
    elif func.lower().replace(" ", "") == "workdone" or func.lower().replace(" ", "") == "w":
        force = int(input("Force: "))
        distance = int(input("Distance: "))
        print(f'Workdone is {phy.workDone(force, distance)} joules')
    elif func.lower().replace(" ", "") == "power" or func.lower().replace(" ", "") == "p":
        current = int(input("Current: "))
        volt = int(input("Voltage: "))
        print(f'Power is {phy.power(current, volt)} watts')
    elif func.lower().replace(" ", "") == "force" or func.lower().replace(" ", "") == "f":
        mass = int(input("Mass: "))
        acc = int(input("Acceleration: "))
        print(f'Force is {phy.force(mass, acc)} newton')
