import xmltodict

def get_group_by_name(session, str_name):
    response = session.get(f'http://127.0.0.1/admin/getgroupbyname?groupname={str_name}')
    return xmltodict.parse(response.content)

def add_group(session, str_name):
    response = session.post(f'http://127.0.0.1/admin/addgroup?groupname={str_name}')
    return xmltodict.parse(response.content)

def add_member_to_group(session, str_group_id, str_user_id):
    response = session.post(f'http://127.0.0.1/admin/addmembertogroup?groupid={str_group_id}&userid={str_user_id.lower()}')
    return xmltodict.parse(response.content)

