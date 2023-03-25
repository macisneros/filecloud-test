from requests import Session

from service import login_controller

def get_admin_session() -> Session:
    return login_controller.adminLogin()

def close_admin_session(session: Session) -> None:
    login_controller.adminLogout(session)