from pypdf import PdfReader 


def pdfReader(fileName):
    reader = PdfReader(fileName) 
    text = ""
    pageNum = 1
    for page in reader.pages:
        text += f"\nPN: {page.page_number}\n"
        text += page.extract_text() + "\n"
        print(text)
    return text
        

pdfReader("code/dummy.pdf")
