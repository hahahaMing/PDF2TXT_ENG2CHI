
SOUT = 'txt/sort.txt'
class sortItemCount:
    def __init__(self):
        self.item = []
        self.value = []
        self.length = 0

    ## 插入元素，同时统计该元素出现的次数并排序
    def insert(self, item):
        if item is not '' and len(item)>2 and not item.isdigit():
            if self.length == 0:
                self.item.append(item)
                self.value.append(1)
                self.length += 1
            else:
                flag = 0
                for i in range(self.length):
                    if self.item[i] == item:
                        self.value[i] += 1
                        flag = 1
                        ## 插入重复元素，可能需要重新排序，（段部分重排）
                        index = i
                        while self.value[index] > self.value[index - 1] and index > 0:
                            self.value[index - 1], self.value[index] = self.value[index], self.value[index - 1]
                            self.item[index - 1], self.item[index] = self.item[index], self.item[index - 1]
                            index -= 1
                        break
                        ## 新元素插入不用排序
                if flag == 0:
                    self.item.append(item)
                    self.value.append(1)
                    self.length += 1


def sorter(split,length):

    ## 遍历array,自定义sortItemCount保存每种元素(item)和它出现的次数(value),并排序
    sIC = sortItemCount()
    for m in range(length):
        sIC.insert(split[m])

    item = sIC.item
    value = sIC.value
    print(item)
    # print(value)
    print(len(value))
    with open(SOUT, "w", encoding='utf-8')as f:
        f.write("sort begins!" + '\n')
    with open(SOUT, "a", encoding='utf-8')as f:
        for i in range(0,len(value)):
            f.write(str(value[i])+'\t'+item[i]+'\n')
