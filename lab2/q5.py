Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Q5. Write a program to prepare a grocery bill."""
... item_name = "Rice"
... item_quantity = 5 
... item_price = 30.50
... 
... total_amount = item_quantity * item_price
... 
... print("***********BILL************")
... print("Item Name\tItem Quantity\tItem Price")
... print(f"{item_name}\t\t{item_quantity} kg\t\t{item_price} per kg")
... print("****************************")
... print(f"Total Amount to be paid: Rs. {total_amount:.2f}")
... print("****************************")
... 
... #Output-
... """***********BILL************
... Item Name       Item Quantity   Item Price
... Rice            5 kg            30.5 per kg
... ****************************
... Total Amount to be paid: Rs. 152.50
