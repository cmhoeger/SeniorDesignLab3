
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        source = str(request.form['button'])
        if source == "Our Team":
            return redirect(url_for('team_intro'))
        elif source == "Connor's Portfolio":
            return redirect(url_for('connor'))
        elif source == "Joey's Portfolio":
            return redirect(url_for('joey'))
        elif source == "Brianna's Portfolio":
            return redirect(url_for('brianna'))
        elif source == "JT's Portfolio":
            return redirect(url_for('jt'))

    return render_template('homePage.html', message=message)

@app.route('/connor')
def connor():
    return render_template('connor.html')

@app.route('/jt')
def jt():
    return render_template('jt.html')

@app.route('/brianna')
def brianna():
    return render_template('brianna.html')

@app.route('/joey')
def joey():
    return render_template('joey.html')

@app.route('/team_intro')
def team_intro():
    return render_template('team_intro.html')

if __name__ == '__main__':
    app.run(debug = True)

