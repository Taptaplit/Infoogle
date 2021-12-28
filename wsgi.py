from dotenv import load_dotenv
load_dotenv()

import app
handler = app.create_app()


if __name__ == '__main__':
    print("== Running in debug mode ==")
    app.create_app().run(host='0.0.0.0', port=8080, debug=True)