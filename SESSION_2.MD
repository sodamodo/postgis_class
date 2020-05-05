
## Projected Coordinated

WGS84 UTM Zone 10 North: 32610

Spatial Data Types Continued:

POINT(0 0)

LINESTRING(0 0,1 1,1 2)

POLYGON((0 0,4 0,4 4,0 4,0 0),(1 1, 2 1, 2 2, 1 2,1 1))

MULTIPOINT((0 0),(1 2))

MULTILINESTRING((0 0,1 1,1 2),(2 3,3 2,5 4))

MULTIPOLYGON(((0 0,4 0,4 4,0 4,0 0),(1 1,2 1,2 2,1 2,1 1)), ((-1 -1,-1 -2,-2 -2,-2 -1,-1 -1)))


Functions:

ST_Centroid(geometry g1);

boolean ST_Contains(geometry geomA, geometry geomB);

boolean ST_IsEmpty(geometry geomA);

boolean ST_Touches(geometry g1, geometry g2);

Extent

```SQL 
CREATE TABLE points(id SERIAL PRIMARY KEY, geom geometry(POLYGON, 4326));

CREATE TABLE point_extent AS (SELECT ST_SetSRID(ST_Extent(geom), 4326) FROM points);
```



* Boston Exercise
```SQ
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


```SQL
ALTER TABLE coffee_shops
	ADD COLUMN geom geometry(POINT,4326)
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


* Census Data

1. Extra data from spreadsheet
2. Create table with extracted spreadsheet data


```SQL
CREATE TABLE combined AS (
		SELECT id, geom, statefp10, countyfp10, tractce10, blockce10, geoid10, name10, mtfcc10, ur10, uace10, 			uatyp10, funcstat10, aland10, awater10, intptlat10, intptlon10, shape_area, shape_len,
		block_data.gisjoin, total, white_alone, aa_alone, native_alone, asian_alone, pi_alone, two_plus
		FROM public."CA_block_2010" INNER JOIN block_data ON public."CA_block_2010".gisjoin = block_data.gisjoin
	);
	
SELECT * FROM block_data LIMIT 10;
SELECT * FROM combined LIMIT 10;


ALTER TABLE combined ALTER COLUMN total TYPE FLOAT USING total::double precision;  
ALTER TABLE combined ALTER COLUMN white_alone TYPE FLOAT USING white_alone::double precision;  
ALTER TABLE combined ALTER COLUMN aa_alone TYPE FLOAT USING aa_alone::double precision;  
ALTER TABLE combined ALTER COLUMN native_alone TYPE FLOAT USING total::double precision;  
ALTER TABLE combined ALTER COLUMN asian_alone TYPE FLOAT USING asian_alone::double precision;  
ALTER TABLE combined ALTER COLUMN pi_alone TYPE FLOAT USING pi_alone::double precision;  
ALTER TABLE combined ALTER COLUMN two_plus TYPE FLOAT USING two_plus::double precision;  


ALTER TABLE combined ADD COLUMN white_percentage FLOAT;

UPDATE combined SET white_percentage = white_alone / total * 100 WHERE total != 0;
```

* Exercise -- Do different calculations for LA. 












