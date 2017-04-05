from flask import Flask, render_template

app = Flask(__name__)
app.config.from_envvar('HPFS_SETTINGS')

@app.route('/')
def index():
	return render_template('base.html')

if __name__ == '__main__':
	app.run()
