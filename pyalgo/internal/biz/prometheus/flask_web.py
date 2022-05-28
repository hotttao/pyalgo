from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter


c = Counter('my_failures', 'Description of counter')


# Create my app
app = Flask(__name__)
app.config.from_mapping({"DEBUG": True})


view_metric = Counter('view', 'Product view', ['product'])
buy_metric = Counter('buy', 'Product buy', ['product'])


@app.route('/')
def hello():
    view_metric.labels(product=id).inc()
    return "hello "


@app.route('/view/<id>')
def view_product(id):
    view_metric.labels(product=id).inc()
    return "View %s" % id


@app.route('/buy/<id>')
def buy_product(id):
    buy_metric.labels(product=id).inc()
    return "Buy %s" % id


# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})
