import pandas as pd

# 读取CSV文件
df = pd.read_csv('D:\\pycahrm\\Spider-work\\result\\result.csv',encoding='gbk')


# 将数据保存为Excel文件
df.to_excel('result_excel.xlsx', index=False)
print("转化完成")
