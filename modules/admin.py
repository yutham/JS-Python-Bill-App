import openpyxl  # This Import is for using excel is python
import pandas as pd  # Its For creating data frames
import numpy as np
import os


def load_workbook(wb_path):  # Loading Excel Sheet
    if os.path.exists(wb_path):
        return openpyxl.load_workbook(wb_path)
    else:
        return None


try:
    wb_path = "./data/product.xlsx"
    wb = load_workbook(wb_path)

    if wb is not None:
        sheet = wb['Sheet1']
        sheet_obj = wb.active
    else:
        print(f"Excel file '{wb_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


def Add_Data():
    try:
        df = pd.read_excel("./data/product.xlsx")
        max_value = df['Id'].max()
        print(type(max_value))
        if isinstance(max_value, (int, np.int64)):
            max_value += 1
        else:
            max_value = 1
        new_record = {'Id': max_value,
                      'Column1': 'Value1',
                      'Column2': 'Value2'}
        new_record['Column1'] = input("\nEnter the Product Name: ")
        new_record['Column2'] = int(input("Enter the Rate: "))
        sheet_obj.append([new_record['Id'],
                          new_record['Column1'],
                          new_record['Column2']])
        wb.save(wb_path)
        print("Added Successfully")
        add_more = input("\nWant to Add more Data? (yes/no): ")
        if add_more.lower() == "yes":
            Add_Data()
    except Exception as e:
        print(f"An error occurred while adding data: {str(e)}")


def view():
    # viewing the data using data-frame
    df = pd.read_excel("./data/product.xlsx", index_col=0)
    return print(df)


def search(id):  # this function is to search the data in the excel sheet
    max_row = sheet.max_row
    for i in range(1, max_row+1):
        if sheet.cell(row=i, column=1).value == id:
            print("record Found")
            return i


def Display_record(row):  # this function is to the single data in the excel sheet
    try:
        max_column = sheet.max_column
        for i in range(1, max_column+1):
            cell_obj = sheet.cell(row=row, column=i)
            print(cell_obj.value)
    except Exception as e:
        print(f"An error occurred while displaying the record: {str(e)}")


def Update_records(row):  # this function is to update the data in the excel sheet
    try:
        new_record = input("\n Enter the Product Name:")
        new_rate = int(input("\n Enter the Rate:"))
    except ValueError:
        print("Invalid Rate. Rate should be an integer.")
        return
    sheet.cell(row=row, column=2, value=new_record)
    sheet.cell(row=row, column=3, value=new_rate)
    wb.save(wb_path)
    return print("record updated")


def Delete_record(row):  # this function is to delete the data in the excel sheet
    sheet.delete_rows(row)
    wb.save(wb_path)
    print(row)
    max_row = sheet.max_row
    for i in range(row, max_row + 1):
        sheet.cell(row=i, column=1, value=i-1)
    wb.save(wb_path)


#
while True:
    print("\n 1:add")
    print("\n 2:view")
    print("\n 3:Update")
    print("\n 4:Delete")
    ch = int(input("enter your choic:"))
    if ch == 1:
        Add_Data()
    elif ch == 2:
        view()
    elif ch == 3:
        x = int(input("\n Enter the Id:"))
        row = search(x)
        Display_record(row)
        y = input("\n want to edit the record ? yes/no:")
        if y.lower() == 'yes':
            Update_records(row)
    elif ch == 4:
        x = int(input("\n Enter the Id:"))
        row = search(x)
        Display_record(row)
        y = input("\n want to Delete the record ? yes/no:")
        if y.lower() == 'yes':
            Delete_record(row)
