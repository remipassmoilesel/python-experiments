# Memo Mysql / MariaDB

Se connecter en tant que root:

    $ sudo mysql -u root

Créer un utilisateur:

    > CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

Changer un mot de passe:

    > SET PASSWORD FOR 'jeffrey'@'localhost' = password_option;

Créer une base de données:

    > CREATE DATABASE abcmapfrnopgrm

Autoriser l'accès à une base de données:

    > GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON piwik_db.* TO 'piwik'@'localhost';
    -- ou
    > GRANT ALL PRIVILEGES ON dbname.* TO 'newuser'@'localhost';

Créer un dump:

    $ sudo mysqldump -u root -p[root_password] [database_name] > dumpfilename.sql

Restorer un dump:

    $ sudo mysql -u root -p[root_password] [database_name] < dumpfilename.sql


