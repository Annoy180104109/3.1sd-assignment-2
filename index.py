from flask import Flask, redirect, url_for, request, render_template

app=Flask(__name__)  #server create kore vitore file er name ashbe




@app.route('/about')        #landing page e giye run korbe
def aboutpage():
    return render_template("about.html")







@app.route('/dummy', defaults={'name' : " "})
@app.route('/<name>')        #landing page e giye run korbe
def dummypage(name):
    return render_template("dummy.html",name=name)


@app.route('/submit', methods=['GET'])        #landing page e giye run korbe
def sub1():
    print(request.method)
    if request.method == 'GET':
        sl=request.args['SL']
        sw=request.args['SW']
        operation=request.args['operation']
        if operation== 'add':

            print(float(sl)+float(sw))
            return redirect(url_for('dummypage',name=float(sl)+float(sw)))    
        if operation== 'sub':

            print(float(sl)-float(sw))
            return redirect(url_for('dummypage',name=float(sl)-float(sw)))    
        if operation== 'mul':

            print(float(sl)*float(sw))
            return redirect(url_for('dummypage',name=float(sl)*float(sw)))    

        if operation== 'div':

            print(float(sl)/float(sw))
            return redirect(url_for('dummypage',name=float(sl)/float(sw)))    

    else:
        return redirect(url_for('dummypage'))



















@app.route('/', defaults={'name' : " "})
@app.route('/<name>')        #landing page e giye run korbe
def mainpage(name):
    return render_template("index.html",name=name)


@app.route('/submit', methods=['GET'])        #landing page e giye run korbe
def sub():
    print(request.method)
    if request.method == 'GET':
        sl=request.args['SL']
        sw=request.args['SW']
        pl=request.args['PL']
        pw=request.args['PW']
        print(" "+sl+" "+sw+" "+pl+" "+pw)

        

        return redirect(url_for('mainpage',name=" "+sl+" "+sw+" "+pl+" "+pw))        
    else:
        return redirect(url_for('mainpage'))






if __name__== '__main__':
    app.run(debug = True)   # update korle save hobe

