all: build

content/publication.md: scripts/wen.bib scripts/bib2md.py
	python scripts/bib2md.py scripts/wen.bib content/publication.md

build: content/publication.md
	hugo

deploy: clean build
	lftp -c "debug 1; set ftps:initial-prot ; open ftp://${FTP_USER}:${FTP_PASSWD}@${FTP_HOST};  mirror -cRvPn --Remove-source-files --delete-first public web; quit;"
clean:
	-rm -r public/
