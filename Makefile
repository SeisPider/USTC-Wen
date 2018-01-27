all: build

content/publications.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publications.md

build: content/publications.md
	hugo

deploy: clean build
	lftp -c "open ftp://${FTP_USER}:${FTP_PASSWORD}@${FTP_HOST}; mirror -eRv public public_html; quit;"

clean:
	-rm -r public/
