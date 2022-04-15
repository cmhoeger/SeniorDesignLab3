
import flask

app = flask.Flask(__name__)

@app.route('/homepage.html', methods=['GET', 'POST'])
def index():
    message = ''
    if flask.request.method == 'POST':
        message = 'Hello ' + flask.request.form['name-input'] + '!'
    return flask.render_template('homePage.html', message=message)

@app.route('/connor.html')
def connor():
    return flask.render_template('connor.html')

@app.route('/jt.html')
def jt():
    return flask.render_template('jt.html')

@app.route('/brianna.html')
def brianna():
    return flask.render_template('brianna.html')

@app.route('/joey.html')
def joey():
    return flask.render_template('joey.html')

@app.route('/team_intro.html')
def team_intro():
    return flask.render_template('team_intro.html')

if __name__ == '__main__':
    app.run()
