class Usuario:
    def __init__(self, id_usuario=None, usuario=None, password=None, rol=None):
        self._id_usuario = id_usuario
        self._usuario = usuario
        self._password = password
        self._rol = rol

    def __str__(self):
        return f'Usuario: {self._id_usuario} {self._usuario} {self._password} {self._rol}'

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol
