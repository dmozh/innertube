from . import adaptor
from . import services

class BaseClient(object):
    adaptor: adaptor.Adaptor

    def __repr__(self):
        return f'<Client({self.adaptor.service.client.to_string()})>'

# class BaseYouTubeClient(BaseClient):
#     ...
#
# class BaseYouTubeMusicClient(BaseClient):
#     ...

class Web(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.WEB)

class WebRemix(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.WEB_REMIX)

class Android(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.ANDROID)

class AndroidMusic(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.ANDROID_MUSIC)

class Ios(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.IOS)

class IosMusic(BaseClient):
    def __init__(self):
        self.adaptor = adaptor.Adaptor(services.IOS_MUSIC)