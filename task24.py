from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
        <h1>hello_world!</h1>
        <ul>
            <li><a href="/about">О компании</a></li>
            <li><a href="/contacts">Контакты</a></li>
            <li><a href="/posts">Список постов</a></li>
        </ul>
        """
    return html

# todo: добавьте во Flask маршруты для страниц (endpoint)
@app.route("/about")
def about():
    return "<p>Здесь вы можете узнать больше.</p>"

@app.route("/contacts")
def contacts():
    return "<p>Есть контакты.</p>"

@app.route("/posts")
def posts():
    return "<p>Очень важные посты.</p>"

if __name__ == "__main__":
    app.run()
