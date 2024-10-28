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
    pdf.image("shirtificate.png", x=0, y=0, w=pdf.w, h=pdf.h        )
    # Setting font: helvetica bold 15
    pdf.set_font("helvetica", "B", 15)
    # Add name and msg
    pdf.cell(0, -250, f"{user_text} took CS50", border=1, align="C")
    # Generate output
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
