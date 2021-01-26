import docx

d = docx.Document('TCC - Versão 1.docx')
fullText = []
for p in d.paragraphs:
    #print(p.text)
    fullText.append(p.text)

for p in fullText:
    print(p)
