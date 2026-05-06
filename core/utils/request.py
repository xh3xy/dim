import re


def get_app_version_from_ua(ua: str) -> str | None:
    match = re.search(r'^immich-(?:android|ios|unknown)/(?P<appVersion>.+)$', ua) or \
            re.search(r'^Immich_(?:Android|iOS|Unknown)_(?P<appVersion>.+)$', ua)

    return match.group('appVersion') if match else None


def get_user_agent_details(headers):
    #TODO: Use appropriate parser
    user_agent = headers.get('user-agent')
    #TODO: If appropriate parser is used, user_agent will not be a string.
    app_version = get_app_version_from_ua(user_agent)

    #TODO: Same
    device_type = user_agent
    if headers.get('devicemodel'):
        device_type = headers.get('devicemodel')

    device_os = user_agent
    if headers.get('devicetype'):
        device_os = headers.get('devicetype')

    return {
        'device_type': device_type,
        'device_os': device_os,
        'app_version': app_version,
    }