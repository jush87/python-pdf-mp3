from gtts import gTTS
import pdfplumber
from pathlib import Path
def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix =='.pdf':
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode ='rb')) as pdf:
            pages =[page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        myaudio =gTTS(text=text, lang=language, slow=False)
        file_name =Path(file_path).stem
        myaudio.save(f'{file_name}.mp3')
        return f'[+] {file_name}.mp3 saved successfully!\n--Have a good day!---'

    else:
        return 'File not exists, check the file path!'
def main ():
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'fr': ")
    while language not in ("en", "fr"):
        language = input("Choose language, for example 'en' or 'fr': ")
    print(pdf_to_mp3(file_path=file_path, language=language))

    if __name__ == '__main__':
        main()

