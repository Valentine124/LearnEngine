""" This module contains code for WSGI """


from api.v1.app import app

if __name__ == '__main__':
    app.run()
