
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




y_block_subset(GISJOIN VARCHAR, YEAR INT, STATE VARCHAR, COUNTY VARCHAR, COUNTYA INT, COUSUBA INT, TRACTA INT, 
							 BLKGRPA INT, BLOCKA INT, CDA INT, NAME VARCHAR);


DROP TABLE bay_block_subset;

CREATE TABLE bay_block_data_subset(GISJOIN VARCHAR, YEAR VARCHAR, STATE VARCHAR, COUNTY VARCHAR, COUNTYA VARCHAR, COUSUBA VARCHAR, TRACTA VARCHAR, 
							 BLKGRPA VARCHAR, BLOCKA VARCHAR, CDA VARCHAR, NAME VARCHAR);

DROP TABLE IF EXISTS bay_block_data_subset;
CREATE TABLE bay_block_data_subset(GISJOIN VARCHAR, YEAR VARCHAR, STATE VARCHAR, COUNTY VARCHAR, COUNTYA VARCHAR, COUSUBA VARCHAR, TRACTA VARCHAR, 
							 BLKGRPA VARCHAR, BLOCKA VARCHAR, CDA VARCHAR, NAME VARCHAR,
								TOTAL VARCHAR, WHITE_ALONE VARCHAR, AA_ALONE VARCHAR, NATIVE_ALONE VARCHAR, ASIAN_ALONE VARCHAR, PI_ALONE VARCHAR, TWO_PLUS_ALONE VARCHAR, TWO_PLUS VARCHAR  
								  );


DROP TABLE IF EXISTS bay_block_data_subset;
CREATE TABLE bay_block_data_subset(GISJOIN VARCHAR, YEAR VARCHAR, STATE VARCHAR, COUNTY VARCHAR, COUNTYA VARCHAR, COUSUBA VARCHAR, TRACTA VARCHAR, 
							 BLKGRPA VARCHAR, BLOCKA VARCHAR, CDA VARCHAR, NAME VARCHAR,
								TOTAL VARCHAR, WHITE_ALONE VARCHAR, AA_ALONE VARCHAR, NATIVE_ALONE VARCHAR, ASIAN_ALONE VARCHAR, PI_ALONE VARCHAR, TWO_PLUS_ALONE VARCHAR, TWO_PLUS VARCHAR  
								  );
								  
								  
								  
```SQL
SELECT blocka, aa_alone, geom FROM "CA_blocks_bay_subset" INNER JOIN bay_block_data_subset
	ON  "CA_blocks_bay_subset".gisjoin = bay_block_data_subset.gisjoin;
```



ALTER TABLE public.bay_block_data_subset ADD COLUMN asian_percentage INTEGER;


UPDATE public.bay_block_data_subset SET asian_percentage = asian_alone :: FLOAT / total :: FLOAT WHERE total :: INTEGER != 0;

DROP TABLE IF EXISTS asian_percentage;
CREATE TABLE asian_percentage AS
(SELECT geom, asian_percentage FROM bay_block_data_subset INNER JOIN "CA_blocks_bay_subset" ON bay_block_data_subset.gisjoin = "CA_blocks_bay_subset".gisjoin);

ALTER TABLE bay_block_data_subset ALTER COLUMN asian_percentage TYPE FLOAT USING asian_percentage::FLOAT;
SELECT * FROM asian_percentage LIMIT 10;

UPDATE public.bay_block_data_subset SET asian_percentage = asian_alone :: FLOAT / total :: FLOAT WHERE total :: INTEGER != 0;

SELECT * FROM asian_percentage LIMIT 10;

ALTER TABLE bay_block_data_subset ALTER COLUMN white_alone TYPE FLOAT USING white_alone::FLOAT;
ALTER TABLE bay_block_data_subset ALTER COLUMN total TYPE FLOAT USING total::FLOAT;
ALTER TABLE bay_block_data_subset ALTER COLUMN asian_alone TYPE FLOAT USING asian_alone::FLOAT;
ALTER TABLE bay_block_data_subset ALTER COLUMN aa_alone TYPE FLOAT USING aa_alone::FLOAT;

SELECT white_alone / total FROM bay_block_data_subset WHERE total != 0;

UPDATE public.bay_block_data_subset SET asian_percentage = asian_alone / total WHERE total != 0;


-- Black
ALTER TABLE bay_block_data_subset ADD COLUMN aa_percentage FLOAT;

UPDATE public.bay_block_data_subset SET aa_percentage = aa_alone / total * 100 WHERE total != 0;
