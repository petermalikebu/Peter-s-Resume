from flask import Flask, redirect, url_for, flash, render_template

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route('/')
@app.route('/index')
def index():
    try:
        # Your main logic here
        pass
    except Exception as e:
        flash("Connection failed. Please try again later.")
        return redirect(url_for('index'))

    # Always return something at the end of the function
    return render_template('index.html')
