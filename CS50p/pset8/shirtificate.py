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
    pdf.image("shirtificate.png")
    # Header text
    pdf.text(0, 0,"hello")
    # Output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
