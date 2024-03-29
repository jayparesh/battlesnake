import logging,os,typing
from flask import Flask,request
from app import *
app=Flask('Battlesnake')
@app.get('/')
def on_info():return info()
@app.post('/start')
def on_start():game_state=request.get_json();start(game_state);return'ok'        
@app.post('/move')
def on_move():game_state=request.get_json();return move(game_state)
@app.post('/end')
def on_end():game_state=request.get_json();end(game_state);return'ok'
@app.after_request
def identify_server(response):response.headers.set('server','battlesnake/replit/starter-snake-python');return response
host='0.0.0.0'
port=int(os.environ.get('PORT','8000'))
logging.getLogger('werkzeug').setLevel(logging.ERROR)
print(f"\nRunning Battlesnake at http://{host}:{port}")
app.run(host=host,port=port)