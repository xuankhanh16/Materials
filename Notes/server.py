from flask import Flask


app = Flask (__name__)

@app.route('/')
def root():
    #return "Hello"
    return '''
        <html>
        <h1> Hello this is cia </h1>
        <html>
     '''

@app.route('/back_home')
def bye():
    return "bye"

app.run()

