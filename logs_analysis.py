#!/usr/bin/env python3

# imported libs:
import psycopg2


DataBaseName = 'dbname=news'


def most_pop_articles(nb_articles=3):
    db = psycopg2.connect(DataBaseName)
    cursor = db.cursor()
    cursor.execute("""
select pathed_articles.title, count(*) as views
from log join (select title, concat('/article/', slug) as path
                from articles) as pathed_articles
on pathed_articles.path=log.path
group by pathed_articles.title
order by views desc
limit {};""".format(nb_articles))
    result = cursor.fetchall()
    db.close()
    return result


def most_pop_authors():
    db = psycopg2.connect(DataBaseName)
    cursor = db.cursor()
    cursor.execute("""
select authors.name, count(*) as views
from authors JOIN
(
    select a.author
    from log join
        (
            select title, author, concat('/article/', slug) as path
            from articles
        ) as a
    on a.path=log.path
) as b
on b.author=authors.id
group by authors.id
order by views desc;
    """)
    result = cursor.fetchall()
    db.close()
    return result


def errors_above_one():
    db = psycopg2.connect(DataBaseName)
    cursor = db.cursor()
    cursor.execute("""
select a.date, (cast(a.count as decimal) * 100 / b.count) as errors from (
select date(time) as date, count(status) from log
where status!='200 OK'
group by date
order by date asc
) as a
join (select date(time) as date, count(status) from log
group by date
order by date asc) as b
on a.date=b.date
where (cast(a.count as decimal) * 100 / b.count)>=1
order by errors desc;
    """)
    result = cursor.fetchall()
    db.close()
    return result

if __name__ == "__main__":
    # printing the popular articles:
    pop_art = most_pop_articles()
    print("Most popular three articles of all time:")
    print("title".ljust(37), "views")
    print("-"*47)
    for e in pop_art:
        print(e[0], '---', e[1], 'views')
    print("-"*47)

    # printing the popular authors:
    pop_auth = most_pop_authors()
    print("\n\nMost popular authors of all time:")
    print("author".ljust(37), "views")
    print("-"*47)
    for e in pop_auth:
        print(e[0].ljust(32), '---', e[1], 'views')
    print("-"*47)
    # printing the day where error requeset are bigger than 1%:
    errors = errors_above_one()
    print("\n\nDays where error requests are bigger than 1%:")
    print("Date".ljust(37), "error ratio")
    print("-"*47)
    for e in errors:
        print(e[0].strftime('%b %d, %Y').ljust(32), '---  %.2f' % e[1],
              '% erros')
    print("-" * 47)
