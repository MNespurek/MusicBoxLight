from select_ import Select
from input import Input
from markupsafe import Markup
class Form:

    seznam_formular = []
    seznam_inputu = []

    def __init__(self, action, div_pred, method = "POST"):
        if div_pred == 1:
            self.div_pred = div_pred
        else:
            self.div_pred = None            
        self.action = action
        self.method = method

    def __str__(self):
        if self.div_pred:
            class_ = input("Zadejte třídu divu:\n")
            vypis_div = f'<div class="{class_}">\n'
            vypis_form = f'<form action="{self.action}" method="{self.method}">\n'
            vypis = vypis_div + vypis_form
            print(form)
            self.seznam_formular.append(vypis)
        else:
            vypis_form = f'<form action="{self.action}" method="{self.method}">\n'
        return Markup(vypis_form)

    def vytvor_inputy(self, pocet_inputu):
        hodnota = 0
        while hodnota < pocet_inputu:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} inputu:\n")
            type_input = input("zadejte type:\n")
            
            name_input = input("zadejte name:\n")
            id_input = input("zadejte id:\n")
            class_input = input("zadejte classu:\n")
            placeholder_input = input("zadejte placehoder:\n")
            input_objekt = Input(type=type_input, name=name_input, id=id_input, class_=class_input, placeholder=placeholder_input)
            print(input_objekt)
            self.seznam_inputu.append(input_objekt)

    def pridej_input(self, cislo):
        for index in self.seznam_inputu:
            index = cislo - 1
            return self.seznam_inputu[index]        

    def vytvor_selecty(self, name_select, class_select, pocet_moznosti_select):
        select_michal = Select(name=name_select, class_=class_select)
        return select_michal.vypis_select(pocet_moznosti_select)
    
    def pridej_selecty(self):
        pass

    def vytvor_divy(self):
        pass

    def vytvor_img(self):
        pass

    def vytvor_anchor(self):
        pass

    def pridej_anchor(self):
        pass

    def uzavri_form(self):
        uzavri_form = f'</form>'
        return Markup(uzavri_form)

    def vypis_formular(self):    
        for item in self.seznam_formular:
            print(item)


form = Form('pridej', 1)

form.vypis_formular()