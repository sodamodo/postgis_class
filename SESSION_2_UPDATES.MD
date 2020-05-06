CREATE TABLE polygon(
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	geom geometry(POLYGON, 32610)
);

SELECT id, name FROM polygon;

CREATE TABLE polygon_centroid AS (SELECT ST_Centroid(geom) FROM polygon);

CREATE TABLE points(
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	geom geometry(POINT, 32610)
);

SELECT * FROM points;

SELECT point.name, ST_Contains(point.geom, poly.geom) FROM points point, polygon poly;

SELECT ST_IsEmpty(geom) FROM polygon;

SELECT ST_IsEmpty(geom) FROM points;

DROP TABLE coffee_shops;

CREATE TABLE coffee_shops
	(
	  name character varying(50),
	  address character varying(50),
	  city character varying(50),
	  state character varying(50),
	  zip character varying(5),
	  lat numeric,
	  lon numeric,
	  price int	
	);
	
SELECT * FROM coffee_shops;	

ALTER TABLE coffee_shops ADD COLUMN geom geometry(POINT,32610);

SELECT * FROM coffee_shops;	

UPDATE coffee_shops SET geom = ST_SetSRID(ST_MakePoint(lon,lat), 32610);

ALTER TABLE coffee_shops ADD COLUMN price_phrase VARCHAR;

SELECT * FROM coffee_shops;

UPDATE coffee_shops SET price_phrase = 'low' WHERE price = 1;

SELECT * FROM coffee_shops;

UPDATE coffee_shops SET price_phrase = 'medium' WHERE price = 2;
UPDATE coffee_shops SET price_phrase = 'high' WHERE price = 3;

SELECT * FROM coffee_shops;

SELECT COUNT(*) FROM coffee_shops;

SELECT COUNT(*), price_phrase FROM coffee_shops GROUP BY price_phrase;

UPDATE coffee_shops SET geom = ST_SetSRID(ST_MakePoint(lon,lat), 32610);


ALTER TABLE coffee_shops DROP COLUMN geom;

ALTER TABLE coffee_shops ADD COLUMN geom geometry(POINT,4326);

UPDATE coffee_shops SET geom = ST_SetSRID(ST_MakePoint(lon,lat), 4326);

SELECT * FROM coffee_shops;

SELECT Find_SRID('public', 'coffee_shops', 'geom');

SELECT * FROM cambridge_neighborhoods;

SELECT cambridge_neighborhoods.name as name, count(*)
	FROM coffee_shops, cambridge_neighborhoods
	WHERE ST_Intersects(coffee_shops.geom, cambridge_neighborhoods.geom)
	GROUP BY cambridge_neighborhoods.name;

SELECT * FROM coffee_shops;
	
	
SELECT cambridge_neighborhoods.name as name, count(*)
	FROM coffee_shops, cambridge_neighborhoods
	WHERE ST_Intersects(coffee_shops.geom, cambridge_neighborhoods.geom) AND coffee_shops.price_phrase = 'low'
	GROUP BY cambridge_neighborhoods.name;
	

CREATE TABLE polygon(id SERIAL PRIMARY KEY, geom geometry(POLYGON, 4326));


SELECT * FROM polygon;

DROP TABLE IF EXISTS reservoir;
CREATE TABLE reservoir AS (SELECT * FROM polygon WHERE name = 'Reservoir ');

SELECT * FROM polygon;
CREATE TABLE othergon AS (SELECT * FROM polygon WHERE name = 'Othergon');

CREATE TABLE geo_union AS (
	SELECT ST_Union(reservoir.geom, othergon.geom) FROM reservoir, othergon
);

SELECT * FROM geo_union;

