from flask import Flask,request, session
from flask_cors import CORS
from bayes  import BayesClf, PredictBC
import numpy as np
import json
from anytree import Node, RenderTree,AsciiStyle,PreOrderIter
from anytree.dotexport import RenderTreeGraph
from qTree import display, getQ, returnQ,valuate
from anytree import Node, RenderTree,AsciiStyle,PreOrderIter
from anytree.dotexport import RenderTreeGraph
from operator import itemgetter

root = Node('root', value = 'null', label='') 
a = Node('Do you use laptop ?', parent=root, value='null',label='')
a1 = Node('For work / study ?', parent=a, value='null',label='')
a2 = Node('For entertainment (Netflix,Disney+ etc.) ?', parent=a, value='null',label='')
a11 = Node('> 3 hours per day ?', parent=a1, value='null',children=[
    Node('on sofa / on bed ?',  value='null',label='Have a life'),
    Node('on lap ?',  value='null',label='Have a life'),
    Node('do you have to look down on screen ?', value='null',label='Have a life')], label='')
a12 = Node('Do you have to look while you type ?', parent=a1 , value='null',label='Have a life'),
a21 = Node('> 3 hours per day ?', parent=a2, value='null', children=[
    Node('on sofa / on bed ?',  value='null',label='Have a life'),
    Node('on lap ?',  value='null',label='Have a life'),
    Node('do you have to look down on screen ?', value='null',label='Have a life')], label='')
b = Node('Do you use iPad/tablet ?', parent=root, value='null',label='')
b1 = Node('For work ?', parent=b, value='null',label='')
b11 = Node('> 3 hours per day ?', parent=b1, value='null',children=[
    Node('on sofa / on bed ?',  value='null',label='Have a life')], label='')
b12 = Node('Do you use without standing cases ?', parent=b1, value='null',label='')
b2 = Node('For entertainment (Netflix,Disney+ etc.) ?', parent=b, value='null',label='')
b21 = Node('> 3 hours per day ?', parent=b2, value='null',children=[
    Node('on sofa / on bed ?',  value='null',label='Have a life')], label='')
b22 = Node('Do you use without standing cases ?', parent=b2, value='null',label='')
c = Node('Do you do manual work (drawing, drafting, sketching) ?', parent=root, value='null',label='')
c1 = Node('Do you do the work on a table', parent=c, value='null',label='')
c11 = Node('Is it a slope table ?', parent=c1, value='null',label='')
d = Node('Do you use a chair without arm rest ?', parent=root, value='null',label='')
d1 = Node('Do you use a chair without lumbar back support ?', parent=d, value='null',label='')

app = Flask(__name__)
CORS(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
screen_route = str (hash("screening"))

@app.route("/username", methods=['POST'])
def login():
    username = request.get_json()
    # username = request.form.get("username", "") or request.form["username"]
    session["username"]=username
    return {'user': username} # from flask import jsonify 

@app.route("/api")
def api():
    k = session.get("username") 
    #m = 'eu' + k['username']
    return {'username': PredictBC(int(k['username']),int(k['symptoms']))[-1]}

@app.route("/subentry" , methods=['POST'])
def sub():
    entry = request.get_json()
    session["entry"]=entry
    return entry 

@app.route("/request")
def getreq():
    key = [1,[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],0] #sample_data
    return {'r_key': key }

@app.route("/subrequest", methods=['POST'])
def getarr():
    arr = request.get_json
    return arr

@app.route("/display")
def tree():
    return {'text': getQ()}

def merge(list1, list2):
      
    merged_list = []
    for i in range(max((len(list1), len(list2)))):
  
        while True:
            try:
                tup = (list1[i], list2[i])
            except IndexError:
                if len(list1) > len(list2):
                    list2.append('')
                    tup = (list1[i], list2[i])
                elif len(list1) < len(list2):
                    list1.append('')
                    tup = (list1[i], list2[i])
                continue
  
            merged_list.append(tup)
            break
    return merged_list

@app.route("/intervention")
def intervent():
    num=valuate()
    new_array = []
    arr = session.get("entry")['payload']
    index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    array = merge(arr,index)
    array.sort(key=itemgetter(0),reverse=True)
    array = merge(array,num)
    new_array = sorted(array,key=itemgetter(1),reverse=True)
    return {'text': new_array}
