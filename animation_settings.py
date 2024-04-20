from settings import Settings


class AnimationSettings(Settings):
    class Builder():
        def __init__(self):
            self.__lines = True
            self.__frames = 200
            self.__interval = 20
            self.__blit = False

        def set_lines(self, boolean):
            self.__lines = boolean
            return self

        def set_frames(self, frames):
            self.__frames = frames
            return self

        def set_interval(self, interval):
            self.__interval = interval
            return self

        def set_blit(self, boolean):
            self.__blit = boolean
            return self

        def build(self):
            return AnimationSettings(self.__lines,
                                     self.__frames,
                                     self.__interval,
                                     self.__blit)

    def __init__(self, lines, frames, interval, blit):
        self.__lines = lines
        self.__frames = frames
        self.__interval = interval
        self.__blit = blit

    def get_lines(self):
        return self.__lines

    def get_frames(self):
        return self.__frames

    def get_interval(self):
        return self.__interval

    def get_blit(self):
        return self.__blit

    def display(self):
        pass
