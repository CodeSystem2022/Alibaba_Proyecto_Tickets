-- Table: public.usuarios

-- DROP TABLE IF EXISTS public.usuarios;

-- Crea la secuencia
CREATE SEQUENCE IF NOT EXISTS usuarios_id_usuario_seq;

CREATE TABLE IF NOT EXISTS public.usuarios
(
    id_usuario integer NOT NULL DEFAULT nextval('usuarios_id_usuario_seq'),
    usuario character varying(50) COLLATE pg_catalog."default",
    password character varying(50) COLLATE pg_catalog."default",
    rol character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;

-- Inserta datos en la tabla persona
INSERT INTO usuarios(usuario,password,rol) VALUES ('alibaba','alibaba123','admin');