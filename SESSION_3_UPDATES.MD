DROP TABLE sf_parcels;

CREATE TABLE sf_parcels(
	zoning_code VARCHAR,
	property_area VARCHAR,
	improv_value VARCHAR,
	land_value VARCHAR,
	geom_input VARCHAR
);

ALTER TABLE sf_parcels ADD COLUMN parcel_number VARCHAR;


SELECT * FROM sf_parcels LIMIT 10;

CREATE TABLE luis_sf_parcels AS (SELECT * FROM sf_parcels);

ALTER TABLE sf_parcels ADD COLUMN geom geometry(POLYGON, 4326);

ALTER TABLE sf_parcels ADD COLUMN latitude VARCHAR;
ALTER TABLE sf_parcels ADD COLUMN longitude VARCHAR;

SELECT * FROM sf_parcels LIMIT 10;

SELECT  split_part(geom_input, ',', 2) FROM sf_parcels;

UPDATE sf_parcels SET latitude = split_part(geom_input, ',', 1);
UPDATE sf_parcels SET longitude = split_part(geom_input, ',', 2);

SELECT * FROM sf_parcels LIMIT 10;

SELECT TRIM(LEADING '(' FROM latitude) FROM sf_parcels LIMIT 10;


UPDATE sf_parcels SET latitude = TRIM(LEADING '(' FROM latitude);

SELECT * FROM sf_parcels LIMIT 10;


UPDATE sf_parcels SET longitude = TRIM(TRAILING ')' FROM longitude);

SELECT * FROM sf_parcels LIMIT 10;


ALTER TABLE sf_parcels ADD COLUMN geom geometry(POINT,4326);

UPDATE sf_parcels SET geom = ST_SetSRID(ST_MakePoint(longitude:: FLOAT,latitude:: FLOAT),4326);

SELECT * FROM sf_parcels WHERE zoning_code LIKE 'NCT_' OR zoning_code LIKE 'C%';

CREATE TABLE commercial_parcels AS
(SELECT * FROM sf_parcels WHERE zoning_code LIKE 'NCT_' OR zoning_code LIKE 'C%');


ALTER TABLE sf_parcels ADD COLUMN total_value INT;

SELECT * FROM sf_parcels LIMIT 10;

UPDATE sf_parcels SET total_value = land_value:: INT + improv_value :: INT;

SELECT * FROM sf_parcels LIMIT 10;

ALTER TABLE commercial_parcels ADD COLUMN total_value INT;


UPDATE commercial_parcels SET total_value = land_value:: INT + improv_value :: INT;

SELECT * FROM commercial_parcels LIMIT 10;

ALTER TABLE sf_parcels ADD COLUMN value_density FLOAT;

SELECT * FROM sf_parcels LIMIT 10;

UPDATE sf_parcels SET value_density = total_value / property_area :: FLOAT WHERE property_area :: INT != 0;

SELECT * FROM sf_parcels LIMIT 10;

SELECT * FROM sf_parcels WHERE value_density IS NOT NULL;

DELETE FROM sf_parcels WHERE value_density IS NULL;

SELECT * FROM sf_parcels;

SELECT MAX(total_value), zoning_code FROM commercial_parcels GROUP BY zoning_code;


DROP TABLE most_expensive_parcel;
CREATE TABLE most_expensive_parcel AS (SELECT * FROM sf_parcels WHERE total_value > 109416588);

SELECT * FROM most_expensive_parcel;

SELECT MIN(total_value), zoning_code FROM commercial_parcels WHERE total_value:: INT > 1 GROUP BY zoning_code;

SELECT AVG(total_value) :: INT, zoning_code FROM commercial_parcels GROUP BY zoning_code;

SELECT COUNT(*) FROM sf_parcels WHERE value_density > 5000;

SELECT ST_AsGeoJSON(geom) FROM sf_parcels LIMIT 10;




















