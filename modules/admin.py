import os
import sys
import openpyxl


def load_workbook(wb_path):  # Loading Excel Sheet
    return openpyxl.load_workbook(wb_path)


wb_path = "data\stocks.xlsx"
wb = load_workbook(wb_path)
sheet = wb['Sheet1']
sheet_obj = wb.active


def Add_Stock(new_record):
    try:
        index = int(sheet_obj.max_row)-1
        print(sheet_obj)
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
    data = []
    header = [cell.value for cell in sheet_obj[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = dict(zip(header, row))
        data.append(row_data)

    print(data)
    return data


if __name__ == "__main__":
    print(display_stocks())
