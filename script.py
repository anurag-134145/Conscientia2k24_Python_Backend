from flask import Flask, send_file
import pdfkit

app = Flask(__name__)

# Configure pdfkit to use the installed wkhtmltopdf executable
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')  # Adjust path as necessary

@app.route('/generate-pdf-from-html', methods=['GET'])
def generate_pdf_from_html():
    html_file_path = './template.html'  # Path to your HTML file
    pdf_filename = 'output.pdf'

    # Generate PDF from the HTML file
    pdfkit.from_file(html_file_path, pdf_filename, configuration=PDFKIT_CONFIG)

    # Send the generated PDF file as a response
    return send_file(pdf_filename, as_attachment=True, download_name='downloaded.pdf')

if __name__ == '__main__':
    app.run()
