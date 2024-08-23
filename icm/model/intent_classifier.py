"""The classifier interface. You can modify/refactor it according to your needs."""


class IntentClassifier:

    def __init__(self) -> None:
        self.ready = False

    def is_ready(self) -> bool:
        """Check if the classifier is ready to classify intents."""
        return self.ready

    def load(self, file_path) -> None:
        """Load the model or configuration the specified file path."""
        self.ready = True
