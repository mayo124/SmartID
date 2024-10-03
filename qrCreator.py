import random
import qrcode

def generate_qr_code(data, file_name):
    """Generates a QR code and saves it as a PNG file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def generate_html(name, dob, qr_code_image):
    """Generates an HTML file with the given data."""
    html_content = f'''
   
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ID Card</title>
        <style>
            body{{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .id-card {{
                width: 300px;
                height: 150px;
                background-color: #fef3e3;
                border-radius: 15px;
                display: flex;
                justify-content: space-between;
                align-items: bottom;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                position: relative;
            }}
            .qr-code {{
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .qr-code img {{
                width: 150px;
                height: 150px;
            }}
            .info {{
                flex: 2;
                text-align: right;
                text-align: bottom;
                margin-right: 20px;
            }}
            .info h2 {{
                margin: 0;
                font-size: 24px;
                font-weight: bold;
                text-transform: lowercase;
            }}
            .info p {{
                margin: 5px 0;
                font-size: 18px;
            }}
            .school-logo {{
                position: absolute;
                top: 120px;
                right: 10px;
                width: 150px;
            }}
        </style>
    </head>
    <body>

    <div class="id-card">
        <div class="qr-code">
            <img src="qrcode.png" alt="QR Code">
        </div>
        <div class="info">
            <img class="school-logo" src="logo.png" alt="School Logo">
            <h2>mihir</h2>
            <p>14/01/2009</p>
        </div>
    </div>

    </body>
    </html>
    
    '''
    # Save the HTML content to a file
    with open("id_card.html", "w") as file:
        file.write(html_content)
    print("HTML file has been generated.")

if __name__ == "__main__":
    
    # Data for QR Code and user info
    name =input("Name:")
    dob = input("Date of birth:")
    qr_code_file = "qrcode.png"
    
    generate_qr_code(f"Name: {name}", qr_code_file)
    # Generate the QR code
    

    # Generate the HTML file
    generate_html(name, dob, qr_code_file)
