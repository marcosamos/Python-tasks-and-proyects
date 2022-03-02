# Wrote by Marcos Uc

# Libreries
import csv
from datetime import datetime


# main function
def main():
    currently_time = datetime.now() 
    PRODUCT_NUMBER_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    print("Inkom Emporium")
    print()
    products = read_products("products.csv",PRODUCT_NUMBER_INDEX)
    #print("Products")
    #for key,produc_list in products.items():
    #    print(f"{key} {produc_list}")
    print("*-------------------------------------------------------------*")
    print("Request Items")
    NAME_PRODUT_INDEX = 0
    PRICE_INDEX = 1   
    request = "request.csv"
    try:
        with open(request, "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            running_quantity = 0
            sub_total = 0
            tax = 0.06
            for row in reader:
                key_produc_number = row[0]
                quantity = int(row[1])
                key = products[key_produc_number]
                product_name = key[NAME_PRODUT_INDEX]
                price = float(key[PRICE_INDEX])
                running_quantity +=  quantity
                compute_sub_total = quantity * price
                sub_total += compute_sub_total
                compute_tax = sub_total * tax
                Total = sub_total + compute_tax
                print(f"{product_name}: {quantity} @ {price}")

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {request}"
                " because it doesn't exist.")
    except PermissionError as perm_err:
        print(f"Error: cannot read from {request}"
                " because you don't have permission.")
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

    print()
    print(f"Number of Items: {running_quantity}")
    print(f"Subtotal: {sub_total:.2f}")
    print(f"Sales Tax: {round(compute_tax,2)}")
    print(f"Total: {round(Total,2)}")
    print("*-------------------------------------------------------------*")
   # Exceeds requirements, I added some if statements, for the customer receive a discount.
    if Total > 15:
        print("Congratulations you get a discount for 10% !!!")
        print("You bought more than 15 dollars")
        discount = Total * .10
        total_discount = Total - discount
        print(f"Total: {round(total_discount,2)}")
    elif Total > 30:
        print("Congratulations you get a discount for 20% !!!")
        print("You bought more than 30 dollars")
        discount = Total * .20
        total_discount = Total - discount
        print(f"Total: {round(total_discount,2)}")
    elif Total < 15:
        print(f"Total: {round(Total,2)}")
    print()
    print("Thank you for shopping at the Inkom Emporium")
    print(f"{currently_time:%a %b %d %I:%M:%S %Y}")


# read_products function     
def read_products(products_file,key_column_index):
    
    product_dictionary = {}

    try:
        with open(products_file, "rt") as products_file:
            reader = csv.reader(products_file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                product_dictionary[key] = row
                row.pop(0) 

        return product_dictionary

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {products_file}"
                " because it doesn't exist.")
    except PermissionError as perm_err:
        print(f"Error: cannot read from {products_file}"
                " because you don't have permission.")
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

if __name__ == "__main__":
    main()