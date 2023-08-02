import csv
import pandas as pd
import numpy as np
import os

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

def store_job():
    path_file = "./最终总表.csv"

    data = pd.read_csv(path_file,encoding='gbk')


    #Large companies Medium companies Small companies
    Java_job = []
    C_job = []
    python_job = []
    AI_job = []
    testor_job = []
    headend_job = []
    full_stack_job = []
    operator_job = []

    for i in range(len(data)):
        if data['职位'][i] == 'C开发工程师':
            C_job.append(data.loc[i])
            continue
        if data['职位'][i] == '运维工程师':
            operator_job.append(data.loc[i])
            continue
        if data['职位'][i] == '人工智能工程师':
            AI_job.append(data.loc[i])
            continue
        if data['职位'][i] == '全栈工程师':
            full_stack_job.append(data.loc[i])
            continue
        if data['职位'][i] == '前端工程师':
            headend_job.append(data.loc[i])
            continue
        if data['职位'][i] == '测试工程师':
            testor_job.append(data.loc[i])
            continue
        if data['职位'][i] == 'python开发工程师':
            python_job.append(data.loc[i])
            continue
        if data['职位'][i] == 'Java开发工程师':
            Java_job.append(data.loc[i])
            continue
    companies = ['Java开发工程师','python开发工程师','测试工程师','前端工程师','全栈工程师','人工智能工程师','运维工程师','C开发工程师']
    companies_data = [Java_job,python_job,testor_job,headend_job,full_stack_job,AI_job,operator_job,C_job]
    for i in range(8):
        print(companies[i])
        store_main(companies[i], companies_data[i])

def store_salary_job():
    path_files = ["./C开发工程师.csv",'./Java开发工程师.csv','./python开发工程师.csv','./测试工程师.csv','./前端工程师.csv','./全栈工程师.csv','./人工智能工程师.csv','./运维工程师.csv']
    for path_file in path_files:
        data_companies = pd.read_csv(path_file, encoding='utf-8')
        column_mean = data_companies['薪资'].mean()
        print(path_file)
        print(column_mean)

def store_salary_job_max():
    path_files = ["./C开发工程师.csv",'./Java开发工程师.csv','./python开发工程师.csv','./测试工程师.csv','./前端工程师.csv','./全栈工程师.csv','./人工智能工程师.csv','./运维工程师.csv']
    for path_file in path_files:
        data_companies = pd.read_csv(path_file, encoding='utf-8')
        max_salary_job = data_companies['薪资'].max()
        job_name = os.path.basename(path_file)
        print(job_name)
        print(max_salary_job)

store_salary_job_max()