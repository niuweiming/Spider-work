import requests as r
import time
import json
import pandas as pd
map = {
    "&#xe059": "2",
    "&#xe6d2": "0",
    "&#xec59": "人",
    "&#xe08f": "5",
    "&#xe572": "1"
}
def generate(city, maxsalary, minsalary, degree, scale: str, jobname = "java开发工程师"):
    for k,v in map.items():
        scale = scale.replace(k, v)
    return [jobname, city, scale, degree, minsalary, maxsalary, 12]

# city　城市
# cname 公司名称
# maxsalary 好像是按天算的 为0即面议。
# minsalary
# degree 学历
# scale 公司规模 映射编码

def run(words):
    result = list()
    cur = 0
    url = url = "https://www.shixiseng.com/app/interns/search/v2?build_time=1690451714124&page=1&type=intern&keyword=" + str(words) + "&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    re = r.get(url)
    total = int(json.loads(re.text)["msg"]["total"])
    print(f"{words}初始化完成，共{total}条数据。")
    print("进入循环。。。。")
    for i in range(int(total / 20) + 1):
        page = str(i + 1)
        url = "https://www.shixiseng.com/app/interns/search/v2?build_time=1690451714124&page=" + page + "&type=intern&keyword=" + str(words) + "&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
        re = r.get(url)
        js = json.loads(re.text)
        for i in range(20):
            cur += 1
            try:
                data = js["msg"]["data"][i]
            except:
                break
            city = data["city"]
            # cname = data["cname"]
            maxsalary = data["maxsalary"]
            minsalary = data["minsalary"]
            degree = data["degree"]
            scale = data["scale"]
            one = generate(city=city,maxsalary=maxsalary,minsalary=minsalary,degree=degree,scale=scale)
            result.append(one)
        print(f"{words}--->已查询{cur}")
        time.sleep(2)
    print(f"{words}--->正在写入:" + f"{words}.csv")
    df = pd.DataFrame(result)
    df.to_csv(f"./{words}.csv")

    