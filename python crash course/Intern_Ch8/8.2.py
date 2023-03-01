def get_formatted_name(first_name,last_name): #defines get_formatted_name and creates variables 'first_name' and 'last_name'
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name 
    return full_name.title()
musician = get_formatted_name('jimi','hendrix') #assigns jimi to 'first_name' and hendrix to 'last_name'
print(musician)

def get_formatted_name(first_name,middle_name,last_name): #defines get_formatted_name and creates variables 'first_name', middle_name, and 'last_name'
    """Return a full name, neatly formatted."""
    if middle_name: #if 'get_formatted_anem' contains 'middle_name' runs below
         full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix') #assigns jimi to 'first_name' and hendrix to 'last_name'
print(musician)
musician = get_formatted_name('jimi','hooker','hendrix') #assigns jimi to 'first_name', hooker to 'middle_name', hendrix to 'last_name'
print(musician)

def build_person(first_name,last_name): #defines build_person and creates variables 'first_name' and 'last_name'
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} #inserts the variables as values in the dictionary
    return person
musician = build_person('jimi','hendrix') #assigns jimi to 'first_name' and hendrix to 'last_name'
print(musician) #prints the whole dictionary

def build_person(first_name,last_name,age): #defines build_person and creates variables 'first_name' and 'last_name'
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} #inserts the variables as values in the dictionary
    if age: #if 'build_person' contains 'age'
        person['age'] = age #sets 'age' as the valuse of age in the dictionary
    return person
musician = build_person('jimi','hendrix', age=27) #assigns jimi to 'first_name', hendrix to 'last_name', and 27 to 'age'
print(musician) #prints the whole dictionary

def get_formatted_name(first_name,last_name): #defines get_formatted_name and creates variables 'first_name' and 'last_name'
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me you name:")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
formatted_name = get_formatted_name(f_name,l_name)
print("\nHello, " + formatted_name + "!")

def get_formatted_name(first_name,last_name): #defines get_formatted_name and creates variables 'first_name' and 'last_name'
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True: #while true
    print("\nPlease tell me you name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break #if q is entered it will stop
    l_name = input("First name: ")
    if l_name == 'q':
        break
formatted_name = get_formatted_name(f_name,l_name)
print("\nHello, " + formatted_name + "!")