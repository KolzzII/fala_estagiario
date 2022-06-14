from flask import render_template
from application import app
from application.model.dao import postDAO

@app.route("/", methods=['GET'])
def home():
    list_post = postDAO.list_post()
    ordered_list = sorted(list_post, key=lambda x: x._created_date, reverse=True)
    return render_template("index.html", posts = ordered_list)
