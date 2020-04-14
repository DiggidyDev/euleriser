from PIL import Image, ImageDraw


class Interface:

    def __init__(self, node_count):

        self.dimensions = (64*(node_count+1), 36*(node_count+1))
        self.graph = None
        self.image = Image.new(mode="1", size=self.dimensions, color=1)
        self.draw = ImageDraw.Draw(self.image)

    def draw_node(self, node: "Node object", centre, radius):

        node.set_position(centre[0], centre[1])
        node.set_radius(radius)
        identifier = node.identifier

        self.draw.ellipse(node.border_positions, 255, outline=0)

        text_pos = ((node.centre[0]) - (node.radius/16), (node.centre[1]) - (node.radius/4))
        self.draw.text(text_pos, f"{identifier}", align="left")

        return self.image

    def draw_path(self, pos1: "Node object", pos2: "Node object", action=None):

        line_pos = (pos1[0], pos1[1], pos2[0], pos2[1])

        if action == "remove":
            self.draw.line(line_pos, fill=255, width=3, joint="curve")
        elif action == "add":
            self.draw.line(line_pos, fill=0, width=3, joint="curve")
        else:
            raise NameError("Action does not exist. Please use actions: \"add\" or \"remove\".")

        return self.image
