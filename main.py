# Script to export tables from PDF files
# Requirements:
# Pandas (cmd --> pip install pandas)
# Tabula (cmd --> pip install tabula-py)
# openpyxl (cmd --> pip install openpyxl) to export to Excel from pandas dataframe

import tabula
import pandas as pd

# Path to input PDF file
pdf_in = "D:/Folder/File.pdf" #Path to PDF

# pages and multiple_tables are optional attributes
# outputs df as list
PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)

#View result
print('\nTables from PDF file\n'+str(PDF))

#CSV and Excel save paths
pdf_out_xlsx = "D:\Temp\From_PDF.xlsx"
#pdf_out_csv = "D:\Temp\From_PDF.csv"

# to Excel
PDF = pd.DataFrame(PDF)
PDF.to_excel(pdf_out_xlsx, index=False)

# to CSV
#tabula.convert_into (input_PDF, pdf_out_csv, pages='all',multiple_tables=True)
#print("Done")