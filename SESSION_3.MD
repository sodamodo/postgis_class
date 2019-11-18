https://data.sfgov.org/Housing-and-Buildings/Map-of-Historic-Secured-Property-Tax-Rolls-Fiscal-/qxyp-2pa4
https://www.propertyshark.com/mason/text/san_francisco_zoning_codes.html


CREATE TABLE pf_parcels(
	zoning_code VARCHAR,
	property_area VARCHAR,
	improv_value VARCHAR,
	land_value VARCHAR,
	geom_input VARCHAR
);

ALTER TABLE pf_parcels ADD COLUMN geom geometry(POLYGON, 4326);


ALTER TABLE pf_parcels ADD COLUMN latitude VARCHAR;

ALTER TABLE pf_parcels ADD COLUMN longitude VARCHAR;

UPDATE pf_parcels SET longitude = split_part(geom_input, ',', 1);
UPDATE pf_parcels SET longitude = split_part(geom_input, ',', 2);


SELECT TRIM(LEADING '(' FROM longitude) FROM pf_parcels LIMIT 10;

UPDATE pf_parcels SET latitude = TRIM(LEADING '(' FROM latitude);
UPDATE pf_parcels SET longitude = TRIM(TRAILING ')' FROM longitude);


ALTER TABLE pf_parcels	ADD COLUMN geom geometry(POINT,4326)


UPDATE pf_parcels SET geom = ST_SetSRID(ST_MakePoint(longitude:: FLOAT,latitude:: FLOAT),4326);


SELECT DISTINCT zoning_code FROM pf_parcels WHERE zoning_code LIKE 'NCT_' OR zoning_code LIKE 'C%';


SELECT MAX(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;

ALTER TABLE pf_parcels ADD COLUMN total_value INT;

UPDATE pf_parcels SET total_value = land_value:: INT + improv_value :: INT;

ALTER TABLE pf_parcels ADD COLUMN value_density FLOAT;

UPDATE pf_parcels SET value_density = total_value / property_area :: FLOAT WHERE property_area :: INT != 0;

SELECT DISTINCT zoning_code FROM pf_parcels WHERE zoning_code LIKE 'NCT_';
