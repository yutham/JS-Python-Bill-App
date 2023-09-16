import admin
data = admin.Display_stocks()
formatted_data = [{d['Index']: {'product name': d['Product Name'],
                                'price': d['Price'], 'quantity': d['Quantity']}} for d in data]


def Search_stocks(Search_Record):  # This function is to search stocks
    try:
        matches = []
        for item in formatted_data:
            for index, product_info in item.items():
                product_name = product_info.get('product name', '')
                price = product_info.get('price', '')
                quantity = product_info.get('quantity', '')
                if Search_Record['Product Name'].lower() in product_name.lower():
                    matches.append((index, product_name, price, quantity))
        return matches
    except Exception as e:
        print(f"An error occurred while adding data: {str(e)}")
        return False


def Display_search():  # To Display Searched Record
    try:
        data = []
        header = [cell.value for cell in admin.sheet_obj[1]]
        for row in Search_stocks():
            row_data = dict(zip(header, row))
            data.append(row_data)
        return data
    except Exception as e:
        print(f"An error occurred while adding data: {str(e)}")
        return False
