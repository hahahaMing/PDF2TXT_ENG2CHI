import google_trans

OUTPUT = 'txt/answer1031.txt'
with open('txt/homework1031.txt', "r") as f1:
    str = f1.read()

split = str.split('.')
with open(OUTPUT, "w", encoding='utf-8')as f:
    f.write("translate begins!" + '\n')
for i in range(0, len(split) - 1):
    aaa = split[i].replace('\n', ' ') + '.'
    print(aaa)
    if len(aaa) > 2:
        ch = google_trans.G_tr(aaa)
        with open(OUTPUT, "a", encoding='utf-8')as f:
            f.write(aaa + '\n')
            f.write(' ' + ch + '\n' + '\n')