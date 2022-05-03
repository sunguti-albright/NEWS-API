from flask import render_template
from app import app

@app.errorhandler(404)
def errorpage(error):
    """
    Functions to render the 404 error page
    """
    return render_template("errorpage.html"), 404