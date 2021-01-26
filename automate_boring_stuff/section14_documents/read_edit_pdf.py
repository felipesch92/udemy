import PyPDF2

pdf_file = open('Passagem.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())
for p in range(reader.numPages):
    print(reader.getPage(p).extractText())
