--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-06-18 18:00:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16411)
-- Name: facturacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.facturacion (
    id_factura integer NOT NULL,
    total_ventas integer,
    cant_vendidas integer,
    descuento double precision
);


ALTER TABLE public.facturacion OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16410)
-- Name: facturacion_id_factura_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.facturacion_id_factura_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facturacion_id_factura_seq OWNER TO postgres;

--
-- TOC entry 3325 (class 0 OID 0)
-- Dependencies: 214
-- Name: facturacion_id_factura_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.facturacion_id_factura_seq OWNED BY public.facturacion.id_factura;


--
-- TOC entry 3173 (class 2604 OID 16414)
-- Name: facturacion id_factura; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion ALTER COLUMN id_factura SET DEFAULT nextval('public.facturacion_id_factura_seq'::regclass);


--
-- TOC entry 3319 (class 0 OID 16411)
-- Dependencies: 215
-- Data for Name: facturacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.facturacion (id_factura, total_ventas, cant_vendidas, descuento) FROM stdin;
\.


--
-- TOC entry 3326 (class 0 OID 0)
-- Dependencies: 214
-- Name: facturacion_id_factura_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.facturacion_id_factura_seq', 1, false);


--
-- TOC entry 3175 (class 2606 OID 16416)
-- Name: facturacion facturacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion
    ADD CONSTRAINT facturacion_pkey PRIMARY KEY (id_factura);


-- Completed on 2023-06-18 18:00:11

--
-- PostgreSQL database dump complete
--

