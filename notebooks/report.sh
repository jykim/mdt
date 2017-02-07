#!/bin/bash
source ~/.bashrc
source ~/.bash_common
cd /home/jink/jupyter/mdt/notebooks
/home/jink/bin/conda3/bin/jupyter nbconvert --to html --template basic --execute ./MDT\ -\ prod.ipynb < body.txt
mailx -s "Daily Report" myleo.jerry@gmail.com -A MDT\ -\ prod.html < body.txt
