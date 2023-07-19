from markupsafe import Markup
class Form:
    def __init__(self, action, method = "POST"):
        self.action = action
        self.method = method

    def vypis_form(self):
        vypis_form = f'<form action="{self.action}" method="{self.method}">'
        return Markup(vypis_form)
    
    def uzavri_form(self):
        uzavri_form = f'</form>'
        return Markup(uzavri_form)
    
