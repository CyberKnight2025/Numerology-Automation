-- init.sql

-- Geographic Lookup Tables
CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER REFERENCES countries(id)
);

CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state_id INTEGER REFERENCES states(id)
);

-- Reports Table with Location Foreign Keys
CREATE TABLE IF NOT EXISTS reports (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birthdate DATE NOT NULL,
    life_path INT,
    expression_number INT,
    soul_urge INT,
    personality INT,
    destiny_number INT,
    fingerprint VARCHAR(255) UNIQUE,
    pinnacle_1 INT,
    pinnacle_2 INT,
    pinnacle_3 INT,
    pinnacle_4 INT,
    personal_year INT,
    personal_month INT,
    personal_day INT,
    country_id INTEGER REFERENCES countries(id),
    state_id INTEGER REFERENCES states(id),
    city_id INTEGER REFERENCES cities(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Normalized Core Schema (future-ready)

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    birthdate DATE,
    country_id INTEGER REFERENCES countries(id),
    state_id INTEGER REFERENCES states(id),
    city_id INTEGER REFERENCES cities(id)
);

-- Calculations Table
CREATE TABLE IF NOT EXISTS calculations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    life_path INTEGER,
    expression_number INTEGER,
    soul_urge_number INTEGER,
    destiny_number INTEGER,
    personality_number INTEGER
);

-- Cycles Table
CREATE TABLE IF NOT EXISTS cycles (
    id SERIAL PRIMARY KEY,
    calculation_id INTEGER REFERENCES calculations(id),
    personal_year INTEGER,
    personal_month INTEGER,
    personal_day INTEGER
);

-- Pinnacles Table
CREATE TABLE IF NOT EXISTS pinnacles (
    id SERIAL PRIMARY KEY,
    calculation_id INTEGER REFERENCES calculations(id),
    first_pinnacle INTEGER,
    second_pinnacle INTEGER,
    third_pinnacle INTEGER,
    fourth_pinnacle INTEGER
);

-- Life Path Traits Lookup Table
CREATE TABLE IF NOT EXISTS life_path_traits (
    id SERIAL PRIMARY KEY,
    life_path INTEGER UNIQUE,
    trait TEXT
);
