all: build

content/publications.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publications.md

build: content/publications.md
	hugo

deploy: clean build
	lftp -c "debug 1; set ftps:initial-prot '';  open ftp://${FTP_USER}:${FTP_PASSWD}@${FTP_HOST}; mirror -eRv public htdocs; quit;"
clean:
	-rm -r public/
