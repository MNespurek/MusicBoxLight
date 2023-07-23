from form import Form

#vytváření formuláře
form = Form(action='pridej', div_pred = "ano")
form.vytvor_inputy(2)
form.vytvor_selecty(2)
form.vytvor_divy(2)
form.vytvor_img(2)
form.vytvor_anchor(2)
form.pridej_anchor(2)
form.pridej_uzavri_anchor()
form.pridej_anchor(1)
form.pridej_uzavri_anchor()
form.pridej_img(2)
form.pridej_img(1)
form.pridej_div(2)
form.pridej_uzavri_div()
form.pridej_div(1)
form.pridej_uzavri_div()
form.pridej_select(2)
form.pridej_select(1)
form.pridej_input(2)
form.pridej_input(1)
form.pridej_uzavri_form()
print(form)

#vytisknutí zvoleného formuláře
for element in form.seznam_formular:
    print(element)

