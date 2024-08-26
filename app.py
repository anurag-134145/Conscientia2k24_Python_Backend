from flask import Flask, request, send_file, render_template_string
import pdfkit
import os
import flask_cors
import threading
import time

app = Flask(__name__)
flask_cors.CORS(app)

# Configure pdfkit to use the installed wkhtmltopdf executable
# PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Adjust path as necessary
def delete_file_after_delay(file_path, delay):
    # Wait for the specified delay (in seconds)
    time.sleep(delay)
    # Check if the file exists and delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")

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
    threading.Thread(target=delete_file_after_delay, args=(fileName, 300)).start()
    return send_file(fileName, as_attachment=True, download_name='downloaded.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))