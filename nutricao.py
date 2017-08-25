import openpyxl

wb = openpyxl.load_workbook('fiat.xlsx')
ws = wb.get_sheet_by_name('Carros')
wb = wb.get_sheet_by_name('Carros')





import sqlite3
conexao = sqlite3.connect('ITAU')
cursor = conexao.cursor()






conexao.commit()
cursor.close()
