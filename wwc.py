import glob as g
import time as t


ts=t.strftime("%Y_%m_%d_%H_%M")
sum_fn="Log/"+ts+"_SUM.txt"
tasks_fn="Log/"+ts+"_TASKS.txt"
f_tasks=open(tasks_fn,'wb')
f_sum = open(sum_fn,'wb')
def read_file(fn):
  f=open(fn,'rb')
  f_tasks.write('\n'+'='*80+'\n')
  f_tasks.write(' '*10 + fn+'\n')
  f_tasks.write('='*80+'\n')
  n=0
  for l in f:
    f_tasks.write(l)
    n += 1
  
  f.close()
  return n


fl=g.glob('*/TODO.txt')
s=0
for f in fl:
  n = read_file(f)
  s += n
  print n,f
  f_sum.write("%d %s\n" % (n,f))
print s, 'total'
f_sum.write("%d total\n"%s)
f_tasks.close()
f_sum.close()