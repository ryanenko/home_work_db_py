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


INSERT INTO music_genre(name) VALUES('Рок'), ('Поп-музыка'), ('Хип-Хоп'), ('Шансон'), ('Джаз');

INSERT INTO music_artist(name) VALUES('Баста'), ('Ночные снайперы'), 
('Каста'), ('Михаил Шуфутинский'), ('Лариса Долина'), ('Алиса'),('Полина Гагарина'), ('Егор Крид');

INSERT INTO music_album(name, year_of_release) 
VALUES('Баста 5. Часть 2', 2016), 
('Вдох', 2022), ('Лучшие песни', 2014), 
('Альбомба', 2021), ('02.Deluxe', 2020), ('Ресторанный хит', 2016), 
('Мы вместе 20 лет', 2003), ('По встречной', 2020), ('Pussy Boy', 2021);


INSERT INTO single(name, duration, music_album_ID) 
VALUES('Финальный матч', 4.38, 1), ('Выпускной(Медлячок)',5.35, 1), 
('Мои разбитые мечты', 3.45, 1), ('Бабочки', 3.08, 2), ('Вдох', 2.59, 2), 
('Корабельная песня', 4.00, 3),('Вокруг шум', 3.33, 3), ('Я чувак', 2.53, 4), 
('Турбочелюсть', 2.12, 4), ('Заметь', 3.51, 5), ('Авиарежим', 2.58, 5), 
('Наколочка', 3.57, 6), ('Марджанджа', 3.18, 6), ('Небо славян', 4.47, 7), 
('По встречной', 4.03, 8), ('PUSSY BOY', 2.14, 9);

INSERT INTO music_collection(name, date_of_release) 
VALUES('Русский рэп', 2021), 
('Популярная музыка', 2022), ('ГангстаРэп', 2017), 
('Русский хит', 2021), ('РОК. Лучшее', 2020), ('Песни для караоке', 2022), 
('Классика российской эстрады', 2021), ('Музыка в машину', 2020);


INSERT INTO genre_artist VALUES(1, 2), (1, 6), (2, 7), (2, 8), (3, 1), (3, 3), (4, 4), (5, 5);

INSERT INTO album_artist VALUES(1, 1), (2, 7), (3, 3), (4, 3), (5, 2), (6, 4), (7, 6), (8, 4), (9, 9);

INSERT INTO single_collection VALUES(17, 1), (17, 2), (17, 6), (18, 4), (18, 5), (18, 16), (19, 2), (19, 7), (20, 2), (20, 8), (20, 15), (21, 10), (21, 11), (21, 14), (22, 2), (22, 12), (22, 13), (22, 15), (23, 5), (23, 3), (23, 6), (24, 9), (24, 10), (24, 16)