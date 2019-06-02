import pygments, markdown
from flask import Flask, render_template, url_for, request, render_template_string
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from datetime import date, datetime, time
from pygments.styles import get_style_by_name

FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PAGE_DIR = 'pages'


# Renders blog content and passes through Pygments to highlight any code on a blog post page
def code_highlight(data):
    markdown_text = render_template_string(data)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
    return pygmented_text


app = Flask(__name__)
app.config["FLATPAGES_HTML_RENDERER"] = code_highlight
flatpages = FlatPages(app)
app.config.from_object(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    path = '{}/{}'.format(PAGE_DIR, 'about')
    post = flatpages.get_or_404(path)
    return render_template("about.html", post=post)

@app.route("/work/")
def experience():
    path = '{}/{}'.format('pages', 'work')
    post = flatpages.get_or_404(path)
    return render_template("work.html", post=post)

@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("monokai"), 200, {"Content-Type":"text/css"}

@app.route("/blog/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    return render_template('blog.html', posts=posts)

@app.route("/blog/<name>/")
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('blog.html', post=post)

if __name__ == '__main__':
    app.run()