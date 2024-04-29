def capitalize_last_name(name, new): #user defined function to turn the inputted name into the format
    if not isinstance(name, str): #If the input is not a string
        raise TypeError
    for char in name: #If there is a number in the name
        if char.isdigit():
            raise TypeError
    list_form = name.split()
    if len(list_form) != 2: #If there is not exactly two words inputted
        raise ValueError
    first_name = "" + list_form[0]
    new += first_name.capitalize()
    last_name = "" + list_form[1]
    new += " "
    new += last_name.upper()
    print(new)
try: 
    new_name = ""
    full_name = input("Input your Given name and Last name separated by a space: ")
    capitalize_last_name(full_name, new_name) #To call the def function
#Calling all the type of errors
except TypeError:
    print("Please input a proper name.")
except ValueError:
    print("Please input only two words, your first name and your last name.")