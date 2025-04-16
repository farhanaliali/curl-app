from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Fetcher</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Enter a URL to Fetch</h2>
    <form method="post">
        <input type="text" name="url" style="width: 400px;" placeholder="https://example.com" required />
        <button type="submit">Fetch</button>
    </form>
    {% if result %}
        <h3>Response:</h3>
        <pre style="white-space: pre-wrap; word-wrap: break-word;">{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url)
            result = f"Status Code: {response.status_code}\n\n{response.text}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

