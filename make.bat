mkdir dist

pandoc $(cat pandoc_order.txt) metadata.yaml --include-before-body=version.md -s -o dist/developer_handbook.html --toc --number-sections --wrap=none

pandoc dist/developer_handbook.html -s --pdf-engine=xelatex -o dist/developer_handbook.pdf