from .base import Base


class ReviewReply(Base):
    def __init__(self, swell):
        super().__init__(swell, "review-reply")

        self._swell = swell
