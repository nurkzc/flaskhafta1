from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

@app.route('/uzman')
def uzman():
    return render_template('uzman.html')

@app.route('/kullanici-panel')
def kullanici_panel():
    return render_template('kullanici-panel.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/yanitla')
def yanitla():
    return render_template('yanitla.html')

if __name__ == '__main__':
    app.run(debug=True)
