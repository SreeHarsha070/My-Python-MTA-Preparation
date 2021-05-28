import os,PyPDF2

userpdflocation=str(input('D:\PythonProjs'))
os.chdir(userpdflocation)

userfilename=input('modified')
pdf2merge=[]

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdfWriter=PyPDF2.PdfFileWriter()

for filename in pdf2merge:
    pdfFileObj=open(filename,'rb')
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pageObj=pdfReader.getPage(pageNum)
        pdfWriter.addPages(pageObj)
pdfOutput=open(userfilename+'.pdf','wb')

pdfWriter.write(pdfOutput)

pdfOutput.close()
        
    
    
