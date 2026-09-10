SHELL=/bin/bash


.PHONY: plain
plain:
	pandoc start.md -s -c ../common.css -o start.html


.PHONY: bootstrap
bootstrap:
	pandoc start.md -s \
		-c https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css \
		-o start.html




