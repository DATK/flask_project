from src import site_1 as s
from src import sh
from flask import Flask, request, redirect

c = s.Reg_or_chek_reg("data.txt")
# c.clear_data()
voshel = False
result = 'None'
html = s.read_html("html1.html")
html2 = s.read_html("html2.html")
html3 = s.read_html("html3.html")
html4=s.read_html("html4.html")
app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def mainS():
   return html4




@app.route('/reg', methods=["GET", "POST"])
def reg_or_input():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if c.chek_reg(username) == False:
            c.reg(username, password)
            return redirect("/")
        else:
            return redirect("vhod")
    else:
        return html


@app.route('/vhod', methods=["GET", "POST"])
def vhod():
    if request.method == "POST":
        user = request.form["username"]
        pasd = request.form["password"]
        if c.vhode(user, pasd) == True:
            global voshel
            voshel = True
            return redirect("/vhod/move")
        else:
            return redirect("/vhod")
    else:
        return html2


@app.route('/vhod/move', methods=["GET", "POST"])
def shi():
    global voshel
    global result
    if request.method == "POST":
        move = request.form["move"]
        text = request.form["text"]
        key = request.form["key"]
        key = int(key)
        if voshel == True:
            if move == "cezar":
                result = sh.cezar(text, sh.alf, key)

                print(result)
                return redirect("/vhod/move/res")
            elif move == "uncez":
                result = sh.cezar_unsc(text, sh.alf, key)
                return redirect("/vhod/move/res")
            elif move == "polib":
                result = sh.polibia(text, sh.table)
                return redirect("/vhod/move/res")
        else:
            return redirect("/vhod")
    else:
        return html3


@app.route('/vhod/move/res')
def ress():
    global result
    return result


app.run(host="0.0.0.0", debug=True)
