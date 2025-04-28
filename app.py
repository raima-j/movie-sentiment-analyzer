from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        movie_name=request.form['movie']
        return f"You searched for {movie_name}"
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)