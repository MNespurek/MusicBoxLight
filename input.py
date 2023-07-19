from markupsafe import Markup
class Input:
    def __init__(self, type, name, id, class_, placeholder):
        self.type = type
        self.name = name
        self.id = id
        self.class_ = class_
        self.placeholder = placeholder
        

    def vypis_input(self):
        vypis_input = f'<input type="{self.type}" name="{self.name}" id="{self.id}" class="{self.class_}" placeholder="{self.placeholder}">'
        return Markup(vypis_input)