import requests

def adminLogin():
    session = requests.Session()
    session.post("http://127.0.0.1/admin/adminlogin?adminuser=admin&adminpassword=password")

    return session

def adminLogout(session):
    session.post("http://127.0.0.1/admin/logout")