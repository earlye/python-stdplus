CHAPTERS=$(wildcard _chapters/chapter-*.markdown)

all : .build

publish : .build
	scp -r .build/* www.stdplus.org:~/subdomains/python/

serve : .build
	bundle exec jekyll serve --destination .build --host 0.0.0.0 --port 4001

clean :
	-rm -rf .build
	-rm -rf .setup

.build : .setup
	jekyll build --destination $@

.setup :
	bundle install
	touch $@
