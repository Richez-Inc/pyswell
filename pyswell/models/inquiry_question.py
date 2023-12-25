from .base import Base


class InquiryQuestion(Base):
    def __init__(self, swell):
        super().__init__(swell, "inquiry-question")

        self._swell = swell
