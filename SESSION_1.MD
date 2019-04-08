Load shapefiles into PgAdmin4
Install PgAdmin4

### Loading shapefiles
shp2pgsql - http://www.bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg
ogr2ogr
## Geography vs Geometry 

#### Funcs

#### ST_Segmentize
Can only be used in geography!



##### ST_Distance
Gives the distance between two features. Notice that the features are in the Geometry data type,
but in order for the output to be in meters instead of decimal degrees, you need to cast it using the 
<column_name>::[datatype]

```SQL
SELECT  * FROM points;

WITH one AS (SELECT geom FROM points WHERE name = 'Zam'),
two AS (SELECT geom FROM points WHERE name = 'PAP')

SELECT ST_Distance(one.geom:: geography, two.geom:: geography) FROM one, two;
```

##### ST_Union
```SQL

DROP TABLE IF EXISTS polygon_union;
CREATE TABLE polygon_union AS (
				SELECT ST_Union(geom) FROM polygon
				);
SELECT * FROM polygon_union;


```

*Subdivide
*Disolve
* ST_Segmentize 
#### Foreign Key

```SQL
CREATE TABLE tests 
( 
   subject_id SERIAL,
   subject_name text,
   highestStudent_id integer REFERENCES students
);

CREATE TABLE students 
( 
  student_id SERIAL PRIMARY KEY,
  player_name TEXT
);
```
#### Common Table Expression

```SQL
WITH subquery AS (SELECT * FROM X)
```


###  Exercise

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


ALTER TABLE parcel_points ADD COLUMN geom geometry(POINT,4326);


UPDATE parcel_points SET geom = ST_SetSRID(ST_Point(lon, lat),4326)
	

CREATE TABLE universities(
	name VARCHAR,
	geom GEOMETRY(POINT, 4326)

);

```
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
```

### Rando dump
DELETE FROM lines;

DROP TABLE IF EXISTS segmented_line;

CREATE TABLE segmented_line AS (
		SELECT ST_Segmentize(geog, 1200000) FROM lines

);


SELECT * FROM segmented_line;

SELECT ST_AsText(st_segmentize) FROM segmented_line;

SELECT * FROM _segmented_line;

SELECT ST_Segmentize('LINESTRING(1 2, 3 4)'::geometry,0.5)

DELETE FROM lines;
INSERT INTO lines (name, geog) VALUES ('unsegmented', ST_GeomFromText('LINESTRING(1 2, 3 4)'));

DELETE FROM lines WHERE id = 4;

SELECT * FROM lines;

SELECT * FROM segmented_line;

SELECT * FROM commercial_parcels LIMIT 100;


##### ST_Union
```SQL

DROP TABLE IF EXISTS polygon_union;
CREATE TABLE polygon_union AS (
				SELECT ST_Union(geom) FROM polygon
				);
SELECT * FROM polygon_union;


```

*Subdivide
*Disolve
* ST_Segmentize 
#### Foreign Key

```SQL
CREATE TABLE tests 
( 
   subject_id SERIAL,
   subject_name text,
   highestStudent_id integer REFERENCES students
);

CREATE TABLE students 
( 
  student_id SERIAL PRIMARY KEY,
  player_name TEXT
);
```
#### Common Table Expression

```SQL
WITH subquery AS (SELECT * FROM X)
```
