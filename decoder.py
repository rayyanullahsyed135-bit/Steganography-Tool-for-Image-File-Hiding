from PIL import Image

def binary_to_message(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)
    return message

def decode_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_data = ""

    for pixel in pixels:
        for color in pixel[:3]:
            binary_data += str(color & 1)

    delimiter = "1111111111111110"
    end_index = binary_data.find(delimiter)

    if end_index != -1:
        binary_data = binary_data[:end_index]

    return binary_to_message(binary_data)
