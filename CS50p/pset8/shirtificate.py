# Program to create "shirtificate"

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

def main():
    name  = input("Enter your name: ")

    create_shirtificate(name)


def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.cell(0, 10, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
