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
SELECT * FROM burgers
```

```SQL
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('bob''s burgers', 'NJ', 5.95, 2, FALSE);
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('veggie town', 'CA', 5.95, 5, TRUE);
INSERT INTO burgers(name, origin_state, price, quantity, vegetarian) VALUES('the slab', 'TX', 25.95, 10, FALSE);
```

```SQL
SELECT price FROM burgers;
```

```SQL
SELECT price:: INT FROM burgers;
```

```SQL
ALTER TABLE burgers ADD COLUMN cheap BOOLEAN;
```

```SQL
UPDATE burgers SET cheap = TRUE where price < 10;
```

SELECTIONS

```SQL
SELECT * FROM burgers WHERE quantity > 3;
```

```SQL
SELECT * FROM burgers WHERE quantity > 3 AND vegetarian = TRUE;
```



#JOINS

```
CREATE TABLE reviews(name VARCHAR, review TEXT)
```

```SQL
INSERT INTO reviews VALUES ('bob''s burgers', 'Delicious and cheap');
```


```SQL
SELECT * FROM burgers INNER JOIN reviews ON burgers.name = reviews.name WHERE burgers.name = 'bob''s burgers';
```


## Spatial Data 


### Points 

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
INSERT INTO points(name, geom) VALUES('first', ST_SetSRID(ST_GeomFromText('POINT(0 0)'), 4326))
```

```SQL
SELECT * FROM points;

INSERT INTO points(name, geom) VALUES('zero', ST_SetSRID(ST_GeomFromText('POINT(3 3)'), 4326))

SELECT * FROM points;
```


#### Buffer Point

```SQL
CREATE TABLE buffered_points AS (
	SELECT ST_Buffer(geom, 100) FROM points
)
```

#### Get perimeter of points 

```SQL
SELECT ST_Perimeter(geom) FROM points;
```

```SQL
SELECT ST_Perimeter(geom) FROM buffered_points;
```

```SQL
SELECT ST_Perimeter(geom) FROM buffered_points;
```

```SQL
SELECT * FROM buffered_points
```

```SQL
SELECT ST_Perimeter(st_buffer) FROM buffered_points;
```


##### Formula!

####### C=2πr


#### Get area of points 

```SQL
SELECT ST_Area(geom) FROM points;

```

```SQL
SELECT ST_Area(st_buffer) FROM buffered_points;
```

#### Get distance between two points

```SQL
SELECT ST_Distance(a.geom, b.geom)
FROM points a, points b
WHERE a.name ='zero' AND b.name ='first';
```

```SQL
SELECT ST_Distance(a.geom:: geography, b.geom:: geography)
FROM points a, points b
WHERE a.name ='zero' AND b.name ='first';
```

Delivers results in meters but assumes coordinates are in degrees!


#### Line Table 

```SQL
CREATE TABLE line (
	id SERIAL PRIMARY KEY,
	line_name VARCHAR,
	geom GEOMETRY(LINESTRING, 4326)
);

INSERT INTO line VALUES('first line', ST_GeomFromText('LINESTRING(10 5, 10 6, 10 9, 11 9)', 4326));

SELECT ST_Length(geom) FROM line;

Compare geometry and geography

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

* Add polygons

##### Change SRID

```SQL

SELECT geom FROM points

SELECT Find_SRID('public', 'points', 'geom');

SELECT ST_Transform(geom, 6855) FROM points
```


##### ST_Difference 
```SQL
WITH buffered_lines AS (SELECT * FROM buffered_lines)	
SELECT ST_Difference(buffered_lines.st_buffer, polygon.geom) FROM polygon, buffered_lines
```


```SQL
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

#### Cambridge Neighborhoods


```SQL
CREATE TABLE coffee_shops
	(
	  id serial NOT NULL,
	  name character varying(50),
	  address character varying(50),
	  city character varying(50),
	  state character varying(50),
	  zip character varying(10),
	  lat numeric,
	  lon numeric
	);

```

##### Load in CSV

Add geometry column

```SQL
ALTER TABLE coffee_shop	ADD COLUMN geom geometry(POINT,4326)
```

```SQL
UPDATE coffee_shops SET geom = ST_SetSRID(ST_MakePoint(lon,lat),4326);
```

```SQL
SELECT cambridge_neighborhoods.name as name, count(*)
	FROM coffee_shops, cambridge_neighborhoods
	WHERE ST_Intersects(coffee_shops.geom, cambridge_neighborhoods.geom)
	GROUP BY cambridge_neighborhoods.name;
```

```SQL
SELECT cambridge_neighborhoods.name as name, count(*)
	FROM coffee_shops, cambridge_neighborhoods
	WHERE ST_Intersects(coffee_shops.geom, cambridge_neighborhoods.geom)
	GROUP BY cambridge_neighborhoods.name;
```








