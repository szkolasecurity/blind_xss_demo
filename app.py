from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

        return render_template('index.html',
                           thankyou="Your comment was sent to admin.")

    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def stats():
    if request.method == 'POST':
        if request.form.get('login') !=  'admin' or request.form.get('password') != 'admin':
            return redirect('/admin?error=incorrect+login', code = 302)

        search_query = request.args.get('q')

        comments = db.get_comments(search_query)
        return render_template('admin.html', comments = comments)

    return render_template('admin_login.html', error = request.args.get('error') or "")