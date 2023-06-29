from cursor_del_pool import CursorDelPool
from Usuarios import Usuario


class UsuarioDAO:
    '''
    DAO - Data Access Object para la tabla de usuario
    CRUD - Create - Read - Update - Delete para la tabla de usuario
    '''
    _SELECT_ALL = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _SELECT_ONE = 'SELECT * FROM usuarios WHERE usuario=%s AND password=%s'
    _INSERTAR = 'INSERT INTO usuarios(usuario, password, rol) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET password=%s, rol=%s WHERE usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_ALL)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def seleccionarOne(cls):
        with CursorDelPool() as cursor:
            usuario = input("                                     Escriba un Usuario: ")
            password = input("                                     Escriba una Contraseña: ")
            cursor.execute(cls._SELECT_ONE, (usuario, password))
            registro = cursor.fetchone()
            return registro

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.password, usuario.rol, usuario.usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
