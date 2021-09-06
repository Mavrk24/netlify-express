from anytree import Node, RenderTree,AsciiStyle,PreOrderIter
from anytree.dotexport import RenderTreeGraph

root = Node('root', value = 'null', label='') 
a = Node('Do you use laptop ?', parent=root, value='null',label='') #-
a1 = Node('For work / study ?', parent=a, value='null',label='') #-
a2 = Node('For entertainment (Netflix,Disney+ etc.) ?', parent=a, value='null',label='') #-
a11 = Node('> 3 hours per day ?', parent=a1, value='null',children=[
    Node('on sofa / on bed ?',  value='null',label='Have a life'),#5
    Node('on lap ?',  value='null',label='Have a life'), #6
    Node('do you have to look down on screen ?', value='null',label='Have a life')], label='') #7s
a12 = Node('Do you have to look while you type ?', parent=a1 , value='null',label='Have a life'), 
a21 = Node('> 3 hours per day ?', parent=a2, value='null', children=[ 
    Node('on sofa / on bed ?',  value='null',label='Have a life'), #10
    Node('on lap ?',  value='null',label='Have a life'), #11
    Node('do you have to look down on screen ?', value='null',label='Have a life')], label='') #12s
b = Node('Do you use iPad/tablet ?', parent=root, value='null',label='')
b1 = Node('For work ?', parent=b, value='null',label='')
b11 = Node('> 3 hours per day ?', parent=b1, value='null',children=[
    Node('on table / on lap (or bed) ?',  value='null',label='Have a life')], label='') #16
b12 = Node('Do you use without standing cases ?', parent=b1, value='null',label='') #17
b2 = Node('For entertainment (Netflix,Disney+ etc.) ?', parent=b, value='null',label='')
b21 = Node('> 3 hours per day ?', parent=b2, value='null',children=[
    Node('on table / on lap (or bed) ?',  value='null',label='Have a life')], label='') #20
b22 = Node('Do you use without standing cases ?', parent=b2, value='null',label='') #21
c = Node('Do you do manual work (drawing, drafting, sketching) ?', parent=root, value='null',label='')
c1 = Node('Do you do the work on a table', parent=c, value='null',label='')
c11 = Node('Is it a slope table ?', parent=c1, value='null',label='') #24s
d = Node('Do you use a chair without arm rest ?', parent=root, value='null',label='')
d1 = Node('Do you use a chair without lumbar back support ?', parent=d, value='null',label='')

arr = []
for a in PreOrderIter(root):
    arr.append(a.name)

def getQ():
    return arr

val = []
for a in PreOrderIter(root):
    val.append(a.depth)

def valuate():
    return val

def returnnotQ(arr):
    array = []
    for a in PreOrderIter(root):
        array.append(a.name)
    return array

def returnQ(t):
    inputs = []
    x = ''
    for a in PreOrderIter(root):
        x = a.name
        inputs.append(x)
    return inputs

def returnofQ(arr):
    return len(arr)

def func():   
    for a in PreOrderIter(root):
        b = a.parent
        if b != None:
            if (b.value != 'N'):
                print(a.name)
                a.value = input(': ')
            else:
                if (a.children!=None):   
                    del a.children
max = -1
max_q = ''
for a in PreOrderIter(root):
    if (a.value=='Y'):
        if(a.depth >= max):
            max = a.depth
            max_q = a.name
    else:
        a.parent = None

def display():
    return max_q
