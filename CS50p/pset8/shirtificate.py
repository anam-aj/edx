# Program to create "shirtificate"

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png")
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)

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

    pdf.cell(0, 10, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
