# team-generator-api

Postgres Installation

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04


Sample Team Request JSON

```{
  "fantacy_app_id": "1",
  "match_id": "3",
  "team1_alias": "BRZ",
  "team2_alias": "SER",
  "players": {
      "Teixeirea" : {
          "credit": 20,
          "team": "BRZ",
          "must_pick": 0,
          "skill": "universal"
      },
      "Lozo" : {
          "credit": 19,
          "team": "SER",
          "must_pick": 0,
          "skill": "universal"
      },
      "Bjelica" : {
          "credit": 1.5,
          "team": "SER",
          "must_pick": 0,
          "skill": "universal"
      },
      "Candido" : {
          "credit": 1.5,
          "team": "BRZ",
          "must_pick": 1,
          "skill": "attacker"
      },
      "BBusha" : {
          "credit": 18,
          "team": "SER",
          "must_pick": 0,
          "skill": "attacker"
      },
      "BMilenkovic" : {
          "credit": 16.5,
          "team": "SER",
          "must_pick": 0,
          "skill": "attacker"
      },
      "FClaudino" : {
          "credit": 15.5,
          "team": "BRZ",
          "must_pick": 0,
          "skill": "blocker"
      },
      "MLeao" : {
          "credit": 13.5,
          "team": "BRZ",
          "must_pick": 0,
          "skill": "blocker"
      },
      "MSavic" : {
          "credit": 11,
          "team": "SER",
          "must_pick": 0,
          "skill": "blocker"
      },
      "Mpopovic" : {
          "credit": 13.5,
          "team": "SER",
          "must_pick": 0,
          "skill": "blocker"
      },
      "MCarneiro" : {
          "credit": 4,
          "team": "BRZ",
          "must_pick": 1,
          "skill": "setter"
      },
      "SMirkovic" : {
          "credit": 14.5,
          "team": "SER",
          "must_pick": 0,
          "skill": "setter"
      },
      "MDjordjevic" : {
          "credit": 4,
          "team": "SER",
          "must_pick": 0,
          "skill": "setter"
      },
      "Pinto" : {
          "credit": 5,
          "team": "BRZ",
          "must_pick": 0,
          "skill": "libero"
      },
      "Gocanin" : {
          "credit": 1,
          "team": "SER",
          "must_pick": 0,
          "skill": "libero"
      }
  }
}```




su - postgres
createuser --interactive --pwprompt
createdb -O chinchan fantacydb
dropuser username
dropdb dbname
GRANT permissions ON DATABASE dbname TO username;


sudo -u postgres createuser chinchan
sudo -u postgres createdb fantacydb
sudo -u postgres psql
alter user chinchan with encrypted password 'Diveinn123';
grant all privileges on database fantacydb to chinchan;


sudo service postgresql restart


sudo su - postgres
psql -U postgres
CREATE ROLE demorole1 WITH LOGIN ENCRYPTED PASSWORD 'password1';
\du
DROP ROLE demorole1;

CREATE ROLE chinchan WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'Diveinn123';

psql -U chinchan fantacydb -W

\l

REVOKE ALL PRIVILEGES ON database fantacydb FROM postgres;

\c fantacydb

 vi /etc/postgresql/11/main/pg_hba.conf
 sudo service postgresql restart
 psql -U chinchan fantacydb -W


 sudo apt-get install python-psycopg2

 sudo apt-get install libpq-dev
sudo apt-get install python-dev
