--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2024-02-25 18:34:18

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

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3580 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 877 (class 1247 OID 57348)
-- Name: categorytypeenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.categorytypeenum AS ENUM (
    'UPPER_BODY',
    'LOWER_BODY',
    'FULL_BODY',
    'ACCESSORIES',
    'FOOTWEAR',
    'OTHERS'
);


ALTER TYPE public.categorytypeenum OWNER TO postgres;

--
-- TOC entry 880 (class 1247 OID 57362)
-- Name: colorenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.colorenum AS ENUM (
    'RED',
    'BLUE',
    'GREEN',
    'YELLOW',
    'BLACK',
    'WHITE',
    'GREY',
    'PINK',
    'PURPLE',
    'BROWN',
    'ORANGE',
    'OTHERS'
);


ALTER TYPE public.colorenum OWNER TO postgres;

--
-- TOC entry 952 (class 1247 OID 57660)
-- Name: genderenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.genderenum AS ENUM (
    'MEN',
    'WOMEN'
);


ALTER TYPE public.genderenum OWNER TO postgres;

--
-- TOC entry 883 (class 1247 OID 57388)
-- Name: orderstatusenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.orderstatusenum AS ENUM (
    'PENDING',
    'CONFIRMED',
    'SHIPPING',
    'DELIVERED',
    'CANCELLED'
);


ALTER TYPE public.orderstatusenum OWNER TO postgres;

--
-- TOC entry 886 (class 1247 OID 57400)
-- Name: sizeenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.sizeenum AS ENUM (
    'S',
    'M',
    'L',
    'XL',
    'XXL',
    'XXXL'
);


ALTER TYPE public.sizeenum OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 57413)
-- Name: ai_configs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ai_configs (
    id integer NOT NULL,
    config_name character varying(255),
    string_value character varying(255),
    int_value integer,
    float_value double precision,
    description character varying(255),
    bool_value boolean
);


ALTER TABLE public.ai_configs OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 57418)
-- Name: ai_configs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ai_configs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ai_configs_id_seq OWNER TO postgres;

--
-- TOC entry 3581 (class 0 OID 0)
-- Dependencies: 215
-- Name: ai_configs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ai_configs_id_seq OWNED BY public.ai_configs.id;


--
-- TOC entry 216 (class 1259 OID 57419)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 57422)
-- Name: attribute_prediction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attribute_prediction (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.attribute_prediction OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 57425)
-- Name: attribute_prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attribute_prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attribute_prediction_id_seq OWNER TO postgres;

--
-- TOC entry 3582 (class 0 OID 0)
-- Dependencies: 218
-- Name: attribute_prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attribute_prediction_id_seq OWNED BY public.attribute_prediction.id;


--
-- TOC entry 219 (class 1259 OID 57426)
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    category_name character varying(255) NOT NULL,
    category_type public.categorytypeenum NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 57429)
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- TOC entry 3583 (class 0 OID 0)
-- Dependencies: 220
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- TOC entry 221 (class 1259 OID 57430)
-- Name: category_prediction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category_prediction (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    categorytypeenum public.categorytypeenum,
    gender public.genderenum DEFAULT 'MEN'::public.genderenum NOT NULL
);


ALTER TABLE public.category_prediction OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 57433)
-- Name: category_prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_prediction_id_seq OWNER TO postgres;

--
-- TOC entry 3584 (class 0 OID 0)
-- Dependencies: 222
-- Name: category_prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_prediction_id_seq OWNED BY public.category_prediction.id;


--
-- TOC entry 223 (class 1259 OID 57434)
-- Name: clothing_image_features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clothing_image_features (
    id integer NOT NULL,
    image_name character varying(255) NOT NULL,
    item_id character varying(100) NOT NULL,
    evaluation_status character varying(255) NOT NULL,
    landmark_visibility_1 integer DEFAULT 0,
    landmark_visibility_2 integer DEFAULT 0,
    landmark_visibility_3 integer DEFAULT 0,
    landmark_visibility_4 integer DEFAULT 0,
    landmark_visibility_5 integer DEFAULT 0,
    landmark_visibility_6 integer DEFAULT 0,
    landmark_visibility_7 integer DEFAULT 0,
    landmark_visibility_8 integer DEFAULT 0,
    landmark_location_x_1 double precision DEFAULT 0.0,
    landmark_location_x_2 double precision DEFAULT 0.0,
    landmark_location_x_3 double precision DEFAULT 0.0,
    landmark_location_x_4 double precision DEFAULT 0.0,
    landmark_location_x_5 double precision DEFAULT 0.0,
    landmark_location_x_6 double precision DEFAULT 0.0,
    landmark_location_x_7 double precision DEFAULT 0.0,
    landmark_location_x_8 double precision DEFAULT 0.0,
    landmark_location_y_1 double precision DEFAULT 0.0,
    landmark_location_y_2 double precision DEFAULT 0.0,
    landmark_location_y_3 double precision DEFAULT 0.0,
    landmark_location_y_4 double precision DEFAULT 0.0,
    landmark_location_y_5 double precision DEFAULT 0.0,
    landmark_location_y_6 double precision DEFAULT 0.0,
    landmark_location_y_7 double precision DEFAULT 0.0,
    landmark_location_y_8 double precision DEFAULT 0.0,
    attribute_labels character varying(255) NOT NULL,
    category_label character varying(255) NOT NULL,
    gender integer DEFAULT 0,
    box_top_left_x double precision,
    box_top_left_y double precision,
    box_bottom_right_x double precision,
    box_bottom_right_y double precision
);


ALTER TABLE public.clothing_image_features OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 57464)
-- Name: clothing_image_features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clothing_image_features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clothing_image_features_id_seq OWNER TO postgres;

--
-- TOC entry 3585 (class 0 OID 0)
-- Dependencies: 224
-- Name: clothing_image_features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clothing_image_features_id_seq OWNED BY public.clothing_image_features.id;


--
-- TOC entry 225 (class 1259 OID 57465)
-- Name: dictionaries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dictionaries (
    id integer NOT NULL,
    word character varying(255) NOT NULL,
    synonyms character varying[] NOT NULL
);


ALTER TABLE public.dictionaries OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 57470)
-- Name: dictionaries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dictionaries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dictionaries_id_seq OWNER TO postgres;

--
-- TOC entry 3586 (class 0 OID 0)
-- Dependencies: 226
-- Name: dictionaries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dictionaries_id_seq OWNED BY public.dictionaries.id;


--
-- TOC entry 227 (class 1259 OID 57471)
-- Name: fashion_net_models; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fashion_net_models (
    id integer NOT NULL,
    model_file character varying(255),
    batch_size integer,
    lr double precision,
    stage integer,
    epoch integer,
    attribute_loss double precision,
    blue_cates_loss double precision,
    blue_cates_top1 double precision,
    blue_cates_top2 double precision,
    blue_cates_top3 double precision,
    blue_cates_top5 double precision,
    blue_lands_loss double precision,
    concate_category_loss double precision,
    loss double precision,
    val_attribute_loss double precision,
    val_blue_cates_loss double precision,
    val_blue_cates_top1 double precision,
    val_blue_cates_top2 double precision,
    val_blue_cates_top3 double precision,
    val_blue_cates_top5 double precision,
    val_blue_lands_loss double precision,
    val_concate_category_loss double precision,
    val_loss double precision,
    created_at timestamp without time zone,
    test_accuracy double precision,
    blue_cates_acc double precision,
    blue_lands_acc double precision,
    red_green_cates_acc double precision,
    red_green_attrs_acc double precision
);


ALTER TABLE public.fashion_net_models OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 57474)
-- Name: fashion_net_models_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fashion_net_models_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fashion_net_models_id_seq OWNER TO postgres;

--
-- TOC entry 3587 (class 0 OID 0)
-- Dependencies: 228
-- Name: fashion_net_models_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fashion_net_models_id_seq OWNED BY public.fashion_net_models.id;


--
-- TOC entry 229 (class 1259 OID 57475)
-- Name: histories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.histories (
    id integer NOT NULL,
    "session_user" character varying(255) NOT NULL,
    user_say text NOT NULL,
    chat_response text NOT NULL,
    concepts text NOT NULL,
    message_type text NOT NULL
);


ALTER TABLE public.histories OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 57480)
-- Name: histories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.histories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.histories_id_seq OWNER TO postgres;

--
-- TOC entry 3588 (class 0 OID 0)
-- Dependencies: 230
-- Name: histories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.histories_id_seq OWNED BY public.histories.id;


--
-- TOC entry 254 (class 1259 OID 122881)
-- Name: history_nlus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.history_nlus (
    id integer NOT NULL,
    user_id character varying(255) NOT NULL,
    user_say text NOT NULL,
    intent character varying(255) NOT NULL,
    slots text NOT NULL
);


ALTER TABLE public.history_nlus OWNER TO postgres;

--
-- TOC entry 253 (class 1259 OID 122880)
-- Name: history_nlus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.history_nlus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.history_nlus_id_seq OWNER TO postgres;

--
-- TOC entry 3589 (class 0 OID 0)
-- Dependencies: 253
-- Name: history_nlus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.history_nlus_id_seq OWNED BY public.history_nlus.id;


--
-- TOC entry 231 (class 1259 OID 57481)
-- Name: intent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.intent (
    id integer NOT NULL,
    tag character varying(100) NOT NULL,
    description character varying(255)
);


ALTER TABLE public.intent OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 57484)
-- Name: intent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.intent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.intent_id_seq OWNER TO postgres;

--
-- TOC entry 3590 (class 0 OID 0)
-- Dependencies: 232
-- Name: intent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.intent_id_seq OWNED BY public.intent.id;


--
-- TOC entry 233 (class 1259 OID 57485)
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    id integer NOT NULL,
    order_date timestamp with time zone NOT NULL,
    customer_email character varying(255) NOT NULL,
    customer_phone character varying(255) NOT NULL,
    customer_address character varying(255) NOT NULL,
    total_price double precision,
    status public.orderstatusenum NOT NULL,
    fullname character varying(255) NOT NULL
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 57490)
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_id_seq OWNER TO postgres;

--
-- TOC entry 3591 (class 0 OID 0)
-- Dependencies: 234
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- TOC entry 235 (class 1259 OID 57491)
-- Name: order_product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_product (
    id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    order_size public.sizeenum,
    order_color public.colorenum
);


ALTER TABLE public.order_product OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 57494)
-- Name: order_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_product_id_seq OWNER TO postgres;

--
-- TOC entry 3592 (class 0 OID 0)
-- Dependencies: 236
-- Name: order_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_product_id_seq OWNED BY public.order_product.id;


--
-- TOC entry 237 (class 1259 OID 57495)
-- Name: pattern; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pattern (
    id integer NOT NULL,
    pattern_text character varying(255) NOT NULL,
    intent_id integer NOT NULL
);


ALTER TABLE public.pattern OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 57498)
-- Name: pattern_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pattern_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pattern_id_seq OWNER TO postgres;

--
-- TOC entry 3593 (class 0 OID 0)
-- Dependencies: 238
-- Name: pattern_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pattern_id_seq OWNED BY public.pattern.id;


--
-- TOC entry 239 (class 1259 OID 57499)
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    price integer NOT NULL,
    quantity integer NOT NULL,
    category_id integer NOT NULL,
    image_url character varying(255) NOT NULL,
    description character varying(255)
);


ALTER TABLE public.product OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 57504)
-- Name: product_attributes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_attributes (
    id integer NOT NULL,
    product_id integer NOT NULL,
    attribute_predict_id integer NOT NULL
);


ALTER TABLE public.product_attributes OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 57507)
-- Name: product_attributes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_attributes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_attributes_id_seq OWNER TO postgres;

--
-- TOC entry 3594 (class 0 OID 0)
-- Dependencies: 241
-- Name: product_attributes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_attributes_id_seq OWNED BY public.product_attributes.id;


--
-- TOC entry 242 (class 1259 OID 57508)
-- Name: product_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_categories (
    id integer NOT NULL,
    product_id integer NOT NULL,
    category_predict_id integer NOT NULL
);


ALTER TABLE public.product_categories OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 57511)
-- Name: product_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_categories_id_seq OWNER TO postgres;

--
-- TOC entry 3595 (class 0 OID 0)
-- Dependencies: 243
-- Name: product_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_categories_id_seq OWNED BY public.product_categories.id;


--
-- TOC entry 244 (class 1259 OID 57512)
-- Name: product_color_enum; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_color_enum (
    product_id integer NOT NULL,
    color public.colorenum NOT NULL
);


ALTER TABLE public.product_color_enum OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 57515)
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- TOC entry 3596 (class 0 OID 0)
-- Dependencies: 245
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- TOC entry 246 (class 1259 OID 57516)
-- Name: product_size_enum; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_size_enum (
    product_id integer NOT NULL,
    size public.sizeenum NOT NULL
);


ALTER TABLE public.product_size_enum OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 57519)
-- Name: product_tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_tag (
    id integer NOT NULL,
    product_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.product_tag OWNER TO postgres;

--
-- TOC entry 248 (class 1259 OID 57522)
-- Name: product_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_tag_id_seq OWNER TO postgres;

--
-- TOC entry 3597 (class 0 OID 0)
-- Dependencies: 248
-- Name: product_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_tag_id_seq OWNED BY public.product_tag.id;


--
-- TOC entry 249 (class 1259 OID 57523)
-- Name: response; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.response (
    id integer NOT NULL,
    response_text character varying(255) NOT NULL,
    intent_id integer NOT NULL
);


ALTER TABLE public.response OWNER TO postgres;

--
-- TOC entry 250 (class 1259 OID 57526)
-- Name: response_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.response_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.response_id_seq OWNER TO postgres;

--
-- TOC entry 3598 (class 0 OID 0)
-- Dependencies: 250
-- Name: response_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.response_id_seq OWNED BY public.response.id;


--
-- TOC entry 251 (class 1259 OID 57527)
-- Name: tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    tag_name character varying(255) NOT NULL
);


ALTER TABLE public.tag OWNER TO postgres;

--
-- TOC entry 252 (class 1259 OID 57530)
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO postgres;

--
-- TOC entry 3599 (class 0 OID 0)
-- Dependencies: 252
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- TOC entry 3290 (class 2604 OID 57531)
-- Name: ai_configs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ai_configs ALTER COLUMN id SET DEFAULT nextval('public.ai_configs_id_seq'::regclass);


--
-- TOC entry 3291 (class 2604 OID 57532)
-- Name: attribute_prediction id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_prediction ALTER COLUMN id SET DEFAULT nextval('public.attribute_prediction_id_seq'::regclass);


--
-- TOC entry 3292 (class 2604 OID 57533)
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- TOC entry 3293 (class 2604 OID 57534)
-- Name: category_prediction id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category_prediction ALTER COLUMN id SET DEFAULT nextval('public.category_prediction_id_seq'::regclass);


--
-- TOC entry 3295 (class 2604 OID 57535)
-- Name: clothing_image_features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clothing_image_features ALTER COLUMN id SET DEFAULT nextval('public.clothing_image_features_id_seq'::regclass);


--
-- TOC entry 3321 (class 2604 OID 57536)
-- Name: dictionaries id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dictionaries ALTER COLUMN id SET DEFAULT nextval('public.dictionaries_id_seq'::regclass);


--
-- TOC entry 3322 (class 2604 OID 57537)
-- Name: fashion_net_models id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fashion_net_models ALTER COLUMN id SET DEFAULT nextval('public.fashion_net_models_id_seq'::regclass);


--
-- TOC entry 3323 (class 2604 OID 57538)
-- Name: histories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.histories ALTER COLUMN id SET DEFAULT nextval('public.histories_id_seq'::regclass);


--
-- TOC entry 3334 (class 2604 OID 122884)
-- Name: history_nlus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_nlus ALTER COLUMN id SET DEFAULT nextval('public.history_nlus_id_seq'::regclass);


--
-- TOC entry 3324 (class 2604 OID 57539)
-- Name: intent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intent ALTER COLUMN id SET DEFAULT nextval('public.intent_id_seq'::regclass);


--
-- TOC entry 3325 (class 2604 OID 57540)
-- Name: order id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- TOC entry 3326 (class 2604 OID 57541)
-- Name: order_product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product ALTER COLUMN id SET DEFAULT nextval('public.order_product_id_seq'::regclass);


--
-- TOC entry 3327 (class 2604 OID 57542)
-- Name: pattern id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pattern ALTER COLUMN id SET DEFAULT nextval('public.pattern_id_seq'::regclass);


--
-- TOC entry 3328 (class 2604 OID 57543)
-- Name: product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- TOC entry 3329 (class 2604 OID 57544)
-- Name: product_attributes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_attributes ALTER COLUMN id SET DEFAULT nextval('public.product_attributes_id_seq'::regclass);


--
-- TOC entry 3330 (class 2604 OID 57545)
-- Name: product_categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_categories ALTER COLUMN id SET DEFAULT nextval('public.product_categories_id_seq'::regclass);


--
-- TOC entry 3331 (class 2604 OID 57546)
-- Name: product_tag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_tag ALTER COLUMN id SET DEFAULT nextval('public.product_tag_id_seq'::regclass);


