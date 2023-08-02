import requests
import random
import pandas as pd

import requests
import random
import pandas as pd

def spider_main(url, recruitType, num, careerJobId, database_all):
    """
    爬取数据并返回职位地点、人数、学历和薪资信息列表

    参数:
    url (str): API的URL
    recruitType (int): 招聘类型
    num (list): 每种招聘类型的数量列表
    careerJobId (int): 职位ID
    database_all (list): 存储数据的列表

    返回:
    list: 职位地点、人数、学历和薪资信息列表
    """
    j = 1
    for _ in range(num):
        payload = {
            "page": j,
            "random": "true",
            "jobCity": "",
            "careerJobId": careerJobId,
            "recruitType": recruitType,
            "pageSize": 20,
            "recommend": "false",
            "requestFrom": 0,
            "pageSource": 5026,
            "visitorId": "bf74ad80-411a-4bad-b95a-0e8ef3f12f4b"
        }
        res = requests.post(url, data=payload)
        database = res.json()
        try:
            datas = database["data"]["datas"]
        except KeyError:
            print("Error: Failed to retrieve job data from API.")
            break
        if not datas:
            break
        for data in datas:
            job_name = data["jobName"]
            job_citylist = data["jobCityList"][0]
            job_personScales = data["recommendInternCompany"]["personScales"]
            job_edulevel = data["eduLevel"]
            job_salaryMin = data["salaryMin"]
            job_salaryMax = data["salaryMax"]
            job_salaryMonth = data["salaryMonth"]

            if job_edulevel == 0:
                job_edulevel = '学历不限'
            elif job_edulevel == 5000:
                job_edulevel = '本科'
            elif job_edulevel == 4000:
                job_edulevel = '大专'
            else:
                job_edulevel = '硕士'
            print(job_name)
            database_Line = [job_name, job_citylist, job_personScales, job_edulevel, job_salaryMin, job_salaryMax, job_salaryMonth]
            database_all.append(database_Line)
        j += 1
    return database_all

def store_main(job, get_database_source):
    """
    将获取到的数据存储到CSV文件

    参数:
    job (str): 职位名称
    get_database_source (function): 获取数据的函数

    返回:
    None
    """
    source = get_database_source()  # 调用获取数据的函数
    df = pd.DataFrame(source)  # 使用获取的数据创建DataFrame
    df.to_csv(f"./{job}.csv")  # 将DataFrame保存为CSV文件

def get_database_java():
    """
    获取Java职位数据

    返回:
    list: Java职位数据列表
    """
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904141{}".format(random_number)
    recruitType = 1
    num = [8, 36, 38]
    careerJobId = 11002
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType, num[i], careerJobId, database_all)
        recruitType += 1
    return database_all


def get_database_C_plus():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904453{}".format(random_number)
    recruitType = 1
    num = [6,13,36]
    database_all = []
    careerJobId = 11003
    for i in range(3):
        database_all = (url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_C():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=1690446{}".format(random_number)
    num = [1,1,5]
    careerJobId = 11011
    recruitType = 1
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_Python():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904469{}".format(random_number)
    recruitType = 1
    num = [1,4,10]
    careerJobId = 11014
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_back_end_engineer():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904478{}".format(random_number)
    recruitType = 1
    num = [2,8,9]
    careerJobId = 11234
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_full_Stack():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904504{}".format(random_number)
    recruitType = 1
    num = [1,36,38]
    careerJobId = 143752
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_Front_end():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904508{}".format(random_number)
    recruitType = 1
    num = [2,10,18]
    careerJobId = 11022
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_Web_Front_end():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904141{}".format(random_number)
    recruitType = 1
    num = [1,5,9]
    careerJobId = 11235
    database_all = []
    for i in range(3):
        database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
        recruitType += 1
    return database_all

def get_database_senior_test_engineer():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=1690451{}".format(random_number)
    recruitType = 1
    num = [9,9,9]
    careerJobIds = [11025,11026,11238,143761,143763,143764]
    database_all = []
    for careerJobId in careerJobIds:
        for i in range(3):
            database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
            recruitType += 1
    return database_all

def get_database_data_Analysist():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904552{}".format(random_number)
    recruitType = 1
    num = [9,9,9]
    careerJobIds = [11027,11028,11029,11239,143764]
    database_all = []
    for careerJobId in careerJobIds:
        for i in range(3):
            database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
            recruitType += 1
    return database_all

def get_database_Devops():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904643{}".format(random_number)
    recruitType = 1
    num = [9,9,9]
    careerJobIds = [11030,11031,11032,11033,11250,142693,143765,143768,143767]
    database_all = []
    for careerJobId in careerJobIds:
        for i in range(3):
            database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
            recruitType += 1
    return database_all

def get_database_AI():
    random_number = random.randint(10000, 99999)
    url = "https://www.nowcoder.com/np-api/u/job/search?_=16904664{}".format(random_number)
    recruitType = 1
    num = [10,10,30]
    careerJobIds = [11006,143769,11247,11246,11249,143770,11245,11244,11243,11242,11241]
    database_all = []
    for careerJobId in careerJobIds:
        for i in range(3):
            database_all = spider_main(url, recruitType,num[i],careerJobId,database_all)
            recruitType += 1
    return database_all

# 其他get_database_xxx函数的注释与get_database_java函数类似

# 调用存储函数
# store_main(job, get_database_AI)

# job = 'java'
# store_main(job,get_database_java())
# job = 'C_plus'
# store_main(job,get_database_C_plus())
# job = 'C'
# store_main(job,get_database_C())
# job = 'Python'
# store_main(job,get_database_Python())
# job = 'back_end_engineer'
# store_main(job,get_database_back_end_engineer())
# job = "full_Stack"
# store_main(job,get_database_full_Stack())
# job = "Front_end"
# store_main(job,get_database_Front_end())
# job = "Web_Front_end"
# store_main(job,get_database_Web_Front_end())
# job = "senior_test_engineer"
# store_main(job,get_database_senior_test_engineer())
# job = "data_Analysist"
# store_main(job,get_database_data_Analysist())
# job = "Devops"
# store_main(job,get_database_Devops())
# job = "AI"
# store_main(job,get_database_AI)