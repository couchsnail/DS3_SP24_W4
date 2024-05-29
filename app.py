from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/open_new_tab', methods=['POST'])
def open_new_tab():
    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
