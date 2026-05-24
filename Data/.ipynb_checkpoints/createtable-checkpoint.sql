
DROP TABLE IF EXISTS birds;
CREATE TABLE birds (
  latitude real,
  longitude real,
  taxon_name TEXT,
  common_name TEXT,
  iconic_taxon TEXT,
  place_geuss VARCHAR(6000),
  observer VARCHAR(100));


DROP TABLE IF EXISTS amphibians;
CREATE TABLE amphibians (
  latitude real,
  longitude real,
  taxon_name TEXT,
  common_name TEXT,
  iconic_taxon TEXT,
  place_geuss VARCHAR(6000),
  observer VARCHAR(100));

DROP TABLE IF EXISTS reptiles;
CREATE TABLE reptiles (
  latitude real,
  longitude real,
  taxon_name TEXT,
  common_name TEXT,
  iconic_taxon TEXT,
  place_geuss VARCHAR(6000),
  observer VARCHAR(100));


DROP TABLE IF EXISTS mammals;
CREATE TABLE mammals (
  latitude real,
  longitude real,
  taxon_name TEXT,
  common_name TEXT,
  iconic_taxon TEXT,
  place_geuss VARCHAR(6000),
  observer VARCHAR(100));

DROP TABLE IF EXISTS insects;
CREATE TABLE insects (
  latitude real,
  longitude real,
  taxon_name TEXT,
  common_name TEXT,
  iconic_taxon TEXT,
  place_geuss VARCHAR(6000),
  observer VARCHAR(100));