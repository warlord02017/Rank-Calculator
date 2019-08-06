import PyPDF2
import re
pdfFileObj = open('Result.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
l=list()
for i in range(pdfReader.getNumPages()):
    pageObj = pdfReader.getPage(i)
    z=pageObj.extractText()
    a=' '.join(re.findall(r'THIRD YEAR SGPA : (\d+\.\d+\d+)',z))
    l.extend(a.split(" "))
l[:]=(value for value in l if value != '')
print(l)
your_score=float(input("Enter your cgpa (eg: 9.00): "))
n=0
for i in l:
    if(float(i)>your_score): n=n+1
print(f'Your rank is: {n+1}')










