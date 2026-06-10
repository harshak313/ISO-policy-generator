import pandas as pd

# Update path if needed
excel_file = "../documents/standards/ISO_27001_2022.xlsx"

# Read sheets
clauses_df = pd.read_excel(excel_file, sheet_name="Clauses")
controls_df = pd.read_excel(excel_file, sheet_name="Annex A Controls")

print("\n=== CLAUSES ===")
print(clauses_df.head())

print("\n=== CONTROLS ===")
print(controls_df.head())

print("\nTotal Clauses:", len(clauses_df))
print("Total Controls:", len(controls_df))