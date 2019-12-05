class Monster:
    # The constructor. Initialize. When we create 'methods' within the class they receive the instance as the first
    # argument automatically. So we can now specify any other arguments we want to accept. Everything within the
    # brackets are attributes/variables/properties of the monster class.

    def __init__(self, name, skills):
        self.name = name
        self.skill_list = skills

    # Now when we create our objects/instances of types of monsters now we can pass in values that we specified
    # in the init method.

    def sleep(self):
        return "zzzzz *I can't wait to eat some kids* zzzzz"

    # Each method within a class always takes the instance as the first argument, which is always called self. But can
    # also take other arguments in the __init__, meaning if we want to pull for example the name in this method for
    # sleep, we would not need to specify it in the definition and simply put 'self.name' and it will automatically
    # do it for us.

    def eat(self):
        return "I'm awake and now I can't wait to eat some kids!"

    def scare_attack(self):
        return 'RAAAHHH IM GONNA EAT YOU!'

    # This method here adds a skill to the list of skills for the monsters. It does so by first prompting the user
    # to input a skill. Then adding the skill to the last spot on the list using '.append'. Finally it prints the new
    # list but first must be converted to a string in order for it to be concatenated with the other sting in the
    # statement

    def add_skill(self):
        add_a_skill = input('What new skill have you gotten Mr. ' + self.name + '?')
        self.skill_list.append(add_a_skill)
        return print('Hello! I have just finished my monster training and now my list of skills are' + str(
            self.skill_list))


monster_1 = Monster('Paul', ['Quick', 'Invisible', 'Loud'])
monster_2 = Monster('Harry', ['Strong', 'Creepy', 'Fire Breath'])
monster_3 = Monster('Yemi', ['Running', 'Jumping', 'Swimming'])

    # I created methods (which are similar but not equal to functions as they only operate withing instances of
    # the class) to do different actions. As we can see the methods can call on the arguments from the initial
    # initialization meaning we do not need to individually input new parameters for each new monster or every time
    # we want to define a new method.


print(monster_1.add_skill())
print(monster_3.scare_attack())
