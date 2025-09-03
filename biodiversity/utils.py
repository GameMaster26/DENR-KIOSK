import qrcode
from django.conf import settings
import os

def generate_qr_for_url(url, filename="qr_upload.png"):
    """
    Generate QR code image para sa URL at i-save sa MEDIA folder.
    """
    qr_img = qrcode.make(url)
    media_dir = os.path.join(settings.MEDIA_ROOT, "qr_codes")
    os.makedirs(media_dir, exist_ok=True)  # siguraduhing may folder
    file_path = os.path.join(media_dir, filename)
    qr_img.save(file_path)
    # Return URL para ma-access sa template
    return os.path.join(settings.MEDIA_URL, "qr_codes", filename)
