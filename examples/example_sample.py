from flask import Flask, redirect
from donationalerts_api import DonationAlertsApi, Scopes

app = Flask(__name__)
api = DonationAlertsApi("client id", "client secret", "http://127.0.0.1:5000/login", [Scopes.USER_SHOW, Scopes.DONATION_INDEX])


@app.route("/", methods=["get"])
def index():
	return redirect(api.login()) # Log in your application


@app.route("/login", methods=["get"])
def login():
	code = api.get_code()
	access_token = api.get_access_token(code)

	user = api.get_user(access_token)
	donation_list = api.get_donations(access_token)

	return user

if __name__ == "__main__":
	app.run(debug=True)