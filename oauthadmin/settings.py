defaults = {
    # default values for all django-oauth2-admin settings
    "GET_USER": 'oauthadmin.stubs.get_user'
}

global_prefix = 'OAUTHADMIN_'

def app_setting(name):
    return getattr(global_settings, global_prefix+name, defaults[name])
