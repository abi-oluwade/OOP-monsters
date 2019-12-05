# - OOP

First we need to understand 'class' vs 'instance of a class'. The 'class' is a blueprint for creating instances.
Each unique object that we create will be 'an instance of that class'. Thus there is also a difference between
'class variables' and 'instance variables'. Instance variables contain data that is unique to each instance.

The constructor. Initialize. When we create 'methods' within the class they receive the instance as the first
argument automatically. So we can now specify any other arguments we want to accept. Everything within the
brackets are attributes/variables/properties of the monster class.

Now when we create our objects/instances of types of monsters now we can pass in values that we specified
in the init method.

Each method within a class always takes the instance as the first argument, which is always called self.

This method here adds a skill to the list of skills for the monsters. It does so by first prompting the user
to input a skill. Then adding the skill to the last spot on the list using '.append'. Finally it prints the new
list but first must be converted to a string in order for it to be concatenated with the other sting in the
statement

I created methods (which are similar but not equal to functions as they only operate withing instances of
the class) to do different actions. As we can see the methods can call on the arguments from the initial
initialization meaning we do not need to individually input new parameters for each new monster

CLASS = the class can be seen as the blueprint or schematic of the object, and would hold all the details about
the size,colour,height etc. Classes contain contain objects, and objects are comprised of methods and
attributes/variables that are related. It wraps methods and attributes/variables. Classes can init many many
instances of different objects.

OBJECTS = An object/instance is an instantiation of a class, when a class is defined ONLY the description of the object/instance is defined.
it is a collection of 'variables' aka 'properties or attributes' and some 'functions' aka 'behaviours or methods'.
objects can be designed to hold specific info (properties/attributes/variables) eg person(object) = id,hair,height,
skin_tone eg car(object) =make,colour,horsepower these objects will also hold (methods/behaviours/functions),
can take arguments but can only be used by an instance of its class.

Inheritance == A process of using details from a new class without modifying existing class.
Ability of classes to inherit behaviours and characteristics of parent class

Encapsulation == Hiding the private details of a class from other objects.

Polymorphism == A concept of using common operation in different ways for different data input.
The ability to change the methods and characteristics of instance of child classes.

Abstraction == The concept of hiding complexity.

Methods != functions Just like function, they can take in arguments, run a block of code.
However, they can only be used by an instance of it's class.

Attributes/variables == Hold information about our SPECIFIC object. Are set in the def init() method
with arguments like any other function.

__ init __ () AKA - Constructor or initializer. This method runs every time an object is created. So when you do:
````
animal1 = Animal('Fred', 10, 2)
````
self == refers to the object / instance