import pandas as pd

file1_name = "1"
file2_name = "2"

target1 = pd.read_csv(f'{file1_name}.csv')
target1 = target1.values.tolist()

target2 = pd.read_csv(f'{file2_name}.csv')
target2 = target2.values.tolist()

print(len(target1))
print(len(target2))

for i in target1:
    i.pop(0)
for i in target2:
    i.pop(0)
for i in target2:
    target1.append(i)

df = pd.DataFrame(target1)
df.to_csv(f"./测试工程师.csv")
