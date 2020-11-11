import sys
import re
import nxo64

def main(pattern, filename):
	f = nxo64.load_nxo(open(filename, 'rb'))

	f.binfile.seek(0)
	target_text = f.binfile.read(f.textsize)

	rows = eval('[' + open(pattern).read() + ']')
	with open(filename + '-sdk-syms.json', 'wb') as f:
		f.write('{\n')
		first = True;
		for value, size, regex, name in rows:
			#print '(0x%X, 0x%X, %r, %r),' % (sym.value, sym.size, regex, sym.name)
			positions = [m.start() for m in re.finditer(regex, target_text)]
			if len(positions) == 1:
				f.write((',\n' if not first else "") + '	"0x%X" : "%s"' % (0x7100000000 + positions[0], name))
				first = False
		f.write('}\n')

			
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'usage: applypattern.py pattern.txt [nxo files...]'
		print 'writes output to input filename + "-sdk-syms.py"'
	for filename in sys.argv[2:]:
		main(sys.argv[1], filename)
