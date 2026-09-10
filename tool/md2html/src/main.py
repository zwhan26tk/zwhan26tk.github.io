import sys
import re

from util.xlog import log_dbg


def usage(prog):
    print('usage: %s [input-md-file] [output-html-file]' % prog)


def md2html(ifile, ofile):
    log_dbg('convert "%s" to "%s"...' % (ifile, ofile))
    worker = Md2HtmlWorker()
    worker.input = ifile
    worker.output = ofile
    worker.run()


class Md2HtmlWorker(object):

    def __init__(self):
        self.input = ''
        self.output = ''

    def run(self):
        doc = MdReader().read(self.input)
        HtmlWriter().write_doc(doc, self.output)


class MdDocument(object):

    def __init__(self):
        self.blocks = list()

    def add_header(self, txt):
        pttn = re.compile('(#+?)\s+?.*')
        mt = pttn.match(txt)
        hashes = mt.group(1)
        lv = len(hashes)
        self.add_block(MdHeader(lv, txt[lv:].strip()))

    def add_code_block(self, txt):
        self.add_block(MdCodeBlock(txt))

    def add_par(self, txt):
        self.add_block(MdPar(txt))

    def add_block(self, block):
        self.blocks.append(block)



class MdObject(object):

    def __init__(self, txt):
        self.text = txt


class MdHeader(MdObject):

    def __init__(self, lv, txt):
        super().__init__(txt)
        self.level = lv


class MdCodeBlock(MdObject):

    def __init__(self, txt):
        super().__init__(txt)


class MdPar(MdObject):

    def __init__(self, txt):
        super().__init__(txt)


class MdReader(object):

    def __init__(self):
        self.current_type = ''

    def read(self, input_file):
        doc = MdDocument()
        lines = self.read_lines_from_file(input_file)
        for line in lines:
            if not len(line.strip()) > 0:
                continue

            if is_header(line):
                self.current_type = ''
                doc.add_header(line)
            elif line.startswith('\t'):
                self.current_type = 'code-block'
                doc.add_code_block(line.strip())
            else:
                self.current_type = ''
                doc.add_par(line.strip())
        return doc

    def read_lines_from_file(self, input_file):
        with open(input_file, 'r') as fh:
            return fh.readlines()



def is_header(txt):
    pttn = re.compile('#+?\s+?.*')
    if pttn.match(txt):
        return True
    return False


class HtmlWriter(object):

    def __init__(self):
        self.fh = None
        self.current_state = ''

    def write_doc(self, doc: MdDocument, output_file):
        with open(output_file, 'w') as fh:
            self.fh = fh
            self.write_start()
            for block in doc.blocks:
                self.write_block(block)
            self.write_end()

    def write_start(self):
        self.fh.write('''
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>Batch-Programmierung</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
		integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>
        ''')

    def write_end(self):
        self.fh.write('''
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
		integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
		crossorigin="anonymous"></script>
</body>

</html>
        ''')

    def write_block(self, block):
        if block.__class__.__name__ == 'MdHeader':
            self.write_header(block)
        elif block.__class__.__name__ == 'MdCodeBlock':
            self.write_code_block(block)
        else:
            self.write_par(block)

    def write_header(self, obj: MdHeader):
        self.fh.write('<h%d>%s</h%d>' % (obj.level, obj.text, obj.level))

    def write_code_block(self, obj: MdHeader):
        self.fh.write('<code>%s</code>' % (obj.text))

    def write_par(self, obj: MdHeader):
        self.fh.write('<p>%s</p>' % (obj.text))


if '__main__' == __name__:
    log_dbg('--- start ---')
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        exit(1)
    md2html(sys.argv[1], sys.argv[2])
    log_dbg('--- end ---')

