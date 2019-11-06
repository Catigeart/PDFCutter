from PyPDF2 import PdfFileWriter, PdfFileReader
import os
filename = os.listdir('./')

def cutter(filename):
    fr = PdfFileReader(open('./' + filename, 'rb'), strict=False)
    fw = PdfFileWriter()
    for pageNum in range(0, fr.getNumPages()):
        p = fr.getPage(pageNum)
        fw.addPage(p)
        fwPath = './output/'
        if not os.path.exists(fwPath):
            os.makedirs(fwPath)
        outputStream = open('./output/' + filename[0:-4] + str(pageNum) + '.pdf', "wb")
        fw.write(outputStream)
        outputStream.close()

for i in filename:
    filename = i
    if 'pdf' in filename[-4:]:
        cutter(filename)
    fwName = os.listdir('./output/')
    for i in fwName:
        print(i)