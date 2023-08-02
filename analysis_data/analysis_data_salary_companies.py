import csv
import pandas as pd
import numpy as np


def store_main(companies,companies_data ):
    """
    将获取到的数据存储到CSV文件

    参数:
    job (str): 职位名称
    get_database_source (function): 获取数据的函数

    返回:
    None
    """
    source = companies_data  # 调用获取数据的函数
    df = pd.DataFrame(source)  # 使用获取的数据创建DataFrame
    df.to_csv(f"./{companies}.csv")  # 将DataFrame保存为CSV文件

def store_companies():
    path_file = "./最终总表.csv"

    data = pd.read_csv(path_file,encoding='gbk')


    #Large companies Medium companies Small companies
    Large_companies = []
    Medium_companies = []
    Small_companies = []


    for i in range(len(data)):
        if data['公司规模'][i] == '大型公司':
            Large_companies.append(data.loc[i])
            continue
        if data['公司规模'][i] == '中型公司':
            Medium_companies.append(data.loc[i])
            continue
        if data['公司规模'][i] == '小型公司':
            Small_companies.append(data.loc[i])
            continue

    companies = ['大型公司','中型公司','小型公司']
    companies_data = [Large_companies,Medium_companies,Small_companies]
    for i in range(3) :
        store_main(companies[i],companies_data[i])

def store_salary(path_file,store_salary_companies):
    data_companies = pd.read_csv(path_file, encoding='utf-8')
    column_mean = data_companies['薪资'].mean()
    store_salary_companies.append(column_mean)


def store_salary_companies():
    store_salary_companies = []
    path_files = ["./大型公司.csv","./中型公司.csv","./小型公司.csv"]
    for i in range(3):
        path_file = path_files[i]
        store_salary(path_file,store_salary_companies)

def store_salary_max(path_file,store_salary_companies):
    data_companies = pd.read_csv(path_file, encoding='utf-8')
    column_mean = data_companies['薪资'].max()
    store_salary_companies.append(column_mean)


def store_salary_companies_max():
    store_salary_companies_max = []
    path_files = ["./大型公司.csv","./中型公司.csv","./小型公司.csv"]
    for i in range(3):
        path_file = path_files[i]
        store_salary_max(path_file,store_salary_companies_max)
    return store_salary_companies_max

store_companies()
print(store_salary_companies())
print(store_salary_companies_max())