from PyPDF2 import PdfFileReader, PdfFileWriter
import translate

readFile = 'pdf/wtf_trans.pdf'

pdf = PdfFileReader(open(readFile, "rb"))

print(pdf.getOutlines())


