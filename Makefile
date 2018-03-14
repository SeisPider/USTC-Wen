all: build

content/publications.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publications.md

build: content/publications.md
	hugo

clean:
	-rm -r public/