--
-- TOC entry 3332 (class 2604 OID 57547)
-- Name: response id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.response ALTER COLUMN id SET DEFAULT nextval('public.response_id_seq'::regclass);


--
-- TOC entry 3333 (class 2604 OID 57548)
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- TOC entry 3534 (class 0 OID 57413)
-- Dependencies: 214
-- Data for Name: ai_configs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ai_configs (id, config_name, string_value, int_value, float_value, description, bool_value) FROM stdin;
1	cnn_model_name	ckpt_model.06-7.1912-1.3291.h5	\N	\N	\N	\N
2	min_match_percentage	\N	\N	0.85	\N	\N
\.


--
-- TOC entry 3536 (class 0 OID 57419)
-- Dependencies: 216
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;

\.


--
-- TOC entry 3537 (class 0 OID 57422)
-- Dependencies: 217
-- Data for Name: attribute_prediction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attribute_prediction (id, name) FROM stdin;
1	lightweight
2	polyester
3	woven
4	knit
5	cotton
6	unlined
7	rayon
8	spandex
9	top
10	print
11	pockets
12	dress
13	classic
14	lined
15	fit
16	round
17	love
18	elasticized
19	tee
20	trim
21	lining
22	sleeveless
23	buttoned
24	zipper
25	ribbed
26	sleek
27	floral
28	denim
29	shorts
30	graphic
31	black
32	forever
33	nylon
34	pocket
35	long-sleeved
36	cami
37	straps
38	fabrication
39	drawstring
40	bust
41	black-cream
42	shoulder
43	skirt
44	fly
45	pattern
46	jeans
47	contrast
48	little
49	point
50	basic
51	makes
52	chic
53	neck
54	patch
55	cool
56	zip
57	acrylic
58	comfort
59	cream
60	lace
61	casual
62	relaxed
63	fabric
64	shirt
65	black-white
66	comfy
67	short-sleeved
68	v-neckline
69	design
70	touch
71	soft
72	pretty
73	adjustable
74	simple
75	tank
76	keyhole
77	semi-sheer
78	self-tie
79	faux
80	boxy
81	wardrobe
82	crochet
83	stripes
84	sweater
85	leather
86	warm
87	crop
88	effortless
89	closet
90	staple
91	cardigan
92	abstract
93	button
94	flirty
95	laid-back
96	jacket
97	button-down
98	cozy
99	heathered
100	essential
101	five-pocket
102	tailored
103	chiffon
104	comfortable
105	down
106	striped
107	breezy
108	great
109	every
110	want
111	pieces
112	sheer
113	longline
114	polished
115	vibe
116	embroidery
117	exposed
118	maxi
119	pants
120	cropped
121	cuffs
122	cutoffs
123	midweight
124	textured
125	eye-catching
126	appeal
127	linen
128	skinny
129	subtle
130	scoop
131	viscose
132	flattering
133	flat
134	high-waisted
135	modal
136	closure
137	cutout
138	dropped
139	off-duty
140	summer
141	invisible
142	throw
143	cuffed
144	outfit
145	bold
146	delicate
147	sweet
148	blouse
149	slant
150	feminine
151	zippered
152	shoulders
153	crisp
154	modern
155	joggers
156	femme
157	mesh
158	everyday
159	distressed
160	trousers
161	slim
162	oversized
163	sandals
164	heather grey
165	muscle
166	romper
167	slip
168	marled
169	stretch
170	airy
171	crepe
172	white
173	belt
174	printed
175	sultry
176	versatile
177	boho
178	panels
179	need
180	welt
181	heels
182	open-front
183	skirts
184	beach
185	plaid
186	pleated
187	warm-weather
188	leggings
189	cute
190	traditional
191	skater
192	slit
193	sporty
194	vented
195	bodice
196	refined
197	embroidered
198	hood
199	light
200	pencil
201	placket
202	burgundy
203	tribal
204	sweatshirt
205	flap
206	slits
207	slub
208	spaghetti
209	stylish
210	blazer
211	raglan
212	topper
213	armholes
214	halter
215	timeless
216	basics
217	drapey
218	skin
219	addition
220	elegant
221	rose
222	bodycon
223	overlay
224	super-soft
225	blend
226	bottoms
227	elevated
228	structured
229	tees
230	scalloped
231	smocked
232	boyfriend
233	covered
234	vintage
235	billowy
236	flowy
237	worn
238	dolman
239	fresh
240	olive
241	peasant
242	throughout
243	vibes
244	vibrant
245	dressed
246	office
247	racerback
248	sunny
249	booties
250	layered
251	navy
252	strappy
253	tops
254	notched
255	edgy
256	sharp
257	flare
258	chambray
259	necklace
260	raw-cut
261	slouchy
262	curved
263	jumpsuit
264	polyurethane
265	split
266	girl
267	ornate
268	cream-navy
269	loose
270	on-seam
271	mix
272	polish
273	standout
274	moto
275	paired
276	a-line
277	panel
278	stretch-knit
279	free-spirited
280	light denim
281	bright
282	blush
283	hoodie
284	surplice
285	flair
286	mini
287	romantic
288	dresses
289	ensemble
290	stand
291	fall
292	sophisticated
293	luxe
294	wool
295	fringe
296	lyocell
297	metallic
298	sartorial
299	tumble
300	colorblocked
301	paisley
302	stripe
303	blue-cream
304	ethereal
305	festival
306	intricate
307	match
308	streamlined
309	wide
310	sweatpants
311	tonal
312	call
313	street
314	swingy
315	fitted
316	stretchy
317	boots
318	line
319	navy-white
320	taupe
321	cap
322	pop
323	vintage-inspired
324	flared
325	aesthetic
326	geo
327	complement
328	crisscross
329	denim washed
330	dot
331	mixed
332	pleats
333	rust
334	strapless
335	bralette
336	shawl
337	staples
338	chunky
339	draped
340	rock
341	sweetheart
342	black-heather grey
343	black-red
344	blue-white
345	crinkled
346	running
347	serious
348	sneakers
349	tailoring
350	tasseled
351	versatility
352	balance
353	vest
354	accessories
355	brunch
356	girly
357	open-knit
358	polka
359	gauze
360	grey
361	southwestern
362	cutouts
363	round neckline
364	long sleeve
365	fully lined
366	short sleeve
367	elasticized waist
368	front pocket
369	back zipper
370	partially lined
371	zip fly
372	patch pocket
373	ribbed trim
374	drawstring waist
375	crop top
376	crew neck
377	basic collar
378	3/4 sleeve
379	keyhole back
380	open front
381	faux leather
382	buttoned keyhole
383	side zipper
384	buttoned front
385	chest patch
386	elasticized drawstring
387	exposed back
388	chest pocket
389	muscle tee
390	relaxed fit
391	skinny jean
392	floral lace
393	maxi dress
394	scoop neckline
395	adjustable strap
396	french terry
397	welt pocket
398	slant pocket
399	woven fabric
400	pencil skirt
401	spaghetti strap
402	slub knit
403	ribbed knit
404	sleeveless top
405	cami strap
406	knit fabrication
407	short-sleeved tee
408	crew neckline
409	longline silhouette
410	button-down front
411	side slit
412	sleeveless dress
413	stretch knit
414	medium weight
415	heathered knit
416	marled knit
417	back pocket
418	boyfriend jean
419	denim short
420	buttoned cuff
421	front slant
422	raglan sleeve
423	zippered front
424	pretty much
425	cutout back
426	front patch
427	woven fabrication
428	skater skirt
429	night out
430	adjustable cami
431	contrast trim
432	peasant top
433	striped pattern
434	adjustable spaghetti
435	dolman sleeve
436	moto jacket
437	back patch
438	stand out
439	boxy fit
440	classic detail
441	knit fabric
442	cap sleeve
443	flap pocket
444	boxy silhouette
445	kangaroo pocket
446	vented side
447	polka dot
448	slim fit
449	high point shoulder
450	slanted front pocket
451	elasticized drawstring waist
452	chest patch pocket
453	exposed back zipper
454	buttoned keyhole back
455	concealed back zipper
456	invisible back zipper
457	concealed side zipper
458	front slant pocket
459	front patch pocket
460	adjustable cami strap
461	adjustable spaghetti strap
462	back patch pocket
463	invisible side zipper
\.


--
-- TOC entry 3539 (class 0 OID 57426)
-- Dependencies: 219
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, category_name, category_type) FROM stdin;
1	Anorak	UPPER_BODY
2	Blazer	UPPER_BODY
3	Blouse	UPPER_BODY
4	Bomber	UPPER_BODY
5	Button-Down	UPPER_BODY
6	Cardigan	UPPER_BODY
7	Flannel	UPPER_BODY
8	Halter	UPPER_BODY
9	Henley	UPPER_BODY
10	Hoodie	UPPER_BODY
11	Jacket	UPPER_BODY
12	Jersey	UPPER_BODY
13	Parka	UPPER_BODY
14	Peacoat	UPPER_BODY
15	Poncho	UPPER_BODY
16	Sweater	UPPER_BODY
17	Tank	UPPER_BODY
18	Tee	UPPER_BODY
19	Top	UPPER_BODY
20	Turtleneck	UPPER_BODY
21	Capris	LOWER_BODY
22	Chinos	LOWER_BODY
23	Culottes	LOWER_BODY
24	Cutoffs	LOWER_BODY
25	Gauchos	LOWER_BODY
26	Jeans	LOWER_BODY
27	Jeggings	LOWER_BODY
28	Jodhpurs	LOWER_BODY
29	Joggers	LOWER_BODY
30	Leggings	LOWER_BODY
31	Sarong	LOWER_BODY
32	Shorts	LOWER_BODY
33	Skirt	LOWER_BODY
34	Sweatpants	LOWER_BODY
35	Sweatshorts	LOWER_BODY
36	Trunks	LOWER_BODY
37	Caftan	FULL_BODY
38	Cape	FULL_BODY
39	Coat	FULL_BODY
40	Coverup	FULL_BODY
41	Dress	FULL_BODY
42	Jumpsuit	FULL_BODY
43	Kaftan	FULL_BODY
44	Kimono	FULL_BODY
45	Nightdress	FULL_BODY
46	Onesie	FULL_BODY
47	Robe	FULL_BODY
48	Romper	FULL_BODY
49	Shirtdress	FULL_BODY
50	Sundress	FULL_BODY
\.


--
-- TOC entry 3541 (class 0 OID 57430)
-- Dependencies: 221
-- Data for Name: category_prediction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category_prediction (id, name, categorytypeenum, gender) FROM stdin;
23	Turtleneck	\N	MEN
1	Denim	\N	MEN
2	Pants	\N	MEN
3	Shorts	\N	MEN
4	Sweaters	\N	MEN
5	Tees_Tanks	\N	MEN
6	Jackets_Vests	\N	MEN
7	Shirts_Polos	\N	MEN
8	Suiting	\N	MEN
9	Sweatshirts_Hoodies	\N	MEN
10	Blouses_Shirts	\N	MEN
11	Dresses	\N	MEN
12	Leggings	\N	MEN
13	Cardigans	\N	MEN
14	Graphic_Tees	\N	MEN
15	Skirts	\N	MEN
16	Jackets_Coats	\N	MEN
17	Rompers_Jumpsuits	\N	MEN
18	Sundress	\N	MEN
19	Romper	\N	MEN
20	Bomber	\N	MEN
21	Cape	\N	MEN
22	Parka	\N	MEN
\.


--
-- TOC entry 3543 (class 0 OID 57434)
-- Dependencies: 223
-- Data for Name: clothing_image_features; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clothing_image_features (id, image_name, item_id, evaluation_status, landmark_visibility_1, landmark_visibility_2, landmark_visibility_3, landmark_visibility_4, landmark_visibility_5, landmark_visibility_6, landmark_visibility_7, landmark_visibility_8, landmark_location_x_1, landmark_location_x_2, landmark_location_x_3, landmark_location_x_4, landmark_location_x_5, landmark_location_x_6, landmark_location_x_7, landmark_location_x_8, landmark_location_y_1, landmark_location_y_2, landmark_location_y_3, landmark_location_y_4, landmark_location_y_5, landmark_location_y_6, landmark_location_y_7, landmark_location_y_8, attribute_labels, category_label, gender, box_top_left_x, box_top_left_y, box_bottom_right_x, box_bottom_right_y) FROM stdin;
\.


--
-- TOC entry 3545 (class 0 OID 57465)
-- Dependencies: 225
-- Data for Name: dictionaries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dictionaries (id, word, synonyms) FROM stdin;
6	Anorak	{"mũ trùm đầu","mũ trùm","mũ trùm kín","mũ trùm kín đầu","mũ che đầu","mũ chụp đầu","mũ đội đầu","mũ đeo đầu","mũ lưỡi trai","mũ bucket","mũ fedora","mũ rộng vònh"}
7	Blouse	{"áo lót","áo trong","áo ngực","áo nút ngực","áo nút vú"}
8	Cardigan	{"áo khoác len","áo len","áo len chui đầu","áo len có nón","áo len mũng","áo len dày","áo len dài tay","áo len ngắn tay","áo len cổ lọ","áo len cổ tim","áo len vằn thẳng"}
9	Flannel	{"nỉ lót","nỉ lông","nỉ bông","nỉ mềm","nỉ ấm","nỉ dày","nỉ mịn","nỉ co giãn","nỉ không co giãn"}
10	Halter	{"áo hở vai","áo hai dây","áo tank top","áo bra top","áo crop top","áo halter top","áo chéo vai","áo ba lỗ","áo hở lưng","áo yếm"}
11	Henley	{"áo thun cổ lọ","áo thun cổ lọ tròn","áo thun cổ lọ thuyền","áo thun cổ lọ có cổ","áo thun cổ lọ tròn có cổ","áo thun cổ lọ thuyền có cổ"}
12	Hoodie	{"Áo nỉ","Áo có mũ trùm đầu","Áo len","áo len","Áo gió","Ao gió"}
14	Jersey	{"áo cổ lọ","áo phông","áo thun có cổ","áo cánh"}
15	Parka	{"áo khoác ngoài","áo khoác lau bụi","áo khoác dã ngoại","áo khoác thám hiểm","áo khoác lót lông","áo khoác cách nhiệt","áo lạnh"}
16	Peacoat	{"áo khoác vải thô","áo khoác hải quân","áo khoác thủy thủ","áo khoác đồng hồ"}
17	Poncho	{"áo mưa","áo choàng"}
18	Sweater	{"áo len chui đầu","áo len liền quần","áo cổ lọ","áo len cao cổ","áo nỉ"}
19	Tank	{"áo sơ mi","áo vest","áo sơ mi không tay","áo sơ mi tay ngắn","áo cơ bắp","áo ngực thể thao"}
20	Tee	{"áo phông","áo thun","áo thun có cổ","áo ba lỗ","áo sơ mi không tay","áo sơ mi","áo nỉ","áo đầu"}
21	Top	{"áo cánh","áo sơ mi","áo khoác","áo len đan","quần áo ba lỗ","áo ba lỗ"}
22	Leggings	{"quần bó","quần yoga","quần thun","quần capri","quần xe đạp","quần bó sát chân","quần legging capris","quần legging","váy legging"}
23	Turtleneck	{"áo len cổ cao","áo len cổ cuộn","áo len cổ polo","áo len cao cổ","áo cổ lọ","áo sơ mi cao cổ","áo cao cổ giả","áo cổ cuộn","áo cổ tròn","áo sơ mi henley","áo len cổ giả"}
24	Capris	{"quần cắt","quần ba phần tự","quần lót","quần thủy thủ","quần thuốc lá","quần ôm sát chân"}
25	Chinos	{"quần kaki","quần dockers","quần yếm","quần vải thô","quần vải chéo","quần vải tơ sợi","quần dài","quần lửng","quần tây thường","quần ẩu"}
26	Culottes	{"quần ông túm","quần áo đầy bản đạp","quần áo lót","quần váy","quần áo nửa váy","quần palazzo","quần culotte"}
27	Cutoffs	{"quần short","quần short bermuda","quần jean cắt","quần cắt","quần nóng","quần ngắn","quần short ngắn","quần ba phần tự"}
28	Gauchos	{"áo choàng","mũ rộng vành"}
29	Jeans	{"quần jean",levis,"quần jean xanh","quần jean đá","quần jean rách","quần jean đau khổ","quần jean ôm loe","quần jean mềm","quần jean bạn trai"}
30	Jeggings	{"quần jean co giãn","quần jean","quần legging jean","quần co giãn","quần cầu lông","quần jegging","quần jegging gầy"}
31	Jodhpurs	{"quần ông túm","quần cưỡi ngựa","quần jodhpuri","quần cưỡi ngựa","quần kỹ binh","quần short jodhpuri","quần short cưỡi ngựa","quần da bê"}
32	Joggers	{"quần thể thao","quần chạy bộ","quần dài","quần xích đạo","quần mỏ hôi"}
34	Sarong	{"váy mã lai","váy quần","váy xà rông","váy dài","xà rông bãi biển"}
35	Shorts	{"quần short bermuda","quần lót ống rộng","quần short tập gym","quần nóng","quần lót","quần short","quần bơi"}
37	Sweatpants	{"quần chạy bộ","quần thể thao","quần nỉ","quần tập thể dục","quần dài","quần vừa vặn thoải mái","quần lưng thun"}
38	Sweatshorts	{"quần short tập gym","quần chạy bộ","quần thể thao","quần dài","quần pyjama","quần short thường ngày","quần short thoải mái"}
39	Trunks	{"quần bơi","đồ tắm",bikini,"quần short","quần short bermuda","quần short jamaica","quần short lượt sóng"}
40	Caftan	{"áo choàng",kimono,"xà rông"}
13	Jacket	{"Áo choàng","Áo len đan","Áo khoác lau bụi","Áo khoác dài","Áo khoác"}
48	GREEN	{"mau xanh la","xanh la cay","mau la cay"}
47	BLUE	{"mau xanh","mau da troi","xanh da troi","mau da troi"}
51	BROWN	{"mau nau","da nau"}
41	PURPLE	{"màu tím","tim sen"}
42	WHITE	{"mau trang","trang duc"}
43	YELLOW	{"mau vang","da vang"}
44	ORANGE	{"mau cam","mau da cam","da cam"}
49	RED	{"mau do","mau đo"}
50	BLACK	{"mau den","mau đen"}
46	GREY	{"mau xam","mau sam"}
45	PINK	{"mau hong"}
36	Skirt	{váy,"váy lót","áo choàng",đầm,"xà rông","yếm dài trẻ con","áo dài","quần quanh","váy maxi","váy màu"}
\.


