from .base import Base

class Brand(Base):
    def __init__(self, swell):
        super().__init__(swell, "brand")

        self._swell = swell
