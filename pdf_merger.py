# pdf merger

import pypdf

pdffiles =["1.pdf","2.pdf"]

merger =pypdf.PdfMerger()
for filename in pdffiles:
    pdffile= open(filename,'rb')
    pdfReader = pypdf.PdfReader(pdffile)
    merger.append(pdfReader)

pdffile.close()
merger.write("merged.pdf")
