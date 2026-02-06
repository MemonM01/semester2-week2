import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# ============= LEVEL 1: WARM-UP =============

def task1(db):
    """Task 1: List all product categories in the database."""
    query = "SELECT DISTINCT category FROM products ORDER BY category;"
    result = db.execute(query).fetchall()
    
    print("\n=== Task 1: Product Categories ===")
    categories = [row[0] for row in result]
    for cat in categories:
        print(f"  - {cat}")
    return categories

def task2(db):
    """Task 2: Count the total number of customers."""
    query = "SELECT COUNT(*) as total_customers FROM customers;"
    result = db.execute(query).fetchone()
    
    print("\n=== Task 2: Total Number of Customers ===")
    print(f"  Total customers: {result[0]}")
    return result[0]

def task3(db, customer_email=None):
    """Task 3: Show all orders for a given customer (by email)."""
    if customer_email is None:
        customer_email = input("Enter customer email: ")
    
    query = """
    SELECT o.order_id, o.order_date, o.status, o.total_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE c.email = ?
    ORDER BY o.order_date DESC;
    """
    result = db.execute(query, (customer_email,)).fetchall()
    
    print(f"\n=== Task 3: Orders for {customer_email} ===")
    if not result:
        print(f"  No orders found for {customer_email}")
    else:
        print(f"  {'Order ID':<10} {'Date':<12} {'Status':<12} {'Total':<10}")
        print("  " + "-" * 50)
        for row in result:
            print(f"  {row[0]:<10} {row[1]:<12} {row[2]:<12} £{row[3]:<9.2f}")
    return result

def task4(db, price_limit=2.0):
    """Task 4: Display all products priced below £2."""
    query = """
    SELECT product_id, name, category, price
    FROM products
    WHERE price < ?
    ORDER BY price ASC;
    """
    result = db.execute(query, (price_limit,)).fetchall()
    
    print(f"\n=== Task 4: Products Below £{price_limit} ===")
    if not result:
        print(f"  No products found below £{price_limit}")
    else:
        print(f"  {'Product ID':<12} {'Name':<30} {'Category':<15} {'Price':<8}")
        print("  " + "-" * 70)
        for row in result:
            print(f"  {row[0]:<12} {row[1]:<30} {row[2]:<15} £{row[3]:<7.2f}")
    return result

def menu(db):
    """Interactive menu for Level 1 tasks."""
    while True:
        print("\n" + "="*50)
        print("LEVEL 1 - WARM-UP TASKS")
        print("="*50)
        print("1. List all product categories")
        print("2. Count total customers")
        print("3. Show orders for a customer")
        print("4. Show products below £2")
        print("5. Run all tasks")
        print("0. Exit")
        print("="*50)
        
        choice = input("Select task (0-5): ").strip()
        
        if choice == "1":
            task1(db)
        elif choice == "2":
            task2(db)
        elif choice == "3":
            task3(db)
        elif choice == "4":
            task4(db)
        elif choice == "5":
            task1(db)
            task2(db)
            task3(db)
            task4(db)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main(db=None):
    """Main entry point."""
    if db is None:
        db = get_connection()
    menu(db)

if __name__=="__main__":
    main()



