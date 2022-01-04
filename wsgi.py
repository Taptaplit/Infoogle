from dotenv import load_dotenv
import os
load_dotenv()

import app
handler = app.create_app()

debug = eval(os.environ.get('debug'))

if __name__ == '__main__':
    app.create_app().run(host='0.0.0.0', port=8080, debug=debug)