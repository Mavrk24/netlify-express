from anytree import Node, RenderTree,AsciiStyle,PreOrderIter
from anytree.dotexport import RenderTreeGraph

root = Node('root', value = 'null', label='') 
a1 = Node('Do you use laptop for > 3 hours per day ?', parent=root, value='null',children=[ #1
    Node('Do you use laptop on sofa / on bed ?',  value='null',label='Have a life'),#2
    Node('Do you use laptop on lap ?',  value='null',label='Have a life'), #3
    Node('Do you have to look down on screen ?', value='null',label='Have a life')], label='') #4s
a2 = Node('Do you have to look while you type ?', parent=root , value='null',label='')
b11 = Node('Do you use iPad/Tablet > 3 hours per day ?', parent=root, value='null',children=[
    Node('Do you use iPad/Tablet on table / on lap (or bed) ?',  value='null',label='')], label='') #7
b2 = Node('Do you use without standing cases ?', parent=root, value='null',label='') #8
c = Node('Do you do manual work (drawing, drafting, sketching) ?', parent=root, value='null',label='')
c1 = Node('Do you do the work on a table', parent=c, value='null',label='')
c11 = Node('Is it a slope table ?', parent=c1, value='null',label='') #11s
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
