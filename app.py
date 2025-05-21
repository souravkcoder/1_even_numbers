
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    if request.method == "POST":
        try:
            n = int(request.form["number"])
            result = [2 * i for i in range(1, n + 1)]
        except:
            result = ["Invalid input."]
    return render_template_string("""
        <html><head><title>Even Numbers</title><style>
        body { font-family: Arial; margin: 40px; }
        input, button { padding: 5px; margin: 5px; }
        </style></head><body>
        <h2>Generate N Even Numbers</h2>
        <form method="POST">
            Enter N: <input name="number" type="number">
            <button type="submit">Generate</button>
        </form>
        <p>{{ result }}</p>
        </body></html>
    """, result=result)
        