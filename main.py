from flask import Flask
from routes.payment_routes import payment_routes
from routes.organizer_routes import organizer_routes
from routes.attendee_routes import attendee_routes
from routes.events_routes import event_routes
app = Flask(__name__)

app.register_blueprint(payment_routes)
app.register_blueprint(organizer_routes)
app.register_blueprint(attendee_routes)
app.register_blueprint(event_routes)

app.run(debug=True)