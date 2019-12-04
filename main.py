from app import application

import view

if __name__ == "__main__":
    from waitress import serve
    serve(application, host="127.0.0.1", port=5000)
    application.run()