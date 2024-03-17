import pathlib

import qrcode


def generate_qr(user_message, user_id, user_name):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)

    qr.add_data(user_message)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    unique_qr_name = str(user_id)+'_'+str(user_name)
    path = pathlib.Path(f'qr_bank/{unique_qr_name}')
    img.save(path)
    return path
