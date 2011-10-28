"""%s source_pdf dest_pdf top [right [bottom [left]]]

top, right, bottom, left just like the CSS expressions.


EXAMPLE:
    ./crop-pdf.py Seven.pdf cropped-seven.pdf 5

"""
import sys
from pyPdf import PdfFileWriter, PdfFileReader

if len(sys.argv) < 3:
    print __doc__ % sys.argv[0]
    sys.exit()
    
pdf_file = sys.argv[1]
dest_file_name = sys.argv[2]

top = right = bottom = left = sys.argv[3]

position_count = len(sys.argv) -3
get_position = lambda index: sys.argv[index+3]

if position_count > 1:
    right = left = sys.argv[4]
if position_count > 2:
    bottom = sys.argv[5]
if position_count == 4:
    left = sys.argv[6]
    
try:
    top, right, bottom, left = map(int, [top, right, bottom, left])
except ValueError:
    print "position must be number"
    sys.exit()

print "cropping ", top, right, bottom, left

output = PdfFileWriter()
input = PdfFileReader(file(pdf_file, "rb"))

page_count = input.getNumPages()
pages = range(0, page_count)
for page_no in pages:
    page = input.getPage(page_no)
    page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - bottom)
    page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x() + left, page.mediaBox.getLowerLeft_y() + top)

    output.addPage(page)
    
stream = file(dest_file_name, 'wb')
output.write(stream)
stream.close()
