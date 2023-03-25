import xmltodict

def add_user(session, str_name):
    return xmltodict.parse(session.post(f"http://127.0.0.1/admin/adduser?username={str_name}&email={str_name.replace(' ','_').lower() + '@gmail.com'}&password=1234567890&authtype=0").content)
