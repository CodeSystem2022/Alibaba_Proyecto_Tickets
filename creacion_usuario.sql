-- Crea la secuencia
CREATE SEQUENCE IF NOT EXISTS usuarios;

-- Crea la tabla persona
CREATE TABLE IF NOT EXISTS public.usuarios  --se crea la tabla si no existe en el esquema publico
(
    id_usuario integer NOT NULL DEFAULT nextval('usarios'),  --se crea la columna id_usuarios
    nom_usuario character varying COLLATE pg_catalog."default", --se crea la columna nom_usuario
    contraseña character varying COLLATE pg_catalog."default", --se crea la columna contraseña 
    rol character varying COLLATE pg_catalog."default", --se crea la columna rol
    CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario) -- se le asigna una clave primaria para que se pueda identificar de manera unica cada registro dentro de una tabla
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;

-- Inserta datos en la tabla persona
--INSERT INTO usuarios() VALUES ();
--INSERT INTO usuarios() VALUES ();

-- Selecciona todas las filas de la tabla persona
SELECT * FROM usuarios;