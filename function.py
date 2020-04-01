def greet_user():
   print("Hello!")
    
greet_user()

#passing information to function
def greet_user(username):
    print("Hello!,"+username.title())
    
greet_user('venkatesh')

#multiple fun() calls
def describe_pet(animal_type, pet_name):
    
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
