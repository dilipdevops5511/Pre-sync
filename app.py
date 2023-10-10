import subprocess
from flask import Flask, render_template

app = Flask(__name__)



# Redirect stderr to a null file (suppressing error messages)
#sys.stderr = open('/dev/null', 'w')  # On Unix-like systems

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/run_script')
def run_script():
    try:
        result = subprocess.check_output(['python', 'Application.py'], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


if __name__ == '__main__':
    app.run(debug=True)

