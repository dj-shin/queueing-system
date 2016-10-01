from system import System


if __name__ == '__main__':
    n = 100
    testSet = [
        (0.030, 0.10),
        (0.30, 1.0),
        (3.0, 10.0),
        (0.040, 0.10),
        (0.40, 1.0),
        (4.0, 10.0),
        (0.050, 0.10),
        (0.50, 1.0),
        (5.0, 10.0),
        (0.060, 0.10),
        (0.60, 1.0),
        (6.0, 10.0),
        (0.070, 0.10),
        (0.70, 1.0),
        (7.0, 10.0),
        (0.080, 0.10),
        (0.80, 1.0),
        (8.0, 10.0),
        (0.090, 0.10),
        (0.90, 1.0),
        (9.0, 10.0),
        (0.095, 0.10),
        (0.95, 1.0),
        (9.5, 10.0),
    ]
    for l, u in testSet:
        result = {
            'Ls': [],
            'Lq': [],
            'L' : [],
            'Ws': [],
            'Wq': [],
            'W' : [],
        }
        for i in range(n):
            system = System(('M', l), ('M', u), 1)
            totalTime = 10000.0 / u
            stableTime = totalTime / 10
            system.run(stableTime, totalTime)

            Ls = system.server.L()
            Lq = system.queue.L()
            L = Ls + Lq
            Ws = system.server.W()
            Wq = system.queue.W()
            W = Ws + Wq

            # print('Ls = %lf' % Ls, end='\t')
            # print('Lq = %lf' % Lq, end='\t')
            # print('L  = %lf' % L,  end='\t')
            # print('Ws = %lf' % Ws, end='\t')
            # print('Wq = %lf' % Wq, end='\t')
            # print('W  = %lf' % W,  end='\t')
            # print('')

            result['Lq'].append(Lq)
            result['Ls'].append(Ls)
            result['L'].append(L)
            result['Wq'].append(Wq)
            result['Ws'].append(Ws)
            result['W'].append(W)
            print('#', end='', flush=True)
        print('')

        print('l = %lf\tu = %lf' % (l, u), end='\t')
        print('Average Ls = %lf' % (sum(result['Ls']) / n), end='\t')
        print('Average Lq = %lf' % (sum(result['Lq']) / n), end='\t')
        print('Average L  = %lf' % (sum(result['L'])  / n),  end='\t')
        print('Average Ws = %lf' % (sum(result['Ws']) / n), end='\t')
        print('Average Wq = %lf' % (sum(result['Wq']) / n), end='\t')
        print('Average W  = %lf' % (sum(result['W'])  / n),  end='\t')
        print('')
