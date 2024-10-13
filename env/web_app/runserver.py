import os

from web_app import app    # Imports the code from web_app/__init__.py

if __name__ == '__main__':
    app.run(port=1977, debug=True)