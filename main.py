from src import site_1 as s, sh
from flask import Flask, request, redirect

c = s.Reg_or_chek_reg("data.txt")
#c.clear_data()
voshel = False
result = 'None'
html4 = """<form>
</form>"""
html3 = """<form action = "http://localhost:5000/vhod/move" method = "post">
<p>Input move,text,key</p>
<p><input type = "text" name = "move" /></p>
<p><input type = "text" name = "text" /></p>
<p><input type = "text" name = "key" /></p>
<p><input type = "submit" value = "отправить" /></p>
</form>"""

html = """
<form action = "http://localhost:5000/reg" method = "post">
<p>Enter Login and Password</p>
<p><input type = "text" name = "username" /></p>
<p><input type = "password" name = "password" /></p>
<p><input type = "submit" value = "отправить" /></p>
</form>
"""
html2 = """
<form action = "http://localhost:5000/vhod" method = "post">
<p>Enter Login and Password</p>
<p><input type = "text" name = "username" /></p>
<p><input type = "password" name = "password" /></p>
<p><input type = "submit" value = "отправить" /></p>
</form>
"""
app = Flask(__name__)


@app.route('/')
def mainS():
    return "hello world"


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
