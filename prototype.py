'''
------------------------------------------
@auth - cdjoanem
------------------------------------------

Objectives:
    1. Write into an excel file
    2. Import AI to impliment desired excel format
    3. Create GUI face for ease of use
'''

#----import statements-----------------
import xlwt
from xlwt import *
from datetime import datetime

#----main------------------------------

wb = Workbook() # excel workbook is created 

sheet1 = wb.add_sheet('Due Date Organizer') # creates a sheet within the workbook

# font style
style1 = xlwt.easyxf("""
                     font: name Biome;
                     borders: left thick, right thick, top thick, bottom thick;
                     pattern: pattern solid, fore_colour yellow;
                     """,
                     num_format_str='MM-DD-YYYY')

# writing in cell format 
sheet1.write(1, 0, '7281', style1)
sheet1.write(2, 0, '78921')
sheet1.write(3, 0, '1234')
sheet1.write(4, 0, '982')
sheet1.write(5, 0, '198812', style1)
sheet1.write(6, 0, '6786')
sheet1.write(7, 0, '87912')


# sheet1.write(3, 3, xlwt.Formula("A2+A1"))
wb.save('Master To-Do Generator/example.xls')