# Terminal-app-documentation #
[Github Repo](https://github.com/fahimagithub/Terminal-app)
<br/>
## Features of the application ##
There are mainly four features in the app. Those are listed below-
1. Verify Membership: This Feature will verify the membership and influence a user to become a new member if the user is not listed in the existing membership list.
<br/>
Membership confirmation: In the Membership Verification, at first User has to put the confirmation whether he/she is a member or not. If the User writes “yes”, then the app will ask for the username of the member. When the value will match with the existing membership database, it will ask for the password. By providing the password correctly, the app will give you access to the website. Otherwise, it will show a message “Wrong password!…..” and will let user access as a guest. Here, the input is taken as a variable. And the member checking process goes with a loop and conditional functions. Also sometimes, user can put some input which is invalid. That moment it will show a message which will guide him/her to write correct input.Here if a user writes an input other than "y" or "n". It will simply print a message "Enter y or n!" and go back to the input to collect the new input.
<br/>
Influence User to become the new Member:  If in the confirmation message the user writes “no” that means he/she is not a member right now. Then there will be a message which contains that for a new member  he/she will get 5% discount of the purchase. Then the app will will ask the user whether he/she is interested or not. If the User writes “yes” then it will ask the user to give a preferred username and password. This new set of data will be added to the existing membership database. And if the user responds “no” means still now not interested to become a member then it will count him/her as a guest. And everytime, if the user enters an invalid input, the app will guide them to write it correctly.
<br/>
2.Product List: In this feature, all products will appear depending on each category and user can add those products in his/her cart.
<br/>
Category list: After completing the membership task, next it will take the user to the category list. There will be 3 categories. The app will ask for the input to access to the user’s preferred category. Each category will show all products with price and ID. Then there will be a place where the customer has to put the full name of the product. It will automatically add the product to the cart and print the same category to the user again. So that the user can choose as many products as he/ she can from the same category. By entering “no” , the user can exit from the existing category.
<br/>
Move to other Category /Checkout process: Next, it asks for the response from the user whether he/she wants to check other categories or not. If “y” means yes, then it will directly take the user to the category list again and let him/her to choose for the next category. If “n” means no then the app will go the checkout process or edit the cart.
