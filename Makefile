FTP_USER=byu3906270001
FTP_PASSWORD=NibxBgWUSn4H
FTP_HOST=101.200.75.132

all: build

content/publications.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publications.md

build: content/publications.md
	hugo

deploy: clean build
	lftp -c "open ftp://${FTP_USER}:${FTP_PASSWORD}@${FTP_HOST}; mirror -eRv public htdocs; quit;"

clean:
	-rm -r public/
