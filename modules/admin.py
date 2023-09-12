import pandas as pd
import os
import openpyxl


def load_workbook(wb_path):  # Loading Excel Sheet
    if os.path.exists(wb_path):
        return openpyxl.load_workbook(wb_path)
    else:
        return None


wb_path = "./data/stocks.xlsx"
wb = load_workbook(wb_path)
sheet = wb['Sheet1']
sheet_obj = wb.active


def Add_Stock(new_record):
    try:
        df = pd.read_excel("data/stocks.xlsx")
        index = int(df['Index'].max())

        if not isinstance(index, int):
            index = 1
        else:
            index += 1

        sheet_obj.append([index,
                          new_record['Product Name'],
                          new_record['Price'],
                          new_record['Quantity']])
        wb.save(wb_path)
        print("Data Added")
        return True

    except Exception as e:
        print(f"An error occurred while adding data: {str(e)}")
        return False


def display_stocks():
    data = pd.read_excel("./data/stocks.xlsx")
    data = data.to_dict(orient='records')
    return data


if __name__ == "__main__":
    print(display_stocks())
