from PyPDF2 import PdfFileReader, PdfFileWriter
import translate
import sort_words

OUTPUT = 'txt/output.txt'

# readFile = 'pdf/split.pdf'  # one page pdf for test
# readFile = 'pdf/ks.pdf'
readFile = 'pdf/wtf_trans.pdf'


def getPdfContent(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0, pdf.getNumPages()):
        pageObj = pdf.getPage(i)

        extractedText = pageObj.extractText()
        content += extractedText + "\n"
        # return content.encode("ascii", "ignore")
    return content


"""translate
"""
# pdf_char = getPdfContent(readFile)
# split = pdf_char.split('.')
# print(len(split))
# with open(OUTPUT, "w", encoding='utf-8')as f:
#     f.write("translate begins!" + '\n')
# for i in range(0,len(split)-1):
#     # print(i)
#     aaa = split[i].replace('\n', ' ')+'.'
#     print(aaa)
#     ch = translate.translate2(aaa)
#
#     with open(OUTPUT, "a", encoding='utf-8')as f:
#         f.write(aaa+'\n')
#         f.write(ch +'\n'+'\n')

"""words statistics
"""
pdf_char = getPdfContent(readFile)

for i in ['\n','.',',','(',')','*','/',':','&','，','[',']','=',"™",'‚','Œ']:
    pdf_char = pdf_char.replace(i, ' ')

split = pdf_char.split(' ')
# print(len(split))
# print(split)

sort_words.sorter(split, len(split))


