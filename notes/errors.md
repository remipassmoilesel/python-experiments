# Erreurs courantes

## UnicodeEncodeError: 'ascii' codec can't encode character '\xb4' in position 57: ordinal not in range(128)

... dans un conteneur Docker.

Solution: Ajotuer dans le Dockerfile:

    ENV LANG="C.UTF-8"
