from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    even_numbers = []

    if request.method == "POST":
        try:
            n = int(request.form["number"])
            if n <= 0:
                result = "❌ Please enter a number greater than 0."
            else:
                even_numbers = [2 * i for i in range(1, n + 1)]
                result = f"✅ First {n} even numbers:"
        except ValueError:
            result = "❌ Invalid input. Please enter a valid number."

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Even Number Generator</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f4f9ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                text-align: center;
                width: 90%;
                max-width: 500px;
            }
            input[type="number"], button {
                padding: 10px;
                margin: 10px 0;
                width: 100%;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                font-size: 18px;
                color: #333;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                padding: 5px;
                display: inline-block;
                background: #e8f0fe;
                margin: 5px;
                border-radius: 5px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Even Number Generator</h2>
            <p>Enter a number N to generate the first N even numbers.</p>
            <form method="POST">
                <input name="number" type="number" placeholder="Enter a positive number" required>
                <button type="submit">Generate</button>
            </form>
            {% if result %}
                <div class="result">{{ result }}</div>
                {% if even_numbers %}
                    <ul>
                        {% for num in even_numbers %}
                            <li>{{ num }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
            {% endif %}
        </div>
    </body>
    </html>
    """, result=result, even_numbers=even_numbers)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)
