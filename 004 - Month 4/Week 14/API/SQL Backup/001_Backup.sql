PGDMP      ;                |           fastapi    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    fastapi    DATABASE     �   CREATE DATABASE fastapi WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE fastapi;
                postgres    false            �            1259    16513    posts    TABLE       CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    content character varying NOT NULL,
    published boolean DEFAULT true NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    owner_id integer NOT NULL
);
    DROP TABLE public.posts;
       public         heap    postgres    false            �            1259    16512    posts_id_seq    SEQUENCE     �   CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.posts_id_seq;
       public          postgres    false    218            �           0    0    posts_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;
          public          postgres    false    217            V           2604    16516    posts id    DEFAULT     d   ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);
 7   ALTER TABLE public.posts ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    16513    posts 
   TABLE DATA           T   COPY public.posts (id, title, content, published, created_at, owner_id) FROM stdin;
    public          postgres    false    218   a       �           0    0    posts_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.posts_id_seq', 25, true);
          public          postgres    false    217            Z           2606    16522    posts posts_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pkey;
       public            postgres    false    218            [           2606    16523    posts posts_owner_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.users(id) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_owner_id_fkey;
       public          postgres    false    218            �   �  x���mn� ��S�E�1���	��f�*�(D\���D��ZM:@Xzal���m.3�z�5_�L�T��'�O�F�A� (��[�A�kn��U�E��}�h
�H���z��`~a�d��n'��S,�4�KyMHJ<�:��M%M�o?A��XKC� � ^������t��)��y����WB��J���Bx�q�!�GXN�C�������xc)1�kNE[�Ծ8���j�OR��"��))���9�U�h�����;�-�l����4���I�O���NP �s�� ��%�#���Q{i�5f�;JЭ64�ݽ�b*�:��� �oQY�f��}j��\`��8p~U���5�Z�؟���s�!u+Ab��MS��j �65�/QO�ؓS��~R��"��w���o�#�a� Cf|�     