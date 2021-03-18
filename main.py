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

@app.route('/ang')
def ang():
    return flask.render_template('ang.html')

# want to focus on making app RESTful and CRUD
# Create Read Update Delete (the 4 main things your app should be able to do)
# on top of that, using REST commands POST, GET, PUT, DELETE match CRUD

# REST
# Uniform interface (UI)- resources should be uniquely identifiable through a single url
# Clear client/server break. UI and request-gathering (client). Data access, workload management (Server)
# Stateless - all operations stateless, any state management takes place on client side
# Cache resources from requests so that 2 identical requests do not have to be made
# REST alows for multiple layers of servers
# Server sends back static resource as XML/JSON, sometimes as executable code

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)