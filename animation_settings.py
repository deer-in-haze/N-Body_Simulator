class AnimationSettings:
    def __init__(self):
        self.__lines = True
        self.__frames = 200
        self.__interval = 20
        self.__blit = False

    def set_lines(self, boolean):
        self.__lines = boolean

    def get_lines(self):
        return self.__lines

    def set_frames(self, frames):
        self.__frames = frames

    def get_frames(self):
        return self.__frames

    def set_interval(self, interval):
        self.__interval = interval

    def get_interval(self):
        return self.__interval

    def set_blit(self, boolean):
        self.__blit = boolean

    def get_blit(self):
        return self.__blit


class AnimationSettingsBuilder:
    def __init__(self):
        self.__settings = None
        self.__reset()

    def __reset(self):
        self.__settings = AnimationSettings()
        return self

    def set_lines(self, boolean):
        self.__settings.set_lines(boolean)
        return self

    def get_lines(self):
        return self.__settings.get_lines()

    def set_frames(self, frames):
        self.__settings.set_interval(frames)
        return self

    def get_frames(self):
        return self.__settings.get_frames()

    def set_interval(self, interval):
        self.__settings.set_interval(interval)
        return self

    def get_interval(self):
        return self.__settings.get_interval()

    def set_blit(self, boolean):
        self.__settings.set_blit(boolean)
        return self

    def get_blit(self):
        return self.__settings.get_blit()

    def build(self):
        return self.__settings
