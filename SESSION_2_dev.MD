
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
