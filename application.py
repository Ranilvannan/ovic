from flask import Flask, request, url_for, render_template, abort, send_from_directory, jsonify
from blog_insert import BlogInsert
from flask_paginate import Pagination, get_page_parameter
import pymongo

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
PER_PAGE = 5


@app.route('/test')
def test_page():
    pagination = Pagination(page=1, total=200, search=False, record_name='users', css_framework='bootstrap4')
    return render_template('test_page.html', pagination=pagination)


def blog_collect():
    uri = app.config.get("MONGO_URI")
    database = app.config.get("DATABASE")
    blog = app.config.get("BLOG")
    client = pymongo.MongoClient(uri)
    db = client[database]
    return db[blog]


@app.route('/images/<path:filename>')
def custom_images(filename):
    path = app.config['CUSTOM_STATIC_PATH']
    return send_from_directory(path, filename)


@app.route('/')
def home_page():
    blog_col = blog_collect()

    total_story = story_col.find(data_dict).count(True)
    pagination = Pagination(total_count=total_story, page=page, per_page=PER_PAGE)

    # No story found
    if not(1 <= page <= pagination.total_page):
        abort(404)

    story_list = blog_col.find(data_dict)\
        .sort("story_id", -1)\
        .skip(PER_PAGE*(page-1))\
        .limit(PER_PAGE)

    category_list = category_col.find()
    ref_url = "{0}".format(request.host_url)

    return render_template('home_page.html',
                           records=story_list,
                           pagination=pagination,
                           category_list=category_list,
                           ref_url=ref_url)


@app.route('/blog/<category_url>/')
def category_page(category_url):
    blog_col = blog_collect()
    page = request.args.get("page", type=int, default=1)

    data_dict = {"variety": "technical_blog", "category_url": category_url}
    total_story = blog_col.find(data_dict).count(True)
    pagination = Pagination(total_count=total_story, page=page, per_page=PER_PAGE)

    # No Blog found
    if not (1 <= page <= pagination.total_page):
        abort(404)

    articles = blog_col.find(data_dict)\
        .sort("blog_id", -1)\
        .skip(PER_PAGE*(page-1))\
        .limit(PER_PAGE)

    return render_template('category_page.html',
                           articles=articles,
                           pagination=pagination)


@app.route('/blog/<category_url>/<blog_url>')
def blog_page(category_url, blog_url):
    blog_col = blog_collect()
    article = blog_col.find_one({"blog_url": blog_url})

    if not article:
        abort(404)

    return render_template('blog_page.html', article=article)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@app.cli.command('blog_update')
def blog_update():
    path = app.config.get("IMPORT_PATH")
    col = blog_collect()
    params = "blog_id"
    file_suffix = ".json"

    bi = BlogInsert(path, col, params, file_suffix)
    bi.trigger_import()
