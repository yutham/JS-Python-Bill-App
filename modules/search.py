import admin
data = admin.Display_stocks()
# print(data)  #for checking in cli
formatted_data = [{d['Index']: {'product name': d['Product Name'],
                                'price': d['Price'], 'quantity': d['Quantity']}} for d in data]

# Print the formatted data     #for checking in cli
# print(formatted_data)    #for checking in cli
# p = 'hoo'   #for checking in cli


def Search_stocks(Search_Record):  # This function is to search stocks
    matches = []
    for item in formatted_data:
        for index, product_info in item.items():
            product_name = product_info.get('product name', '')
            price = product_info.get('price', '')
            quantity = product_info.get('quantity', '')
            if Search_Record['Product Name'].lower() in product_name.lower():
                matches.append((index, product_name, price, quantity))
    return matches


# c = Search_stocks()
# print(c)
