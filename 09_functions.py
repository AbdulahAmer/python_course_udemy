def say_hello(person1,person2 = "The police"):
    print("Hello,",person1+"!",person2, "is waiting for you.")


say_hello('me')
          

def fahr2cel(fahrtemp):
    celsius = (5*(fahrtemp-32))/9
    return celsius

print("Celsius:",round(fahr2cel(100),2))
print("Kelvin:",round(fahr2cel(100) + 273,2))
