from api.server.instance import server
from flask import render_template,request,make_response
from galaxyAI_api.galaxyAI import get_response
from trello_api.boards import create_board

@server.app.route('/')
@server.app.route('/index')
def index():
    return render_template('index.html')

@server.app.route('/generate',methods = ['POST'])
def generate():
    i=0
    user_prompt = request.form.get('prompt')
    
    # create_board(user_prompt,None)
    
    cards_list = get_response(user_prompt)
    for card in cards_list:
        i+=1
        print(type(card))
        
    return make_response("sucesso",200)

