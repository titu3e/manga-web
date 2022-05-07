#!/usr/bin/env python3


### Importing Modules, Files, etc.
from flask import (
    Flask,
    render_template,
    url_for,
    request
)
from helper.manga_page import *
from helper.search import SearchEngine, RandomAnimeGif


### Creating App Object
app = Flask(__name__)


### Routing
# Home Page with search Engine
@app.route("/")
def homePage():
    query = request.args.get('search')
    if query is not None:
        if query:
            search = SearchEngine(query)
            return render_template('search.html', result = search.mangaList, query = query)
        
    gif = RandomAnimeGif()
    return render_template('index.html', gifUrl = gif.imgUrl)

# About Page
@app.route("/about")
def aboutPage():
    return render_template('about.html')

# Contact Page
@app.route("/contact")
def contactPage():
    return render_template('contact.html')

# Manga Page
@app.route("/manga/<string:manga_id>")
def mangaPage(manga_id):
    if manga_id:
        chapter_no = request.args.get('chapter')
        if chapter_no:
            chapp = ChapterPage(manga_id, chapter_no)
            return render_template(
                'manga_page.html'
            )
        else:
            chap = Chapter(manga_id)
            return render_template(
                'manga.html',
                chapList = chap.chapJson,
                title = chap.title,
                poster = chap.posterUrl
            )


### Running Web
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

