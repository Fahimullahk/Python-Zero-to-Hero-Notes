from pypdf import PdfWriter

merger = PdfWriter()
pdfs = ["Deep-01.pdf", "Deep-02.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("finalpdf.pdf")
merger.close()
print("Your merger is successfully done...")

