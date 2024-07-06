PGDMP      %                |           fastapi    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    fastapi    DATABASE     �   CREATE DATABASE fastapi WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE fastapi;
                postgres    false            �            1259    16400    products    TABLE       CREATE TABLE public.products (
    name character varying NOT NULL,
    price integer NOT NULL,
    id integer NOT NULL,
    is_sale boolean DEFAULT false,
    inventory integer DEFAULT 0 NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16399    products_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.products_id_seq;
       public          postgres    false    216            �           0    0    products_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;
          public          postgres    false    215            O           2604    16403    products id    DEFAULT     j   ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);
 :   ALTER TABLE public.products ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �          0    16400    products 
   TABLE DATA           S   COPY public.products (name, price, id, is_sale, inventory, created_at) FROM stdin;
    public          postgres    false    216   %       �           0    0    products_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.products_id_seq', 19, true);
          public          postgres    false    215            T           2606    16407    products products_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    216            �   >  x����n�0���S��l'!m���4�1i� �Z�#�����-�&�RQ��o�^����Pn�GhGhb�J�M�ՙ�Fsؕ0����p��|2hz��W�S �:憰9��2�[b�N<���W��J��)3�sU��H�ș{��b[}m%H�K��o�;v-���lm��T*1��M�|����ʝ��0< ����o���xG0����"<(}C�y��e�2��	����
����9rB�1�_`1�\��ӿNg���vw�fW�#BݔU����K`׈D@�u*#�Z�-�������     