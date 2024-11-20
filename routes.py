from main import app


#rotas 
@app.route("/")
def homepage():
    return "Meu Site no Flask"

#rotas 
@app.route("/blog")
def homepage():
    return "Bem vindo ao blog"

