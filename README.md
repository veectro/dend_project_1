# Project: Data Modeling with Postgres

## Background

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new
music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity
on the app, as well as a directory with JSON metadata on the songs in their app.
---

## Project Description

The startup sparkify want to analyze the behavior of their users on their music
streaming app, so they could understand what songs users are listening to. Therefore in this project, a star schema 
is chosen, because it is optimized for querying the user's behaviour.


---

## Project Structure

```
.
├── data
│   ├── log_data : dataset of user activity logs
│   └── song_data : dataset of song metadata
├── create_table.py : script to create the tables (run this script first)
├── docker-compose.yml : docker compose file
├── etl.ipynb : notebook to develop ETL pipeline
├── etl.py : script to run the ETL pipeline 
├── README.md : project documentation
├── requirements.txt : list of dependencies need to be installed
├── sql_queries.py : script containes sql queries and schema for the projects
└── test.ipynb : script to confirm that records were successfully inserted into each table. 
```

---

## Project Datasets
There are the S3 links for each:

- Song data: `s3://udacity-dend/song_data`
- Log data: `s3://udacity-dend/log_data`

Log data json path: `s3://udacity-dend/log_json_path.json`

### Song Dataset

The first dataset is a subset of real data from the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/)
. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned
by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```json
{
  "num_songs": 1,
  "artist_id": "ARJIE2Y1187B994AB7",
  "artist_latitude": null,
  "artist_longitude": null,
  "artist_location": "",
  "artist_name": "Line Renaud",
  "song_id": "SOUPIRU12A6D4FA1E1",
  "title": "Der Kleine Dompfaff",
  "duration": 152.92036,
  "year": 0
}
```

### Log Dataset

The second dataset consists of log files in JSON format generated by
this [event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate app
activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset are partitioned by year and month. For example, here are filepaths
to two files in this dataset.

``
log_data/2018/11/2018-11-12-events.json log_data/2018/11/2018-11-13-events.json
``

**Example**

```json
{
  "artist": "Muse",
  "auth": "Logged In",
  "firstName": "Harper",
  "gender": "M",
  "itemInSession": 1,
  "lastName": "Barrett",
  "length": 209.50159,
  "level": "paid",
  "location": "New York-Newark-Jersey City, NY-NJ-PA",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1540685364796,
  "sessionId": 275,
  "song": "Supermassive Black Hole (Twilight Soundtrack Version)",
  "status": 200,
  "ts": 1541721977796,
  "userAgent": "\"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
  "userId": "42"
}
```

---

## Star Schema (Data Catalog)
The star schema is chosen because it is optimized for querying the user's behaviour.

The goal to be achieved with the star schema is to optimize queries on song play analysis.

### Fact Table

#### songplays table

This tables contains the song play events in the log data.

| Column Name | Type       | Example                            |
|-------------|------------|------------------------------------|
| songplay_id | SERIAL     | 1210                               |
| start_time  | TIMESTAMP  | 2018-11-21 21:56:47.796000         |
| user_id     | INT        | 15                                 |
| level       | VARCHAR(5) | paid                               |
| song_id     | VARCHAR    | SOZCTXZ12AB0182364                 |
| artist_id   | VARCHAR    | AR5KOSW1187FB35FF4                 |
| session_id  | INT        | 818                                |
| location    | VARCHAR    | Chicago-Naperville-Elgin, IL-IN-WI |
| user_agent  | VARCHAR    | "Mozilla/5.0 (X11; .."             |

---

### Dimension Table

#### songs table

This table contains the songs from the music dataset.

| Column Name | Type      | Example              |
|-------------|-----------|----------------------|
| song_id     | VARCHAR   | SOGVQGJ12AB017F169   |
| title       | VARCHAR   | Ten Tonne            |
| artist_id   | VARCHAR   | AR62SOJ1187FB47BB5   |
| year        | SMALLINT  | 2005                 |
| duration    | FLOAT     | 337.68444            |

---

#### artist table

This tables contains the artist from music dataset.

| Column Name | Type    | Example |
|-------------|---------|---------|
| artist_id   | VARCHAR | AR0IAWL1187B9A96D0      |
| name        | VARCHAR | Danilo Perez    |
| location    | VARCHAR | Panama   |
| latitude    | FLOAT   | 8.4177       |
| longitude   | FLOAT   | -80.11278    |

---

#### time table

This tables contains timestamps of records in **songplays** broken down into specific units.

| Column Name | Type      | Example                    |
|-------------|-----------|----------------------------|
| start_time  | TIMESTAMP | 2018-11-17 00:02:24.796000 |
| hour        | SMALLINT  | 0                          |
| day         | SMALLINT  | 17                         |
| week        | SMALLINT  | 46                         |
| month       | SMALLINT  | 11                         |
| year        | SMALLINT  | 2018                       |
| weekday     | SMALLINT  | 5                          |

---

## Run the project
1. Run docker compose to start the PostgreSQL server
```bash
docker-compose up -d
```
2. Run the `create_tables.py` to create the schema and tables
```bash
python create_tables.py
```
3. Run the `etl.py` to load the data into the tables
```bash
python etl.py
```