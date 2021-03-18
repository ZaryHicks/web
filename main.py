import flask

app = flask.Flask(__name__)
app.secret_key = b'oaijrwoizsdfmnvoiajw34foinmzsdv98j234'

@app.route('/')
def root():
    return show_page('home.html', 'Home')

# when a user signs in, the username is in the session[user], so we can get it at any time
#def get_user():
#    return flask.session.get('user', None)

def show_page(page, title):
    # removed a lot of the show page fields, and thus the render fields
    # as we decide what needs to be passed to templates, we will add back in with this
    # same format

    # always need a page, page title, and user to pass into template
    # show? - also, does errors work?
    # errors is an array of error strings, to be displayed in the errors field in the event of errors *note: errors*
    #return flask.render_template(page, page_title=title, user=get_user())
    return flask.render_template(page, page_title=title)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)