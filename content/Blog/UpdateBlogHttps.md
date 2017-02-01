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

实现根据修改时间排序，并可分页。