from flask import Flask, request, render_template

app = Flask(__name__)

# Custom logic function
def process_logic(input_data):
    # Example: Reverse the string and make it uppercase
    return input_data[::-1].upper()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_data = request.form.get('input_data')
        if input_data:
            result = process_logic(input_data)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
