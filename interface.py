from PIL import Image, ImageDraw


im = Image.new(mode="1", size=(256, 256), color=1)


def add_node(count: int):
    draw = ImageDraw.Draw(im)
    xy = ((count - 1) * 30, (count - 1) * 30, count * 30, count * 30)
    draw.ellipse(xy, None, outline=0)
    return im
