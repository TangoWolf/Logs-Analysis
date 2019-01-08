import psycopg2


DBNAME = "news"

def get_report():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, num from articles join (select path, count(*) as num from log where path like '/article/%' and status like '200%' group by path order by num desc limit 3) as middle on path like '%'||slug;")
    article = c.fetchone()

    print("\n\nMost popular articles\n")

    while article is not None:
        name, views = article
        print(name + " -- %i Views" % views)
        article = c.fetchone()

    c.execute("select name, views from authors join (select author, sum(num) as views from articles join (select path, count(*) as num from log where path like '/article/%' and status like '200%' group by path order by num desc) as middle on path like '%'||slug group by author) as second on authors.id = second.author;")
    author = c.fetchone()

    print("\n\nMost popular authors\n")

    while author is not None:
        name, views = author
        print("%s -- %i Views" % (name, views))
        author = c.fetchone()

    c.execute("select error.date, error.errors, success.successes from (select date(time), count(*) as successes from log where status like '200%' group by date(time)) as success join (select date(time), count(*) as errors from log where status not like '200%' group by date(time)) as error on success.date = error.date group by error.date, error.errors, success.successes having error.errors > .01*(error.errors+success.successes);")
    errors = c.fetchone()

    print("\n\nDays on which more than 1% of requests led to errors\n")

    while errors is not None:
        day, error, success = errors
        percent = 100*(error/float(error+success))
        print("%i%% of the requests on %s led to errors" % (percent, day))
        errors = c.fetchone()


    db.close()

get_report()
