'''
-------------------------------------
Author: Madhava Kulkarni
Email : madhav.kulkarni1986@gmail.com
-------------------------------------
'''
from flask import Flask, request, json
import sys
from ntfy import notify

app = Flask(__name__)
port = '5010'

@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.get_data())
    commitid = data['commits'][0]['id']
    commitmsg = data['commits'][0]['message']
    committername = data['commits'][0]['committer']['name']
    modifiedfile = ', '.join(data['commits'][0]['modified'])
    repo = data['repository']['name']

    messagetowin = 'Repo: \"{}\"\nComitter: \"{}\"\nFile(s): \"{}\"\nCommit Message: \"{}\"'.format(repo,committername,modifiedfile,commitmsg)
    ret = notifyUser(messagetowin)
    return "ACK"
 
@app.route('/errors', methods=['POST'])
def errors():
    print(json.loads(request.get_data()))
    return 200

def notifyUser(msg):
    notify(msg,"GitHub Update")

if(__name__ == '__main__'):
    app.run(port=port, debug=True)