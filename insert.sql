INSERT INTO auths (auth_id,
    email,
    password, 
    created_at, 
    updated_at) 
VALUES ('0',
    'olcorp_auth', 
    'olcorp', 
    CURRENT_DATE, 
    CURRENT_DATE);

INSERT INTO users (id,
    email,
    created_at, 
    updated_at) 
VALUES ('0',
    'olcorp_user',
    CURRENT_DATE,
    CURRENT_DATE);

INSERT INTO groups (id,
    label,
    created_at, 
    updated_at) 
VALUES ('0',
    'olcorp_group',
    CURRENT_DATE,
    CURRENT_DATE);

INSERT INTO units (id,
    label,
    created_at,
    updated_at)
VALUES ('0',
    'olcorp_unit',
    CURRENT_DATE,
    CURRENT_DATE);
