from api.server.instance import server
from flask import render_template,request,make_response
from galaxyAI_api.galaxyAI import get_response

@server.app.route('/')
@server.app.route('/index')
def index():
    return render_template('index.html')

@server.app.route('/generate',methods = ['POST'])
def generate():
    user_prompt = request.form.get('prompt')
    get_response(user_prompt)
    return make_response("sucesso",200)

