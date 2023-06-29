-- Table: public.tickets

-- DROP TABLE IF EXISTS public.tickets;

-- Crea la secuencia
CREATE SEQUENCE IF NOT EXISTS tickets_id_ticket_seq;

CREATE TABLE IF NOT EXISTS public.tickets
(
    id_ticket integer NOT NULL DEFAULT nextval('tickets_id_ticket_seq'),
    ticket text COLLATE pg_catalog."default",
    vendido boolean,
    verificado boolean,
    CONSTRAINT tickets_pkey PRIMARY KEY (id_ticket)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tickets
    OWNER to postgres;