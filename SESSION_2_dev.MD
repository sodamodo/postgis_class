
0 Cambridge Coffee shosp

1 NHGIS INTRO
3 California Clone 
2 Data Prep
	2.1 Move between spreadsheets 
	2.2 Create table
	2.3 Load CSV (VARCHAR)
3 Talk about data type conversion
4 Convert numbers to floats
5 Yelp
	5.1 Show python script
	5.2 Load yelp data
	5.3 Confine yelp data to SF
	5.4 Load parcel data
	
	


- COPY DATA FROM INFO SPReADSHEET 
- CREATE CENSUS TABLE 
- COPY CSV
- ADJUST DATA TYPE


-- CREATE CENSUS TABLE!


```SQL
CREATE TABLE combined AS (
		SELECT id, geom, statefp10, countyfp10, tractce10, blockce10, geoid10, name10, mtfcc10, ur10, uace10, uatyp10,
		funcstat10, aland10, awater10, intptlat10, intptlon10, shape_area, shape_len,
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



YELP
--Show website
--Show script
--Create table
--Upload CSV


CREATE BUSINESS TABLE

```SQL
CREATE TABLE business(
	business_id VARCHAR,
	business_name VARCHAR,
	address VARCHAR,
	city VARCHAR,
	location_state VARCHAR,
	postal_code VARCHAR,
	latitude VARCHAR,
	longitude VARCHAR,
	stars VARCHAR,
	review_count VARCHAR,
	is_open VARCHAR,
	business_attributes VARCHAR,
	categories VARCHAR,
	hours VARCHAR 
);

```

LOAD THE DATA!




