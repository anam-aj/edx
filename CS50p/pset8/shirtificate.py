# Program to create "shirtificate"

from fpdf import FPDF

def main():
    name  = input("Enter your name: ")

    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
