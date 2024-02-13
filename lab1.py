"""class Person:
    def __init__(self, person):
        self.person = person
    def greet(self, p):
        return f"{self.person}:'Hello, '{p}!"


if __name__ == '__main__':
    alice = Person("Alice")
    bob = Person("Bob")
    alice.greet(bob)"""


string = input()

def r_s_wbw(string):
    string = string.split(" ")
    string = (string[::-1])
    return ' '.join(string)

print(r_s_wbw(string))







