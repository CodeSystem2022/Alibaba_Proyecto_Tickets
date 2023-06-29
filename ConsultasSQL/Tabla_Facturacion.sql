-- Table: public.facturacion

-- DROP TABLE IF EXISTS public.facturacion;

-- Crea la secuencia
CREATE SEQUENCE IF NOT EXISTS facturacion_id_factura_seq;

CREATE TABLE IF NOT EXISTS public.facturacion
(
    id_factura integer NOT NULL DEFAULT nextval('facturacion_id_factura_seq'),
    total_venta integer,
    cant_vendidas integer,
    descuento integer,
    CONSTRAINT facturacion_pkey PRIMARY KEY (id_factura)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.facturacion
    OWNER to postgres;