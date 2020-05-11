```SQL
CREATE TABLE bay_block_data (

  gisjoin VARCHAR,
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
SELECT blocka, aa_alone, geom FROM "CA_blocks_bay_subset" INNER JOIN bay_block_data_subset
	ON  "CA_blocks_bay_subset".gisjoin = bay_block_data_subset.gisjoin;
```
