from flask import Flask, render_template, redirect
from input import Input
from select_ import Select
from div import Div
from img import Img
from anchor import Anchor
from form import Form
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def index():
    form = Form("/pridej_zanr")
    anchor = Anchor(url="http://www.seznam.cz", text="Žánr")
    img = Img(src="/static/obrazky/music.webp", alt="Music", height="150px", width="150px", class_="center")
    div = Div(class_="center")
    select = Select("index_select", class_="nav-link")
    input = Input("text", "index_input", id="input", class_="nav-link", placeholder="Vlož text")
    print(form.vypis_form())
    print(select.vypis_select())
    print(input.vypis_input())
    print(img.vypis_img())
    print(div.vypis_div())
    print(div.uzavri_div())
    print(form.uzavri_form())
    return render_template('index.html', form = form, anchor = anchor, img = img, div = div, select = select, input = input)

if __name__ == '__main__':
    app.run(debug=True)

