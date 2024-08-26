from flask import Flask, request, send_file, render_template_string
import pdfkit
import os

app = Flask(__name__)

# Configure pdfkit to use the installed wkhtmltopdf executable
# PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Adjust path as necessary

@app.route('/')
def index():
    return 'PDF Generator'

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    html_content = data.get('htmlContent')
    fileName = data.get('tempName');

    # You can customize the HTML content or use a template
    # html_content = render_template_string(html_content)

    pdf = pdfkit.from_string(html_content, False)

    # Save PDF to a file
    with open(fileName, 'wb') as f:
        f.write(pdf)

    # Send the file to the client
    return send_file(fileName, as_attachment=True, download_name='downloaded.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