--
-- TOC entry 3547 (class 0 OID 57471)
-- Dependencies: 227
-- Data for Name: fashion_net_models; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fashion_net_models (id, model_file, batch_size, lr, stage, epoch, attribute_loss, blue_cates_loss, blue_cates_top1, blue_cates_top2, blue_cates_top3, blue_cates_top5, blue_lands_loss, concate_category_loss, loss, val_attribute_loss, val_blue_cates_loss, val_blue_cates_top1, val_blue_cates_top2, val_blue_cates_top3, val_blue_cates_top5, val_blue_lands_loss, val_concate_category_loss, val_loss, created_at, test_accuracy, blue_cates_acc, blue_lands_acc, red_green_cates_acc, red_green_attrs_acc) FROM stdin;
4	ckpt_model.05-6.0860-1.0666.h5	64	0.0003	1	5	4.459405899047852	0.8935626149177551	0.2934163510799408	0.4858759343624115	0.6169033050537109	0.7856708765029907	5.426295280456543	0.6080940961837769	6.826608180999756	4.4711503982543945	1.066557765007019	0.40461185574531555	0.6338896155357361	0.7539644241333008	0.884841799736023	4.474458694458008	0.9788269400596619	6.086013317108154	2023-10-01 09:54:51.056573	\N	\N	\N	\N	\N
5	ckpt_model.06-7.1912-1.3291.h5	54	0.0003	1	5	4.393494606018066	0.9351233839988708	0.29148000478744507	0.49138128757476807	0.6290150880813599	0.7957703471183777	5.481119632720947	0.5251420736312866	6.9080986976623535	4.517523765563965	1.3291352987289429	0.31119728088378906	0.5181081891059875	0.6239872574806213	0.7730073928833008	5.31638765335083	0.938864529132843	7.191159248352051	2023-10-01 09:54:51.056573	\N	\N	\N	\N	\N
1	ckpt_model.01-6.8683-1.1238.h5	64	0.0003	1	0	11.975455284118652	1.2736766338348389	0.15008732676506042	0.2718505561351776	0.3745538890361786	0.5348545908927917	7.03001594543457	1.072117805480957	9.608450889587402	4.782472610473633	1.1237858533859253	0.28017449378967285	0.4733744263648987	0.6043902635574341	0.7739768624305725	5.165818214416504	1.0047944784164429	6.868325233459473	2023-10-01 09:54:51.056573	0.2866	0	0.1033	0.0435	0.9998
2	ckpt_model.02-6.3518-1.0271.h5	64	0.0003	1	1	4.758098602294922	1.0239932537078857	0.25096818804740906	0.42417800426483154	0.5458652973175049	0.7141392827033997	5.9656877517700195	0.8569537401199341	7.551190376281738	4.664026260375977	1.027093768119812	0.382868230342865	0.6044595241546631	0.7160168886184692	0.8621286749839783	4.760622024536133	0.9770946502685547	6.351831436157227	2023-10-01 09:54:51.056573	0.2841	0	0.093	0.0435	0.9998
3	ckpt_model.04-6.1616-1.0569.h5	64	0.0003	1	3	4.5156331062316895	0.9780272245407104	0.26843345165252686	0.45276787877082825	0.582504391670227	0.7509301900863647	5.587883949279785	0.6047686338424683	7.077954292297363	4.489806652069092	1.0568585395812988	0.25669968128204346	0.4543314278125763	0.5816771984100342	0.7619278430938721	4.557888031005859	0.9783905744552612	6.161563873291016	2023-10-01 09:54:51.056573	0.287	0	0.1052	0.0435	0.9993
\.


--
-- TOC entry 3549 (class 0 OID 57475)
-- Dependencies: 229
-- Data for Name: histories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.histories (id, "session_user", user_say, chat_response, concepts, message_type) FROM stdin;
\.


