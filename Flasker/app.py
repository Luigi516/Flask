from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('Homepage.html')

@app.route('/Progetti.html')
def page2():
    return render_template('Progetti.html')

@app.route('/Astropedia.html')
def page3():
    return render_template('Astropedia.html')


@app.route('/Contact.html')
def page5():
    return render_template('Contact.html')


@app.route('/Earth.html')
def page6():
    return render_template('Earth.html')

if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0')