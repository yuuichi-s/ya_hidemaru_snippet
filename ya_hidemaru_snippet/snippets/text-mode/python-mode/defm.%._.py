def Main():
    head = "def %s(self," % argv[1]
    body = ",".join(argv[2:])
    tail = "):\n\t";
    doc  = '''"""docstring for %s"""\n\t%%|''' % argv[1]
    print(head + body + tail + doc)

Main()
