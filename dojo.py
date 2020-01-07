from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

get_counter = 0
post_counter = 0

@app.route('/')
@app.route('/request-counter', methods=['GET', 'POST'])
def route():
    if request.method == 'GET':
        global get_counter
        get_counter += 1
    elif request.method == 'POST':
        global post_counter
        post_counter += 1
    return render_template('counter.html', GET=get_counter, POST=post_counter)



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
