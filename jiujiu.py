#print ('\n'.join([' '.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)])) 
for i in range(1, 10) :
    for j in range(1, i+1) :
        print j, 'x', i, '=', j*i, '\t',
     
