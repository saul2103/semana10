class Usuario:
    def __init__(self, nombre: str, email: str) -> None:
        self._nombre = nombre
        self._email = email

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"Usuario: {self._nombre} | Email: {self._email}"