from markupsafe import Markup
class Select:
    def __init__(self, name, class_ ):
        self.name = name
        self.class_ = class_
        
        
    def vypis_select(self):
        moznosti = []
        pokracovat = True
        while pokracovat:
            print("Kolik chcete možností?")
            try: 
                vstup = int(input())
                hodnota = 0
                while hodnota < vstup:
                    hodnota +=1
                    moznost = f'<option value="moznost{hodnota}">Možnost {hodnota}</option>\n'
                    moznosti.append(moznost)
                moznosti_text = ""
                for moznost in moznosti:
                    moznosti_text += f"\t{moznost}"
                
                vypis_select = f'<select name="{self.name}" class="{self.class_}">\n{moznosti_text}</select>'
                return Markup(vypis_select)                
        
            except ValueError: 
                print("Nezadali jste číslo")

        