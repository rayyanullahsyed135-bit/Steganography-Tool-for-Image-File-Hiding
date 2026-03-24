from PIL import Image

def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    binary_message = message_to_binary(message) + '1111111111111110'  # delimiter

    pixels = list(image.getdata())
    new_pixels = []

    data_index = 0

    for pixel in pixels:
        r, g, b = pixel

        if data_index < len(binary_message):
            r = (r & ~1) | int(binary_message[data_index])
            data_index += 1

        if data_index < len(binary_message):
            g = (g & ~1) | int(binary_message[data_index])
            data_index += 1

        if data_index < len(binary_message):
            b = (b & ~1) | int(binary_message[data_index])
            data_index += 1

        new_pixels.append((r, g, b))

    image.putdata(new_pixels)
    image.save(output_path)
