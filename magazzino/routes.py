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
        btnUpd=request.form.getlist('btnUpd')
        print (checkBox)
        if btnUpd:
            checkBox=['']
            dsar=request.form.getlist('dsar') 
            cdar=request.form.getlist('cdar') 
            c=DbPoweri()
            c.connection()
            c.callUpdArtp(c.c1,cdar[0], dsar[0])

    db=DbPoweri()
    db.connection()
    rows=db.selectMgesi(db.c1)
    
    if request.method != 'POST': 
        checkBox=['']

    if not checkBox[0]: 
        return render_template('magazzino.html', len = len(rows), lenr = len(rows[0]), rows=rows, check=' ')
    if  checkBox[0]: 
        print (checkBox[0])        
        a=checkBox[0].split(',')
        return render_template('form.html', len = len(rows), lenr = len(rows[0]), rows=rows, articolo=a[0].strip(),
                descrizione=a[1].strip())
                            
