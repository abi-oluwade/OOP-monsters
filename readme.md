# - OOP

First we need to understand 'class' vs 'instance of a class'. The 'class' is a blueprint for creating instances. Each unique object that we
create will be 'an instance of that class'. Thus there is also a difference between 'class variables' and
'instance variables'. Instance variables contain data that is unique to each instance.

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