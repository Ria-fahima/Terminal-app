print("ZEIN")

member = input("Are you a member of Zein? (y/n): ")
while member != "y" and member != "n":
    print("Enter y or n!")
    member = input("Are you a member of Zein? (y/n): ")
if member ==    "y":
    print("Welcome to our website!")
    
else:
    print("For our new member, you can get 5 percent discount on your first purchase!") 
    confirmation = input("Are you interested? (y/n):")
    while confirmation != "y" and confirmation != "n":
        print("Enter y or n!")
        confirmation = input("Are you still interested? (y/n): ")
    if confirmation == "y":
        print("please fill up some information about yourself.")
    else:
        print("It's okay! Let's get started!")    
   

# Catagories started
cart = []
def available_products(p):  
    import json
    import pandas as pd
    with open(p) as f:
        data = json.load(f)  
    for i in range (len(data)):
        print(pd.DataFrame(data))
        
        choice = input("Please write the full name or 'no' to stop ")
        def mix(n):
            for value in data:
                if n.lower() == value['Name'].lower():
                    return value['Price']
        if choice != None and choice != "no":
            print("price is almost: $", mix(choice))            
        if choice == 'no':
            option = input("Do you want to check other catagories? (y/n): ")
            if option == 'y':
                main()
            else:    
                break
            break    
        cart.append(choice.upper())  



def main():
    print("There are mainly 3 catagories of products.\n 1. Bags \n 2. Cloths \n 3. Shoes")
    catagory = input("Please enter the number of your desired Catagory. (1/2/3)")
    match catagory:
        case "1":
            available_products("bags.json") 
        case "2":
            available_products("cloths.json") 
        case "3":
            available_products("shoes.json")              
        case _:
            print("default") 
             
main()  
print(f"Your collections are: {cart}")  

def delete_cart():
    delete_item = input("Please write the product name to remove.")
    cart.remove(delete_item.upper())
    print(f"Your collections are: {cart}")
    del_choice = input("Do you want to delete more? (y/n): ")
    if del_choice == "y":
        delete_cart()
        
    else:
        edit_cart()


def edit_cart():

    proceed = input("Do you want to proceed for checkout (y/n)?:  ")
    if proceed == "y":
        print("payment")
        print(f"Your collections are: {cart}")  

    else:
        print("Edit your cart")
        modify = input("Do you want to add or delete (add / delete)?: ")
        if modify == "add":
            main()
            edit_cart()
        elif modify == "delete":
            delete_cart()
edit_cart()            

# def payment():







           
    