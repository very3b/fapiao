#docker container run --rm -it   svcvit/mupdf python3 main.py -i ./invoice -o output.xlsx
#docker container run --rm -it   svcvit/mupdf python3 main.py -o output.xlsx
#docker run --rm -it -v /app/eda/skill/fapiao/invoice_extraction:/opt/invoice svcvit/mupdf python3 main2.py -o output.xlsx
#docker run --rm -it -v /app/eda/skill/fapiao/invoice_extraction:/code2 svcvit/mupdf python3 /code2/main.py
docker run -it -v /app/eda/skill/fapiao/invoice_extraction:/code fapiao python3 fapiao.py -i 202004 

