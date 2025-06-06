def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    formated_fname = f_name.title()
    formaated_lname = l_name.title()
    return f"{formated_fname} {formaated_lname}"

output = format_name("hola", "mundo")
print(output)

def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_fname = f_name.title()
    formaated_lname = l_name.title()
    return f"{formated_fname} {formaated_lname}"

def format_name3(f_name, l_name):
    return f_name.title(), l_name.title()

first, last = format_name3("hola", "mundo")
print(first)
print(last)