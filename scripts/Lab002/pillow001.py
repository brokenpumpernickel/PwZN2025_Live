from PIL import Image, ImageDraw
    
image = Image.new('RGB', (1000, 1000), 'pink')
draw = ImageDraw.Draw(image)

draw.text((100, 100), 'Hello, World!', fill='white', stroke_width=2, stroke_fill='black')
draw.rectangle([200, 200, 400, 400], outline='blue', width=5)

image.save('scripts/Lab002/pink_image.png')