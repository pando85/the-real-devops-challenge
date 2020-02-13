#!/bin/bash
mongo -- "${MONGO_INITDB_DATABASE}" <<EOF
    var rootUser = '${MONGO_INITDB_ROOT_USERNAME}';
    var rootPassword = '${MONGO_INITDB_ROOT_PASSWORD}';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);

    var user = '${MONGO_INITDB_USERNAME}';
    var passwd = '${MONGO_INITDB_PASSWORD}';
    db.createUser({user: user, pwd: passwd, roles: ["readWrite"]});
EOF

mongoimport --db ${MONGO_INITDB_DATABASE} -u ${MONGO_INITDB_USERNAME} \
    -p ${MONGO_INITDB_PASSWORD} --collection restaurant \
    --file /docker-entrypoint-initdb.d/restaurant.json
