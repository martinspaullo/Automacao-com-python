import PyPDF2 as pdf, os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from PIL import Image

# Busca dados e metadata de um arquivo PDF
def get_pdf_metadata(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results)

#Dividindo pdf por paginas
def split_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            output_filename = f"files/{filename}_{page_num+1}.pdf"
            with open(output_filename, "wb") as out:
                writer.write(out)
            print(f"PDF criado com o nome: {output_filename}")

#Dividindo paginas por paginas especifica
def get_pdf_upto(pdf_path, start_page:int=0,stop_page:int=0):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            output_filename = f"files/{filename}_from_{start_page+1}_to_{stop_page+1}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

#Listando pdf e unindo os pdf
def fetch_all_pdf_files(parent_folder:str): #Listando
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path,name))
    return target_files

def merge_pdf(list_pdfs, output_filename="files/final_pdf.pdf"): #unindo
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in list_pdfs:
            merger.append(file)
        merger.write(f)


# Rotacionado PDF
def rotate_pdf(pdf_path, page_num:int, rotation:int=90):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        output_filename = f"files/{filename}_{rotation}_rotated_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

#Extraindo imagens de PDF
def extract_images_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            for img_file_obj in selected_page.images:
                with open(f"files/{img_file_obj.name}", "wb") as out:
                    out.write(img_file_obj.data)

#Convertendo imagem em PDF
def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    filename = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(filename)


# Busca dados e metadata de um arquivo PDF
print(get_pdf_metadata("files/teste.pdf"))
print(get_pdf_metadata("files/teste.pdf").title)
print(get_pdf_metadata("files/teste.pdf").author)

print('---------------/ Extract Teste/----------------------------')
print(extract_text_from_pdf("files/teste.pdf"))

print('---------------/ Extract sample/----------------------------')
print(extract_text_from_pdf("files/sample.pdf"))

#Dividindo pdf por paginas
split_pdf("files/check.pdf")

#Dividindo paginas por paginas especifica
get_pdf_upto("files/check.pdf", 1, 2)

#Listando pdf e unindo os pdf
#print(fetch_all_pdf_files("files/")) #Listando os pdf
pdf_list = fetch_all_pdf_files("files/")  #unindo os pdf
merge_pdf(pdf_list)

# Rotacionado PDF
rotate_pdf("files/sample.pdf", 0)

#Extraindo imagens de PDF
extract_images_from_pdf("files/test_img.pdf")

#Convertendo imagem em PDF
convert_img_pdf("files/Image34.jpg")