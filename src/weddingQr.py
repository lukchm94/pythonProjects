import segno # type: ignore
from segno import helpers
from PIL import Image # type: ignore

# --- 1. Data to Encode ---
# Replace this URL with the website you want to encode
WEBSITE_URL = 'https://agata-i-lukasz.pl/' 
RSVP_URL = f'{WEBSITE_URL}rsvp/'
# --- 2. Generate the QR Code ---
# Using the basic make() function
# error='h' sets the error correction level to High (H) for better readability
qrcode = segno.make(WEBSITE_URL, error='h')
rsvpCode = segno.make(RSVP_URL, error='h')
# --- 3. Save the QR Code Image ---
title = 'website_qr_code.png'
# Save the QR code to a PNG file with transparent background
# Using RGBA values where the last two digits control transparency (00 = fully transparent)
qrcode.save(
    title,
    scale=128,        # Scale determines the size of the image (8x the base size)
    dark='#e4c9d7', # Sets the color of the dark modules (e.g., a light pink)
    light=None,       # Transparent background (None for segno library)
    border=4        # Sets the border size
)

rsvpCode.save(
    'rsvp.png',
    scale=128,        # Scale determines the size of the image (8x the base size)
    dark='#374151', # Sets the color of the dark modules (dark gray)
    light=None,       # Transparent background (None for segno library)
    border=4        # Sets the border size
)

print(f"Successfully generated '{title}' for URL: {WEBSITE_URL}")