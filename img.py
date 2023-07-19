from markupsafe import Markup
class Img:
    def __init__(self, src, alt, class_, width, height):
        self.src = src
        self.class_=class_
        self.alt = alt
        self.width = width
        self.height = height

    def vypis_img(self):
        vypis_img = f'<img src="{self.src}" alt="{self.alt}" class="{self.class_}" width="{self.width}" height="{self.height}" />'
        return Markup(vypis_img)



