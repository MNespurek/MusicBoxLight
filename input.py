from markupsafe import Markup

#třída Input
class Input:

#paramentry při inicializaci objektu    
    def __init__(self, type, name, id, class_, placeholder):
        self.type = type
        self.name = name
        self.id = id
        self.class_ = class_
        self.placeholder = placeholder

#popis objektu třídy        
    def __str__(self):
        vypis_input = f'<input type="{self.type}" name="{self.name}" id="{self.id}" class="{self.class_}" placeholder="{self.placeholder}">'
        return Markup(vypis_input)