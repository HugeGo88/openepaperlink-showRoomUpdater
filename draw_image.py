from PIL import Image, ImageDraw, ImageFont


def draw_image(price, article_name):

    # Create a new paletted image with indexed colors
    image = Image.new('P', (296, 152))

    # Define the color palette (white, black, red)
    palette = [
        255, 255, 255,  # white
        0, 0, 0,        # black
        255, 0, 0       # red
    ]

    # Assign the color palette to the image
    image.putpalette(palette)

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define the text lines
    line1 = price
    line2 = article_name

    # Define the fonts and sizes
    # Change the font file and size as per your preference
    font_line1 = ImageFont.truetype('Arial.ttf', size=40)
    # Change the font file and size as per your preference
    font_line2 = ImageFont.truetype('Arial.ttf', size=24)

    # Calculate the text bounding boxes to get the text widths and heights
    text_bbox_line1 = draw.textbbox((0, 0), line1, font=font_line1)
    text_bbox_line2 = draw.textbbox((0, 0), line2, font=font_line2)

    # Calculate the text positions to center the lines horizontally
    text_position_line1 = (
        (image.width - (text_bbox_line1[2] - text_bbox_line1[0])) // 2, 20)
    text_position_line2 = (
        (image.width - (text_bbox_line2[2] - text_bbox_line2[0])) // 2, 100)

    # Draw the black rectangle at the top
    draw.rectangle([0, 0, 296, 80], fill=2)

    # Draw the large red rectangle
    draw.rectangle([0, 80, 296, 152], fill=1)

    # Write the text on the image
    # Use palette index 0 for white color
    draw.text(text_position_line1, line1, fill=0, font=font_line1)
    # Use palette index 0 for white color
    draw.text(text_position_line2, line2, fill=0, font=font_line2)

    # Convert the image to 24-bit RGB
    rgb_image = image.convert('RGB')

    # Save the image as JPEG with maximum quality
    image_path = 'output.jpg'
    rgb_image.save(image_path, 'JPEG', quality="maximum")
    return image_path


if __name__ == "__main__":
    draw_image('9.99 €', 'Sample Article')
