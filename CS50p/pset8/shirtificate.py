# Program to create "shirtificate"

from fpdf import FPDF


def main():
    name = input("Enter your name: ")

    create_shirtificate(name)


def create_shirtificate(user_text):

    # Create object
    pdf = FPDF()
    pdf.add_page()
    # Render image:
    pdf.image("shirtificate.png", x=10, y=60, w=190)
    # Header text
    pdf.set_font("Arial", "B", 50)
    pdf.cell(0, 30, "CS50 Shirtificate", 0, 1, "C")
    # Shirt text
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 30)
    pdf.cell(0, 150, f"{user_text} took CS50", 0, 1, "C")
    # Output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
