"""
MY FIRST PYTHON MINI PROJECT.
"""

# Defining Our Variables

# create a product and price for three items
p1_name, p1_price = "books", 49.95
p2_name, p2_price = "computer", 579.99      # ability to declare multiple variables on the same line  
p3_name, p3_price = "monitor", 124.89

company_name = "silver walusimbi, inc."
company_address = "356 Hamburg Jt."
company_city = "Berlin, ST"

message = "Thanks for shopping with us today!"

print("*" * 50)

# Displaying the Company Info
# print company information first, using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address) )        # insertion of a tab indentation 
print("\t\t{}".format(company_city))

# print a line between sections
print( "=" * 50 )

# Displaying the Product Info
# print out header for section of items
print("\tProduct Name\tProduct Price")

# create a print statement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t${}".format(p2_name.title(), p2_price))
print("\t{}\t\t${}".format(p3_name.title(), p3_price))

print( "=" * 50 )

# Displaying the Total
print("\t\t\tTotal")

total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))

print( "=" * 50 )

print( "\n\t{}\n".format(message))

print( "*" * 50 )


