from .base import Base


class Alarm(Base):
    def __init__(self, swell):
        super().__init__(swell, "alarm")

        self._swell = swell
