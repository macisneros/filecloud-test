from business import user_business
from service import group_controller, login_controller, user_controller
from unidecode import unidecode


def addUsersToGroups(dict_user):
    session = user_business.get_admin_session()

    for group in dict_user.keys():
        response_group_details = group_controller.get_group_by_name(session, group)

        # Verify if group does not exist, if so group will be created else it will retrieve group data
        if "groups" in response_group_details and "meta" in response_group_details["groups"] and "message" in response_group_details["groups"]["meta"]:
            response_add_group = group_controller.add_group(session, group)
            str_group_id = response_add_group['groups']['group']['groupid']
        else:
            str_group_id = response_group_details['groups']['group']['groupid']

        for user in dict_user[group]: # create a new user and add it in a group
            user = unidecode(user) # clean user name of non latin characters
            user_controller.add_user(session, user)
            group_controller.add_member_to_group(session, str_group_id, user)

    login_controller.adminLogout(session)