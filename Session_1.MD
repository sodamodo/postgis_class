# postgis_class


#### Create a table with a variety of data types

```SQL
CREATE EXTENSION postgis;
```


```SQL
CREATE TABLE burgers
	(
	  id SERIAL PRIMARY KEY,
	  name VARCHAR(20),
	  origin_state CHAR(2),
	  price NUMERIC,
	  quantity INTEGER,
	  vegetarian BOOLEAN
	);

```
```SQL
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('bob''s burgers', 'NJ', 5.95, 2, FALSE);
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('veggie town', 'CA', 5.95, 5, TRUE);
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('the slab', 'TX', 25.95, 10, FALSE);
```

SELECTIONS

```SQL
SELECT * FROM burgers WHERE quantity > 3;
```

SELECT * FROM burgers WHERE quantity > 3 AND vegetarian = TRUE;


#### Insert Data into table



```SQL
SELECT * FROM foods INNER JOIN foods_reviews ON foods.name = foods_reviews.name;

```SQL

* Always use single quotes!
* USE EXPLICIT ORDERING 
```SQL

INSERT INTO burgers VALUES ('cheese burger', 'WA', 2.34, 5, False)

```


#### Create points table
```SQL
CREATE TABLE points (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	geom geometry(POINT, 4326)
)
```
#### Insert points

```SQL
	INSERT INTO points VALUES('first', ST_SetSRID(ST_GeomFromText('POINT(-71.064544 42.28787)'), 4326))


SELECT * FROM points;
```
* Go to QGIS


```SQL
CREATE TABLE line (
	##### SETUP ID
	line_name VARCHAR,
	geom GEOMETRY(LINESTRING, 4326)
);

INSERT INTO line VALUES('first line', ST_GeomFromText('LINESTRING(10 5, 10 6, 10 9, 11 9)', 4326));


SELECT ST_Length(geom) FROM line;
SELECT ST_Length(geom:: geography) FROM line;
```


```SQL
CREATE TABLE buffered_lines AS (
	SELECT ST_Buffer(geom, 100) FROM line
);
```

```SQL

SELECT * FROM line;

SELECT ST_AsGeoJSON(geom) FROM line;


SELECT * FROM buffered_lines;
SELECT ST_AsGeoJSON(st_buffer) FROM buffered_lines;
```




```SQL
CREATE TABLE polygon(name VARCHAR, geom GEOMETRY(POLYGON,4326));


INSERT INTO polygon VALUES('Polygonner', ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))', 4326));

```

##### Change SRID

```SQL

SELECT geom FROM points
SELECT ST_Transform(geom, 6855) FROM points
```


##### ST_Difference 
```SQL
WITH buffered_lines AS (SELECT * FROM buffered_lines)	
SELECT ST_Difference(buffered_lines.st_buffer, polygon.geom) FROM polygon, buffered_lines


CREATE TABLE intersection AS(
	WITH buffered_lines AS (SELECT * FROM buffered_lines)	
	SELECT ST_Difference(buffered_lines.st_buffer, polygon.geom) FROM polygon, buffered_lines
);

```


##### EXERCISE CREATE TWO FEATURES, BUFFER THEM, and CREATE INTERSECT



Difference + Buffer

```SQL

CREATE TABLE difference_buffer AS(
	WITH points AS (SELECT * FROM points)

	SELECT ST_Difference(ST_Buffer(points.geom, .1), polygon.geom) FROM points, polygon
);
```

##### create table / data types

```SQL
CREATE TABLE coffee_shops
	(

	  name VARCHAR(50),
	  address VARCHAR(50),
	  city VARCHAR(50),
	  state VARCHAR(50),
	  zip VARCHAR(10),
	  lat VARCHAR(50),
	  lon VARCHAR(50),
	  price VARCHAR(50)
	);

```

##### Change Data Types

```
ALTER TABLE coffee_shops 
ALTER COLUMN price TYPE NUMERIC USING price::numeric;
```
##### New column

`ALTER TABLE coffee_shops ADD COLUMN price_word VARCHAR(5);`
* SET THE WORD LEVEL HERE*


###### Spatial Data Types

* ###### Geometry 
* ###### Geography


##### CREATE NEW COLUMN
```SQL
ALTER TABLE coffee_shops
	ADD COLUMN geom geometry(POINT,4326)
```

##### Set to geom

```SQL
UPDATE coffee_shops SET geom = ST_SetSRID(ST_Point(lon, lat),4326)
```
##### Create Parcel Points Table


```SQL
CREATE TABLE parcel_points (
	lat VARCHAR(50),
	lon VARCHAR(50),
	type VARCHAR(50),
	sub_type VARCHAR(50),
	area VARCHAR(50),
	value VARCHAR(50)
);
```


##### Update for geometry 
```
ALTER TABLE parcel_points 
ALTER COLUMN lat TYPE NUMERIC USING lat::numeric;

ALTER TABLE parcel_points 
ALTER COLUMN lon TYPE NUMERIC USING lon::numeric;


ALTER TABLE parcel_points
	ADD COLUMN geom geometry(POINT,4326);


UPDATE parcel_points SET geom = ST_SetSRID(ST_Point(lon, lat),4326)
	
```
CREATE TABLE universities(
	name VARCHAR,
	geom GEOMETRY(POINT, 4326)

);


```SQL
INSERT INTO universities VALUES('Harvard', ST_SetSRID(ST_Point(-71.1167, 42.3770), 4326)); 


CREATE TABLE harvard_buffer AS (SELECT name, ST_Buffer(geom:: geography, 800) AS geom FROM universities WHERE name = 'Harvard');

CREATE TABLE harvard_buffer AS (SELECT name, ST_Buffer(geom:: geography, 1000) AS geom FROM universities WHERE name = 'Harvard');

CREATE TABLE commercial_parcels AS (
	SELECT * FROM parcel_points WHERE type = 'Commercial'
);


ALTER TABLE commercial_parcels ALTER COLUMN area TYPE numeric USING area::numeric; 
ALTER TABLE commercial_parcels ALTER COLUMN value TYPE numeric USING value::numeric; 

ALTER TABLE commercial_parcels ADD COLUMN val_per_area NUMERIC;

UPDATE commercial_parcels SET val_per_area = value / area WHERE area != 0 AND value != 0;


CREATE TABLE parcels_near_harvard AS (
	SELECT commercial_parcels.geom, commercial_parcels.val_per_area FROM commercial_parcels, harvard_buffer WHERE ST_Contains(commercial_parcels.geom, harvard_buffer.geom:: geometry)

);

```


```SQL
DROP TABLE IF EXISTS parcels_within;

CREATE TABLE parcels_within AS (
	
SELECT ST_DWithin(ST_SetSRID(ST_Point(42.3770, -71.1167), 4326), geom, 200) AS within, id, geom, value, type FROM parcel_points_copy


);

SELECT COUNT(*) FROM parcels_within WHERE within = TRUE AND type = 'Commercial';

CREATE TABLE coffee_shops_buffer AS (
	SELECT ST_Buffer(geom, 100) FROM coffee_shops

	);

```

##### THINGS TO PUT INTO

* Select by distance to location
* Intersects with incidences of crime
