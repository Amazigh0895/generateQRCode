import qrcode
import qrcode.constants


def generate_qr_code(data, filename):
    """
    Fonction qui génére le QRCode
    Arguments:
     data(ca peut etre une chaine de caractére ou autre chose) :ca represente le contenue du QRCode
     filename(str) : le nom du fichier
    """
    if not filename.lower().endswith(".png"):
        filename += ".png"

    # on crée une instance de l'objet QRCode et on parametre les valeurs
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f" QR code généré et sauvegardé sous le nom {filename}")


data = "https://www.seia-electronique.fr/"
generate_qr_code(data, "scannermoi.png")
