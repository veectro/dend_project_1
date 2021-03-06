# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY , 
        start_time TIMESTAMP NOT NULL, 
        user_id INT NOT NULL, 
        level VARCHAR(5), 
        song_id VARCHAR, 
        artist_id VARCHAR, 
        session_id INT, 
        location VARCHAR, 
        user_agent VARCHAR,
        CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(user_id),
        CONSTRAINT fk_start_time FOREIGN KEY (start_time) REFERENCES time(start_time),
        CONSTRAINT fk_song FOREIGN KEY (song_id) REFERENCES songs(song_id),
        CONSTRAINT fk_artist FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INT PRIMARY KEY, 
        first_name VARCHAR, 
        last_name VARCHAR, 
        gender CHAR(1), 
        level VARCHAR(5)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id VARCHAR PRIMARY KEY, 
        title VARCHAR, 
        artist_id VARCHAR, 
        year SMALLINT, 
        duration FLOAT
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id VARCHAR PRIMARY KEY, 
        name VARCHAR, 
        location VARCHAR, 
        latitude FLOAT, 
        longitude FLOAT
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time TIMESTAMP PRIMARY KEY, 
        hour SMALLINT, 
        day SMALLINT, 
        week SMALLINT, 
        month SMALLINT, 
        year SMALLINT, 
        weekday SMALLINT
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users 
    ( user_id, first_name, last_name, gender, level) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(user_id) DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
    INSERT INTO songs 
    (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists 
    ( artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO time 
    (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artist_id 
    FROM songs
    WHERE title = %s 
        AND artist_id = (SELECT artist_id FROM artists WHERE name=%s) 
        AND duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create,
                        time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]
