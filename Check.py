import dataset
blog_id = 'ytyaru.hatenablog.com'
db_entries = dataset.connect('sqlite:///' + "meta_Hatena.Blog.Entries.{0}.sqlite3".format(blog_id))
sql = "select EntryId,Published from Entries order by Published asc;"
for record in db_entries.query(sql):
    print("{0},{1}".format(record['EntryId'],record['Published']))

