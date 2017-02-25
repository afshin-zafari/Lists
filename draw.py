import glob as g
import pylab as plt
import datetime as dtm
tasks={'P1':list(),'P2':list(),'P4':list(),'total':list(),
       'Review':list(),'P3':list(),'DT':list(),'SE':list(),'Kappa':list(),'plan':list()}
def read_file(fn,out):
  fns=fn.split('_')
  dt=int(fns[1])*100+int(fns[2])#MMDD
  d1=dtm.date(2017,02,01)
  d2=dtm.date(2017,dt/100,dt%100)
  d3=d2-d1
  dt=d3.days
  
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
l=g.glob('Log/*SUM.txt')
recs=list()
tasks['plan'].append([1,300])
tasks['plan'].append([365-31-31-30-31,0])
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
import time as tt
ts=tt.strftime("%Y_%m_%d_%H_%M")
plt.xticks([0,28,59,89,119,149,179,209,239,269],['Feb','March','April','May','June','July','August','Sept.','Oct.','Nov.'])
plt.savefig("Log/"+ts+'.png')
plt.show()