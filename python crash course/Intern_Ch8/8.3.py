def greet_users(names): #defines 'greet_user' and creates 'names'
    """Print a simple greeting to each user in the list."""
    for name in names: #creates loop for each name in 'names'
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames) #assign usernames to 'names'
#-----------------------------------------------------------------------------------------------------------------
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs: #while there still are 'unprinted designs'
    current_design = unprinted_designs.pop() #assign the deleted item from 'unprinted_designs' to 'current_design'
    print("Printing model: " + current_design) 
    completed_models.append(current_design) #adds 'current_design' to the end of 'completed_models'
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model) #prints 'completed_models' list
#---------------------------------------------------------------------------------------------------------------------------------
def print_models(unprinted_designs,completed_models): #defines 'print_models' and creates 'unprinted_designs and completed_models'
    """
    Simulate printing each design, until non are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models) #assigns unprinted_designs and completed_models to 'print_models'
show_completed_models(completed_models) #assigns completed_models to 'show_completed_models'
print_models(unprinted_designs[:], completed_models) #sends a copy of 'unprinted_designs' to 'print_models'