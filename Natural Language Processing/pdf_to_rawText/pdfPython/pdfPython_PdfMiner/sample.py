"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import BytesIO
import string
import codecs

#import binascii

def pdf_to_text(pdfname):
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from BytesIO
    text = sio.getvalue()
    
    # Cleanup
    device.close()
    sio.close()
    
    return text

t = pdf_to_text("test1.pdf")
print(t)
#output =open("output.doc","w")
#b =t.decode("utf-8")

#filter unprintable character
#f ="".join(filter(lambda x: x in string.printable, b))

#output.write(b)
#output.close()
