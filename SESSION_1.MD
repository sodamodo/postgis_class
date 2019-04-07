Load shapefiles into PgAdmin4
Install PgAdmin4

### Loading shapefiles
shp2pgsql
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
