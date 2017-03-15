# このソフトウェアについて

はてなAPIでブログ記事を一括取得してDBに挿入する。

# 開発環境

* Linux Mint 17.3 MATE
* Python 3.4.3

## Webサービス

* [はてなブログAPI](http://developer.hatena.ne.jp/ja/documents/blog/apis/atom)

# 準備

## DBを作成する

* [はてなアカウントDBを作る](http://ytyaru.hatenablog.com/entry/2017/06/30/000000)
* [はてなブログDBを作る](http://ytyaru.hatenablog.com/entry/2017/07/01/000000)
    * [はてなAPIで取得したXMLからブログ情報を取得しDBに保存する](http://ytyaru.hatenablog.com/entry/2017/07/04/000000)
* [はてなブログ記事DBを作る](http://ytyaru.hatenablog.com/entry/2017/07/02/000000)
    * [はてなAPIで取得したXMLから記事データを取得しDBに保存する](http://ytyaru.hatenablog.com/entry/2017/07/05/000000)
* [はてなフォトライフDBを作る](http://ytyaru.hatenablog.com/entry/2017/07/03/000000)
    * [フォトライフRSSのデータをローカルDBへマージする](http://ytyaru.hatenablog.com/entry/2017/07/10/000000)
    * [Pythonでフォトライフから画像をダウンロードする](http://ytyaru.hatenablog.com/entry/2017/07/11/000000)

## 設定する

はてなID、ブログID(URLドメイン名)、DBのパスを指定する。

HatenaBlogEntries.py
```python
if __name__ == '__main__':
    blog_id = 'ytyaru.hatenablog.com'
    client = HatenaBlogEntries(
        hatena_id = 'ytyaru',
        blog_id = blog_id,
        path_hatena_accounts_sqlite3 = "meta_Hatena.Accounts.sqlite3",
        path_hatena_blogs_sqlite3 = "meta_Hatena.Blogs.sqlite3",
        path_hatena_blog_entries_sqlite3 = "meta_Hatena.Blog.Entries.{0}.sqlite3".format(blog_id)
    )
    client.update()
```

# 実行

```sh
python3 HatenaBlogEntries.py
```

# 結果

指定したはてなIDとブログの全記事がDBに挿入される。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[xmltodict](https://github.com/martinblech/xmltodict)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (C) 2012 Martin Blech and individual contributors.](https://github.com/martinblech/xmltodict/blob/master/LICENSE)
[requests_oauthlib](https://github.com/requests/requests-oauthlib)|[ISC](https://opensource.org/licenses/ISC)|[Copyright (c) 2014 Kenneth Reitz.](https://github.com/requests/requests-oauthlib/blob/master/LICENSE)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)

