import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_viewport = re.compile('<meta name="viewport" content="(?P<viewport>(.*))" />')
			regexp_identifier = re.compile('<meta name="identifier" content="(?P<identifier>([\d]*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				print("title:",title)

			result = regexp_viewport.search(content_string, re.IGNORECASE)

			if result:
				viewport = result.group("viewport")
				print("viewport:",viewport)

			result = regexp_identifier.search(content_string, re.IGNORECASE)

			if result:
				identifier = result.group("identifier")
				print("identifier:",identifier)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")