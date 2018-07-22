"""
This coding exercise takins in a list, and adds a ','
between and then an 'and' before the last item
"""

def Add_comma(user_list):
    
    # Create new list string
    list_string =''

    for i in user_list:

        # Check if last item in the list
        if i == user_list[-1]:

            list_string = (list_string + 'and ' + i)

        else: 
            
            list_string = (list_string + i + ', ')

    print(list_string)


def main():

    new_list = ['apples', 'bananas', 'tofu', 'cats']
    Add_comma(new_list)

if __name__ == "__main__":
    main()