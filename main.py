from flask import Flask
app=flask(__name__)
@app.route('/', method=['GET','POST'])
def index():
    return "hy this rahul web"

if __name__=="__main__":
    app.run()
