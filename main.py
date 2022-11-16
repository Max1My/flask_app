from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/",methods=['GET'])
def main():
    name = request.args.get('name')
    message = request.args.get('message')
    content = f"Hello {name}! {message}!"
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run(debug=True)
