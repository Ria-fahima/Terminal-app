from pyfiglet import figlet_format
import json
import pandas as pd
Total = 0
print(figlet_format("ZEIN" , font= "standard"))

member = input("Are you a member of Zein? (y/n): ")
while member != "y" and member != "n":
    print("Enter y or n!")
    member = input("Are you a member of Zein? (y/n): ")
if member ==    "y":
    user_name = input("Please enter your user name: ")
    with open("members.json") as f:
        store_data = json.load(f)
        for member in store_data:
            
            if user_name == member['name']:
                password = input("Please enter your password: ")
                if password == member['password']:
                    print("Welcome to our website!", member['name'])
                else:
                    print("Wrong password! You are not out member!")       

else:
    print("For our new member, you can get 5 percent discount on your first purchase!") 
    confirmation = input("Are you interested? (y/n):")
    while confirmation != "y" and confirmation != "n":
        print("Enter y or n!")
        confirmation = input("Are you still interested? (y/n): ")
    if confirmation == "y":
        print("please fill up some information about yourself.")
        new_user = input("Write Your preferred username:")
        new_pass = input("Create your password: ")
        with open("members.json") as f:
            store_data = json.load(f)
            new_dict = {"name" : new_user, "password" : new_pass}
            store_data.append(new_dict)
        with open("members.json", "w") as f:
            json.dump(store_data, f)
        print("Welcome to our website!", new_dict['name'])  

    else:
        print("It's okay! Let's get started!")  
   

# Catagories started
cart = []
def available_products(p):  
    
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
            print("The product price is: $", mix(choice))            
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

def payment(m,z):
    
    with open(m) as f:
        pay_data = json.load(f)
        z = 0
        for o in range (len(cart)):
            for l in pay_data:
                if cart[o].lower() == l['Name'].lower():
                    print ("Product price is :", l['Price'])
                    z += l['Price']   
        return z  
                               
def edit_cart():

    proceed = input("Do you want to proceed for checkout (y/n)?:  ")
    if proceed == "y":
        print("payment")
        bag_sum = payment("bags.json",Total)
        cloth_sum =payment("cloths.json",Total)
        shoes_sum = payment("shoes.json",Total) 
        total = bag_sum +cloth_sum + shoes_sum
        print(f"Your Final collections are: {cart}") 
        print("Your total amount is: $", total)

    else:
        print("Edit your cart")
        modify = input("Do you want to add or delete (add / delete)?: ")
        if modify == "add":
            main()
            edit_cart()
        elif modify == "delete":
            delete_cart()
edit_cart()    

       











           
    