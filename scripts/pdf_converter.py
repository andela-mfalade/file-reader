"""Read a pdf file."""

import sys
import time

import pyPdf


def read_pdf_file(path):
    """Read a pdf file."""
    content = ""
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"
    return content


def sys_exit(feedback):
    """End process with exit code of 1."""
    sys_print(feedback)
    time.sleep(0.5)
    sys.exit(1)


def sys_print(text_list):
    """Print given text to command line."""
    for text in text_list:
        sys.stdout.write(text)


def main():
    """Read a pdf file."""
    if len(sys.argv) < 2:
        feedback = [
            "Please specify a file path,\n\n",
            "run >  python converter.py <path_to_pdf_file> \n\n"
        ]
        sys_print(feedback)

    elif not sys.argv[-1].lower().endswith('.pdf'):
        feedback = [
            "Invalid File Type\n\n",
            "The expect file is a PDF is.\n\n",
            "python converter.py <path_to_pdf_file>\n"
        ]
        sys_exit(feedback)
    else:
        text = [read_pdf_file("test1.pdf")]
        sys_exit(text)


if __name__ == '__main__':
    main()
