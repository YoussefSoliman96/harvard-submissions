from fpdf import FPDF

def main():

    class PDF(FPDF):
        def __init__(self, name):
            pdf = PDF()
            pdf.add_page()
            pdf.set_font("Times", "B", 40)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(20, 40, f"{name}", new_x="LMARGIN", new_y="NEXT")
            pdf.output("new_shirtificate.pdf")
            # Rendering logo:
            self.image("shirtificate.png", 10, 50, w=pdf.epw)
            # Setting font: helvetica bold 15
            self.set_font("helvetica", "B", 40)
            # Printing title:
            self.cell(0, 10, "CS50 Shirtificate", align="C")
            # Performing a line break:
            self.ln(20)

    name = input("Name: ")


if __name__ == "__main__":
    main()