--
-- TOC entry 3574 (class 0 OID 122881)
-- Dependencies: 254
-- Data for Name: history_nlus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.history_nlus (id, user_id, user_say, intent, slots) FROM stdin;
315	e7216345-63cb-494f-98f4-8b6bb33b1234	Cho tôi một cái áo khoác	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
316	e7216345-63cb-494f-98f4-8b6bb33b1234	Cho tôi một cái áo khoác	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
317	e7216345-63cb-494f-98f4-8b6bb33b5678	Cho xem màu xanh đi	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": null, "price_from": null, "price_to": null}
318	e7216345-63cb-494f-98f4-8b6bb33b5678	Cho xem màu xanh đi	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": null, "price_from": null, "price_to": null}
319	e7216345-63cb-494f-98f4-8b6bb33b1122	có size M không á	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
320	e7216345-63cb-494f-98f4-8b6bb33b1122	có size M không á	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
321	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
322	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
323	e7216345-63cb-494f-98f4-8b6bb33b3322	Cho tôi một chiếc quần jeans	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
324	e7216345-63cb-494f-98f4-8b6bb33b3322	Cho tôi một chiếc quần jeans	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
325	e7216345-63cb-494f-98f4-8b6bb33b4433	Hãy cho tôi xem màu đen	request_color	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": null, "price_to": null}
326	e7216345-63cb-494f-98f4-8b6bb33b4433	Hãy cho tôi xem màu đen	request_color	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": null, "price_to": null}
327	e7216345-63cb-494f-98f4-8b6bb33b5511	Bạn có size L không?	request_size	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": null, "price_to": null}
328	e7216345-63cb-494f-98f4-8b6bb33b5511	Bạn có size L không?	request_size	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": null, "price_to": null}
329	e7216345-63cb-494f-98f4-8b6bb33b1144	Tôi muốn một chiếc áo polo	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": null, "price_to": null}
330	e7216345-63cb-494f-98f4-8b6bb33b1144	Tôi muốn một chiếc áo polo	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": null, "price_to": null}
331	e7216345-63cb-494f-98f4-8b6bb33b4455	Cho tôi thấy màu hồng	request_color	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size L", "price_from": null, "price_to": null}
332	e7216345-63cb-494f-98f4-8b6bb33b4455	Cho tôi thấy màu hồng	request_color	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size L", "price_from": null, "price_to": null}
333	e7216345-63cb-494f-98f4-8b6bb33b3355	Có size S không ạ?	request_size	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": null, "price_to": null}
334	e7216345-63cb-494f-98f4-8b6bb33b3355	Có size S không ạ?	request_size	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": null, "price_to": null}
335	e7216345-63cb-494f-98f4-8b6bb33b1199	Tôi cần một chiếc áo len ấm áp	buy_fashion	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": null, "price_to": null}
336	e7216345-63cb-494f-98f4-8b6bb33b1199	Tôi cần một chiếc áo len ấm áp	buy_fashion	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": null, "price_to": null}
337	e7216345-63cb-494f-98f4-8b6bb33b1166	Cần tìm áo sơ mi màu trắng	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size S", "price_from": null, "price_to": null}
338	e7216345-63cb-494f-98f4-8b6bb33b1166	Cần tìm áo sơ mi màu trắng	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size S", "price_from": null, "price_to": null}
339	e7216345-63cb-494f-98f4-8b6bb33b1212	Xem mẫu áo phông màu đen đi	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
340	e7216345-63cb-494f-98f4-8b6bb33b1212	Xem mẫu áo phông màu đen đi	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
341	e7216345-63cb-494f-98f4-8b6bb33b1313	Có size XL không ạ?	request_size	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
342	e7216345-63cb-494f-98f4-8b6bb33b1313	Có size XL không ạ?	request_size	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
494		xin chào	greeting	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
343	e7216345-63cb-494f-98f4-8b6bb33b1414	Mình muốn một chiếc váy ngắn	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
344	e7216345-63cb-494f-98f4-8b6bb33b1414	Mình muốn một chiếc váy ngắn	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
345	e7216345-63cb-494f-98f4-8b6bb33b1515	Tôi muốn xem màu vàng	request_color	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XL", "price_from": null, "price_to": null}
346	e7216345-63cb-494f-98f4-8b6bb33b1515	Tôi muốn xem màu vàng	request_color	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XL", "price_from": null, "price_to": null}
347	e7216345-63cb-494f-98f4-8b6bb33b2121	Có size XS không shop?	request_size	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": null, "price_to": null}
348	e7216345-63cb-494f-98f4-8b6bb33b2121	Có size XS không shop?	request_size	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": null, "price_to": null}
349	e7216345-63cb-494f-98f4-8b6bb33b3131	Tôi đang tìm áo khoác phong cách thể thao	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": null, "price_to": null}
350	e7216345-63cb-494f-98f4-8b6bb33b3131	Tôi đang tìm áo khoác phong cách thể thao	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": null, "price_to": null}
351	e7216345-63cb-494f-98f4-8b6bb33b4242	Có màu đỏ không ạ?	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XS", "price_from": null, "price_to": null}
352	e7216345-63cb-494f-98f4-8b6bb33b4242	Có màu đỏ không ạ?	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XS", "price_from": null, "price_to": null}
353	e7216345-63cb-494f-98f4-8b6bb33b5353	Tôi cần size XL	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XL", "price_from": null, "price_to": null}
354	e7216345-63cb-494f-98f4-8b6bb33b5353	Tôi cần size XL	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XL", "price_from": null, "price_to": null}
355	e7216345-63cb-494f-98f4-8b6bb33b6464	Cho xem áo hoodie màu đen được không?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
356	e7216345-63cb-494f-98f4-8b6bb33b6464	Cho xem áo hoodie màu đen được không?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": null, "price_to": null}
357	e7216345-63cb-494f-98f4-8b6bb33b7575	Giá từ 500000 đến 1000000 đồng được không ạ?	request_price	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
358	e7216345-63cb-494f-98f4-8b6bb33b7575	Giá từ 500000 đến 1000000 đồng được không ạ?	request_price	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
359	e7216345-63cb-494f-98f4-8b6bb33b8686	Cần một chiếc áo khoác phong cách retro	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
360	e7216345-63cb-494f-98f4-8b6bb33b8686	Cần một chiếc áo khoác phong cách retro	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
361	e7216345-63cb-494f-98f4-8b6bb33b9799	Mình thích màu nâu	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
362	e7216345-63cb-494f-98f4-8b6bb33b9799	Mình thích màu nâu	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
363	e7216345-63cb-494f-98f4-8b6bb33b1088	Có size L không shop?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
364	e7216345-63cb-494f-98f4-8b6bb33b1088	Có size L không shop?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
365	e7216345-63cb-494f-98f4-8b6bb33b1199	Tôi muốn mua một chiếc áo len cổ lọ	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
366	e7216345-63cb-494f-98f4-8b6bb33b1199	Tôi muốn mua một chiếc áo len cổ lọ	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
367	e7216345-63cb-494f-98f4-8b6bb33b2200	Xem màu xám nhé	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
368	e7216345-63cb-494f-98f4-8b6bb33b2200	Xem màu xám nhé	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
369	e7216345-63cb-494f-98f4-8b6bb33b3311	Có size M không ạ?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
370	e7216345-63cb-494f-98f4-8b6bb33b3311	Có size M không ạ?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
371	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
372	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
373	e7216345-63cb-494f-98f4-8b6bb33b2222	Cho tôi xem màu đỏ của chiếc áo sơ mi	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
374	e7216345-63cb-494f-98f4-8b6bb33b2222	Cho tôi xem màu đỏ của chiếc áo sơ mi	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
375	e7216345-63cb-494f-98f4-8b6bb33b3333	Có size XS cho áo polo màu đen không?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
376	e7216345-63cb-494f-98f4-8b6bb33b3333	Có size XS cho áo polo màu đen không?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
377	e7216345-63cb-494f-98f4-8b6bb33b4444	Tôi muốn một chiếc quần jogger màu xanh	buy_fashion	{"clothing": "qu\\u1ea7n jogger", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
378	e7216345-63cb-494f-98f4-8b6bb33b4444	Tôi muốn một chiếc quần jogger màu xanh	buy_fashion	{"clothing": "qu\\u1ea7n jogger", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
379	e7216345-63cb-494f-98f4-8b6bb33b5555	Cho xem chiếc áo thun phong cách retro đi	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
446	e7216345-63cb-494f-98f4-8b6bb33b9994	Tôi muốn mua chiếc váy dài màu đen	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
447	e7216345-63cb-494f-98f4-8b6bb33b9995	Cho tôi xem áo len màu vàng	buy_fashion	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
448	e7216345-63cb-494f-98f4-8b6bb33b9995	Cho tôi xem áo len màu vàng	buy_fashion	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
449	e7216345-63cb-494f-98f4-8b6bb33b2121	Có size XS không shop?	request_size	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
450	e7216345-63cb-494f-98f4-8b6bb33b2121	Có size XS không shop?	request_size	{"clothing": "\\u00e1o len", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
451	e7216345-63cb-494f-98f4-8b6bb33b9997	Tôi muốn mua áo khoác phong cách casual	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
452	e7216345-63cb-494f-98f4-8b6bb33b9997	Tôi muốn mua áo khoác phong cách casual	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
453	e7216345-63cb-494f-98f4-8b6bb33b9998	Cho xem áo hoodie màu xanh được không?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
454	e7216345-63cb-494f-98f4-8b6bb33b9998	Cho xem áo hoodie màu xanh được không?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
455	e7216345-63cb-494f-98f4-8b6bb33b9999	Giá từ 300000 đến 500000 đồng được không ạ?	request_price	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
456	e7216345-63cb-494f-98f4-8b6bb33b9999	Giá từ 300000 đến 500000 đồng được không ạ?	request_price	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
457	e7216345-63cb-494f-98f4-8b6bb33b1000	Cần một chiếc áo khoác phong cách vintage	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
458	e7216345-63cb-494f-98f4-8b6bb33b1000	Cần một chiếc áo khoác phong cách vintage	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
495		xin chào	greeting	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
380	e7216345-63cb-494f-98f4-8b6bb33b5555	Cho xem chiếc áo thun phong cách retro đi	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
381	e7216345-63cb-494f-98f4-8b6bb33b6666	Màu hồng phấn của chiếc váy ngắn này thế nào?	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "M\\u00e0u h\\u1ed3ng ph\\u1ea5n", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
382	e7216345-63cb-494f-98f4-8b6bb33b6666	Màu hồng phấn của chiếc váy ngắn này thế nào?	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "M\\u00e0u h\\u1ed3ng ph\\u1ea5n", "size_clothing": "size XS", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
383	e7216345-63cb-494f-98f4-8b6bb33b7777	Có size M không cho áo hoodie màu đen?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
384	e7216345-63cb-494f-98f4-8b6bb33b7777	Có size M không cho áo hoodie màu đen?	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
385	e7216345-63cb-494f-98f4-8b6bb33b8888	Tôi muốn một chiếc áo khoác da màu nâu	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
386	e7216345-63cb-494f-98f4-8b6bb33b8888	Tôi muốn một chiếc áo khoác da màu nâu	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
387	e7216345-63cb-494f-98f4-8b6bb33b9999	Hãy cho tôi xem mẫu áo sơ mi màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
388	e7216345-63cb-494f-98f4-8b6bb33b9999	Hãy cho tôi xem mẫu áo sơ mi màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
389	e7216345-63cb-494f-98f4-8b6bb33b1022	Có size L không cho chiếc áo phông màu đen?	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
390	e7216345-63cb-494f-98f4-8b6bb33b1022	Có size L không cho chiếc áo phông màu đen?	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
391	e7216345-63cb-494f-98f4-8b6bb33b1133	Tôi muốn một chiếc quần jeans màu xám	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
392	e7216345-63cb-494f-98f4-8b6bb33b1133	Tôi muốn một chiếc quần jeans màu xám	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
393	e7216345-63cb-494f-98f4-8b6bb33b1244	Cho tôi xem chiếc áo hoodie phong cách thể thao đi	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
394	e7216345-63cb-494f-98f4-8b6bb33b1244	Cho tôi xem chiếc áo hoodie phong cách thể thao đi	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u x\\u00e1m", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
395	e7216345-63cb-494f-98f4-8b6bb33b2355	Có màu trắng không cho chiếc áo thun?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
396	e7216345-63cb-494f-98f4-8b6bb33b2355	Có màu trắng không cho chiếc áo thun?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size L", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
397	e7216345-63cb-494f-98f4-8b6bb33b3466	Có size XL không cho chiếc áo sơ mi màu đỏ?	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
398	e7216345-63cb-494f-98f4-8b6bb33b3466	Có size XL không cho chiếc áo sơ mi màu đỏ?	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
399	e7216345-63cb-494f-98f4-8b6bb33b4577	Tôi muốn mua chiếc áo len cổ lọ màu nâu	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
400	e7216345-63cb-494f-98f4-8b6bb33b4577	Tôi muốn mua chiếc áo len cổ lọ màu nâu	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
401	e7216345-63cb-494f-98f4-8b6bb33b5688	Hãy cho tôi xem mẫu váy ngắn màu đen đi	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
402	e7216345-63cb-494f-98f4-8b6bb33b5688	Hãy cho tôi xem mẫu váy ngắn màu đen đi	buy_fashion	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
403	e7216345-63cb-494f-98f4-8b6bb33b6799	Có màu vàng cho chiếc áo thun không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
404	e7216345-63cb-494f-98f4-8b6bb33b6799	Có màu vàng cho chiếc áo thun không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size XL", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
405	e7216345-63cb-494f-98f4-8b6bb33b7800	Có size S không cho chiếc áo polo màu đen?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
406	e7216345-63cb-494f-98f4-8b6bb33b7800	Có size S không cho chiếc áo polo màu đen?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
407	e7216345-63cb-494f-98f4-8b6bb33b8911	Giá từ 1000000 đến 2000000 đồng cho áo khoác màu đen được không?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
408	e7216345-63cb-494f-98f4-8b6bb33b8911	Giá từ 1000000 đến 2000000 đồng cho áo khoác màu đen được không?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
409	e7216345-63cb-494f-98f4-8b6bb33b9022	Cần tìm áo sơ mi màu xanh dương	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh d\\u01b0\\u01a1ng", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
410	e7216345-63cb-494f-98f4-8b6bb33b9022	Cần tìm áo sơ mi màu xanh dương	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh d\\u01b0\\u01a1ng", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
411	e7216345-63cb-494f-98f4-8b6bb33b1993	Cho tôi xem mẫu áo phông màu trắng đi	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
412	e7216345-63cb-494f-98f4-8b6bb33b1993	Cho tôi xem mẫu áo phông màu trắng đi	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size S", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
413	e7216345-63cb-494f-98f4-8b6bb33b1004	Có size XL không cho chiếc quần jogger màu đen?	buy_fashion	{"clothing": "qu\\u1ea7n jogger", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
414	e7216345-63cb-494f-98f4-8b6bb33b1004	Có size XL không cho chiếc quần jogger màu đen?	buy_fashion	{"clothing": "qu\\u1ea7n jogger", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
415	e7216345-63cb-494f-98f4-8b6bb33b1355	Tôi muốn một chiếc áo khoác phong cách retro màu hồng nhạt	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng nh\\u1ea1t", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
416	e7216345-63cb-494f-98f4-8b6bb33b1355	Tôi muốn một chiếc áo khoác phong cách retro màu hồng nhạt	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng nh\\u1ea1t", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
417	e7216345-63cb-494f-98f4-8b6bb33b1466	Có màu đen không cho chiếc áo len cổ lọ?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
418	e7216345-63cb-494f-98f4-8b6bb33b1466	Có màu đen không cho chiếc áo len cổ lọ?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
419	e7216345-63cb-494f-98f4-8b6bb33b1577	Có size M không cho chiếc áo thun màu vàng?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
420	e7216345-63cb-494f-98f4-8b6bb33b1577	Có size M không cho chiếc áo thun màu vàng?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 2000000"}
421	e7216345-63cb-494f-98f4-8b6bb33b1688	Giá từ 800.000 đến 1.500.000 đồng cho chiếc váy ngắn màu vàng được không?	request_price	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
422	e7216345-63cb-494f-98f4-8b6bb33b1688	Giá từ 800.000 đến 1.500.000 đồng cho chiếc váy ngắn màu vàng được không?	request_price	{"clothing": "v\\u00e1y ng\\u1eafn", "category_type_clothing": null, "color_clothing": "m\\u00e0u v\\u00e0ng", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
423	e7216345-63cb-494f-98f4-8b6bb33b1799	Cần tìm chiếc áo polo màu trắng	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
424	e7216345-63cb-494f-98f4-8b6bb33b1799	Cần tìm chiếc áo polo màu trắng	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
425	e7216345-63cb-494f-98f4-8b6bb33b2800	Cho tôi xem chiếc áo hoodie màu xanh lá cây đi	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
426	e7216345-63cb-494f-98f4-8b6bb33b2800	Cho tôi xem chiếc áo hoodie màu xanh lá cây đi	buy_fashion	{"clothing": "\\u00e1o hoodie", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
427	e7216345-63cb-494f-98f4-8b6bb33b9876	Có áo khoác nào màu đen không?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
428	e7216345-63cb-494f-98f4-8b6bb33b9876	Có áo khoác nào màu đen không?	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
429	e7216345-63cb-494f-98f4-8b6bb33b2468	Tìm cho tôi chiếc áo khoác phong cách thể thao đi	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
430	e7216345-63cb-494f-98f4-8b6bb33b2468	Tìm cho tôi chiếc áo khoác phong cách thể thao đi	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 800", "price_to": "\\u0111\\u1ebfn 1 500 000"}
431	e7216345-63cb-494f-98f4-8b6bb33b5432	Tôi muốn mua áo khoác có giá từ 1000000 đồng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 1 500 000"}
432	e7216345-63cb-494f-98f4-8b6bb33b5432	Tôi muốn mua áo khoác có giá từ 1000000 đồng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 1 500 000"}
433	e7216345-63cb-494f-98f4-8b6bb33b7890	Tôi muốn tìm áo khoác bóng chày màu trắng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 1 500 000"}
434	e7216345-63cb-494f-98f4-8b6bb33b7890	Tôi muốn tìm áo khoác bóng chày màu trắng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 1000000", "price_to": "\\u0111\\u1ebfn 1 500 000"}
435	e7216345-63cb-494f-98f4-8b6bb33b4567	Tôi cần mua áo khoác phong cách vintage giá từ 500000 đến 1000000 triệu đồng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
436	e7216345-63cb-494f-98f4-8b6bb33b4567	Tôi cần mua áo khoác phong cách vintage giá từ 500000 đến 1000000 triệu đồng	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 500000", "price_to": "\\u0111\\u1ebfn 1000000"}
437	e7216345-63cb-494f-98f4-8b6bb33b7891	Có áo thun màu đen giá từ 900000 đồng không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 900000", "price_to": "\\u0111\\u1ebfn 1000000"}
438	e7216345-63cb-494f-98f4-8b6bb33b7891	Có áo thun màu đen giá từ 900000 đồng không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 900000", "price_to": "\\u0111\\u1ebfn 1000000"}
439	e7216345-63cb-494f-98f4-8b6bb33b9991	Tôi cần mua áo thun giá từ 200000 đồng	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
440	e7216345-63cb-494f-98f4-8b6bb33b9991	Tôi cần mua áo thun giá từ 200000 đồng	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
441	e7216345-63cb-494f-98f4-8b6bb33b9992	Cho xem màu đỏ đi	request_color	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
442	e7216345-63cb-494f-98f4-8b6bb33b9992	Cho xem màu đỏ đi	request_color	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
443	e7216345-63cb-494f-98f4-8b6bb33b9993	Có size S không á?	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
444	e7216345-63cb-494f-98f4-8b6bb33b9993	Có size S không á?	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
445	e7216345-63cb-494f-98f4-8b6bb33b9994	Tôi muốn mua chiếc váy dài màu đen	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 1000000"}
459	a4f3c235-49e2-4282-b4a8-76c2d14e21a7	Tôi muốn mua quần jean size L màu xanh	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
460	a4f3c235-49e2-4282-b4a8-76c2d14e21a7	Tôi muốn mua quần jean size L màu xanh	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
461	b3d9a7f2-8fe5-4a21-9f91-4cf58a9e7d6b	Cần một chiếc áo sơ mi size M trắng	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
462	b3d9a7f2-8fe5-4a21-9f91-4cf58a9e7d6b	Cần một chiếc áo sơ mi size M trắng	buy_fashion	{"clothing": "\\u00e1o s\\u01a1 mi", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
463	c2f1b98d-2fb7-47e4-b89a-17f943ce2cfe	Tôi đang tìm váy dài màu đen size S	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
464	c2f1b98d-2fb7-47e4-b89a-17f943ce2cfe	Tôi đang tìm váy dài màu đen size S	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
465	f5c3aefc-465d-4d8c-8f32-92768f4d1bdf	Cho tôi xem áo len size XS màu hồng	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
466	f5c3aefc-465d-4d8c-8f32-92768f4d1bdf	Cho tôi xem áo len size XS màu hồng	buy_fashion	{"clothing": "v\\u00e1y d\\u00e0i", "category_type_clothing": null, "color_clothing": "m\\u00e0u h\\u1ed3ng", "size_clothing": "size S", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
467	a1e7b2c4-91fc-4e4a-bf5b-8ef91fd2b29a	Có áo polo nào size XL màu đen không?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
468	a1e7b2c4-91fc-4e4a-bf5b-8ef91fd2b29a	Có áo polo nào size XL màu đen không?	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size XL", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
469	d3c4f456-6d80-4f92-aa2e-975bbf84d1b0	Tôi muốn mua áo khoác màu xanh size L	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
470	d3c4f456-6d80-4f92-aa2e-975bbf84d1b0	Tôi muốn mua áo khoác màu xanh size L	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
471	e4d5c6a7-8b90-4b6d-9a4e-1c3f2d4e5f6e	Tôi cần quần jeans màu đen size L	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
472	e4d5c6a7-8b90-4b6d-9a4e-1c3f2d4e5f6e	Tôi cần quần jeans màu đen size L	buy_fashion	{"clothing": "qu\\u1ea7n jeans", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size L", "price_from": "t\\u1eeb 300000", "price_to": "\\u0111\\u1ebfn 500000"}
473	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo phông size M màu trắng giá từ 200000 VND	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
474	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo phông size M màu trắng giá từ 200000 VND	buy_fashion	{"clothing": "\\u00e1o ph\\u00f4ng", "category_type_clothing": null, "color_clothing": "m\\u00e0u tr\\u1eafng", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
475	c4d5e6f7-8a9b-1c2d-3e4f-5a6b7c8d9e0f	Có bán áo thun nam size S màu cam không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u cam", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
476	c4d5e6f7-8a9b-1c2d-3e4f-5a6b7c8d9e0f	Có bán áo thun nam size S màu cam không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u cam", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
477	d8e9f0a1-b2c3-4d5e-6f7a-8b9c1d2e3f4	Có bán váy dạ hội màu đỏ size XS không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
478	d8e9f0a1-b2c3-4d5e-6f7a-8b9c1d2e3f4	Có bán váy dạ hội màu đỏ size XS không?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size XS", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
479	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tôi đang tìm áo khoác da nam màu nâu size M	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
480	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tôi đang tìm áo khoác da nam màu nâu size M	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u n\\u00e2u", "size_clothing": "size M", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
481	c3d4e5f6-7a8b-9c1d-2e3f-4a5b6c7d8e9	Tôi muốn tìm áo polo nam size XL màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size XL", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
482	c3d4e5f6-7a8b-9c1d-2e3f-4a5b6c7d8e9	Tôi muốn tìm áo polo nam size XL màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o polo", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size XL", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
483	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn mua quần jean nữ màu xanh size S	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
484	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn mua quần jean nữ màu xanh size S	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": "t\\u1eeb 200000", "price_to": "\\u0111\\u1ebfn 500000"}
485	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": "\\u0111\\u1ebfn 500000"}
486	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": "\\u0111\\u1ebfn 500000"}
487	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn tìm áo thun cổ tròn nam size M màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 100000", "price_to": "\\u0111\\u1ebfn 500000"}
488	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn tìm áo thun cổ tròn nam size M màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 100000", "price_to": "\\u0111\\u1ebfn 500000"}
489	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": null}
490	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": null}
491	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": null}
492	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": null}
493	a2b3c4d5-6e7f-8a9b-c1d2e3f4a5b6	Tìm áo thun nữ size S màu đỏ giá rẻ từ 100000	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111\\u1ecf", "size_clothing": "size S", "price_from": "t\\u1eeb 100000", "price_to": null}
496		Bạn được tạo ra bởi ai vậy?	who_created_you	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
497		Bạn được tạo ra bởi ai vậy?	who_created_you	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
498		Bạn thuộc giới tính nào?	gender	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
499		Bạn thuộc giới tính nào?	gender	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
500		Bạn bao nhiêu tuổi rồi?	age	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
501		Bạn bao nhiêu tuổi rồi?	age	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
502		Bạn có người yêu chưa?	do_you_have_a_girlfriend	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
503		Bạn có người yêu chưa?	do_you_have_a_girlfriend	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
504		Bạn có thể nói được tiếng anh không?	can_you_speak_english	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
505		Bạn có thể nói được tiếng anh không?	can_you_speak_english	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
506		Bạn có thể làm những gì?	what_can_you_do	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
507		Bạn có thể làm những gì?	what_can_you_do	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
508	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
509	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
510		Có đồ gì size M không?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size M", "price_from": null, "price_to": null}
511		Có đồ gì size M không?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size M", "price_from": null, "price_to": null}
512		vậy size L thì sao?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size L", "price_from": null, "price_to": null}
513		vậy size L thì sao?	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size L", "price_from": null, "price_to": null}
514		Bạn có cái nào màu xanh không?	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
515		Bạn có cái nào màu xanh không?	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
516	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
517	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
518		size S	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": null, "price_to": null}
519		size S	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": null, "price_to": null}
520		Màu đen	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
521		Màu đen	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
522		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
523		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
524		xóa slots	delete_all_slots	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
525		xóa slots	delete_all_slots	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
526		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
527		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
528		xóa slots	delete_all_slots	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
529		xóa slots	delete_all_slots	{"clothing": null, "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
530	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
531	e7216345-63cb-494f-98f4-8b6bb33b1111	Tôi muốn mua chiếc áo khoác dáng dài	buy_fashion	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": null, "price_from": null, "price_to": null}
532		Có đồ gì size M không	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size M", "price_from": null, "price_to": null}
533		Có đồ gì size M không	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size M", "price_from": null, "price_to": null}
534		Vậy size L thì sao	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size L", "price_from": null, "price_to": null}
535		Vậy size L thì sao	request_size	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": null, "size_clothing": "size L", "price_from": null, "price_to": null}
536		Bạn có cái nào màu xanh không	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
537		Bạn có cái nào màu xanh không	request_color	{"clothing": "\\u00e1o kho\\u00e1c", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
538	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
539	e7216345-63cb-494f-98f4-8b6bb33b2211	có áo thun không shop hén?	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size L", "price_from": null, "price_to": null}
540		size S	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": null, "price_to": null}
541		size S	request_size	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size S", "price_from": null, "price_to": null}
542		Màu đen	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
543		Màu đen	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
544		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
545		quần jean shop còn hàng ko	buy_fashion	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": null, "price_to": null}
546	e7216345-63cb-494f-98f4-8b6bb33b1122	có size M không á	request_size	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": null, "price_to": null}
547	e7216345-63cb-494f-98f4-8b6bb33b1122	có size M không á	request_size	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size M", "price_from": null, "price_to": null}
548	e7216345-63cb-494f-98f4-8b6bb33b5678	Cho xem màu xanh đi	request_color	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
549	e7216345-63cb-494f-98f4-8b6bb33b5678	Cho xem màu xanh đi	request_color	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": null, "price_to": null}
550		Cho xem cái nào có giá từ 150 đến 500 được không?	request_price	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
551		Cho xem cái nào có giá từ 150 đến 500 được không?	request_price	{"clothing": "qu\\u1ea7n jean", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh", "size_clothing": "size M", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
552	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn tìm áo thun cổ tròn nam size M màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
553	a1b2c3d4-5e6f-7a8b-9c1d-2e3f4a5b6c7	Tôi muốn tìm áo thun cổ tròn nam size M màu xanh lá cây	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u xanh l\\u00e1 c\\u00e2y", "size_clothing": "size M", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
554		size S có màu đen á	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
555		size S có màu đen á	buy_fashion	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 150", "price_to": "\\u0111\\u1ebfn 500"}
556		giá từ 100 nha	request_price	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 100", "price_to": "\\u0111\\u1ebfn 500"}
557		giá từ 100 nha	request_price	{"clothing": "\\u00e1o thun", "category_type_clothing": null, "color_clothing": "m\\u00e0u \\u0111en", "size_clothing": "size S", "price_from": "t\\u1eeb 100", "price_to": "\\u0111\\u1ebfn 500"}
\.


--
-- TOC entry 3551 (class 0 OID 57481)
-- Dependencies: 231
-- Data for Name: intent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.intent (id, tag, description) FROM stdin;
3	Jacket	Áo khoác
4	Sweater	Áo len
5	Tee	Áo phông
6	Skirt	Váy ngắn
7	Shorts	Quần short
8	Leggings	Quần ôm sát chân
9	Jeans	Quần jean
29	Size_Skirt	Các câu hỏi về size của chiếc váy
30	Color_Skirt	Câu hỏi về màu sắc của váy
31	Size_L_Jacket	Câu hỏi về size L áo khoác
32	Size_Jacket	Hỏi về size áo khoác
33	Size_XL_Jacket	Câu hỏi size XL áo khoác
34	Size_XL_L_Jacket	Câu hỏi về size L và XL áo khoác
35	Color_Grey_Skirt	Câu hỏi về váy màu Xám
36	Color_Green_Skirt	Câu hỏi về váy màu xanh
26	greeting	Mở đầu câu chuyện chào hỏi nhau
37	Color_Grey_Green_Skirt	Câu hỏi về váy màu xanh và màu xám
38	Size_S_Skirt	Câu hỏi về váy size S
39	Size_M_Skirt	Câu hỏi về váy size M
28	thanks	Thanks cuối hội thoại chào tạm biệt
27	goodbye	Goodbye kết thúc hội thoại
40	Size_M_S_Skirt	Câu hỏi về váy size S và M
\.


--
-- TOC entry 3553 (class 0 OID 57485)
-- Dependencies: 233
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."order" (id, order_date, customer_email, customer_phone, customer_address, total_price, status, fullname) FROM stdin;
10	2023-09-12 05:51:47.371287+07	haha@gmail.com	1233211233	100/10 Hung Vuong	200	CANCELLED	hahha
15	2023-09-14 03:59:16.765344+07	han@gmail.com	1231231231	can tho	600	CANCELLED	han
4	2023-09-05 05:21:02.394259+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	PENDING	Minh Dua
5	2023-09-05 05:22:57.074109+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	PENDING	Minh Dua
6	2023-09-05 05:23:47.223643+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	PENDING	Minh Dua
7	2023-09-05 05:27:42.363915+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	PENDING	Minh Dua
11	2023-09-13 05:44:02.556216+07	toan@gmail.com	1231233211	100/100 haha	540	CANCELLED	Minh Toàn
16	2023-09-17 07:42:17.375069+07	nva@gmail.com	0326598789	3/2 Nguyễn Ánh, Hưng Lợi, Cần Thơ	300	PENDING	Nguyễn Văn A
17	2023-09-18 02:43:36.787229+07	han@gmail.com	0169934401	can tho	700	PENDING	nguyen
18	2023-09-18 03:25:00.423295+07	nva@gmail.com	0326598792	Can tho	200	PENDING	Nguyễn Văn A
2	2023-08-21 01:34:04.156043+07	mypc@example.con	0873645789	Cầu Thoại Giang 1, ấp Tây Bình, xã Thoại Giang, Huyện Thoại Sơn	\N	CONFIRMED	Minh Dua
8	2023-09-05 05:27:57.642195+07	minhdua2@example.com	0123456789	99 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	150	PENDING	Minh Dua2
9	2023-09-05 05:45:59.059599+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	CANCELLED	Minh Dua
3	2023-09-05 05:18:48.075938+07	minhdua@example.com	0123456789	97 Thạnh Huề, Thường Thạnh, Cái Răng, TP. Cần Thơ	500	SHIPPING	Minh Dua
12	2023-09-14 03:04:21.316461+07	2@gmail.com	1231231231	123	900	PENDING	1
13	2023-09-14 03:11:09.162573+07	gdgf@gmai.com	1231231231	321321	75	PENDING	123
1	2023-08-21 01:32:13.84183+07	vothanhhienag1996@gmail.com	0762036198	Cầu Thoại Giang 1, ấp Tây Bình, xã Thoại Giang, Huyện Thoại Sơn	\N	PENDING	Thanh Hiền Võ
14	2023-09-14 03:14:06.398283+07	1@gmail.com	1231231231	1	120	CANCELLED	1
\.


--
-- TOC entry 3555 (class 0 OID 57491)
-- Dependencies: 235
-- Data for Name: order_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_product (id, order_id, product_id, quantity, order_size, order_color) FROM stdin;
6	2	4	1	XL	BLUE
24	8	6	2	XXL	GREEN
26	11	5	1	L	GREEN
28	12	5	3	L	GREEN
29	13	6	1	XXXL	GREY
33	17	9	2	XL	BLACK
34	18	10	2	M	BLACK
\.


--
-- TOC entry 3557 (class 0 OID 57495)
-- Dependencies: 237
-- Data for Name: pattern; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pattern (id, pattern_text, intent_id) FROM stdin;
209	có quần bó không	8
211	mặc quần thun thoải mái	8
213	tôi muốn mua quần bó	8
217	Quần bó sát chân	8
219	quần bó	8
223	Quần jean	9
225	tôi muốn mua Quần jean	9
227	có Quần jean đẹp ko	9
232	cảm ơn shop	27
234	tôi muốn mua sản phẩm	26
236	có ai ko	26
238	hi shop	26
240	cho tôi hỏi	26
241	bạn ơi	26
113	hello	26
114	hi	26
115	hey	26
116	có ai ở đây không?	26
117	chào shop	26
118	Có ai ở đây không nhỉ	26
119	alo	26
120	hú hú	26
121	cho hỏi	26
122	shop ơi	26
123	tôi muốn mua	26
124	tạm biệt	27
125	không mua nữa	27
126	không mua	27
127	baibai	27
128	baybay	27
129	hẹn bửa khác	27
130	goodbye	27
131	bb	27
132	dịp khác nha	27
133	vậy thôi nhé	27
134	bay	27
135	bai	27
136	bửa sau quay lại	27
137	cảm ơn	28
138	cảm ơn nha	28
139	Thank you	28
140	Thank	28
141	Tuyệt vời lắm	28
142	Cảm ơn bạn rất nhiều	28
143	Oke lắm	28
144	điều này tuyệt nhất	28
149	Áo khoác bán như thế nào	3
155	áo khoác dài bán ntn	3
158	có bán áo len không	4
159	tôi muốn mua áo len	4
160	cho xem áo len với	4
165	xin mẫu áo phông	5
166	có bán áo phông không shop	5
167	muốn mua áo phông	5
170	mẫu áo ba lỗ	5
171	áo phông đẹp xin mẫu nha	5
175	tôi mua váy lót	6
178	váy lót còn không shop	6
210	quần bó mặc đẹp	8
212	tôi muốn mua quần thun	8
216	có quần thun ko	8
218	quần thun	8
200	tôi muốn mua quần short	7
202	mua quần short	7
206	quần short	7
220	Quần jean có bán ko shop	9
224	mua Quần jean	9
226	có Quần jean ko	9
201	có quần short không shop	7
203	quần short bán sao	7
205	có quần short không	7
230	cho hỏi có bán Quần jean ko	9
231	bai nhé	27
233	bai shop	27
235	alo alo	26
237	chào	26
239	hello shop	26
243	Chào bạn! Tôi đang tìm kiếm một chiếc váy dài cho buổi tiệc	6
245	cần tim mua váy đi đám cưới	6
246	Váy thì có loại size nào shop?	29
247	váy này shop có mấy size	29
248	shop có size loại váy này ko	29
249	Váy này có mấy size	29
250	size váy này có loại nào lớn ko	29
251	Váy này có size nhỏ không	29
292	Tạm biệt	28
294	bye shop	28
296	bye	28
291	cảm ơn hen	28
293	Cảm ơn shop nha	28
295	bay bay	28
297	bye bye	28
298	tôi muốn xem áo khoác	3
299	Tôi muốn mua áo khoác	3
300	shop có bán áo khoác ko	3
301	có áo khoác nào mặc chống nắng ko	3
302	áo khoác mặc đi chơi có ko shop	3
303	cho xem áo khoác nha	3
304	có bán áo khoác ko	3
305	áo khoác có size L ko shop	31
306	Shop có bán áo khoác size L ko	31
307	có áo khoác size L ko	31
308	cho xem áo khoác size L	31
309	muốn xem áo khoác size L	31
310	áo khoác size L	31
311	shop có bao nhiêu size áo khoác	32
312	có bao nhiêu size áo khoác	32
313	áo khoác có size lớn ko	32
314	có size áo khoác nhỏ ko	32
315	áo khoác size nhỏ	32
316	áo khoác size lớn	32
317	tôi muốn xem size áo khoác	32
318	cho tôi xem các size áo khoác	32
319	áo khoác size XL	33
320	xem áo khoác XL	33
321	Áo khoác XL	33
322	cho xem áo khoác size XL	33
323	muốn xem áo khoác XL	33
324	cho xem áo khoác size L và XL luôn nha	34
325	áo khoác L và XL	34
326	cho xem cả 2 size L và XL của áo khoác nha	34
327	cho tôi xem áo khoác size L và XL	34
328	xem áo khoác size L và XL	34
329	bao nhiêu kg thì mặc áo khoác size L	31
330	cao bao nhiêu thì mặc áo khoác size L	31
331	nam nữ có mặc chung áo khoác size L được ko	31
332	to con mặc áo khoác XL được ko	33
333	nặng 50kg mặc áo khoác size nào shop	32
334	shop gửi các size áo khoác cho mình xem nhé	32
335	Váy có mấy loại màu shop	30
336	cho xem các màu của váy	30
337	váy có mấy màu	30
338	váy này có mấy nào shop	30
339	da trắng mặc váy màu gì đẹp	30
340	người gầy thì mặc váy màu nào hợp	30
341	người bự con mặc váy màu nào ok nhất	30
342	shop có váy màu nào	30
343	váy có những màu nào há	30
344	váy thì shop có những màu nào	30
345	size váy nào thì người gầy mặc đẹp	29
346	cho xem váy màu xám nha shop	35
347	tôi muốn xem váy màu xám	35
348	váy màu xám nha	35
349	Shop có bán váy màu xám ko ?	35
350	váy màu xám shop có ko?	35
351	xem váy màu xám	35
352	cho xem váy màu xám	35
353	cho xem váy màu xanh nhé	36
354	shop còn váy màu xanh ko	36
355	muốn xem váy màu xanh	36
356	váy màu xanh nha	36
357	Váy màu xanh	36
359	cho tôi xem váy màu xanh	36
360	tôi có câu hỏi	26
361	muốn hỏi chút	26
362	cho xem váy màu xanh và màu xám luôn nha	37
363	shop có bán váy màu xanh và màu xám ko	37
364	xem váy màu xanh và màu xám	37
365	tôi muốn xem váy màu xanh và màu xám	37
366	muốn xem váy màu xám và màu xanh nha	37
367	cho xem váy size S nha shop	38
368	muốn xem váy size S	38
369	shop có váy size S ko	38
370	váy size S	38
371	xem váy size S	38
372	cho tôi xem váy size S nha	38
373	cho xem váy size M nha	39
374	shop có váy size M ko	39
375	xem váy size M	39
376	váy size M	39
377	muốn xem váy size M	39
378	cho tôi xem váy size M	39
379	shop còn váy size M ko	39
380	tôi muốn xem váy size M	39
381	cảm ơn Shop	28
382	mơn nhe	28
383	bi bi	28
384	by by	28
385	bay	28
386	chào tạm biệt	28
387	cảm ơn shop rất nhiều	28
388	hẹn gặp lại shop	28
389	muốn xem cả 2 size M và size S	40
390	shop có váy size S và size M ko	40
391	váy size S và M	40
392	xem váy size S và M	40
393	muốn xem váy size S và M nha	40
394	tôi xem váy size S và M	40
395	người nhỏ con thì mặc váy size S và M ok ko shop hé	40
396	có áo phông ko shop ơi	5
397	tôi muốn mua áo phông để đi chơi	5
398	áo phông shop có bán ko	5
399	mẫu áo phông đẹp tôi muốn xem	5
400	tôi muốn xem áo len	4
401	áo len shop có bán ko	4
402	xin mẫu áo len nha	4
403	mẫu áo len	4
404	có áo len ko shop	4
405	có áo len ko	4
406	shop có áo len ko	4
407	quần short shop có bán ko	7
408	tôi muốn xem quần short	7
409	mẫu quần short shop có ko	7
410	quần thun shop có ko	8
411	shop có quần thun ko	8
412	muốn xem quần thun	8
413	quần bó shop có bán ko	8
414	quần bó shop còn hàng ko	8
415	quần jean shop còn hàng ko	9
416	muốn xem quần jean	9
417	cho xem quần jean với	9
418	shop có bán quần jean ko	9
419	gửi mẫu quần jean cho tôi xem	9
420	xem áo khoác	3
421	cho xem áo khoác	3
422	cho xem quần jean	9
423	xem quần jean	9
424	cần váy đẹp	6
425	muốn mua váy	6
426	shop còn váy nào đẹp ko	6
427	shop có bán váy ko	6
428	tôi xem váy màu xanh	36
429	xem váy màu xanh	36
430	gửi tôi xem váy màu xanh	36
\.


--
-- TOC entry 3559 (class 0 OID 57499)
-- Dependencies: 239
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (id, name, price, quantity, category_id, image_url, description) FROM stdin;
27	Quần bó cho nữ thể thao	120	10	30	http://127.0.0.1:5000/static/products/ao-nu-day.jpg	Quần bó cho nữ thể thao
9	Áo khoác dài nữ dạo phố	350	8	19	http://127.0.0.1:5000/static/products/khoac-dai-nu.jpg	Áo khoác dài cho nữ đẹp cho đi dạo phố
5	Quần bó sát nữ	300	10	30	http://127.0.0.1:5000/static/products/quan-dai-nu.jpg	Quần bó sát chân nữ sang trọng
35	Quần jean dài nữ	500	10	26	http://127.0.0.1:5000/static/products/quan-jean-nu.jpg	Quần jean dài nữ mặc đẹp hơn nhiều
6	Áo khoác đẹp nữ	300	10	11	http://127.0.0.1:5000/static/products/ao-khoac-am-nu.jpg	Áo choàng nữ cho nữ
4	Váy màu xanh nữ	50	40	33	http://127.0.0.1:5000/static/products/dam-nu.jpg	Váy đầm màu xanh nữ thời trang
36	Váy ngắn nữ sang chảnh	150	10	41	http://127.0.0.1:5000/static/products/vay-ngan-nu.jpg	Váy ngắn nữ dễ thương, sanh chảnh
30	Áo thun ba lỗ nữ sexy	130	15	18	http://127.0.0.1:5000/static/products/thun-nu-3-lo.jpg	Áo ba lỗ nữ cho nữ
10	Áo thun cho nam	100	10	18	http://127.0.0.1:5000/static/products/khoac-ni.jpg	Áo nỉ cho nam nữ đi nắng
\.


--
-- TOC entry 3560 (class 0 OID 57504)
-- Dependencies: 240
-- Data for Name: product_attributes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_attributes (id, product_id, attribute_predict_id) FROM stdin;
10604	5	235
10606	5	237
10608	5	239
10610	5	242
10612	5	248
10614	5	253
11276	6	164
11278	6	168
11280	6	170
11282	6	176
11284	6	179
11286	6	187
11288	6	189
11290	6	193
11292	6	196
11294	6	200
11296	6	204
11298	6	213
11300	6	220
11302	6	225
11304	6	227
11306	6	234
11308	6	236
11310	6	238
11312	6	241
11314	6	247
11316	6	250
11318	6	254
11320	6	258
11322	6	262
11324	6	265
11326	6	269
11328	6	271
11330	6	273
11332	6	278
11334	6	280
11336	6	285
11338	6	288
11340	6	292
11342	6	296
11344	6	302
11346	6	305
11348	6	308
11350	6	312
11352	6	316
11354	6	318
11356	6	325
11358	6	329
11360	6	332
11362	6	335
11364	6	339
11366	6	341
11368	6	351
11370	6	354
11372	6	356
11374	6	358
11376	6	360
11378	6	363
11380	6	365
11382	6	368
11384	6	373
11386	6	376
11388	6	381
11390	6	383
11392	6	388
11394	6	393
11396	6	395
11398	6	397
11400	6	399
11402	6	403
11404	6	408
11406	6	412
11408	6	417
11410	6	420
11412	6	425
11414	6	430
11416	6	433
11418	6	437
11420	6	441
11422	6	447
11424	6	451
12363	4	5
12365	4	10
12367	4	13
12369	4	15
12371	4	18
12373	4	24
12375	4	28
12377	4	30
12379	4	36
12381	4	38
12383	4	43
12385	4	50
11426	6	453
11428	6	458
11430	6	462
11431	30	2
11433	30	6
11435	30	12
11437	30	14
11439	30	17
11441	30	21
11443	30	25
11445	30	30
11447	30	37
11449	30	40
11451	30	50
11453	30	52
11455	30	58
11457	30	60
11459	30	67
10616	5	257
10618	5	260
10620	5	263
10622	5	267
10624	5	270
10626	5	272
10628	5	274
10630	5	279
10632	5	282
10634	5	286
10636	5	290
10638	5	295
10640	5	298
10642	5	304
10644	5	306
10646	5	310
10648	5	314
10650	5	318
12387	4	52
12389	4	56
12391	4	59
12393	4	61
12395	4	71
12397	4	74
12399	4	77
12401	4	81
12403	4	84
12405	4	89
12407	4	91
12409	4	94
12411	4	100
12413	4	104
12415	4	110
12417	4	112
12419	4	116
12421	4	121
12423	4	130
12425	4	134
12427	4	137
12429	4	139
12431	4	146
12433	4	149
12435	4	154
12437	4	157
12439	4	159
12441	4	161
12443	4	164
12445	4	167
12447	4	169
12449	4	175
12451	4	179
12453	4	184
12455	4	188
12457	4	190
12459	4	195
12461	4	197
12463	4	201
12465	4	206
12467	4	216
12469	4	220
12471	4	225
12473	4	227
12475	4	234
12477	4	236
12479	4	238
12481	4	241
12483	4	247
12485	4	250
12487	4	253
12489	4	257
12491	4	262
12493	4	265
12495	4	269
12497	4	271
10605	5	236
10607	5	238
10609	5	241
10611	5	247
10613	5	250
10615	5	254
11277	6	167
11279	6	169
11281	6	172
11283	6	177
11285	6	183
11287	6	188
11289	6	190
11291	6	195
11293	6	197
11295	6	201
11297	6	206
11299	6	216
11301	6	222
11303	6	226
11305	6	231
11307	6	235
11309	6	237
11311	6	239
11313	6	242
11315	6	248
11317	6	253
11319	6	257
11321	6	260
11323	6	263
11325	6	267
11327	6	270
11329	6	272
11331	6	275
11333	6	279
11335	6	282
11337	6	286
11339	6	290
11341	6	295
11343	6	298
11345	6	304
11347	6	306
11349	6	311
11351	6	314
11353	6	317
11355	6	319
11357	6	328
11359	6	331
11361	6	333
11363	6	337
11365	6	340
11367	6	342
11369	6	352
11371	6	355
11373	6	357
11375	6	359
11377	6	361
11379	6	364
11381	6	367
11383	6	369
11385	6	375
11387	6	380
11389	6	382
11391	6	384
11393	6	390
11395	6	394
11397	6	396
11399	6	398
11401	6	400
11403	6	404
11405	6	411
11407	6	413
11409	6	419
11411	6	421
11413	6	427
11415	6	432
11417	6	434
11419	6	438
11421	6	443
11423	6	448
11425	6	452
11427	6	457
11429	6	459
11432	30	5
11434	30	10
10617	5	258
10619	5	262
10621	5	265
10623	5	269
10625	5	271
10627	5	273
10629	5	275
10631	5	280
10633	5	285
10635	5	288
10637	5	292
10639	5	296
10641	5	302
10643	5	305
10645	5	308
10647	5	312
10649	5	316
10651	5	319
10653	5	331
10655	5	333
10657	5	339
10659	5	341
10661	5	351
10663	5	354
10665	5	356
10667	5	358
10669	5	360
10671	5	363
10673	5	365
10675	5	369
10677	5	378
10679	5	381
11436	30	13
11438	30	15
11440	30	18
11442	30	24
11444	30	28
11446	30	36
11448	30	38
11450	30	43
11452	30	51
11454	30	55
11456	30	59
11458	30	61
11460	30	71
11462	30	74
11464	30	81
11466	30	84
11468	30	90
11470	30	92
11472	30	96
11474	30	104
11476	30	106
11478	30	111
11480	30	113
11482	30	115
11484	30	118
11486	30	121
11488	30	129
11490	30	131
11492	30	135
11494	30	138
11496	30	141
11498	30	148
11500	30	152
11502	30	155
11504	30	158
11506	30	160
11508	30	164
11510	30	168
11512	30	170
11514	30	175
11516	30	179
11518	30	183
11520	30	185
11522	30	188
11524	30	190
11526	30	195
11528	30	197
11530	30	201
11532	30	206
11534	30	216
11536	30	220
11538	30	225
11540	30	227
11542	30	234
11544	30	236
11546	30	238
11548	30	241
11550	30	247
11552	30	250
11554	30	254
11556	30	258
11558	30	262
11560	30	265
11562	30	269
12035	10	286
12037	10	290
12039	10	295
12041	10	304
11461	30	72
11463	30	80
11465	30	83
11467	30	89
11469	30	91
11471	30	94
11473	30	101
11475	30	105
11477	30	110
11479	30	112
11481	30	114
11483	30	116
11485	30	120
11487	30	125
11489	30	130
11491	30	134
11493	30	137
11495	30	139
11497	30	146
11499	30	149
11501	30	154
11503	30	157
11505	30	159
11507	30	162
11509	30	167
11511	30	169
11513	30	172
11515	30	176
11517	30	181
11519	30	184
11521	30	187
11523	30	189
11525	30	193
11527	30	196
11529	30	200
11531	30	204
11533	30	207
11535	30	218
11537	30	222
11539	30	226
11541	30	231
11543	30	235
11545	30	237
11547	30	239
11549	30	242
11551	30	248
11553	30	253
12364	4	6
12366	4	12
12368	4	14
12370	4	17
12372	4	21
12374	4	25
12376	4	29
12378	4	34
12380	4	37
12382	4	40
12384	4	46
12386	4	51
12388	4	55
12390	4	58
12392	4	60
12394	4	67
12396	4	72
12398	4	76
12400	4	80
12402	4	83
12404	4	86
12406	4	90
12408	4	92
12410	4	96
12412	4	101
12414	4	106
12416	4	111
12418	4	115
12420	4	118
11555	30	257
11557	30	260
11559	30	263
11561	30	267
11563	30	270
12036	10	288
12038	10	292
12040	10	298
12042	10	305
12044	10	308
12046	10	314
12048	10	317
12050	10	319
12052	10	332
12054	10	335
12056	10	339
12058	10	341
12060	10	351
12062	10	353
12064	10	355
12066	10	357
12068	10	359
12070	10	361
12072	10	364
12074	10	367
12076	10	369
12078	10	376
12080	10	380
12082	10	382
12084	10	384
12086	10	390
12088	10	393
12090	10	395
12092	10	397
12094	10	399
12096	10	403
12098	10	408
12100	10	413
12102	10	417
12104	10	420
12106	10	425
12108	10	430
12110	10	433
12112	10	436
12114	10	438
12116	10	443
12118	10	448
12120	10	453
12122	10	458
12124	10	462
12126	27	6
12128	27	12
12130	27	14
12132	27	17
12134	27	21
12136	27	24
12138	27	28
12140	27	30
12142	27	37
12144	27	40
12146	27	43
12148	27	51
12150	27	55
12152	27	58
12154	27	60
12156	27	67
12158	27	72
12160	27	77
12162	27	81
12164	27	84
12166	27	90
12168	27	92
12170	27	96
12172	27	100
12174	27	104
12176	27	106
12178	27	110
12180	27	112
12182	27	115
12184	27	118
12186	27	121
12188	27	129
12190	27	131
12192	27	135
12194	27	138
12196	27	141
12198	27	148
12200	27	152
12422	4	125
12424	4	131
12426	4	135
12428	4	138
12430	4	141
12432	4	148
12434	4	152
12436	4	155
12438	4	158
12440	4	160
12442	4	162
12444	4	166
12446	4	168
12448	4	170
12450	4	176
12452	4	183
12454	4	187
12456	4	189
12458	4	193
12460	4	196
12462	4	200
11564	30	271
11566	30	274
11568	30	279
11570	30	282
11572	30	286
11574	30	290
11576	30	295
12464	4	204
12466	4	207
12468	4	218
12470	4	222
12472	4	226
12474	4	231
12476	4	235
12478	4	237
12480	4	239
12482	4	242
12484	4	248
12486	4	252
12488	4	254
10652	5	328
10654	5	332
10656	5	335
10658	5	340
10660	5	342
10662	5	353
10664	5	355
10666	5	357
10668	5	359
10670	5	361
10672	5	364
10674	5	368
10676	5	376
10678	5	380
10680	5	382
10682	5	384
10684	5	389
10686	5	393
10688	5	395
10690	5	397
10692	5	399
10694	5	403
10696	5	408
10698	5	413
10700	5	419
10702	5	421
10704	5	427
10706	5	432
10708	5	434
10710	5	438
10712	5	443
10714	5	447
10716	5	452
10718	5	455
10720	5	458
10722	5	462
10724	35	6
10726	35	12
10728	35	14
10730	35	17
10732	35	21
10734	35	25
10736	35	30
10738	35	36
10740	35	38
10742	35	43
10744	35	51
10746	35	55
10748	35	58
10750	35	60
10752	35	67
10754	35	72
10756	35	76
10758	35	80
10760	35	83
11578	30	298
11580	30	304
11582	30	306
11584	30	312
11586	30	316
11588	30	319
11590	30	328
11592	30	331
11594	30	333
11596	30	337
11598	30	340
11600	30	342
11602	30	354
11604	30	356
11606	30	358
11608	30	360
11610	30	363
11612	30	365
11614	30	368
11616	30	376
11618	30	381
11620	30	383
11622	30	388
11624	30	390
11626	30	394
11628	30	396
11630	30	398
11632	30	400
11634	30	404
11636	30	411
11638	30	413
11640	30	419
11642	30	424
11644	30	427
11646	30	431
11648	30	433
11650	30	437
11652	30	441
11654	30	445
11656	30	448
11658	30	453
11660	30	457
11662	30	459
11665	9	10
11667	9	13
11669	9	15
11671	9	18
11673	9	23
11675	9	25
11677	9	30
11679	9	36
11681	9	38
11683	9	46
11685	9	51
11687	9	55
11689	9	58
12043	10	306
12045	10	312
12047	10	316
12049	10	318
12051	10	329
12053	10	333
12055	10	337
12057	10	340
12059	10	342
12061	10	352
12063	10	354
12065	10	356
12067	10	358
12069	10	360
12071	10	363
12073	10	365
12075	10	368
12077	10	375
12079	10	378
12081	10	381
12083	10	383
12085	10	388
12087	10	392
12089	10	394
12091	10	396
12093	10	398
12095	10	400
12097	10	404
12099	10	412
12101	10	415
12103	10	419
12105	10	421
12107	10	427
12109	10	432
12111	10	434
12113	10	437
12115	10	441
12117	10	447
12119	10	452
12121	10	457
12123	10	459
12125	27	5
12127	27	10
12129	27	13
12131	27	15
12133	27	18
10762	35	85
10764	35	90
10766	35	92
10768	35	96
10770	35	104
10772	35	106
10774	35	111
10776	35	114
11565	30	273
11567	30	278
11569	30	280
11571	30	285
11573	30	288
11575	30	292
11577	30	296
11579	30	302
11581	30	305
11583	30	310
11585	30	314
11587	30	318
11589	30	324
11591	30	329
11593	30	332
11595	30	335
11597	30	339
11599	30	341
11601	30	351
11603	30	355
11605	30	357
11607	30	359
11609	30	361
11611	30	364
11613	30	367
11615	30	369
11617	30	380
11619	30	382
11621	30	384
11623	30	389
11625	30	393
11627	30	395
11629	30	397
11631	30	399
11633	30	403
11635	30	408
11637	30	412
11639	30	417
11641	30	420
10490	5	5
10492	5	10
10494	5	13
10496	5	15
10498	5	18
10500	5	24
10502	5	28
10504	5	36
10506	5	38
10508	5	42
10510	5	50
10512	5	52
10514	5	56
10516	5	59
10518	5	61
10520	5	71
10522	5	74
10524	5	77
10526	5	81
10528	5	84
10530	5	89
10532	5	91
10534	5	94
10536	5	101
10538	5	105
10540	5	110
10542	5	112
10544	5	115
10546	5	118
10548	5	121
10550	5	130
10552	5	134
10554	5	137
10556	5	139
10558	5	146
10560	5	149
10562	5	154
10564	5	157
10566	5	159
10568	5	161
10570	5	164
10572	5	167
10574	5	169
10576	5	172
10578	5	176
10580	5	183
10582	5	185
10584	5	188
11643	30	425
11645	30	430
11647	30	432
11649	30	434
11651	30	438
11653	30	443
11655	30	447
11657	30	452
11659	30	455
11661	30	458
11663	30	462
11664	9	6
11666	9	12
11668	9	14
11670	9	17
11672	9	21
11674	9	24
11676	9	28
11678	9	34
11680	9	37
11682	9	43
11684	9	50
11686	9	52
11688	9	56
11690	9	59
12135	27	23
12137	27	25
12139	27	29
12141	27	36
12143	27	38
12145	27	42
12147	27	50
12149	27	52
12151	27	56
12153	27	59
12155	27	61
12157	27	71
12159	27	74
12161	27	80
12163	27	83
12165	27	89
12167	27	91
12169	27	94
12171	27	97
12173	27	101
12175	27	105
12177	27	107
12179	27	111
12181	27	114
12183	27	116
12185	27	120
12187	27	125
12189	27	130
12191	27	134
12193	27	137
12195	27	139
12197	27	146
12199	27	149
12201	27	154
12203	27	158
12205	27	160
12207	27	162
12209	27	167
12211	27	170
12213	27	175
12215	27	179
12217	27	183
12219	27	188
12221	27	190
12223	27	195
12225	27	197
12227	27	201
12229	27	206
12231	27	213
12233	27	218
12235	27	222
12237	27	226
12239	27	231
12241	27	235
12243	27	237
12245	27	239
12247	27	242
12249	27	248
12251	27	253
12253	27	257
12255	27	260
12257	27	263
12259	27	267
12261	27	270
12263	27	272
12490	4	258
12492	4	263
12494	4	267
12496	4	270
12498	4	273
12500	4	275
12502	4	278
12504	4	280
11691	9	60
11693	9	67
11695	9	72
11697	9	76
11699	9	81
11701	9	84
11703	9	90
11705	9	92
11707	9	96
11709	9	104
11711	9	110
11713	9	112
11715	9	115
11717	9	118
11719	9	121
11721	9	130
11723	9	134
11725	9	137
11727	9	139
11729	9	146
11731	9	149
11733	9	154
11735	9	158
11737	9	160
11739	9	162
11741	9	167
11743	9	169
11745	9	172
11747	9	176
11749	9	183
11751	9	185
10491	5	6
10493	5	12
10495	5	14
10497	5	17
10499	5	21
10501	5	25
10503	5	30
10505	5	37
10507	5	40
10509	5	43
10511	5	51
10513	5	55
10515	5	58
10517	5	60
10519	5	67
10521	5	72
10523	5	76
10525	5	80
10527	5	83
10529	5	85
10531	5	90
10533	5	92
10535	5	96
10537	5	104
10539	5	106
10541	5	111
10543	5	114
10545	5	116
10547	5	120
10549	5	125
10551	5	131
10553	5	135
10555	5	138
10557	5	141
10559	5	148
10561	5	152
10563	5	155
10565	5	158
10567	5	160
10569	5	162
10681	5	383
10683	5	388
10685	5	390
10687	5	394
10689	5	396
10691	5	398
10693	5	400
10695	5	404
10697	5	412
10699	5	417
10701	5	420
10703	5	425
10705	5	430
10707	5	433
10709	5	437
10711	5	441
10713	5	445
10715	5	448
10717	5	453
10719	5	457
10721	5	459
10723	35	5
10725	35	10
10727	35	13
10729	35	15
10731	35	18
10733	35	24
10735	35	28
10737	35	34
10739	35	37
10741	35	40
10743	35	50
10745	35	52
10571	5	166
10573	5	168
10575	5	170
10577	5	175
10579	5	179
10581	5	184
10583	5	187
10585	5	189
10587	5	191
10589	5	195
10747	35	56
10749	35	59
10751	35	61
10753	35	71
10755	35	74
10757	35	77
10759	35	81
10761	35	84
10763	35	89
10765	35	91
10767	35	94
10769	35	101
10771	35	105
10773	35	110
10775	35	112
10777	35	115
10779	35	118
10781	35	121
10783	35	129
10785	35	131
10787	35	135
10789	35	138
10791	35	141
10793	35	148
10795	35	152
10797	35	155
10799	35	158
10801	35	160
10803	35	164
10805	35	167
10807	35	169
10809	35	175
10811	35	177
10813	35	184
10815	35	187
10817	35	189
10819	35	193
10821	35	196
10823	35	200
10825	35	204
10827	35	218
10829	35	222
10831	35	226
10833	35	231
10835	35	235
10837	35	237
10839	35	239
10841	35	242
10843	35	248
10845	35	252
11753	9	188
11755	9	190
11757	9	195
11759	9	197
11761	9	201
11763	9	207
11765	9	216
11767	9	222
11769	9	226
11771	9	231
11773	9	235
11775	9	237
11777	9	239
10591	5	197
10593	5	201
10595	5	207
10597	5	220
10599	5	225
10601	5	227
10603	5	234
11692	9	61
11694	9	71
11696	9	74
11698	9	77
11700	9	83
11702	9	89
11704	9	91
11706	9	94
11708	9	101
11710	9	106
11712	9	111
11714	9	114
11716	9	116
11718	9	120
11720	9	125
11722	9	131
11724	9	135
11726	9	138
11728	9	141
11730	9	148
11732	9	152
11734	9	155
11736	9	159
11738	9	161
11740	9	164
11742	9	168
11744	9	170
11746	9	175
11748	9	179
11750	9	184
11752	9	187
11754	9	189
11756	9	193
11758	9	196
11760	9	200
11762	9	204
11764	9	213
11766	9	220
11768	9	225
11770	9	227
11772	9	234
11774	9	236
11776	9	238
10586	5	190
10588	5	193
10590	5	196
10592	5	200
10594	5	204
10596	5	216
10598	5	222
10600	5	226
10602	5	231
10778	35	116
10780	35	120
10782	35	125
10784	35	130
10786	35	134
10788	35	137
10790	35	139
10792	35	146
10794	35	149
10796	35	154
10798	35	157
10800	35	159
10802	35	162
10804	35	166
10806	35	168
10808	35	170
10810	35	176
10812	35	179
10814	35	185
10816	35	188
10818	35	190
10820	35	195
10822	35	197
10824	35	201
10826	35	216
10828	35	220
10830	35	225
10832	35	227
10834	35	234
10836	35	236
10838	35	238
10840	35	241
10842	35	247
10844	35	250
10846	35	253
11778	9	241
11780	9	245
11782	9	248
11784	9	253
11786	9	257
11788	9	262
11790	9	265
11792	9	269
11794	9	271
11796	9	274
11798	9	278
11800	9	280
11802	9	285
11804	9	290
11806	9	295
11808	9	298
11810	9	304
11812	9	306
11814	9	310
11816	9	314
11818	9	318
11820	9	328
11822	9	330
11824	9	332
11826	9	335
11828	9	339
11830	9	341
11832	9	351
11834	9	354
11836	9	357
11838	9	359
11840	9	361
11842	9	364
11844	9	368
11846	9	376
11848	9	381
11850	9	383
11852	9	388
11854	9	390
11856	9	394
11858	9	396
11860	9	398
11862	9	403
11864	9	408
11866	9	412
11868	9	415
11870	9	419
11872	9	425
11874	9	430
11876	9	432
11878	9	434
11880	9	438
11882	9	443
11884	9	447
11886	9	451
11888	9	453
11890	9	457
11892	9	459
11894	10	5
11896	10	10
11898	10	13
11900	10	15
11902	10	18
11904	10	22
11906	10	25
11908	10	30
11910	10	37
12499	4	274
12501	4	277
12503	4	279
12505	4	282
12507	4	286
12509	4	290
12511	4	295
12513	4	298
12515	4	304
12506	4	285
12508	4	288
12510	4	292
12512	4	296
12514	4	302
12516	4	305
10847	35	254
10849	35	258
10851	35	262
10853	35	265
10855	35	270
10857	35	272
10859	35	274
10861	35	278
10863	35	282
10865	35	286
10867	35	290
10869	35	295
10871	35	304
10873	35	306
10875	35	312
10877	35	318
10879	35	321
10881	35	329
10883	35	333
10885	35	337
10887	35	340
10889	35	342
10891	35	354
10893	35	356
10895	35	358
10897	35	360
10899	35	363
10901	35	365
10903	35	368
10905	35	374
10907	35	378
10909	35	381
10911	35	383
10913	35	387
10915	35	390
10917	35	394
10919	35	396
10921	35	398
10923	35	400
10925	35	404
10927	35	411
10929	35	413
10931	35	417
10933	35	420
10935	35	427
10937	35	432
10939	35	434
10941	35	437
10943	35	441
10945	35	447
10947	35	452
10949	35	455
10951	35	458
10953	35	462
10955	36	5
10957	36	10
10959	36	13
10961	36	15
10963	36	18
10965	36	23
10967	36	25
10969	36	30
10971	36	37
10973	36	40
10975	36	43
10977	36	51
10979	36	55
10981	36	59
10983	36	61
11779	9	242
11781	9	247
11783	9	250
11785	9	254
11787	9	260
11789	9	263
11791	9	267
11793	9	270
11795	9	273
11797	9	277
11799	9	279
11801	9	282
11803	9	288
11805	9	292
11807	9	296
11809	9	302
11811	9	305
11813	9	308
11815	9	312
11817	9	316
11819	9	319
11821	9	329
11823	9	331
11825	9	333
11827	9	337
11829	9	340
11831	9	342
11833	9	352
11835	9	356
11837	9	358
11839	9	360
11841	9	363
11843	9	365
11845	9	369
11847	9	380
11849	9	382
11851	9	384
11853	9	389
11855	9	393
11857	9	395
11859	9	397
11861	9	400
11863	9	404
11865	9	411
11867	9	413
11869	9	417
11871	9	420
11873	9	427
11875	9	431
11877	9	433
11879	9	437
11881	9	441
11883	9	445
11885	9	448
11887	9	452
11889	9	456
11891	9	458
11893	9	462
11895	10	6
11897	10	12
11899	10	14
11901	10	17
11903	10	21
11905	10	24
11907	10	28
11909	10	36
11911	10	38
11913	10	50
11915	10	52
11917	10	58
11919	10	60
11921	10	67
11923	10	72
11925	10	76
11927	10	80
11929	10	83
11931	10	89
11933	10	91
11935	10	94
11937	10	101
11939	10	105
11941	10	110
11943	10	112
11945	10	115
11947	10	118
12517	4	306
12519	4	312
12521	4	316
12523	4	318
12525	4	326
12527	4	330
12529	4	332
12531	4	335
12533	4	339
12535	4	341
12537	4	350
12539	4	354
12541	4	357
12543	4	359
12545	4	361
12547	4	364
12549	4	367
12551	4	369
12553	4	376
12555	4	380
12557	4	382
12559	4	384
12561	4	390
12563	4	394
12565	4	396
12567	4	398
12569	4	400
12571	4	404
12573	4	412
12575	4	414
12577	4	417
12579	4	420
12581	4	425
12583	4	430
12585	4	433
12587	4	438
12589	4	443
12591	4	447
12593	4	452
12595	4	457
12597	4	459
12518	4	308
12520	4	314
12522	4	317
12524	4	319
12526	4	328
12528	4	331
12530	4	333
12532	4	337
12534	4	340
12536	4	342
12538	4	351
12540	4	356
12542	4	358
12544	4	360
12546	4	363
12548	4	365
12550	4	368
12552	4	375
12554	4	378
12556	4	381
12558	4	383
12560	4	388
12562	4	393
12564	4	395
12566	4	397
12568	4	399
12570	4	403
12572	4	408
12574	4	413
12576	4	415
12578	4	419
12580	4	421
12582	4	427
12584	4	432
12586	4	437
12588	4	441
12590	4	445
12592	4	448
12594	4	453
12596	4	458
12598	4	462
10848	35	257
10850	35	260
10852	35	263
10854	35	269
10856	35	271
10858	35	273
10860	35	275
10862	35	280
10864	35	285
10866	35	288
10868	35	292
10870	35	298
10872	35	305
10874	35	308
10876	35	314
10878	35	319
10880	35	328
10882	35	332
10884	35	335
10886	35	339
10888	35	341
10890	35	351
10892	35	355
10894	35	357
10896	35	359
10898	35	361
10900	35	364
10902	35	367
10904	35	369
10906	35	376
10908	35	380
10910	35	382
10912	35	384
10914	35	388
10916	35	393
10918	35	395
10920	35	397
10922	35	399
10924	35	403
10926	35	408
10928	35	412
10930	35	415
10932	35	419
10934	35	425
10936	35	430
10938	35	433
10940	35	436
10942	35	438
10944	35	443
10946	35	448
10948	35	453
10950	35	457
10952	35	459
10954	36	2
10956	36	6
10958	36	12
10960	36	14
10962	36	17
10964	36	21
10966	36	24
10968	36	28
10970	36	36
10972	36	38
10974	36	41
10976	36	50
10978	36	52
10980	36	58
10982	36	60
10984	36	67
11912	10	43
11914	10	51
11916	10	55
11918	10	59
11920	10	61
11922	10	71
11924	10	74
12202	27	155
12204	27	159
12206	27	161
12208	27	164
12210	27	169
12212	27	172
12214	27	176
12216	27	181
12218	27	187
12220	27	189
12222	27	193
12224	27	196
12226	27	200
12228	27	204
12230	27	210
12232	27	216
12234	27	220
12236	27	225
12238	27	227
12240	27	234
12242	27	236
12244	27	238
12246	27	241
12248	27	247
12250	27	250
12252	27	254
12254	27	258
12256	27	262
12258	27	265
12260	27	269
12262	27	271
10985	36	71
10987	36	74
10989	36	77
10991	36	81
10993	36	84
10995	36	90
10997	36	92
10999	36	96
11001	36	101
11003	36	106
11005	36	111
11007	36	114
11009	36	116
11011	36	120
11013	36	125
11015	36	130
11017	36	134
11019	36	137
11021	36	139
11023	36	146
11025	36	149
11027	36	154
11029	36	157
11031	36	159
11033	36	161
11035	36	164
11037	36	168
11039	36	175
11041	36	179
11043	36	183
11045	36	187
11047	36	189
11049	36	193
12264	27	273
12266	27	275
12268	27	279
12270	27	282
12272	27	286
12274	27	290
12276	27	295
12278	27	304
12280	27	306
12282	27	310
12284	27	314
12286	27	318
12288	27	321
12290	27	329
12292	27	332
12294	27	335
12296	27	339
10986	36	72
10988	36	76
10990	36	80
10992	36	83
10994	36	89
10996	36	91
10998	36	94
11000	36	100
11002	36	104
11004	36	110
11006	36	112
11008	36	115
11010	36	118
11012	36	121
11014	36	129
11016	36	131
11018	36	135
11020	36	138
11022	36	141
11024	36	148
11026	36	152
11028	36	155
11030	36	158
11032	36	160
11034	36	162
11036	36	167
11038	36	170
11040	36	176
11042	36	181
11044	36	184
11046	36	188
11048	36	190
11050	36	195
11052	36	197
11054	36	201
11056	36	206
11058	36	216
11060	36	222
11062	36	226
11064	36	231
11066	36	235
11068	36	237
11070	36	239
11072	36	242
11074	36	248
11076	36	253
11078	36	257
11080	36	260
11082	36	263
11084	36	267
11086	36	270
11088	36	272
11090	36	274
11092	36	278
11094	36	280
11096	36	285
11098	36	288
11100	36	292
11102	36	296
11104	36	302
11106	36	305
11108	36	308
11110	36	312
11112	36	316
11114	36	318
11116	36	321
11118	36	329
11120	36	332
11122	36	335
11124	36	339
11126	36	341
11128	36	351
11130	36	354
11132	36	356
11134	36	358
11136	36	360
11138	36	363
11140	36	365
11142	36	368
11144	36	376
11146	36	380
11148	36	382
11150	36	384
11152	36	388
11154	36	393
11156	36	395
11158	36	397
11160	36	399
11162	36	403
11164	36	408
11166	36	411
11168	36	413
11170	36	419
11172	36	424
11174	36	427
11176	36	431
11178	36	433
11180	36	436
11182	36	438
11184	36	443
11186	36	447
11188	36	452
11190	36	455
11192	36	458
11194	36	462
11195	6	5
11197	6	12
11199	6	15
11201	6	18
11203	6	22
11205	6	24
11207	6	28
11209	6	34
12298	27	341
12300	27	351
12302	27	355
12304	27	357
12306	27	359
12308	27	361
12310	27	364
12312	27	368
12314	27	376
12316	27	380
12318	27	382
12320	27	384
12322	27	389
12324	27	393
12326	27	395
12328	27	397
12330	27	400
12332	27	404
12334	27	411
12336	27	413
12338	27	419
12340	27	421
12342	27	427
12344	27	432
12346	27	434
12348	27	437
12350	27	439
12352	27	443
12354	27	447
12356	27	451
12358	27	453
12360	27	458
12362	27	462
12265	27	274
11051	36	196
11053	36	200
11055	36	204
11057	36	207
11059	36	220
11061	36	225
11063	36	227
11065	36	234
11067	36	236
11069	36	238
11071	36	241
11073	36	247
11075	36	250
11077	36	254
11079	36	258
11081	36	262
11083	36	265
11085	36	269
11087	36	271
11089	36	273
11091	36	275
11093	36	279
11095	36	282
11097	36	286
11099	36	290
11101	36	295
11103	36	298
11105	36	304
11107	36	306
11109	36	310
11111	36	314
11113	36	317
11115	36	319
11117	36	328
11119	36	331
11121	36	333
11123	36	337
11125	36	340
11127	36	342
11129	36	353
11131	36	355
11133	36	357
11135	36	359
11137	36	361
11139	36	364
11141	36	367
12267	27	278
12269	27	280
12271	27	285
12273	27	288
12275	27	292
12277	27	298
12279	27	305
11143	36	369
11145	36	378
11147	36	381
11149	36	383
11151	36	387
11153	36	390
11155	36	394
11157	36	396
11159	36	398
11161	36	400
11163	36	404
11165	36	410
11167	36	412
11169	36	417
11171	36	420
11173	36	425
11175	36	430
11177	36	432
11179	36	434
11181	36	437
11183	36	441
11185	36	445
11187	36	448
11189	36	453
11191	36	457
11193	36	459
11196	6	10
11198	6	13
11200	6	17
11202	6	21
12281	27	308
12283	27	312
12285	27	316
12287	27	319
12289	27	328
12291	27	331
12293	27	333
12295	27	337
12297	27	340
12299	27	342
12301	27	354
12303	27	356
12305	27	358
12307	27	360
12309	27	363
12311	27	365
12313	27	369
12315	27	378
12317	27	381
12319	27	383
12321	27	388
12323	27	390
12325	27	394
12327	27	396
12329	27	398
12331	27	403
12333	27	408
12335	27	412
12337	27	417
12339	27	420
12341	27	425
12343	27	430
12345	27	433
12347	27	436
12349	27	438
12351	27	441
12353	27	445
12355	27	448
12357	27	452
12359	27	457
12361	27	459
11204	6	23
11206	6	25
11208	6	30
11210	6	36
11212	6	38
11214	6	46
11216	6	51
11218	6	55
11220	6	58
11222	6	60
11224	6	67
11226	6	72
11228	6	76
11230	6	81
11232	6	84
11234	6	89
11236	6	91
11238	6	94
11240	6	100
11242	6	104
11244	6	106
11246	6	110
11248	6	112
11250	6	114
11252	6	116
11254	6	120
11256	6	125
11258	6	130
11260	6	134
11262	6	137
11264	6	139
11266	6	146
11268	6	149
11270	6	154
11272	6	158
11274	6	160
11926	10	77
11928	10	81
11930	10	84
11932	10	90
11934	10	92
11936	10	96
11938	10	104
11940	10	106
11942	10	111
11944	10	114
11946	10	116
11948	10	120
11950	10	125
11952	10	130
11954	10	134
11956	10	136
11958	10	138
11960	10	141
11962	10	148
11964	10	152
11966	10	155
11968	10	159
11970	10	161
11972	10	164
11974	10	168
11976	10	172
11978	10	176
11980	10	181
11982	10	184
11984	10	188
11986	10	190
11988	10	195
11990	10	197
11992	10	201
11994	10	207
11996	10	216
11998	10	222
12000	10	225
12002	10	227
12004	10	234
12006	10	236
12008	10	238
12010	10	241
12012	10	247
12014	10	250
12016	10	253
12018	10	257
12020	10	260
12022	10	263
12024	10	267
12026	10	270
12028	10	272
12030	10	274
12032	10	279
12034	10	285
11211	6	37
11213	6	43
11215	6	50
11217	6	52
11219	6	56
11221	6	59
11223	6	61
11225	6	71
11227	6	74
11229	6	80
11231	6	83
11233	6	86
11235	6	90
11237	6	92
11239	6	96
11241	6	101
11243	6	105
11245	6	107
11247	6	111
11249	6	113
11251	6	115
11253	6	118
11255	6	121
11257	6	129
11259	6	131
11261	6	135
11263	6	138
11265	6	141
11267	6	148
11269	6	152
11271	6	155
11273	6	159
11275	6	162
11949	10	121
11951	10	129
11953	10	131
11955	10	135
11957	10	137
11959	10	139
11961	10	146
11963	10	149
11965	10	154
11967	10	158
11969	10	160
11971	10	162
11973	10	167
11975	10	170
11977	10	175
11979	10	179
11981	10	183
11983	10	187
11985	10	189
11987	10	193
11989	10	196
11991	10	200
11993	10	204
11995	10	213
11997	10	220
11999	10	224
12001	10	226
12003	10	231
12005	10	235
12007	10	237
12009	10	239
12011	10	242
12013	10	248
12015	10	252
12017	10	254
12019	10	258
12021	10	262
12023	10	265
12025	10	269
12027	10	271
12029	10	273
12031	10	275
12033	10	280
\.


--
-- TOC entry 3562 (class 0 OID 57508)
-- Dependencies: 242
-- Data for Name: product_categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_categories (id, product_id, category_predict_id) FROM stdin;
45	5	7
46	35	7
47	36	7
48	6	3
49	30	3
50	9	3
51	10	7
52	27	3
53	4	7
\.


--
-- TOC entry 3564 (class 0 OID 57512)
-- Dependencies: 244
-- Data for Name: product_color_enum; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_color_enum (product_id, color) FROM stdin;
5	GREY
5	BROWN
35	BLUE
30	BLACK
10	GREY
27	BLACK
27	GREY
9	BLACK
6	BLUE
4	GREEN
36	GREY
\.


--
-- TOC entry 3566 (class 0 OID 57516)
-- Dependencies: 246
-- Data for Name: product_size_enum; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_size_enum (product_id, size) FROM stdin;
5	L
5	XL
5	XXL
35	M
35	L
30	S
30	M
10	L
10	XL
27	S
27	M
9	XL
6	L
4	S
36	M
\.


--
-- TOC entry 3567 (class 0 OID 57519)
-- Dependencies: 247
-- Data for Name: product_tag; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_tag (id, product_id, tag_id) FROM stdin;
\.


--
-- TOC entry 3569 (class 0 OID 57523)
-- Dependencies: 249
-- Data for Name: response; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.response (id, response_text, intent_id) FROM stdin;
41	Rất vui khi được tư vấn cho bạn	26
42	Chào mừng bạn đến với shop thời trang! Shop có thể hỗ trợ gì cho bạn ạ	26
43	Shop có thể giúp gì cho bạn	26
44	Xin chào, tôi có thể giúp thể giúp gì cho quý khách?	26
45	Hẹn gặp lại quý khách	27
46	Chúc quý khách một ngày tốt lành	27
47	Hẹn quý khách một ngày không xa	27
48	Mong rằng quý khách sẽ trở lại sớm	27
49	Rất vui quý khách quay lại!	27
50	Rất vui khi được giúp đỡ	28
51	Đó là trách nhiệm của tôi	28
52	Gọi cho tôi bất cứ lúc nào cần thiết	28
54	Khách sáo quá ạ	28
55	Hân hạnh được giúp đã giúp đỡ bạn	28
56	Trân thành cảm ơn	28
59	Shop gửi sản phẩm mời anh/chị xem ạ	5
63	Dạ bên em có bán quần short giá đang sale. Mời quý khách xem qua ạ!	7
65	Dạ shop gửi các mẫu quần jean. Anh/chị xem qua ạ	9
66	Chúc Anh/Chị nhiều sức khỏe	27
81	Chúc bạn một ngày tốt lành và hẹn gặp lại!	28
82	Rất vui được phục vụ bạn!	28
83	Nếu có bất kỳ thắc mắc nào khác, đừng ngần ngại liên hệ Shop nha	28
85	Chào bạn! Shop có nhiều mẫu size. Bạn thích mẫu size nào ạ?	32
86	Chào bạn! Shop có bán mẫu áo khoác size L. Mời bạn xem!	31
87	Shop có bán loại áo khoác size XL. Mời bạn xem qua	33
88	Shop có mẫu size L và XL. Bạn thích xem size nào ạ	32
89	Shop có bán Áo khoác size L và XL. Shop gửi thông tin để bạn xem trước nha	34
90	Size L và XL Shop hiện tại còn sản phẩm. Mời bạn xem	34
91	Áo khoác size L và XL của shop còn bán. Mời bạn xem qua	34
92	Shop gửi bạn áo khoác size L. Mời xem	31
93	Shop gửi mẫu áo khoác size Xl. Mời xem	33
94	Bên Shop có 2 màu váy. Váy màu xanh và Váy mày xám. Bạn thích váy màu nào ạ?	30
95	Mình gửi váy size S và M. Bạn muốn xem size nào ạ	29
96	Hiện tại Shop có Váy size S và M. Bạn muốn xem size nào nhất ạ	29
97	Shop có nhiều loại váy với đa dạng màu ạ! Bạn chọn váy màu nào ạ?	6
98	Váy bên mình cho nhiều ạ. Không biết bạn chọn loại váy khích thước size như nào ạ?	6
99	Shop có nhiều loại váy với nhiều màu và kích thước size S và M. Không biết bạn chọn váy màu nào với kích thước như nào ạ?	6
100	Hiện tại Shop có bán váy với 2 màu xanh và màu xám. Bạn thích váy màu nào ạ?	30
101	Shop bên em còn Váy màu xám. Shop gửi thông tin về váy màu xám ạ!	35
102	Hiện tại Shop còn váy màu xám mà bạn đang muốn xem. Mời bạn xem qua ạ!	35
103	Hiện tại bên Shop còn hàng áo khoác ạ! Không biết bạn muốn xem áo khoác màu và size như nào ạ	3
104	Áo khoác Shop có nhiều màu và size. Bạn muốn xem áo khoác như nào ạ?	3
105	Shop có loại máy màu xanh rất đẹp a! Mời bạn xem	36
106	Váy màu xanh Shop còn hàng. Mời quý khách xem qua ạ	36
107	Hiện tại Shop còn váy màu xanh mà bạn đang cần. Mời bạn xem qua	36
108	Mình đây! Không biết bạn muốn mình tư vấn gì về trang phục ạ?	26
109	Shop hiện tại còn váy với hai màu xanh và màu xám! Mời bạn xem qua	37
110	Váy màu xanh và màu xám Shop còn hàng. Mời quý khách xem ạ!	37
111	Hên quá! Shop hiện tại váy còn 2 màu xanh và màu xám mà bạn đang cần. Mời bạn xem	37
112	Shop còn váy size S. Mời bạn xem qua	38
113	Hiện tại Shop còn váy size S. Mời bạn xem	38
114	Shop còn hàng váy size S. Mời quý khách xem	38
115	Shop còn hàng váy size M. Mời bạn xem	39
116	Hiện tại váy size M shop còn hàng ạ. Shop gửi bạn xem nha!	39
117	Váy size M shop có bán. Gửi thông tin váy cho bạn xem ạ!	39
118	Quá khen rồi ạ! Rất vui khi được giúp đỡ bạn!	28
119	Chúc bạn nhiều may mắn và gặp nhiều thành công	27
120	Shop gửi thông tin váy size S và M ạ! Mời bạn xem	40
121	Hiện tại shop còn váy size M và S. Shop gửi thông tin quý khách xem qua ạ!	40
122	Váy size M và S shop còn hàng ạ! Mời bạn xem	40
123	Shop gửi thông tin mẫu áo phông ạ!	5
124	Áo phông shop còn hàng. Mời bạn xem qua	5
125	Áo len shop còn hàng nha. Mời bạn xem qua	4
126	Shop vẫn còn hàng áo len. Shop gửi mẫu bạn xem qua	4
127	Hiện tại còn mẫu áo lên bạn đang cần. Shop gửi bạn!	4
128	Quần short bên mình còn hàng. Shop gửi thông tin ạ!	7
129	Shop có bán quần ngắn ạ. Mời bạn xem sản phẩm	7
130	Quần bó hoặc quần thun shop còn hàng ạ! Mời xem sản phẩm	8
131	Shop còn hàng quần thun hoặc quần bó ạ. Quý khách xem sản phẩm ạ!	8
132	Mẫu quần jean shop có nhiều ạ! Mời bạn xem qua	9
133	Shop còn mẫu quần jean ạ. Mời xem sản phẩm	9
\.


--
-- TOC entry 3571 (class 0 OID 57527)
-- Dependencies: 251
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tag (id, tag_name) FROM stdin;
1	Nam
2	Nữ
3	Khuyến mãi 2023
4	Thời trang rẻ đẹp
5	Trẻ trung
6	A
7	B
8	D
9	string
\.


--
-- TOC entry 3600 (class 0 OID 0)
-- Dependencies: 215
-- Name: ai_configs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ai_configs_id_seq', 2, true);


--
-- TOC entry 3601 (class 0 OID 0)
-- Dependencies: 218
-- Name: attribute_prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_prediction_id_seq', 463, true);


--
-- TOC entry 3602 (class 0 OID 0)
-- Dependencies: 220
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 50, true);


--
-- TOC entry 3603 (class 0 OID 0)
-- Dependencies: 222
-- Name: category_prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_prediction_id_seq', 23, true);


--
-- TOC entry 3604 (class 0 OID 0)
-- Dependencies: 224
-- Name: clothing_image_features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clothing_image_features_id_seq', 111419, true);


--
-- TOC entry 3605 (class 0 OID 0)
-- Dependencies: 226
-- Name: dictionaries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dictionaries_id_seq', 51, true);


--
-- TOC entry 3606 (class 0 OID 0)
-- Dependencies: 228
-- Name: fashion_net_models_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fashion_net_models_id_seq', 7, true);


--
-- TOC entry 3607 (class 0 OID 0)
-- Dependencies: 230
-- Name: histories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.histories_id_seq', 791, true);


--
-- TOC entry 3608 (class 0 OID 0)
-- Dependencies: 253
-- Name: history_nlus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.history_nlus_id_seq', 557, true);


--
-- TOC entry 3609 (class 0 OID 0)
-- Dependencies: 232
-- Name: intent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.intent_id_seq', 40, true);


--
-- TOC entry 3610 (class 0 OID 0)
-- Dependencies: 234
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_id_seq', 18, true);


--
-- TOC entry 3611 (class 0 OID 0)
-- Dependencies: 236
-- Name: order_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_product_id_seq', 34, true);


--
-- TOC entry 3612 (class 0 OID 0)
-- Dependencies: 238
-- Name: pattern_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pattern_id_seq', 430, true);


--
-- TOC entry 3613 (class 0 OID 0)
-- Dependencies: 241
-- Name: product_attributes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_attributes_id_seq', 12598, true);


--
-- TOC entry 3614 (class 0 OID 0)
-- Dependencies: 243
-- Name: product_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_categories_id_seq', 53, true);


--
-- TOC entry 3615 (class 0 OID 0)
-- Dependencies: 245
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 38, true);


--
-- TOC entry 3616 (class 0 OID 0)
-- Dependencies: 248
-- Name: product_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_tag_id_seq', 5, true);


--
-- TOC entry 3617 (class 0 OID 0)
-- Dependencies: 250
-- Name: response_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.response_id_seq', 133, true);


--
-- TOC entry 3618 (class 0 OID 0)
-- Dependencies: 252
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tag_id_seq', 9, true);


--
-- TOC entry 3336 (class 2606 OID 57550)
-- Name: ai_configs ai_configs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ai_configs
    ADD CONSTRAINT ai_configs_pkey PRIMARY KEY (id);


--
-- TOC entry 3338 (class 2606 OID 57552)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3340 (class 2606 OID 57554)
-- Name: attribute_prediction attribute_prediction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_prediction
    ADD CONSTRAINT attribute_prediction_pkey PRIMARY KEY (id);


--
-- TOC entry 3342 (class 2606 OID 57556)
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- TOC entry 3344 (class 2606 OID 57558)
-- Name: category_prediction category_prediction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category_prediction
    ADD CONSTRAINT category_prediction_pkey PRIMARY KEY (id);


--
-- TOC entry 3346 (class 2606 OID 57560)
-- Name: clothing_image_features clothing_image_features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clothing_image_features
    ADD CONSTRAINT clothing_image_features_pkey PRIMARY KEY (id);


--
-- TOC entry 3348 (class 2606 OID 57562)
-- Name: dictionaries dictionaries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dictionaries
    ADD CONSTRAINT dictionaries_pkey PRIMARY KEY (id);


--
-- TOC entry 3350 (class 2606 OID 57564)
-- Name: fashion_net_models fashion_net_models_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fashion_net_models
    ADD CONSTRAINT fashion_net_models_pkey PRIMARY KEY (id);


--
-- TOC entry 3352 (class 2606 OID 57566)
-- Name: histories histories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.histories
    ADD CONSTRAINT histories_pkey PRIMARY KEY (id);


--
-- TOC entry 3378 (class 2606 OID 122888)
-- Name: history_nlus history_nlus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_nlus
    ADD CONSTRAINT history_nlus_pkey PRIMARY KEY (id);


--
-- TOC entry 3354 (class 2606 OID 57568)
-- Name: intent intent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intent
    ADD CONSTRAINT intent_pkey PRIMARY KEY (id);


--
-- TOC entry 3356 (class 2606 OID 57570)
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- TOC entry 3358 (class 2606 OID 57572)
-- Name: order_product order_product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product
    ADD CONSTRAINT order_product_pkey PRIMARY KEY (id);


--
-- TOC entry 3360 (class 2606 OID 57574)
-- Name: pattern pattern_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pattern
    ADD CONSTRAINT pattern_pkey PRIMARY KEY (id);


--
-- TOC entry 3364 (class 2606 OID 57576)
-- Name: product_attributes product_attributes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_attributes
    ADD CONSTRAINT product_attributes_pkey PRIMARY KEY (id);


--
-- TOC entry 3366 (class 2606 OID 57578)
-- Name: product_categories product_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_categories
    ADD CONSTRAINT product_categories_pkey PRIMARY KEY (id);


--
-- TOC entry 3368 (class 2606 OID 57580)
-- Name: product_color_enum product_color_enum_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_color_enum
    ADD CONSTRAINT product_color_enum_pkey PRIMARY KEY (product_id, color);


--
-- TOC entry 3362 (class 2606 OID 57582)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- TOC entry 3370 (class 2606 OID 57584)
-- Name: product_size_enum product_size_enum_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_size_enum
    ADD CONSTRAINT product_size_enum_pkey PRIMARY KEY (product_id, size);


--
-- TOC entry 3372 (class 2606 OID 57586)
-- Name: product_tag product_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_tag
    ADD CONSTRAINT product_tag_pkey PRIMARY KEY (id);


--
-- TOC entry 3374 (class 2606 OID 57588)
-- Name: response response_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_pkey PRIMARY KEY (id);


--
-- TOC entry 3376 (class 2606 OID 57590)
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- TOC entry 3379 (class 2606 OID 57591)
-- Name: order_product order_product_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product
    ADD CONSTRAINT order_product_order_id_fkey FOREIGN KEY (order_id) REFERENCES public."order"(id);


--
-- TOC entry 3380 (class 2606 OID 57596)
-- Name: order_product order_product_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product
    ADD CONSTRAINT order_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3381 (class 2606 OID 57601)
-- Name: pattern pattern_intent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pattern
    ADD CONSTRAINT pattern_intent_id_fkey FOREIGN KEY (intent_id) REFERENCES public.intent(id);


--
-- TOC entry 3383 (class 2606 OID 57606)
-- Name: product_attributes product_attributes_attribute_predict_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_attributes
    ADD CONSTRAINT product_attributes_attribute_predict_id_fkey FOREIGN KEY (attribute_predict_id) REFERENCES public.attribute_prediction(id);


--
-- TOC entry 3384 (class 2606 OID 57611)
-- Name: product_attributes product_attributes_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_attributes
    ADD CONSTRAINT product_attributes_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3385 (class 2606 OID 57616)
-- Name: product_categories product_categories_category_predict_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_categories
    ADD CONSTRAINT product_categories_category_predict_id_fkey FOREIGN KEY (category_predict_id) REFERENCES public.category_prediction(id);


--
-- TOC entry 3386 (class 2606 OID 57621)
-- Name: product_categories product_categories_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_categories
    ADD CONSTRAINT product_categories_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3382 (class 2606 OID 57626)
-- Name: product product_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(id);


--
-- TOC entry 3387 (class 2606 OID 57631)
-- Name: product_color_enum product_color_enum_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_color_enum
    ADD CONSTRAINT product_color_enum_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3388 (class 2606 OID 57636)
-- Name: product_size_enum product_size_enum_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_size_enum
    ADD CONSTRAINT product_size_enum_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3389 (class 2606 OID 57641)
-- Name: product_tag product_tag_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_tag
    ADD CONSTRAINT product_tag_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 3390 (class 2606 OID 57646)
-- Name: product_tag product_tag_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_tag
    ADD CONSTRAINT product_tag_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- TOC entry 3391 (class 2606 OID 57651)
-- Name: response response_intent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_intent_id_fkey FOREIGN KEY (intent_id) REFERENCES public.intent(id);


-- Completed on 2024-02-25 18:34:19

--
-- PostgreSQL database dump complete
--

