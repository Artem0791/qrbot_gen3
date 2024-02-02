from pydantic import BaseModel


class QRCode(BaseModel):
    version: int = 1  # QR Code version: 1-40
    box_size: int = 20  # Size of each box in pixels
    border: int = 4  # Border thickness in boxes