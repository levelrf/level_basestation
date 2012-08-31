
#!/usr/bin/python

import sys, os, re
sys.path.append('/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python')
os.environ['srcdir'] = '/home/rob/workspace/gnuradio/level_basestation/gr-digital/include'
os.chdir('/home/rob/workspace/gnuradio/level_basestation/build/gr-digital/include')

if __name__ == '__main__':
    import build_utils
    root, inp = sys.argv[1:3]
    for sig in sys.argv[3:]:
        name = re.sub ('X+', sig, root)
        d = build_utils.standard_dict(name, sig, 'digital')
        build_utils.expand_template(d, inp)

