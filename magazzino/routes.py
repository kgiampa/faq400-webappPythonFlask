from flask import render_template,request
from magazzino import app
from magazzino.DbPoweri import DbPoweri

@app.route('/')
def menu():
     
    return render_template('menu.html')

@app.route('/magazzino', methods=('GET', 'POST'))
def magazzino():
    #print (request.method)
    if request.method == 'POST':
        print ("post")
        checkBox=request.form.getlist('checkBox')
        print (checkBox)
    db=DbPoweri()
    db.connection()
     
    rows=db.selectMgesi(db.c1)
    if request.method != 'POST': 
         
        checkBox=['']

    if not checkBox[0]: 
        return render_template('magazzino.html', len = len(rows), lenr = len(rows[0]), rows=rows, check=' ')
    if  checkBox[0]: 
        return render_template('form.html', len = len(rows), lenr = len(rows[0]), rows=rows, articolo=checkBox[0])
                            
