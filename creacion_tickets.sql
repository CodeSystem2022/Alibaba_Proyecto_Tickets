-- Table: public.TICKETS

-- DROP TABLE IF EXISTS public."TICKETS";

CREATE TABLE IF NOT EXISTS public."TICKETS"
(
    id_tickets integer NOT NULL DEFAULT nextval('"TICKETS_id_tickets_seq"'::regclass),
    num_tickets character varying COLLATE pg_catalog."default" NOT NULL,
    estado_venta boolean NOT NULL,
    estado_verificado boolean NOT NULL,
    zona character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "TICKETS_pkey" PRIMARY KEY (id_tickets)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."TICKETS"
    OWNER to postgres;
