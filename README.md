
# FONVesti

Specifikacija i formulacija korisničkog zahteva

Kako bismo što preciznije i verodostojnije ispunili sve zahteve datog projekta odlučili smo se za izradu veb sajta koji će služiti kao posrednik između korisnika i zvaničnog FONovog sajta i ostalih stranica predmeta. Naime, naš sajt će u sebi sadržati bazu registrovanih korisnika (svaki korisnik se samo jednom može registrovati na sajt) koji će po svom izboru dobijati određene informacije. Šta više, svaki korisnik će na našem sajtu imati mogućnost da izabere vrstu/sector vesti koja ih zanima čime će se prijaviti na njih. Njihov izbor će biti zabeležen, sačuvan i procesuiran u samoj bazi podataka. Kada se na zvaničnom sajtu FONa pojavi nova vest, recimo da je vest o predmetu ITEH, svi korisnici našeg sajta koji su prethodno iskazali interesovanje o vestima te vrste će prvenstveno dobiti notifikaciju o novoj vesti.


Frontend: Bootstrap
Backend: Django
Database: Sqlite3
Task scheduler: Celery
Message broker: Redis
Infinite scroll: Waypoints.js
Rest API: Django Rest framework