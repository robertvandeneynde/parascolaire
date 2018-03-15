echo "this .bat is out of date compared to the linux one, beware"
REM ./generate_txt.py
py -3 generate_html_progra_equivalences_multilang.py
py -3 generate_multilang.py --langs fr en
py -3 generate_html.py
REM ./generate_ln.py
py -3 generate_ls.py REM keep last
cd home/2017-2018
py -3 generate_index.py
cd ../..
