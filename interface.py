from PIL import Image, ImageDraw


class Interface:

    def __init__(self, node_count: int):

        self.image = Image.new(mode="1", size=(64*(node_count+1), 36*(node_count+1)), color=1)

    def draw_node(self, label: int):
        draw = ImageDraw.Draw(self.image)

        ellipse_xy = ((label - 1) * 30, (label - 1) * 30, label * 30, label * 30)
        draw.ellipse(ellipse_xy, None, outline=0)

        text_xy = ((label - 1) * 30 + 13, (label * 30) - 20)
        draw.text(text_xy, f"{label}", align="left")

        return self.image
