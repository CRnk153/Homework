from flask import Flask, render_template, request, redirect

app = Flask(__name__)

text_list = []

@app.route('/')
def get_start():
    return render_template('index.html')


@app.route('/text/new', methods=['GET'])
def text_new():
    return render_template('text_form.html')


@app.route('/display-text', methods=['GET'])
def text():
    global text_list
    text_list.append(text_global)
    return render_template('text.html', data=text_global)


@app.route('/save', methods=['POST'])
def save():
    global text_global
    form = request.form
    text_global = form['text']
    print('Form text', text_global)
    return redirect('/')

@app.route('/register', methods=["POST", "GET"])
def index():
    return render_template("register.html")


@app.route("/register/success", methods=["POST"])
def register():
    name = request.form['name']
    print(name)
    return render_template("register_success.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/news", methods=["GET"])
def news():
    return render_template("news.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")
if __name__ == '__main__':
    app.run(debug=True)
