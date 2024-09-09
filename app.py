from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Include the exclamation mark to match the test case expectation
    return "Hello World!"  # Updated return statement
@app.route("/test")
def home_test():
    # Include the exclamation mark to match the test case expectation
    return "Test Hello World!"  # Updated return statement

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
