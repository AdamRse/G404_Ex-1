--
-- PostgreSQL database dump
--

\restrict vcME3LPf36bdhq6BVCEfrIz3L2rjFx8jRMp9jWwfK7uVTVHQr6mJBYsC1rHawl1

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: jeux_de_societe; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.jeux_de_societe (
    id integer NOT NULL,
    nom character varying(80) NOT NULL,
    editeur character varying(50),
    type_jeu character varying(30),
    nb_joueurs_min integer,
    nb_joueurs_max integer,
    duree_minutes integer,
    note_moyenne numeric(3,1),
    prix numeric(5,2),
    annee_sortie integer,
    est_cooperatif boolean
);


--
-- Data for Name: jeux_de_societe; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.jeux_de_societe (id, nom, editeur, type_jeu, nb_joueurs_min, nb_joueurs_max, duree_minutes, note_moyenne, prix, annee_sortie, est_cooperatif) FROM stdin;
1	Les Aventuriers du Rail	Days of Wonder	Stratégie	2	5	45	7.5	44.90	2004	f
2	Catan	Kosmos	Stratégie	3	4	90	7.3	39.90	1995	f
3	Carcassonne	Hans im Glück	Stratégie	2	5	45	7.4	29.90	2000	f
4	Pandemic	Z-Man Games	Coopératif	2	4	45	7.6	39.90	2008	t
5	7 Wonders	Repos Production	Stratégie	2	7	30	7.7	44.90	2010	f
6	Dixit	Libellud	Ambiance	3	6	30	7.2	29.90	2008	f
7	Ticket to Ride: Europe	Days of Wonder	Stratégie	2	5	60	7.6	44.90	2005	f
8	Azul	Plan B Games	Abstrait	2	4	45	7.8	34.90	2017	f
9	Codenames	Czech Games Edition	Ambiance	2	8	15	7.6	19.90	2015	f
10	Gloomhaven	Cephalofair Games	Aventure	1	4	120	8.7	139.90	2017	t
11	Terraforming Mars	FryxGames	Stratégie	1	5	120	8.4	64.90	2016	f
12	Wingspan	Stonemaier Games	Stratégie	1	5	70	8.1	54.90	2019	f
13	Splendor	Space Cowboys	Stratégie	2	4	30	7.4	32.90	2014	f
14	King of Tokyo	IELLO	Ambiance	2	6	30	7.0	34.90	2011	f
15	Munchkin	Steve Jackson Games	Aventure	3	6	90	6.5	24.90	2001	f
16	Unlock!	Space Cowboys	Coopératif	1	6	60	7.3	29.90	2017	t
17	Dominion	Rio Grande Games	Deck-building	2	4	30	7.6	39.90	2008	f
18	Scythe	Stonemaier Games	Stratégie	1	5	115	8.2	79.90	2016	f
19	The Crew	Kosmos	Coopératif	2	5	20	7.8	14.90	2019	t
20	Everdell	Starling Games	Stratégie	1	4	80	8.0	59.90	2018	f
21	Love Letter	Z-Man Games	Bluff	2	4	20	7.1	11.90	2012	f
22	Root	Leder Games	Stratégie	2	4	90	8.1	54.90	2018	f
23	Brass: Birmingham	Roxley Games	Stratégie	2	4	120	8.6	64.90	2018	f
24	Spirit Island	Greater Than Games	Coopératif	1	4	120	8.3	69.90	2017	t
25	Sushi Go!	Gamewright	Famille	2	5	15	7.2	12.90	2013	f
26	7 Wonders Duel	Repos Production	Stratégie	2	2	30	8.1	24.90	2015	f
27	Hanabi	R&R Games	Coopératif	2	5	25	7.3	10.90	2010	t
28	Takenoko	Matagot	Famille	2	4	45	7.3	34.90	2011	f
29	Patchwork	Lookout Games	Abstrait	2	2	30	7.7	24.90	2014	f
30	Arkham Horror	Fantasy Flight Games	Coopératif	1	6	180	7.4	59.90	2005	t
31	Agricola	Lookout Games	Stratégie	1	5	120	7.9	49.90	2007	f
32	Puerto Rico	Rio Grande Games	Stratégie	2	5	150	8.0	44.90	2002	f
33	Power Grid	Rio Grande Games	Stratégie	2	6	120	7.8	39.90	2004	f
34	Twilight Struggle	GMT Games	Stratégie	2	2	180	8.3	54.90	2005	f
35	Through the Ages	Czech Games Edition	Stratégie	2	4	240	8.2	64.90	2006	f
36	Race for the Galaxy	Rio Grande Games	Stratégie	2	4	60	7.7	34.90	2007	f
37	Le Havre	Lookout Games	Stratégie	1	5	150	7.6	49.90	2008	f
38	Stone Age	Hans im Glück	Stratégie	2	4	90	7.5	39.90	2008	f
39	Small World	Days of Wonder	Stratégie	2	5	80	7.3	44.90	2009	f
40	Jaipur	GameWorks	Stratégie	2	2	30	7.5	19.90	2009	f
41	Kingdomino	Blue Orange	Famille	2	4	20	7.3	19.90	2016	f
42	Lost Cities	Kosmos	Stratégie	2	2	20	7.2	14.90	1999	f
43	Hanamikoji	Deep Water Games	Stratégie	2	2	15	7.6	14.90	2013	f
44	The Quacks of Quedlinburg	Schmidt Spiele	Famille	2	4	45	7.8	34.90	2018	f
45	Welcome To...	Blue Cocker	Famille	1	100	25	7.5	24.90	2018	f
46	Just One	Repos Production	Ambiance	3	7	20	7.6	19.90	2018	f
47	Detective: A Modern Crime Board Game	Portal Games	Coopératif	1	5	180	7.9	49.90	2018	t
48	Nemesis	Awaken Realms	Coopératif	1	5	120	8.1	129.90	2018	t
49	Gloomhaven: Jaws of the Lion	Cephalofair Games	Aventure	1	4	90	8.5	49.90	2020	t
50	Dune: Imperium	Dire Wolf	Stratégie	1	4	90	8.0	54.90	2020	f
51	Wingspan: Oceania Expansion	Stonemaier Games	Stratégie	1	5	70	8.0	29.90	2020	f
52	Calico	Flatout Games	Abstrait	1	4	45	7.7	39.90	2020	f
53	Cascadia	Flatout Games	Abstrait	1	4	45	7.9	39.90	2021	f
54	Ark Nova	Capstone Games	Stratégie	1	4	150	8.5	74.90	2021	f
55	Dune	Gale Force Nine	Stratégie	2	6	120	7.4	49.90	2019	f
56	The Crew: Mission Deep Sea	Kosmos	Coopératif	2	5	20	7.9	14.90	2021	t
57	Heat: Pedal to the Metal	Days of Wonder	Stratégie	1	6	60	7.8	49.90	2022	f
58	Earth	Inside Up Games	Stratégie	1	5	90	7.6	54.90	2023	f
59	Sky Team	Scorpion Masque	Coopératif	2	2	20	8.0	24.90	2023	t
60	Harmonies	Libellud	Abstrait	1	4	30	7.5	29.90	2024	f
\.


--
-- Name: jeux_de_societe jeux_de_societe_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.jeux_de_societe
    ADD CONSTRAINT jeux_de_societe_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict vcME3LPf36bdhq6BVCEfrIz3L2rjFx8jRMp9jWwfK7uVTVHQr6mJBYsC1rHawl1

