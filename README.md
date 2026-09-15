# 🛒 Grocery Store Management System

A simple ** mini grocery cart built in Python**.
This project allows users to view available products, add products to a cart, update quantities, remove products, and calculate the final bill with discounts.

## 📌 Project Overview

This project is designed as a beginner-level Python project to practice important programming concepts such as **dictionaries, tuples, functions, loops, conditional statements, lambda functions, and sorting**.

The system also includes a simple **stock management system** that checks whether the requested quantity is available before adding or updating a product in the cart.

## ✨ Features

* 🛍️ Display available grocery products
* ➕ Add products to the shopping cart
* 🗑️ Remove products from the cart
* 🛒 View cart items
* 🔄 Update product quantities
* 📦 Check available product stock
* 💰 Calculate the total bill
* 🎁 Apply discounts based on the bill amount
* 🔢 Display products sorted by price
* 🚪 Exit the program

## 🧠 Python Concepts Used

This project uses the following Python concepts:

* Variables
* Dictionaries
* Tuples
* Functions
* `for` loops
* `while` loops
* `if-elif-else`
* Operators
* Dictionary `.items()`
* Dictionary `.update()`
* `del` keyword
* `sorted()` function
* Lambda functions
* User input
* Basic calculations

## 📂 Data Structures

### Products Dictionary

Each product stores its **price and unit** using a tuple.

Example:

```python
"apple": (100, "kg")
```

Here:

* `apple` → Product name
* `100` → Price
* `kg` → Unit

### Quantity Dictionary

The `quantity` dictionary stores the available stock for each product.

Example:

```python
"apple": 50
```

This means 50 kg of apples are available.

### Cart Dictionary

The `cart` dictionary stores the products selected by the customer and their quantities.

Example:

```python
cart = {
    "apple": 2,
    "bread": 1
}
```

## 💸 Discount System

The program automatically applies a discount according to the total bill:

| Bill Amount       | Discount |
| ----------------- | -------: |
| Below Rs. 1000    |       0% |
| Rs. 1000 or above |       5% |
| Rs. 2000 or above |      10% |
| Rs. 3000 or above |      20% |

## 🔄 How the Program Works

1. The program displays a menu.
2. The user selects an option.
3. The user can view available products.
4. Products can be added to the cart.
5. The program checks product availability before adding it.
6. Cart quantities can be updated or products can be removed.
7. The user can view the cart.
8. The total bill is calculated.
9. A discount is applied according to the bill amount.
10. The user can exit the program.

## ▶️ How to Run

1. Clone or download this repository.
2. Open the Python file.
3. Run the program using Python.
4. Select an option from the menu.
5. Follow the instructions displayed on the screen.

Example:

```text
1. Show Products
2. Add Product
3. Remove Product
4. View Cart
5. Calculate Bill
6. Update Quantity
7. Exit
```

## 🎯 Learning Purpose

This project was created to strengthen my understanding of **Python fundamentals** and to apply multiple concepts together in a practical project.

It helped me practice:

> **Dictionaries + Tuples + Functions + Loops + Conditions + Lambda + Sorting**

## 👩‍💻 Author

**Bushra Ahmad**

---

⭐ If you find this project useful, feel free to explore the code and give it a star!
