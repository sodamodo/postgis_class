https://data.sfgov.org/Housing-and-Buildings/Map-of-Historic-Secured-Property-Tax-Rolls-Fiscal-/qxyp-2pa4
https://www.propertyshark.com/mason/text/san_francisco_zoning_codes.html

```SQL
CREATE TABLE sf_parcels(
	zoning_code VARCHAR,
	property_area VARCHAR,
	improv_value VARCHAR,
	land_value VARCHAR,
	geom_input VARCHAR
);
```

***IMPORT SUBSET CSV***

```SQL
ALTER TABLE sf_parcels ADD COLUMN geom geometry(POLYGON, 4326);
```

```SQL
ALTER TABLE sf_parcels ADD COLUMN latitude VARCHAR;
```

```SQL
ALTER TABLE sf_parcels ADD COLUMN longitude VARCHAR;
```

```SQL
UPDATE sf_parcels SET longitude = split_part(geom_input, ',', 1);
UPDATE sf_parcels SET longitude = split_part(geom_input, ',', 2);
```

```SQL
SELECT TRIM(LEADING '(' FROM longitude) FROM sf_parcels LIMIT 10;
```

```SQL
UPDATE sf_parcels SET latitude = TRIM(LEADING '(' FROM latitude);
```

```SQL
UPDATE sf_parcels SET longitude = TRIM(TRAILING ')' FROM longitude);
```

```SQL
ALTER TABLE sf_parcels	ADD COLUMN geom geometry(POINT,4326)
```

```SQL
UPDATE sf_parcels SET geom = ST_SetSRID(ST_MakePoint(longitude:: FLOAT,latitude:: FLOAT),4326);
```

```SQL
SELECT DISTINCT zoning_code FROM sf_parcels WHERE zoning_code LIKE 'NCT_' OR zoning_code LIKE 'C%';
```

```SQL
SELECT MAX(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;
```

```SQL
ALTER TABLE sf_parcels ADD COLUMN total_value INT;
```

```SQL
UPDATE sf_parcels SET total_value = land_value:: INT + improv_value :: INT;
```

```SQL
ALTER TABLE sf_parcels ADD COLUMN value_density FLOAT;
```

```SQL
UPDATE sf_parcels SET value_density = total_value / property_area :: FLOAT WHERE property_area :: INT != 0;
```

```SQL
SELECT DISTINCT zoning_code FROM sf_parcels WHERE zoning_code LIKE 'NCT_';
```

```SQL
SELECT MAX(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;
```

```SQL
SELECT MIN(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;
```

```SQL
SELECT AVG(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;
```

```SQL
SELECT COUNT(*) FROM commercial_parcels WHERE value_density > 5000;
```

