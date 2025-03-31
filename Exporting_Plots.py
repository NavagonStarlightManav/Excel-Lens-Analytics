import pandas as pd
import seaborn as sns
import openpyxl
import matplotlib.pyplot as plt

mpg = sns.load_dataset('mpg')
mpg.head()

wb = openpyxl.Workbook()

ws1 = wb.create_sheet('violin')

sns.violinplot(x='origin', y='mpg', data=mpg)
plt.show()

plt.savefig('violin.jpg')

img = openpyxl.drawing.image.Image('violin.jpg')
img.anchor = 'A1'
ws1.add_image(img)

wb.save('plotting.xlsx')

#you can also use swarm plots and other