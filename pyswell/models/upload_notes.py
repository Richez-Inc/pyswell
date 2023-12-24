from .base import Base


class UploadNotes(Base):
    """UploadNotes represent notes that can be attached to an product upload."""

    def __init__(self, swell):
        super().__init__(swell, "upload-notes")

        self._swell = swell
