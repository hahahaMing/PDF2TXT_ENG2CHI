import google_trans

OUTPUT = 'txt/homework1.txt'
with open('txt/data.txt', "r") as f1:
    str = f1.read()
str = str.replace('.', ' ')

split = str.split('\n')
with open(OUTPUT, "w", encoding='utf-8')as f:
    f.write("translate begins!" + '\n')
for i in range(0, len(split) - 1):
    # print(i)
    aaa = split[i].replace('\n', ' ') + '.'
    print(aaa)
    if len(aaa) > 2:
        ch = google_trans.G_tr(aaa[2:])
        with open(OUTPUT, "a", encoding='utf-8')as f:
            f.write(aaa + '\n')
            f.write(' ' + ch + '\n' + '\n')
