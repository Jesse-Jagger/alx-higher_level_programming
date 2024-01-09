0x0A. Python - Inheritance
Python
OOP
Inheritance

SHORT NOTE BY MYSELF

So thsiis all about a master class sharing its attributes to a sub-class.
This means a sub-class is going to recieve the main or master class attributes eg as follows

class Baseclass:
{
	Body
}

Class Derivedclass(Baseclass):
{
	Body
}


class Animal:
{
	alive = True
	def it_eats(self):
		print("this Animal eats")
	def it_sleeps(self):
                print("this Animal sleeps")
}
class Rabbit(Animal):
	pass
class Dog(Animal):
        pass00
class Hare(Animal):
        pass
also note that the sub-class can have it own defined funcs
