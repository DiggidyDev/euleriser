from PIL import Image, ImageDraw


class Interface:

    def __init__(self, node_count):

        self.dimensions = (64*(node_count+1), 36*(node_count+1))
        self.graph = None
        self.image = Image.new(mode="1", size=self.dimensions, color=1)
        self.draw = ImageDraw.Draw(self.image)

    def draw_node(self, node: "Node object", centre, radius):

        node.set_position(centre[0], centre[1], radius)
        identifier = node.identifier

        ellipse_pos = ((identifier - 1) * 30, (identifier - 1) * 30, identifier * 30, identifier * 30)
        self.draw.ellipse(node.border_positions, 255, outline=0)

        text_pos = ((identifier - 1) * 30 + 13, (identifier * 30) - 20)
        self.draw.text(node.centre, f"{identifier}", align="left")

        return self.image

    def draw_path(self, pos1: "Node object", pos2: "Node object"):

        line_pos = (pos1[0], pos1[1], pos2[0], pos2[1])
        print(line_pos)

        self.draw.line(line_pos, fill=0, width=3, joint="curve")

        return self.image
