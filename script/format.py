import pandas as pd

file_name = "全栈工程师"

target = pd.read_csv(f'{file_name}.csv')
target = target.values.tolist()

for i in target:
    # 实习生大概每年240天
    if "K" in i[5]:
        s = i[5].split("K")
        baseSalary = s[0].split("-")
        baseSalary = (int(baseSalary[0]) + int(baseSalary[1])) / 2 * 1000
        if ("·" in s[1]):
            salary = baseSalary * int(s[1].split("·")[1].split("薪")[0])
        else:
            salary = baseSalary * 12
    elif "元/天" in i[5]:
        s = i[5].replace("元/天", "")
        baseSalary = s.split("-")
        salary = (int(baseSalary[0]) + int (baseSalary[1])) * 120
    elif "元/时" in i[5]:
        s = i[5].replace("元/时", "")
        baseSalary = s.split("-")
        salary = (int(baseSalary[0]) + int (baseSalary[1])) * 120 * 6
    elif "元/月" in i[5]:
        s = i[5].replace("元/月", "")
        baseSalary = s.split("-")
        if "-" in s:
            salary = (int(baseSalary[0]) + int (baseSalary[1])) * 12
        else:
            salary = int(baseSalary[0]) * 12
    salary = int(salary)
    i[5] = salary

    ccount = int(i[3].split("人")[0])
    if (ccount < 100):
        ccount = "小型公司"
    elif (ccount > 1000):
        ccount = "大型公司"
    else:
        ccount = "中型公司"
    i[3] = ccount

    if "个月" in i[4]:
        degree = "在校生"
    else:
        degree = i[4]
    i[4] = degree
    i.pop(0) #　删除最开头重复序号
    
for i in range(20):
    print(target[i])

df = pd.DataFrame(target)
df.to_csv(f"./{file_name}.csv")