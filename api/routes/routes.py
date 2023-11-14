from api.server.instance import server
from flask import render_template,request,make_response,url_for
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
    user_prompt = user_prompt.strip()
    
    if(len(user_prompt) == 0):
        return make_response("O prompt não pode estar vazio",400)
    cards_list = get_response(user_prompt)
    for card in cards_list:
        i+=1
        print(type(card))
    board_url = create_board(user_prompt,cards_list)
        
    return make_response(board_url,200)

