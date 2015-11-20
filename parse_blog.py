from bs4 import BeautifulSoup as Soup
from datetime import datetime
import string


file = "blog_remove_escape.xml"
handler = open(file).read()
soup = Soup(handler)
entries = soup.findAll("entry")
num_entries = len(entries)
print "Total posts: ", num_entries

template_file = "post_template_using_blog_folder.html"
blog_ind_digit = 4

for (n_exported, entry) in enumerate(entries):
	print n_exported
	# renew soup for every html file
	template = open(template_file, "r")
	template_soup = Soup(template)
	html_file_name = "../Connie_v1.0/blogs/blog_post_" + str(n_exported).zfill(blog_ind_digit) + ".html"
	with open(html_file_name, "w") as f:
		# title
		t = template_soup.find("h3", class_ = "blogpost_title")
		if entry.title.string is not None:
			t.string = entry.title.string

		# content
		template_soup.find("article", class_="contentarea").append(entry.content)
		# date
		dt = datetime.strptime(entry.updated.string.split(".")[0], "%Y-%m-%dT%H:%M:%S")
		template_soup.find("span", class_ = "box_month").string = dt.strftime('%b')
		template_soup.find("span", class_ = "box_day").string = dt.strftime("%d")
		meta = template_soup.find("div", class_ = "listing_meta").findAll("span")
		meta[0].string = dt.strftime("%Y")
		meta[1].string = "Tags: advertisement, fun"

		# change previous/next page link
		if n_exported > 0:
			previous_blog_post_url = "blog_post_" + str(n_exported-1).zfill(blog_ind_digit) + ".html"
			template_soup.find("div", class_= "fleft").find("a")["href"] = previous_blog_post_url

		if n_exported < num_entries -1:
			next_blog_post_url = "blog_post_" + str(n_exported+1).zfill(blog_ind_digit) + ".html"
			template_soup.find("div", class_= "fright").find("a")["href"] = next_blog_post_url


		html_file = template_soup.prettify("utf-8")
		f.write(html_file)
		n_exported += 1


print n_exported, "files exported!"
