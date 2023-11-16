from docx import Document
import re

def remove_markup(docx_path, txt_path):
    # Load the DOCX file
    doc = Document(docx_path)

    # Open the TXT file for writing
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # Iterate through paragraphs in the DOCX file
        for paragraph in doc.paragraphs:
            # Remove markup using regular expression
            clean_text = re.sub(r'<.*?>', '', paragraph.text)
            
            # Write cleaned text to the TXT file
            txt_file.write(clean_text + '\n')

if __name__ == "__main__":
    remove_markup('/home/robotics/ngant/so_tay_sinh_vien.docx', 'a.txt')
