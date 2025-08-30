import requests
import logging
logger = logging.getLogger(__name__)


def send_image(image_path, mac):
    dither = 0   # set dither to 1 is you're sending photos etc
    apip = "192.168.178.202"   # ip address of your access point

    # Prepare the HTTP POST request
    url = "http://" + apip + "/imgupload"
    payload = {"dither": dither, "mac": mac}  # Additional POST parameter
    files = {"file": open(image_path, "rb")}  # File to be uploaded

    # Send the HTTP POST request
    response = requests.post(url, data=payload, files=files)

    # Check the response status
    if response.status_code == 200:
        logger.info("Image uploaded successfully!")
    else:
        logger.error("Failed to upload the image.")


if __name__ == "__main__":
    send_image("output.jpg", "00000272647F3E11")
