from markupsafe import Markup

#třída Div
class Div:

#paramentry při inicializaci objektu    
    def __init__(self, class_):
        self.class_ = class_

#popis objektu třídy
    def __str__(self):
        vypis_div = f'<div class="{self.class_}">'
        return Markup(vypis_div)

#metoda pro přidání uzavíracího elementu div do formuláře    
    def uzavri_div(self):
        uzavri_div = f'</div>'
        return Markup(uzavri_div)
