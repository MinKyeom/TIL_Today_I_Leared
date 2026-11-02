import pymupdf
import os

pdf_file_path = 'pdf_check.pdf'
doc = pymupdf.open(pdf_file_path)

print(doc)

full_text = ''

header_height = 80
footer_height = 80

for page in doc:
  rect = page.rect
  
  print("check",rect)


for p in doc:
  text= p.get_text()
  full_text += text
  

# print(full_text)

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

print(pdf_file_name)

txt_file_path = f"{pdf_file_name}.txt"

# with open(txt_file_path,'w',encodeing='utf-8') as f:
#   f.wrtie(full_text)