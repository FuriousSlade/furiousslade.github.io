Title:Blog改版
Date:2017-01-31
Category:Blog
Modified:2017-02-01
Tags:Blog,Pelican


博客模版改版,做了一波减法，清爽多了。

通过cloudflare成功https。( ´▽` )ﾉ

使用Pelican插件always_modified给所有的文章默认加上修改时间。

修改index.html模版:

	{% set paginator_articles = articles|sort(reverse=True,attribute='modified') %}
	{% set offset = (articles_page.number - 1) * DEFAULT_PAGINATION %}
	{% set end = DEFAULT_PAGINATION * articles_page.number %}
	{% if end >= paginator_articles|length %}
		{% set end = paginator_articles|length + 1 %}
	{% endif %}
	{% for article in paginator_articles[offset:end] %}
		...
	{% endfor %}

修改发布配置文件：

	PLUGINS = [
    'sitemap',
    'gzip_cache',
    'extract_toc',
    'tipue_search',
    'related_posts',
    'always_modified',
	]

	ALWAYS_MODIFIED = True
	
一开始因为没有增加`ALWAYS_MODIFIED = True`这行配置造成在travis ci构建一直失败。

\_(´ཀ`」 ∠)_

实现根据修改时间排序，并可分页。