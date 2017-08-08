import psycopg2

conn = psycopg2.connect("dbname=news user=postgres password=dawg")
# Open up a connection to the server
cur = conn.cursor()

def repeat_separator():

    print "-" * 25

repeat_separator()

print "The 3 most popular articles of all time are "

repeat_separator()

cur.execute('''
    select articles.title, count(log.path) as num
    from log
    join articles on log.path = CONCAT ('/article/', articles.slug)
    group by articles.title
    order by num desc offset 1 limit 3;
''')

for articles in cur:
    print "The article path is " + str(articles[0])
    print "The number of views for that article is " +str(articles[1])
    print "\n"

repeat_separator()

print "The most popular articles authors of all time are:"

cur.execute('''
    select authors.name, count(log.path)
    from log
    join articles on log.path = CONCAT ('/article/',articles.slug)
    join authors on articles.author = authors.id
    group by authors.name
    having count(log.path) > 1
    order by count(log.path) desc;
''')

for author in cur:
    print "The author's name is " + str(author[0])
    print "The total number of views is " + str(author[1])
    print "\n"

repeat_separator()

print "The percent of errors in the day and the day those errors occurred are:"

print "-" * 25

cur.execute('''
    WITH t
    AS (SELECT
      DATE(log.time) AS failureDate,
      ROUND(
        (SUM(CASE
          WHEN
            log.status != '200 OK' THEN 1
        END
        ) * 100.0) ::DECIMAL /
        (COUNT(log.status)), 1) AS totalFailures
    FROM log
    GROUP BY DATE(log.time))
    SELECT
      CONCAT(t.totalFailures, '%') AS failure,
      to_char(t.failureDate, 'Month DD, YYYY') AS date
    FROM t
    GROUP BY t.totalFailures,
             t.failureDate
    HAVING t.totalFailures > 1;
''')

for record in cur:
    print("The number of errors in that day was " + str(record[0]))
    print("The date of those errors was " + str(record[1]))
