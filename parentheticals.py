BLACKLIST = set([
'1970 acm turing lecture',
'1st ed.',
'1st edition',
'2nd ed.',
'3rd edition',
'abridged version',
'abstract',
'abstract of invited tutorial',
'abstract only',
'abstracts',
"acm president's letter",
'addison-wesley professional ruby series',
'a. m. turing award lecture',
'an announcement',
'an extended abstract',
'a preliminary version',
'avstract',
'awarded best paper!',
'awarded best paper',
'awarded best student paper!',
'awarded best student paper',
'best paper',
'brief announcement',
'brief announement',
'demo',
'demonstration description',
'detailed abstract',
'draft',
'experience paper',
'extenced abstract',
'extended abstract',
'extended abstracts',
'extended announcement',
'extended anstract',
'extended astract',
'extended summary',
'extended version',
'indroduction to the special section on logic programming',
'interview',
'introduction to the special issue',
'introduction to the special section',
'intruduction to the special section',
'invited address',
'invited paper',
'keynote address',
'microsoft windows server system series',
'panel',
'panel abstract',
'panel session, abstract only',
'panel session - title only',
'panel session, title only',
'panel statement',
'partial report',
'pearl',
'podc 1984 invited address',
'poster',
'poster abstract',
'preliminary abstract',
'preliminary draught',
'preliminary report',
'preliminary reports',
'preliminary version',
'prentice hall open source software development series',
'proceedings',
'remarks',
'report of the jtec panel',
'reprint',
'second edition',
'short abstract',
'shortened version',
'sintra, portugal, 7-10 september 1998',
'summary',
"surveyors' forum",
'turing award lecture',
'tutorial',
'working paper',
'work in progress, abstract',
])

WHITELIST = set([
'!=',
'0, 1',
'1',
'1, 2',
'1, 342 times and counting',
'1600 cpi, phase encoded',
'1976-1978',
'1982',
'1993',
'1 + beta',
'1 + eps',
'1 + epsilon',
'1+, varepsilon;, beta',
'2 + epsilon',
'2+epsilon',
'2k',
'800 cpi, nrzi',
'9 track-200 and 800 cpi, nrzi and 1600 cpi, p.e.',
'a case of error reporting system',
'acsii',
'active suspension',
'acyclic',
'advances in information security',
'a fictional case study',
'aims',
'aims-2',
'aims-3',
'algorithm a433',
'algorithm a438',
'almost',
'alpha, beta',
'and a letter',
'and beyond?',
'and beyond',
'and commit',
'and darwinian',
'and everthing in between',
'and everything else',
'and future',
'and how flash memory changes the rules',
'and how not',
'and how not to',
"and how they're sometimes found",
'and mistrust',
'and other',
'and others too!',
'and pretty good for quantum as well',
'and safety',
'and the sesame street syndrome',
'and trusting no one',
'a polynomial algorithm for 3-compatible colouring and the stubborn list partition problem',
'applications of comparative physical maps in molecular evolution',
'april 1984 special section',
'are not',
'a state-of-the-art report on omg/corba',
'a usaai',
'beta,gamma,delta',
'biastm',
'bpm',
'bsr',
'btx',
'bus',
'but we all see the point of tainting',
'byzantine agreement on uniformly random values',
'cam',
'cbids',
'class hierarchical open interface for custom embedded systems',
'commerce edition',
'components + patterns',
'computer',
'computer communications and networks',
'connected',
'connectionless',
'console operator proficiency examination',
'cosers',
'cost',
'creation and use',
'cycles, and partitions',
'data',
'database',
'dctcp',
'de',
'deadlock detection',
'demo abstract',
'deterministic',
'dir',
'dis',
'disco',
'dsdv',
'dynamic',
'early and often?',
'else',
'epsilon, delta',
'esair',
'even and odd orders',
'even order',
'expected time',
'fairly',
'fdna-03',
'febid 2010',
'ferrite',
'+-f(+-f(...+-f(x)...))',
'fitting distances by tree metrics',
'for high-concurrency servers',
'for vlsi',
'gier algol',
'googling the internet',
'gradually',
'h-k',
'hms',
'hopefully',
"hotpower'11",
"hotswup'09",
"hotswup'11",
'hyper',
"ifip/sec'84 proceedings",
"ifip/sec'85 proceedings",
'ii',
'im',
'in',
'in cournot competition',
'incremental',
'indeterministic',
'information pollution',
'in java',
'in networking',
'intermittent assertions in proving program correctness',
'internals overview',
'intervals',
'jsq',
'june 1962',
'<= k',
'k <= 6',
'k, r',
'ladis 2009',
'ladis 2011',
'lbc',
'ldl',
'ldl1',
'learning a string',
'lms',
'log ^c n',
'log c n',
'log n',
"maier's o-logic revisited",
'max, min',
'meta',
'milman',
'mis',
'mlr',
'm&m',
'mod p - mod m',
'more',
'multi',
'multimesh',
'natural',
'n, d',
'nearly',
'netdb 2009',
'networks of workstations',
'nicta',
'n log n',
'non-',
'non',
'non-uniform message-passing',
"nossdav '93",
'not',
'not a privilege',
'not so',
'object database and environment',
'odd and even orders',
'odd and, even orders',
'odd order',
'of communications',
'on behalf of john cocke',
'online',
'only',
"opensig'98",
'optimal',
'oracle curve plotter',
'or, business processes for database researchers',
'or how to turn ideas into live systems in a breeze',
'or not',
'or, programs from outer space',
'or repetitive consensus',
'or, routing issues in mpls',
'or towards a standard ada subset',
'or why capabilities might have been invented',
'or, why mazes are easier to search than graphs',
'output',
'over',
'parallel',
'part 1',
'part 2',
'part i',
'part ii',
'part i: the architecture',
'physical design tuning',
'poly',
'polynomial algorithm for genomic distance problem',
'priority queue',
'probably',
"proc. sigmod'03",
'psa',
'psbgp',
'qspnet',
'raid',
're',
'really',
'rectangular matrices',
'remark on algorithms 352, 385, 392',
'repeated',
'rfcs',
'rladsms',
'rohc',
'rome',
'rwa',
's',
'satnet',
'sba',
'sdd-1',
'secret',
'sembegs',
'semi',
'sharqfec',
'software',
'some',
'some preprocessing required',
"sosp'99",
'source',
'speed08',
's.p.m',
'spo protocol',
's, t',
'stack',
'standard',
'storage',
'stream-enabled',
'sundr',
'systor 2007',
't + 1',
'talking with julian gosper, jean-luc agathos, richard rutter, and terry coatta',
'the choice of decimal or binary representation',
'the odds are on his side',
'the vasa',
'travelocity-based detouring',
'tribute, jonathan b. postel 1943-1998',
u'1+epsilon',
u'1+\u03ad',
u'1 + \u03b5',
'un',
'unproven',
'unto',
'unweighted',
'ural',
'ussr',
'very',
'viewpoint',
'vlsi',
'wavelength',
'weakly',
'wep',
'what once was',
'what time will you die?',
'why id might not be strict',
'wie2009',
'wie2011',
'wit',
'without conditional statements',
'without matrix multiplication',
'without powerdomains',
'workshop rewiew',
'wyxiwyg',
'x',
'x.1500',
'xquery by example',
])

TRANSLATE = {'ISDN, panel': 'ISDN'}
