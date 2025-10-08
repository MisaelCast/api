from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Esta ruta ahora aceptará una URL como /pagina/Misael
@app.route('/pagina/<name>')
# Y también funcionará si solo pones /pagina/
@app.route('/pagina/', defaults={'name': 'Invitado'})
def hello(name):
    # La variable 'person' que envías a HTML contendrá el 'name' de la URL
    return render_template('pagina.html', person=name)