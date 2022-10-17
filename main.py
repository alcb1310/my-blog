from flask import Flask, render_template
from posts import Posts

app = Flask(__name__)

posts = Posts()


@app.route('/')
def home():

    return render_template("index.html", posts=posts.posts)


@app.route("/post/<int:blog_id>")
def post(blog_id: int):

    return render_template('post.html', blog=posts.find(blog_id))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
