from flask import Flask, render_template
app = Flask(__name__)
from controllers.library_controller import library_blueprint

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(library_blueprint)