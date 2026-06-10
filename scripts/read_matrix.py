import pandas as pd

matrix_file = "../documents/matrix/ISO 27001_Document_Coverage_Matrix.xlsx"

# Show sheet names first
xls = pd.ExcelFile(matrix_file)

print("\nAvailable Sheets:")
print(xls.sheet_names)

for sheet in xls.sheet_names:
    print(f"\n===== {sheet} =====")
    df = pd.read_excel(matrix_file, sheet_name=sheet)

    print(df.head())
    print(f"\nRows: {len(df)}")