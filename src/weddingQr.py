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

# Save the QR code to a PNG file with some styling
qrcode.save(
    'approx.png',
    scale=128,        # Scale determines the size of the image (8x the base size)
    dark='#E295BD', # Sets the color of the dark modules (e.g., a dark blue)
    light='#4B638A',  # Sets the color of the light modules (background)
    border=4        # Sets the border size
)

rsvpCode.save(
    'rsvp.png',
    scale=128,        # Scale determines the size of the image (8x the base size)
    dark='#374151', # Sets the color of the dark modules (e.g., a dark blue)
    light='white',  # Sets the color of the light modules (background)
    border=4        # Sets the border size
)

print(f"Successfully generated 'website_qr_code.png' for URL: {WEBSITE_URL}")