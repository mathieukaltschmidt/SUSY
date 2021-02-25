import numpy as np
import matplotlib.pyplot as plt

def run_coup(s, alpha0, b):
    return alpha0-b*s*np.log(10)/(2*np.pi)

alph=[98.369*3/5, 29.584, 8.48]
dalph=[0.018*3/5, 0.005, 0.07]
rs=.15 # dQ/Q
b   =[4.1, -18.75/6, -7]
#b   =[4.1, -19/6, -7]
c   =[6.58, 1, -3]
#c   =[33/5, 1, -3]
col=['r', 'g', 'b']
x=np.array([0, 20])

plt.rc('text', usetex=True)
plt.figure(figsize=(5, 5))

plt.text(15, 10, r'$\mathrm{SM}$', size=20)
for i in range(3):
    plt.plot(x, run_coup(x, alph[i], b[i]), lw=.8, color=col[i])
    plt.plot(x, run_coup(x+rs, alph[i]+dalph[i], b[i]), lw=.4, ls='dotted', color=col[i])
    plt.plot(x, run_coup(x-rs, alph[i]-dalph[i], b[i]), lw=.4, ls='dotted', color=col[i])
    plt.text(5, run_coup(5, alph[i], b[i])+3, r'$\alpha^{-1}_'+str(i+1)+r'$', size=15)

plt.xticks([0, 5, 10, 15, 20])

plt.xlim(-1, 21)
plt.ylim(0, 60)
plt.xlabel(r'$\log\frac{Q}{m_Z}$', size=20)

plt.savefig('dgut-1.pdf', bbox_inches='tight')
plt.show()

plt.rc('text', usetex=True)
plt.figure(figsize=(5, 5))

plt.text(15, 10, r'$\mathrm{MSSM}$', size=20)
for i in range(3):
    plt.plot(x, run_coup(x, alph[i], c[i]), lw=.8, color=col[i])
    plt.plot(x, run_coup(x+rs, alph[i]+dalph[i], c[i]), lw=.4, ls='dotted', color=col[i])
    plt.plot(x, run_coup(x-rs, alph[i]-dalph[i], c[i]), lw=.4, ls='dotted', color=col[i])
    plt.text(5, run_coup(5, alph[i], c[i])+3, r'$\alpha^{-1}_'+str(i+1)+r'$', size=15)

plt.xticks([0, 5, 10, 15, 20])

plt.xlim(-1, 21)
plt.ylim(0, 60)
plt.xlabel(r'$\log\frac{Q}{m_Z}$', size=20)

plt.savefig('dgut-2.pdf', bbox_inches='tight')
plt.show()

