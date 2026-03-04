"""Simple Flask web interface for the CGPA calculator."""

from flask import Flask, request, render_template_string

from cgpa_calculator.cgpa import calculate_cgpa

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>CGPA Calculator</title>
</head>
<body>
<h1>CGPA Calculator</h1>
<form method="post">
    <textarea name="courses" rows="10" cols="40" placeholder="A 3\nB+ 4"></textarea><br>
    <button type="submit">Calculate</button>
</form>
{% if result is not none %}
    <p><strong>Result:</strong> {{ result }}</p>
{% endif %}
{% if error %}
    <p style="color:red;"><strong>Error:</strong> {{ error }}</p>
{% endif %}
</body>
</html>"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = ''
    if request.method == 'POST':
        text = request.form.get('courses', '')
        lines = text.splitlines()
        try:
            entries = []
            for line in lines:
                if not line.strip():
                    continue
                parts = line.strip().split()
                if len(parts) != 2:
                    raise ValueError('Each line must contain grade and credit')
                grade = parts[0]
                credits = float(parts[1])
                entries.append((grade, credits))
            result = calculate_cgpa(entries)
        except Exception as exc:
            error = str(exc)
    return render_template_string(PAGE, result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
