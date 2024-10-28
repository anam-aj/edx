# Program to create "shirtificate"

from fpdf import FPDF


def main():
    #name  = input("Enter your name: ")

    create_shirtificate()


def create_shirtificate():

    # Create object
    pdf = FPDF()
    pdf.add_page()
    # Render image:
    pdf.image("shirtificate.png", x=10, y=60, w=190)
    # Header text
    pdf.set_font("Times", "B", 14)
    pdf.cell(0, 10, "Text with new font",0 , 1, "C")
    # Output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
