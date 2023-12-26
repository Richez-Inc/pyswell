from .base import Base


class Review(Base):
    def __init__(self, swell):
        super().__init__(swell, "review")

        self._swell = swell
