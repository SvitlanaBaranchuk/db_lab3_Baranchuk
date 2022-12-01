import psycopg2
import matplotlib.pyplot as plt

username = 'Baranchuk'
password = '20032003'
database = 'Baranchuk_DB'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW VideoCount AS
SELECT TRIM(channel.channel_title) AS title, COUNT(channel.id_channel) FROM video, channel
WHERE channel.id_channel = video.id_channel
GROUP BY channel.channel_title
ORDER BY channel.channel_title ASC;
'''

query_2 = '''
CREATE VIEW OddID AS 
SELECT TRIM(category.name_category) AS category, COUNT(category.category_id) FROM video, category
WHERE category.category_id = video.category_id
AND category.category_id % 2 != 0
GROUP BY category.name_category;
'''

query_3 = '''
CREATE VIEW VideoDate AS 
SELECT COUNT(video_id), publish_time
FROM video
GROUP BY publish_time;
'''

conn1 = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
conn2 = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
conn3 = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn1:
    cur = conn1.cursor()

    print('1.')
    cur.execute('DROP VIEW IF EXISTS VideoCount')
    cur.execute(query_1)
    cur.execute('SELECT * FROM VideoCount')

    X = []
    Y = []
    for row in cur:
        X.append(row[0])
        Y.append(row[1])

    x_range = range(len(X))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, Y, label='Total')
    bar_ax.set_title('Кількість відео, які попали в рекомендації, для кожного з каналів')
    bar_ax.set_xlabel('Канал')
    bar_ax.set_ylabel('Кількість відео')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(X)

print()
with conn2:
    cur = conn2.cursor()

    print('2.')
    cur.execute('DROP VIEW IF EXISTS OddID')
    cur.execute(query_2)
    cur.execute('SELECT * FROM OddID')

    X = []
    Y = []
    for row in cur:
        X.append(row[0])
        Y.append(row[1])

    pie_ax.pie(Y, labels=X, autopct='%1.1f%%')
    pie_ax.set_title('Частка категорій з непарним id')


print()
with conn3:
    cur = conn3.cursor()

    print('3.')
    cur.execute('DROP VIEW IF EXISTS VideoDate')
    cur.execute(query_3)
    cur.execute('SELECT * FROM VideoDate')

    X = []
    Y = []
    for row in cur:
        X.append(row[0])
        Y.append(row[1])

    plt.plot(Y, X)
    plt.title('Кількість відео, які потрапили в рекомендації, за датами публікації')
    plt.show()


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)
