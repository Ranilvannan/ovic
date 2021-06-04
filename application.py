from flask import Flask, request, url_for, render_template, abort, send_from_directory
from models import db

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.config['SECRET_KEY'] = 'you-will-never-guess'
db.init_app(app)


@app.route('/images/<path:filename>')
def custom_images(filename):
    path = app.config['CUSTOM_STATIC_PATH']
    return send_from_directory(path, filename)


@app.route('/test')
def index():
    return render_template('index.html')


@app.route('/')
def blog_page():
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
        ],
        "previous": {"name": "Jacob deGrom Goes the Distance as Mets Top the Phillies", "url": "#"},
        "next": {"name": "The 52 Places Traveler: Summer in France, in Two Very Different Ways", "url": "#"},
        "latest_news": [
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"}
        ],
        "related_articles": [
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
            {"date": "2019-10-14", "modified_date": "Oct 14, 2019", "title": "This U.S. Airline Has More Legroom Than Any Other", "url": "#"},
        ]
    }


    return render_template('blog.html', article=article)


