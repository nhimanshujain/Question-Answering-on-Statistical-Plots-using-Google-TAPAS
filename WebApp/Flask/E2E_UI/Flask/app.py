from flask import Flask , render_template , request
import pandas as pd

app = Flask(__name__ , static_url_path = '' ,static_folder = 'static', template_folder = 'templates')

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route("/Results" , methods= ['GET','POST'])
def Foo():

  pass

@app.route("/CSV")
def displayer():

   d = pd.read_csv(r"C:\Users\SOORYANATH\Downloads\0.csv")

   d.to_html("Table.htm" , justify='center')

   d_html = d.to_html()

   d_html = d_html.replace('<table border="1" class="dataframe">' , '<table border="2px solid white" style = "color:white ; font-weight:900 ;" class="dataframe">')

   d_html = d_html.replace('<tr>' , '<tr border="2px solid white">')

   return render_template('Result.html' , data = d_html)


if __name__ == '__main__':

   app.run(debug = True)