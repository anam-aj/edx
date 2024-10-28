# Program to create "shirtificate"

from fpdf import FPDF


def main():
    name  = input("Enter your name: ")

    create_shirtificate(name)


def create_shirtificate(user_text):

    # Create object
    pdf = FPDF()
    pdf.add_page()
    # Rendering image:
    pdf.image("shirtificate.png")
    # Output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
