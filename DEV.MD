
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


```SQL
CREATE TABLE bay_block_data (

  county VARCHAR, 
  blocka VARCHAR, 
  total VARCHAR,
  white_alone VARCHAR,
  aa_alone VARCHAR,
  native_alone VARCHAR,
  asian_alone VARCHAR,
  pi_alone VARCHAR,
  two_plus_alone VARCHAR,
  two_plus VARCHAR

);	
	
```

```SQL
ALTER TABLE public.bayareablock00 RENAME TO bay_area_block;
```

```SQL
SELECT blocka, aa_alone, geom FROM "CA_blocks_bay_subset" INNER JOIN bay_block_data_subset
	ON  "CA_blocks_bay_subset".gisjoin = bay_block_data_subset.gisjoin;
```




SELECT county, geom FROM bay_blocks INNER JOIN bay_block_data ON
bay_blocks."BLOCKCE10" = public.bay_block_data.blocka LIMIT 100;
