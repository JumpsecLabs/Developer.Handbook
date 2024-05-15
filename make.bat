mkdir dist

pandoc $(cat pandoc_order.txt) -s -o dist/developer_handbook.html --toc --number-sections

pandoc intermediate_document.html -s -o output_document.pdf