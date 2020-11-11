import json

# based on snippet by astrelsky
infile = askFile('Select symbol file', 'OK')
syms = None
with open(str(infile), 'r') as fd:
    syms = json.load(fd)

    print(syms)
    from ghidra.program.model.symbol import SourceType
    fm = currentProgram.getFunctionManager()
    for addr, sym in syms.iteritems():
        funcAddr = toAddr(str(addr))
        try:
            f = fm.getFunctionAt(funcAddr)
            f.setName(sym, SourceType.ANALYSIS)
            print("Rename " + str(addr))
        except:
            createFunction(funcAddr, sym)
            print("Created " + str(addr))
            pass
