data:
	dvc pull

processed:
	@for samplenum in 1000 10000 100000 ; do \
		if [ ! -d data/processed/$$samplenum  ]; then \
			mkdir data/processed/$$samplenum  ; \
		fi; \
	done
	head -n 1001 data/raw/HK_OOSTENDE/occurrence.txt > data/processed/1000/HK_OOSTENDE.txt
	head -n 1001 data/raw/LBBG_ZEEBRUGGE/occurrence.txt > data/processed/1000/LBBG_ZEEBRUGGE.txt
	head -n 10001 data/raw/HK_OOSTENDE/occurrence.txt > data/processed/10000/HK_OOSTENDE.txt
	head -n 10001 data/raw/LBBG_ZEEBRUGGE/occurrence.txt > data/processed/10000/LBBG_ZEEBRUGGE.txt
	head -n 100001 data/raw/HK_OOSTENDE/occurrence.txt > data/processed/100000/HK_OOSTENDE.txt
	head -n 100001 data/raw/LBBG_ZEEBRUGGE/occurrence.txt > data/processed/100000/LBBG_ZEEBRUGGE.txt
