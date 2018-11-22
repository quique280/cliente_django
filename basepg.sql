--Maria Alvarez Hernandez ID: 4-0239-0850
--Luis Alonso Calderon Achio ID: 1-1702-0626
--Enrique Diaz Delgado ID: 1-1725-0124
--Derian Sibaja Chavarria ID 4-0232-0842

DROP DATABASE servidor_django;
DROP USER usuario_wang;
CREATE USER usuario_wang with PASSWORD 'root';

ALTER ROLE usuario_wang SET client_encoding TO 'utf8';
ALTER ROLE usuario_wang SET timezone TO 'America/Costa_Rica';

CREATE DATABASE servidor_django OWNER usuario_wang;

