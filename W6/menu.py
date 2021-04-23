def menu_list(item): 
    option = 1 
    for choice in item: 
        print(str(option)+". "+ choice)
        option = option + 1 
    print(str(option)+ ". Quit")
    return option