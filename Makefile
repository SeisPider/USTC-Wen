build: content/publications.md
	hugo

content/publications.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publications.md

deploy: build

clean:
	-rm -r public/
