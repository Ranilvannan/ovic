from flask import Flask, request, url_for, render_template, abort, send_from_directory, jsonify
from models import db

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.config['SECRET_KEY'] = 'you-will-never-guess'
db.init_app(app)


@app.route('/images/<path:filename>')
def custom_images(filename):
    path = app.config['CUSTOM_STATIC_PATH']
    return send_from_directory(path, filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog/<category>')
def category_page(category):
    return render_template('category_page.html')


@app.route('/blog/<category>/<blog_url>')
def blog_page(category, blog_url):
    print(app.root_path)

    article = {
        "author": "Ramesh Kumar S",
        "comments_count": 90,
        "last_updated": "02 Feb 2021 10:33AM IST",
        "views": 100,
        "title": "5 Simple Tips to Help Vegetarian or Vegan Travelers Eat Well, Anywhere",
        "content": """<p>Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et 
                      Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a 
                      treatise on the theory of ethics, very popular during the Renaissance. The first line of 
                      Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.""",
        "author_info": {
            "name": "Ramesh Kumar S",
            "description": "Programmer, Father, Husband, I design and develop Bootstrap template, founder of Bootstrap.News",
        },
        "breadcrumbs": [
            {"name": "Home", "url": "#"},
            {"name": "Category", "url": "#"},
            {"name": "Operating System", "url": "#"}
        ]
    }

    return render_template('blog.html', article=article)


def prev_next_article(post_url):
    articles = {
        "previous": {"name": "This is previous title", "url": "#"},
        "next": {"name": "This is next title", "url": "#"}
    }
    return render_template('widgets/prev_next_post.html', articles=articles)


def related_article(post_url):
    articles = [
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
    ]

    return render_template('widgets/related_post.html', articles=articles)


def latest_article(post_url):
    articles = [
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        {"date": "2019-10-14", "modified_date": "Oct 14, 2019",
         "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
    ]

    return render_template('widgets/latest_post.html', articles=articles)


def advertisement_article(post_url):
    return render_template('widgets/advertisement.html')


def author_info(post_url):
    info = {"name": "Ramesh Kumar S",
            "description": "Programmer, Father, Husband, I design and develop Bootstrap template, founder of Bootstrap.News",
        }
    return render_template('widgets/author_box.html', info=info)


@app.route('/api/<post_template>/<post_url>')
def trigger_post_template(post_template, post_url):
    article = None
    if post_template == "prev_next":
        article = prev_next_article(post_url)
    elif post_template == "related":
        article = related_article(post_url)
    elif post_template == "latest":
        article = latest_article(post_url)
    elif post_template == "advertisement":
        article = advertisement_article(post_url)
    elif post_template == "author_info":
        article = author_info(post_url)

    if not article:
        return "Not Found", 400

    return article
