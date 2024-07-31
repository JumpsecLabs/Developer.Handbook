cd docs 

pandoc $(cat pandoc_order.txt) metadata.yaml --include-before-body=version.md -s -o developer_handbook.html --toc --number-sections --wrap=none

pandoc docs/developer_handbook.html -s --pdf-engine=xelatex -o docs/developer_handbook.pdf