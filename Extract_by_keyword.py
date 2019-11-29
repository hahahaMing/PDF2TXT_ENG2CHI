

OUTPUT = 'txt/result_extract.txt'
# 打开文件

# 读取文件
with open('MarkDown\ICRA2019.md', "r") as f1:
    str = f1.read()

# 用|分割
split = str.split('|')

# 遍历看是否含有关键词
with open(OUTPUT, "w", encoding='utf-8')as f:
    f.write("/*************************/" + '\n')


# 输入关键词，输入exit0跳出循环
print("For exit, input 'exit0' .")
keyword = input("keyword = ")
with open(OUTPUT, "a", encoding='utf-8')as f:
    f.write("keyword = "+ '"'+keyword + '"' + '\n' + '\n')
# 遍历
for i in range(0, len(split) - 1):
    if keyword in split[i]:
        # 打印
        print(split[i])
        # 写文件
        with open(OUTPUT, "a", encoding='utf-8')as f:
            f.write(split[i] + '\n'+'\n')







# 打印（翻译）