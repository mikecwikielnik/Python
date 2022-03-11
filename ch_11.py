# CHAPTER 11 
"""Testing your code. """


def get_formatted_name(first, last):
    """Generate a neatly formatted full name. """
    full_name = f"{first} {last}"
    return full_name.title()


# from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")

while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("Please give me a last name: ")
    if last == "q":
        break
    
formatted_name = get_formatted_name(first, last)
print(f"\n Neatly formatted name: {formatted_name}.")




    