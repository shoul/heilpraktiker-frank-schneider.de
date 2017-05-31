from flask import Flask, render_template

app = Flask(__name__)
app.config.from_envvar('HPFS_SETTINGS')


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/impressum/')
def impressum():
	return render_template('impressum.html')


if __name__ == "__main__":
    app.run()
