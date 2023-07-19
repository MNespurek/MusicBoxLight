from markupsafe import Markup
from flask import url_for
class Anchor:
    def __init__(self, text, url, class_ = "nav-link"):
        self.text = text
        self.url = url
        self.class_ = class_
        
   
    def vypis_anchor(self):
        vypis_anchor = f'<a class="{self.class_}" href="{self.url}">{self.text}'
        return Markup(vypis_anchor)
    
    def uzavri_anchor(self):
        uzavri_anchor = f'</a>'
        return Markup(uzavri_anchor)


