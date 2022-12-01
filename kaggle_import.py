import psycopg2

username = 'Baranchuk'
password = '20032003'
database = 'Baranchuk_DB'

query_0 = '''
CREATE TABLE category_new
(
    category_id    INTEGER        NOT NULL,
    name_category  CHAR(50)       NOT NULL,
    CONSTRAINT pk_category_new PRIMARY KEY (category_id)
)
'''

query_1 = '''
CREATE TABLE channel_new
(
    id_channel      CHAR(20)     NOT NULL,
    channel_title   CHAR(10000)  NOT NULL,
    CONSTRAINT pk_channel_new PRIMARY KEY (id_channel)
)
'''

query_2 = '''
CREATE TABLE video_new
(
    video_id       CHAR(15)  NOT NULL,
    video_title    CHAR(200) NOT NULL,
    id_channel     CHAR(15)  NOT NULL,
    category_id    INTEGER   NOT NULL,
    publish_time   DATE      NOT NULL,
    CONSTRAINT pk_video_new PRIMARY KEY (video_id)
)
'''

query_3 = '''
CREATE TABLE video_rating_new
(
    video_id       CHAR(15)       NOT NULL,
    act_date       DATE           NOT NULL,
    likes          DECIMAL(30, 5) NOT NULL,
    dislikes       DECIMAL(30, 5) NOT NULL,
    v_views        DECIMAL(30, 5) NOT NULL,
    comments       DECIMAL(30, 5) NOT NULL,
    CONSTRAINT pk_video_rating_new PRIMARY KEY (video_id)
)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

cur = conn.cursor()

with open('C:/Users/Administrator/Desktop/US_category_id.csv', 'r') as f0:
    cur.execute('DROP TABLE category_new')
    cur.execute(query_0)
    next(f0)
    cur.copy_from(f0, 'category_new', sep=',')
conn.commit()

with open('C:/Users/Administrator/Desktop/US_channels.csv', 'r') as f1:
    cur.execute('DROP TABLE channel_new')
    cur.execute(query_1)
    next(f1)
    cur.copy_from(f1, 'channel_new', sep=',')
conn.commit()

with open('C:/Users/Administrator/Desktop/USvideo.csv', 'r') as f2:
    cur.execute('DROP TABLE video_new')
    cur.execute(query_2)
    next(f2)
    cur.copy_from(f2, 'video_new', sep=',')
conn.commit()

with open('C:/Users/Administrator/Desktop/USvideo_rating.csv', 'r') as f3:
    cur.execute('DROP TABLE video_rating_new')
    cur.execute(query_3)
    next(f3)
    cur.copy_from(f3, 'video_rating_new', sep=',')
conn.commit()
