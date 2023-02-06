###Создание базы данных

CREATE DATABASE homework_db

###Создание таблиц с параметрами

CREATE TABLE IF NOT EXISTS music_artist
(
	music_artist_ID serial PRIMARY KEY,
	name text NOT NULL);

CREATE TABLE IF NOT EXISTS music_genre
(
	music_genre_ID serial PRIMARY KEY,
	name text NOT NULL,);


###Создание таблицы 'многие к многим'

CREATE TABLE genre_artist
(
	music_genre_ID int REFERENCES music_genre(music_genre_ID),
	music_artist_ID int REFERENCES music_artist(music_artist_ID),
	CONSTRAINT genre_artist_pkey PRIMARY KEY(music_genre_ID, music_artist_ID));
	
###Создание таблиц с параметрами 

CREATE TABLE IF NOT EXISTS music_album
(
	music_album_ID serial PRIMARY KEY,
	name text NOT NULL,
	year_of_release int NOT NULL);

###Создание таблицы 'многие к многим'

CREATE TABLE IF NOT EXISTS album_artist
(
	music_album_ID int REFERENCES music_album(music_album_ID),
	music_artist_ID int REFERENCES music_artist(music_artist_ID),
	CONSTRAINT album_artist_pkey PRIMARY KEY(music_album_ID, music_artist_ID));

###Создание таблиц с параметрами

CREATE TABLE IF NOT EXISTS single
(
	single_ID serial PRIMARY KEY,
	name text NOT NULL,
	duration real NOT NULL,
	music_album_ID int REFERENCES music_album(music_album_ID));	
	
CREATE TABLE IF NOT EXISTS music_collection
(
	music_collection_ID serial PRIMARY KEY,
	name text NOT NULL,
	date_of_release real NOT NULL);
	
###Создание таблицы 'многие к многим'

CREATE TABLE IF NOT EXISTS single_collection
(
	music_collection_ID int REFERENCES music_collection(music_collection_ID),
	single_ID int REFERENCES single(single_ID),
	CONSTRAINT single_collection_pkey PRIMARY KEY(music_collection_ID, single_ID));	