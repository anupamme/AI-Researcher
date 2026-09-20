#!/usr/bin/env python3
import io, json, sys, re
props = json.load(io.open('/tmp/appendix_props.json', encoding='utf-8'))
want = sys.argv[1].split(',') if len(sys.argv) > 1 else None
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
sel = [(i, p) for i, p in enumerate(props) if not want or p['rule'] in want]
print("# %d proposals match %s ; showing [%d:%d]" % (len(sel), want, lo, hi))
for n, (i, p) in enumerate(sel):
    if not (lo <= n < hi):
        continue
    tag = "%s:%d" % (p['file'].replace('sections/', ''), p['line'])
    if p['rule'] == 'R4-pair':
        print("[%d] %-5s %-22s %s [%s] %s [%s] %s"
              % (i, n, p['rule'] + ' ' + tag, p['pre'][-52:], p['rep'][0].strip(),
                 p['inner'], p['rep'][1].strip(), p['post'][:52]))
    else:
        print("[%d] %-5s %-22s %s [%s] %s"
              % (i, n, p['rule'] + ' ' + tag, p['pre'][-66:],
                 (p['rep'][0] or '??').strip(), p['post'][:66]))
