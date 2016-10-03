from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the homepage"


@app.route('/questions')
def questions():
    return "What is your name? \n How old are you? \n What kind of liquor is your favorite?"
@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post ID is %s" % post_id


if __name__ == "__main__":
    app.run(debug = True)







