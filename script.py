import pdfkit

def convert_html_to_pdf(html_path, pdf_path):
    # Convert HTML file to PDF
    try:
        pdfkit.from_file(html_path, pdf_path)
        print(f"PDF generated successfully: {pdf_path}")
    except Exception as e:
        print(f"Failed to generate PDF: {e}")

if __name__ == "__main__":
    html_path = 'template.html'  # Path to your HTML file
    pdf_path = 'output.pdf'   # Path where you want to save the PDF
    
    convert_html_to_pdf(html_path, pdf_path)