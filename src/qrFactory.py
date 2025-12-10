import segno # type: ignore
from segno import helpers
from PIL import Image # type: ignore

# --- 1. Data to Encode ---
# Data for the Wi-Fi connection
NETWORK_SSID = 'MyHomeNetwork'
NETWORK_PASSWORD = 'MySecurePassword'
SECURITY_TYPE = 'WPA' # Use 'WPA' or 'WEP' or 'nopass'

# --- 2. Generate the Wi-Fi QR Code ---
# NOTE: This uses the 'helpers' object imported on line 2, 
# correcting the previous 'segno.helpers.make_wifi' error.
wifi_qr = helpers.make_wifi(
    ssid=NETWORK_SSID,
    password=NETWORK_PASSWORD,
    security=SECURITY_TYPE
)

# --- 3. Save the QR Code Image ---

# Save the QR code to a PNG file with some styling
wifi_qr.save(
    'wifi_login.png',
    scale=10, 
    dark='darkblue', 
    light='white', 
    border=2
)

print("Successfully generated 'wifi_login.png'")