from flask import Flask, request, send_file, render_template_string
import pdfkit
import os

app = Flask(__name__)

# Configure pdfkit to use the installed wkhtmltopdf executable
# PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Adjust path as necessary

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    html_content = '<h1>PDF Generated</h1>'

    # You can customize the HTML content or use a template
    # html_content = render_template_string(html_content)

    pdf = pdfkit.from_string(html_content, False)

    # Save PDF to a file
    pdf_filename = 'generated.pdf'
    with open(pdf_filename, 'wb') as f:
        f.write(pdf)

    # Send the file to the client
    return send_file(pdf_filename, as_attachment=True, download_name='downloaded.pdf')

if __name__ == '__main__':
    app.run(debug=True)
