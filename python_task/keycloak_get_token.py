from keycloak import KeycloakOpenID
from flask import Flask, render_template


# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://127.0.0.1:8080/auth",
                                 client_id="myclient",
                                 realm_name="myrealm")


# Get Token
token = keycloak_openid.token("myuser", "1234")

# Create a new Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render a template that displays "Hello, world!"
    return render_template('home.html', message=token)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

