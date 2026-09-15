
products={
    "apple":(100,"kg"),
    "banana":(70,"dozen"),
    "orange":(150,"kg"),
   "bread":(100,"pack"),
   "juice":(50,"box"),
    "milk":(80,"kg"),
    "butter":(200,"box"),
    "cream":(100,"box"),
    "grapes":(50,"kg"),
    "plum":(100,"kg"),
    "egg":(50,"dozen"),
    "coffee":(150,"pack"),
    "flour":(250,"kg"),
    "chicken":(300,"kg"),
    "beef":(400,"kg"),
    "mutton":(500,"kg"),
    "water bottle":(200,"bottle"),
    "noodles":(100,"pack"),
    "rice":(200,"kg"),
    "oats":(100,"pack"),
    "canned beans": (200,"tin"),
    "canned fruit":(250,"tin"),
    "chocolate":(300,"pack"),
    "candy":(50,"pack"),
    "jam":(150,"jar"),
    "nuts":(300,"kg")
    }
quantity={
    "apple":50,
    "banana":10,
    "orange":70,
   "bread":10,
   "juice":50,
    "milk":30,
    "butter":20,
    "cream":10,
    "grapes":50,
    "plum":10,
    "egg":50,
    "coffee":20,
    "flour":25,
    "chicken":20,
    "beef":10,
    "mutton":15,
    "water bottle":20,
    "noodles":30,
    "rice":20,
    "oats":10,
    "canned beans": 20,
    "canned fruit":25,
    "chocolate":30,
    "candy":50,
    "jam":15,
    "nuts":30
    }
cart={}
def showproduct():
    print("        Available products:")

    sorted_products = sorted(
        products.items(),
        key=lambda x: x[1][0]
    )
    for product,details in sorted_products:
        price,unit=details
        print(product,"=",price,"per",unit)

def showcart():
    print("products added to cart:")

    for name,qty in cart.items():
        print(name, "=", qty)

def deleteproduct():
   name=input("enter product name to remove:")
   if name in cart:
       del cart[name]
   else:
       print("product not found in cart")

def total():
    sumamount=0
    for name,qty in cart.items():
     price=products[name][0]
     sumamount=sumamount+qty*price

    if sumamount >= 3000:
        discount = sumamount * 0.20

    elif sumamount >= 2000:
        discount = sumamount * 0.10

    elif sumamount >= 1000:
        discount = sumamount * 0.05

    else:
        discount = 0
    final_price = sumamount - discount
    print("bill before discount:",sumamount)
    print("discount amount",discount)
    print("total price:",final_price,"rs")
    return sumamount

print("enter 0 when your are done and 1 to continue.")
while True:
    print()
    print("1. Show Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Calculate Bill")
    print("6. Update Quantity")
    print("7. Exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        showproduct()

    elif choice == 2:
        name = input("enter product name: ")
        qty = int(input("enter product quantity: "))

        if name in products:
            if qty <= quantity[name]:
                cart[name] = qty
                print("product added to cart")
            else:
                print("product not available in this quantity")
        else:
            print("product not exist")

    elif choice == 3:
        deleteproduct()

    elif choice == 4:
        showcart()

    elif choice == 5:
        total()

    elif choice == 6:
        name = input("enter product name: ")
        qty = int(input("enter new quantity: "))

        if name in cart:
            if qty <= quantity[name]:
                cart.update({name: qty})
                print("quantity updated")
            else:
                print("not enough stock")
        else:
            print("product not in cart")

    elif choice == 7:
        print("Thank you")
        print("Have a best day")
        break

    else:
        print("Invalid choice")





