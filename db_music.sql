CREATE TABLE IF NOT EXISTS typ_zanr (
	id_typ_zanr int NOT NULL GENERATED ALWAYS AS IDENTITY, 
	nazev VARCHAR(30) COLLATE "pg_catalog"."default" NOT NULL UNIQUE,
	CONSTRAINT unique_id_typ_zanr UNIQUE (id_typ_zanr)
);
INSERT INTO typ_zanr (
	nazev)
VALUES 
	('Rock'),
	('Pop'),
	('Folk');

CREATE TABLE IF NOT EXISTS album (
	id_album int NOT NULL GENERATED ALWAYS AS IDENTITY,
	id_typ_zanr INTEGER, 
	FOREIGN KEY (id_typ_zanr)
	REFERENCES typ_zanr(id_typ_zanr),
	nazev VARCHAR(30) NOT NULL,
	datum_vydani DATE NOT NULL,
	CONSTRAINT unique_id_album UNIQUE (id_album)
);
INSERT INTO album (
	id_typ_zanr, nazev, datum_vydani)
VALUES
	(1, 'Bílá', '2015-05-01'),
	(2, 'Koloběžka', '2017-04-01'),
	(3, 'Chart', '2016-08-01');

CREATE TABLE IF NOT EXISTS skladba (
	id_skladba int NOT NULL GENERATED ALWAYS AS IDENTITY,
	nazev VARCHAR(30) NOT NULL,
	delka TIME NOT NULL,
	CONSTRAINT unique_id_skladba UNIQUE (id_skladba)
);
INSERT INTO skladba (
	nazev, delka)
	VALUES 
	('S tebou', '00:03:15'),
	('Ráchel', '00:05:14'),
	('London', '00:04:13');

CREATE TABLE IF NOT EXISTS album_skladba (
	id_album_skladba int NOT NULL GENERATED ALWAYS AS IDENTITY,
	cislo_stopy INTEGER NOT NULL,
	id_album INTEGER NOT NULL,
	FOREIGN KEY (id_album)
	REFERENCES album(id_album)
	ON DELETE CASCADE,
	id_skladba INTEGER NOT NULL,
	FOREIGN KEY (id_skladba)
	REFERENCES skladba(id_skladba)
	ON DELETE CASCADE, 
	UNIQUE (cislo_stopy, id_album, id_skladba),
	CONSTRAINT unique_id_album_skladba UNIQUE (id_album_skladba)
);
INSERT INTO album_skladba (
	cislo_stopy, id_album, id_skladba)
	VALUES 
	(8, 3, 3),
	(4, 2, 1),
	(11, 1, 2);

CREATE TABLE IF NOT EXISTS typ_narodnost (
	id_typ_narodnost int NOT NULL GENERATED ALWAYS AS IDENTITY,
	nazev VARCHAR(30) COLLATE "pg_catalog"."default" NOT NULL UNIQUE,
	CONSTRAINT unique_id_typ_narodnost UNIQUE (id_typ_narodnost)
);
INSERT INTO typ_narodnost
	(nazev)
	VALUES 
	('Česká'),
	('Německá'),
	('Slovenská');

CREATE TABLE IF NOT EXISTS interpret (
	id_interpret int NOT NULL GENERATED ALWAYS AS IDENTITY,
	nazev VARCHAR(30) NOT NULL,
	id_typ_narodnost INTEGER NOT NULL,
	FOREIGN KEY (id_typ_narodnost)
	REFERENCES typ_narodnost(id_typ_narodnost)
	ON DELETE CASCADE,
	CONSTRAINT unique_id_interpret UNIQUE (id_interpret)
);
INSERT INTO interpret(
	nazev, id_typ_narodnost)
	VALUES 
	('Muk', 1),
	('Ramstein', 2),
	('Gombitová', 3);

CREATE TABLE IF NOT EXISTS album_interpret (
	id_album_interpret int NOT NULL GENERATED ALWAYS AS IDENTITY,
	id_album INTEGER NOT NULL,
	FOREIGN KEY (id_album)
	REFERENCES album(id_album)
	ON DELETE CASCADE,
	id_interpret INTEGER NOT NULL,
	FOREIGN KEY (id_interpret)
	REFERENCES interpret(id_interpret)
	ON DELETE CASCADE,
	CONSTRAINT unique_id_album_interpret UNIQUE (id_album_interpret)
);
INSERT INTO album_interpret (
	id_album, id_interpret)
	VALUES
	(3, 2),
	(2, 1),
	(1, 3);

-- Seznam všech alb včetně interpreta, počtu skladeb na albu. Seřazeno dle názvu interpreta a názvu alba
SELECT
  interpret.nazev AS interpret,
  album.nazev AS album,
  pocet_skladeb.pocet AS pocet_skladeb_na_albu
FROM
  interpret
JOIN
  album_interpret ON interpret.id_interpret = album_interpret.id_interpret
JOIN
  album ON album_interpret.id_album = album.id_album
JOIN
  (SELECT
     id_album,
     COUNT(id_skladba) AS pocet
   FROM
     album_skladba
   GROUP BY
     id_album
  ) AS pocet_skladeb ON album.id_album = pocet_skladeb.id_album
ORDER BY
  interpret.nazev,
  album.nazev;
-- pozn. 1 album může mít více interpretů.

-- Najít album včetně interpreta, které obsahuje nejdelší písničku
SELECT
  i.nazev AS interpret,
  a.nazev AS album,
  s.nazev AS nejdelsi_pisnicka,
  s.delka AS delka_pisnicky
FROM interpret i
JOIN album_interpret ai ON i.id_interpret = ai.id_interpret
JOIN album a ON ai.id_album = a.id_album
JOIN album_skladba asl ON a.id_album = asl.id_album
JOIN skladba s ON asl.id_skladba = s.id_skladba
ORDER BY s.delka ASC
LIMIT 1;	
-- pozn. 1 albu může mít více interpretů.
