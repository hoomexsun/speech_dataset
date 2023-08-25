from pathlib import Path


class Project:
    def __init__(
        self,
        title: str = "main",
    ) -> None:
        """Base Class.

        Args:
            title (str, optional): Title for the utility class. Defaults to "main".
        """
        self.title = title

    def __str__(self) -> str:
        return self.title
