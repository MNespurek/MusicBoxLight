from markupsafe import Markup

class Div:
    
    def __init__(self, class_):
        
        self.class_ = class_

    def vypis_div(self):
        vypis_div = f'<div class="{self.class_}">'
        return Markup(vypis_div)
    
    def uzavri_div(self):
        uzavri_div = f'</div>'
        return Markup(uzavri_div)
