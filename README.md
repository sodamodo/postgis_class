# postgis_class


#### Create a table with a variety of data types

```SQL
CREATE TABLE burgers
	(
	  name VARCHAR(20),
	  origin_state CHAR(2),
	  price NUMERIC,
	  quantity INTEGER,
	  vegetarian BOOLEAN
	);

```

* Always use single quotes!

```INSERT INTO burgers VALUES ('cheese burger', 'WA', 2.34, 5, NO)




```SQL
`CREATE EXTENSION postgis;`
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

##### Select by distinct 

##### Select WHERE

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


##### Harvard dist

```SQL
ALTER TABLE parcel_points ADD COLUMN harvard_dist DOUBLE PRECISION;

WITH query AS (
	SELECT ST_Distance(ST_SetSRID(ST_Point(42.3770, -71.1167), 4326), geom) AS distance, type, sub_type, area, value, geom FROM parcel_points_subset
)

UPDATE parcel_points_subset SET harvard_dist = query.distance FROM query;
```




SELECT ST_Distance(ST_SetSRID(ST_Point(42.3770, -71.1167), 4326), geom) AS distance FROM parcel_points ORDER BY distance DESC; 

#### Universities 
```SQL
ALTER TABLE universities ADD COLUMN geom geometry(POINT,4326);

UPDATE universities SET geom = ST_SetSRID(ST_Point(lon, lat),4326)
```




##### THINGS TO PUT INTO

* Select by distance to location
* Intersects with incidences of crime
