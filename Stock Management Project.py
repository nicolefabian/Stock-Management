#Stock Management program by Nicole Fabian

codesList = [1234,5678,9101]
categoriesList = ["Painting", "Drawing", "Papers"]
titlesList = ["Acrylic Paint Set", "Beginner Artist's Sketch set", "Watercolour pad"]
pricesList =[27.99, 25.60, 18.99]
quantitiesList =[18,30,80]
quantity = 0 #initialised for the buyProduct function input argument

#all List and function names are in camel case
#other variables uses this format variable_name

def checkProduct(code) :
    if code in codesList:
        return True
    return False

def addProduct():
    code = int(input("Enter art material code: "))
    while checkProduct(code) == True:
        code=int(input("This code is not available so please choose another code: "))
    codesList.append(code)
    categories = input("Enter art material category: ")
    categoriesList.append(categories)
    titles = input("Enter art material title: ")
    titlesList.append(titles)
    prices = float(input("Enter art material price: "))
    pricesList.append(prices)
    quantities = int(input("Enter art material quantity: "))
    while quantities < 10 or quantities > 50:
        print("Please enter quantity between 10 and 50")
        quantities = int(input("Enter product quantity: "))
    quantitiesList.append(quantities)

    
def addProduct_second(): # a function that loops the entire addProduct(code) if user wants to enter multiple times
    add_newproduct = 'yes'
    while add_newproduct == 'yes':
        addProduct()
        add_newproduct = input("Do you want to add more art material record, enter yes or no: ")
        add_newproduct = add_newproduct.lower()
    print()
    
def searchProduct(code):
    while checkProduct(code) == False: #used if code is not in the codesList
        code = int(input("Please enter correct code :"))
    for i in range(len(codesList)): #prints all details if code is in codesList
        if codesList [i] == code:
                print("Product Information: ")
                print("===========================================")
                print ("Code :", codesList[i])
                print("Category :", categoriesList[i])
                print ("Title :", titlesList[i])
                print("Price :", pricesList[i])
                print("Quantity: ", quantitiesList[i])
                print("===========================================")

def updateProduct(code):
    searchProduct(code)
    update_product = "yes"
    update_product = input("Do you want to update art material category, enter yes or no: ")
    update_product = update_product.lower()
    if update_product == "yes":
        new_category = input("Please enter new category: ")
#------  to update new category------------------------
        for i in range(len(categoriesList)):
            categoriesList[i] = new_category
            categoriesList.append(new_category)
    update_title ="yes"
    update_title = input("Do you want to update title, enter yes or no: ")
    update_title = update_title.lower()
    if update_title == "yes":
        new_title = input("Please enter new title: ")
#------  to update new titles------------------------
        for i in range(len(titlesList)):
            titlesList[i] = new_title
            titlesList.append(new_title)
    update_price = "yes"
    update_price = input("Do you want to update price, enter yes or no: ")
    update_price = update_price.lower()
    if update_price == "yes":
        new_price = float(input("Please enter new price: "))
#------  to update new price------------------------
        for i in range(len(pricesList)):
            pricesList[i] = new_price
            pricesList.append(new_price)
    update_quantity = "yes"
    update_quantity = input("Do you want to update quantity, enter yes or no: ")
    update_quantity = update_quantity.lower()
    if update_quantity == "yes":
        new_quantity = int(input("Please enter new quantity: "))
        while new_quantity < 10 or new_quantity > 50:
            print("Please enter quantity between 10 and 50")
            new_quantity =int(input("Enter product quantity: "))
        print()
#------  to update new quantity------------------------
        for i in range(len(quantitiesList)):
            quantitiesList[i] = new_quantity
            quantitiesList.append(new_quantity)
    else:
        print()
        mainMenu()
        
def getCodeIndex(code):
    for i in range(len(codesList)): 
        if (codesList[i] == code):
            return i # to get the specific code index
    return -1

def buyProduct(code, quantity):
    while checkProduct(code) == False:
        code = int(input("Please enter correct code: "))
    searchProduct(code) #print all product details
    quantity = int(input("Please enter quantity of the product: "))
#---to get the index for specific code, quantity, and title----------
    index=getCodeIndex(code) 
    stockQuantity=quantitiesList[index]
    stockTitles = titlesList[index]
    while quantity > stockQuantity:
        print("There are only ", stockQuantity, "quantities of the product", stockTitles,"available for sale")
        new_quantity = input("Do you want to enter new quantity,enter yes or no: ")
        new_quantity = new_quantity.lower()
        if new_quantity =='yes':
            quantity = int(input("Please enter quantity of the product: "))
        else:
            print()
            mainMenu()
    original_price=pricesList[index] # get the index of specific price
    price = (quantity * original_price)
    gst = price * 0.15
    total_price =  price + gst
    discount=0
    if quantity < 10:
        discount = 0
        updateQuantity(quantity)
        
    elif quantity >= 10 and quantity <20:
        discount= total_price * 0.1
        updateQuantity(quantity)
        
    elif quantity >= 20 and quantity <=30:
        discount=  total_price * 0.2
        updateQuantity(quantity)
        
    else:
        discount= total_price * 0.3
        updateQuantity(quantity)
    print("The total price to pay is $", format(total_price - discount, ".2f")) 
    print()
    
    
def updateQuantity(quantity): #another function to update the quantity once a product has been sold
    for i in range(len(quantitiesList)):
            quantitiesList[i] = quantitiesList[i] - quantity
            quantitiesList.append(quantity)
   
                 
#----main program-----------           
def mainMenu() :
    select_options=0
    while select_options != 6:
        print("Please select one of the following options")
        print("1. Add Product ")
        print("2. SearchProduct")
        print("3. Update product")
        print("4. Buy Product ")
        print("5. Quit")
        select_options = int(input("Please enter 1,2,3,4, or 5: "))
        while select_options not in (1,2,3,4,5):
                select_options = int(input("Please enter only 1,2,3,4 or 5: "))
        if select_options == 1:
            addProduct_second()
        elif select_options == 2:
            code = int(input("Please enter art material code: "))
            searchProduct(code)
        elif select_options == 3:
            code = int(input("Please enter art material code: "))
            updateProduct(code)
        elif select_options ==4:
            code = int(input("Please enter the code of the art material you want to buy: "))
            buyProduct(code,quantity)
        else:
            print("Goodbye")
            print()
    
mainMenu() # calls the mainMenu function to start and loop the program 

