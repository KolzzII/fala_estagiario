from flask import render_template, request
from application import app
from application.model.dao import postDAO
from application.model.entity.Post import Post

@app.route("/add_post", methods=['GET'])
def add_post():
    return render_template("add_post.html")

@app.route("/save", methods=['POST', 'GET'])
def save():
    name = request.form.get('name', 'none')
    text = request.form.get('text', 'none')
    new_post = Post(name, text)
    postDAO.insert_post(new_post)
    return render_template("add_post.html",  post = new_post, post_sent = True)