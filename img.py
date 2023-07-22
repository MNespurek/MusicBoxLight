from markupsafe import Markup

#třída Img
class Img:

#paramentry při inicializaci objektu    
    def __init__(self, src, alt, class_, width, height):
        self.src = src
        self.class_=class_
        self.alt = alt
        self.width = width
        self.height = height

#popis objektu třídy
    def __str__(self):
        vypis_img = f'<img src="{self.src}" alt="{self.alt}" class="{self.class_}" width="{self.width}" height="{self.height}" />'
        return Markup(vypis_img)



