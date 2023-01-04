from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
pdfwriter=PdfFileWriter()
pdf=PdfFileReader('D:\python\Practice_files\python projects\Nitishatakam.pdf') #put here file name/path
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf', 'wb') as f:
    pdfwriter.write(f)

#program not running properly_07/12/22
