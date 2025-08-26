import requests


def send_image(draw_image):
    mac = "00000272647F3E11"   # destination mac address
    dither = 0   # set dither to 1 is you're sending photos etc
    apip = "192.168.178.115"   # ip address of your access point

    mac, dither, apip, image_path = draw_image()

    # Prepare the HTTP POST request
    url = "http://" + apip + "/imgupload"
    payload = {"dither": dither, "mac": mac}  # Additional POST parameter
    files = {"file": open(image_path, "rb")}  # File to be uploaded

    # Send the HTTP POST request
    response = requests.post(url, data=payload, files=files)

    # Check the response status
    if response.status_code == 200:
        print("Image uploaded successfully!")
    else:
        print("Failed to upload the image.")
