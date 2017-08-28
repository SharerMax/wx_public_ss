""" main module """

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    ''' index page '''
    return "I'm index page"


@app.route('/hello_word')
def hello_world():
    ''' test print 'hello, world' '''
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    """ show user profile """
    return "user %s" % username


def main():
    """
    run app
    """
    app.run(debug=True)
    with app.test_request_context():
        print(url_for('hello_world'))
        print(url_for('show_user_profile', username='Max'))


if __name__ == '__main__':
    main()
