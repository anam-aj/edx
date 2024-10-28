# Program to create "shirtificate"

from fpdf import FPDF


def main():
    name  = input("Enter your name: ")

    create_shirtificate(name)


def create_shirtificate(name):

    # Create object
    pdf = FPDF()
    # Add page
    pdf.add_page()
    # Rendering image:
    pdf.image("shirtificate.png")
    # Setting font: helvetica bold 15
    pdf.set_font("helvetica", "B", 15)
    # Add name and msg
    pdf.cell(0, 10, f"{name} took CS50")
    # Generate output
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
