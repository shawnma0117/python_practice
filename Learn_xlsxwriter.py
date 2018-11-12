
# coding: utf-8

# In[ ]:


# %load Learn_xlsxwriter.py
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

##############################################################################
#
#  adding formatting
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Add a number format for cells with money.
money = workbook.add_format({'num_format': '$#,##0'})

# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# Some data we want to write to the worksheet.
expenses = (
 ['Rent', 1000],
 ['Gas',   100],
 ['Food',  300],
 ['Gym',    50],
)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
 worksheet.write(row, col,     item)
 worksheet.write(row, col + 1, cost, money)
 row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total',       bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()


##############################################################################
#
# An example of converting a Pandas dataframe to an xlsx file
# with column formats using Pandas and XlsxWriter.
#
# Copyright 2013-2018, John McNamara, jmcnamara@cpan.org
#

import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Numbers':    [1010, 2020, 3030, 2020, 1515, 3030, 4545],
                   'Percentage': [.1,   .2,   .33,  .25,  .5,   .75,  .45 ],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("pandas_column_formats.xlsx", engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add some cell formats.
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%'})

# Note: It isn't possible to format any cells that already have a format such
# as the index or headers or any cells that contain dates or datetimes.

# Set the column width and format.
worksheet.set_column('B:B', 18, format1)

# Set the format but not the column width.
worksheet.set_column('C:C', None, format2)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# In[4]:


import xlsxwriter
import pandas as pd


# In[37]:


# 实验用户画像代码，应该如何写formatting
df = pd.DataFrame({'Numbers':    [1010, 2020, 3030, 2020, 1515, 3030, 4545],
                   'Percentage': [.1,   .2,   .33,  .25,  .5,   .75,  .45 ],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("pd_col_formats.xlsx", engine='xlsxwriter')


# In[38]:


# 不能直接用df.to_excel, 因为无法控制每个单元格的格式。
wb  = writer.book
# ws = writer.sheets['Sheet1']
ws = wb.add_worksheet('sheet1')


# In[39]:


# 'font_name':,
header_dict = {'bold':True, 'bg_color':'#D9E1F2', 'border':True}
cell_num_dict = {'border':True, 'num_format':'#,##0'}   # 千分位整数
cell_pct_num_dict = {'border':True, 'num_format':'0.0%'} # 百分号后1位


# In[40]:


header_fmt = wb.add_format(header_dict)
cell_num_fmt = wb.add_format(cell_num_dict)
cell_pct_num_fmt = wb.add_format(cell_pct_num_dict)


# In[20]:


df.columns.values


# In[41]:


# 单独打印header
for col_num, value in enumerate(df.columns.values):
    ws.write(0, col_num, value, header_fmt)


# In[27]:


get_ipython().magic(u'pinfo df.iterrows')


# In[42]:


# 打印df主题
col = 0
for idx, row in df.iterrows():
    ws.write(idx+1, col, row[0], cell_num_fmt)
    ws.write(idx+1, col+1, row[1], cell_pct_num_fmt)


# In[ ]:


# 设置一整行，一整列。 会被后面的格式设置覆盖
# ws.set_row(0,None,header_fmt) 
# ws.set_column(1,1,None,cell_num_fmt)
# ws.set_column(2,2,None,cell_pct_num_fmt)


# In[43]:


writer.save()

