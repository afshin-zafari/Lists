import glob as g
import pylab as plt
tasks={'P1':list(),'P2':list(),'P4':list(),'total':list(),
       'Review':list(),'P3':list(),'DT':list(),'SE':list(),'Kappa':list(),'plan':list()}
def read_file(fn,out):
  fns=fn.split('_')
  dt=int(fns[1])*100+int(fns[2])
  f=open(fn,'rb')
  for line in f:
    flds = line.split()
    cnt = int(flds[0])
    grp=flds[1]
    for k in tasks.keys():
      if k in grp:
        tasks[k].append([dt,cnt])
  f.close()
  return out
l=g.glob('./*SUM.txt')
recs=list()
tasks['plan'].append([201,400])
tasks['plan'].append([901,0])
for f in l:
  recs=read_file(f,recs)
for k in tasks.keys():
  print k
  for t in tasks[k]:
    print t

fig = plt.figure()
ax=fig.add_subplot(111)
for k in ['total','plan']:
  x=[t[0] for t in tasks[k]]
  y=[t[1] for t in tasks[k]]
  ax.plot(x,y)

plt.show()