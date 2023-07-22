from markupsafe import Markup

#třída Anchor
class Anchor:

#paramentry při inicializaci objektu    
    def __init__(self, text, url, class_ = "nav-link"):
        self.text = text
        self.url = url
        self.class_ = class_

#popis objektu třídy
    def __str__(self):
        vypis_anchor = f'<a class="{self.class_}" href="{self.url}">{self.text}'
        return Markup(vypis_anchor)

#metoda pro přidání uzavíracího elementu anchor do formuláře    
    def uzavri_anchor(self):
        uzavri_anchor = f'</a>'
        return Markup(uzavri_anchor)


