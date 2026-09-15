from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parent
BG, FG, MUTED = '#0B1424', '#F5F7FC', '#AFBBD0'
fig = plt.figure(figsize=(12, 13.5), facecolor=BG)
def label(x, y, text, size=14, color=FG, weight='normal', **kw):
    fig.text(x, y, text, fontsize=size, color=color, weight=weight, **kw)
label(.08,.948,'HUMAN PERCEPTION / RESEARCH REVIEW',12,'#56DECF','bold')
label(.08,.878,'Can we still spot\nAI-generated faces?',34,weight='bold',linespacing=1.12)
label(.08,.825,'Age matters. So does the viewing device.',18,color=MUTED)
label(.08,.764,'2026 STUDY  /  AGE AND CLASSIFICATION ACCURACY',12,'#56DECF','bold')
label(.08,.724,'Lower accuracy associated with each 10-year age difference',16)
ax = fig.add_axes([.18,.445,.72,.235],facecolor=BG)
values=[6.07,2.30]
ax.barh([1,0],values,color=['#56DECF','#91A9FF'],height=.44)
ax.set_yticks([1,0],['Mobile','PC'],fontsize=16,color=FG)
ax.set_xlim(0,7.5)
ax.set_xticks([0,2,4,6])
ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'{x:g}'))
ax.tick_params(axis='x',colors=MUTED,labelsize=12,length=0)
ax.tick_params(axis='y',length=0,pad=14)
ax.set_xlabel('Associated decrease (percentage points)',color=MUTED,fontsize=12,labelpad=12)
for spine in ax.spines.values(): spine.set_visible(False)
for y,v in zip([1,0],values):
    ax.text(v+.15,y,f'{v:.2f} pp',va='center',color=FG,fontsize=19,weight='bold')
label(.08,.381,'1,664 adults, ages 20–69  •  Mobile n=1,330; PC n=334',13,color=MUTED)
label(.08,.35,'Cross-sectional association, not a measured decline as people age.\nPublished as a preprint in 2026; tested Aug 2025–Jan 2026\nusing portraits generated in July 2025.',11,color=MUTED,linespacing=1.6,va='top')
label(.08,.258,'2022 CONTEXT',12,'#56DECF','bold')
label(.08,.22,'48.2% accuracy',25,weight='bold')
label(.08,.167,'Participants were already near chance when classifying real and\nStyleGAN2 faces in a 2022 experiment. AI faces were not always easy\nto identify. These studies do not establish a 2022–2026 trend.',12,color=MUTED,linespacing=1.5)
label(.08,.092,'SOURCES  Nightingale & Farid (2022), doi:10.1073/pnas.2120481119\nKim & Kim (2026), arXiv:2603.24048, Fig. 2 / Results\nCalculation: published age slopes × 10. Faces only; no video conclusions.',9,color=MUTED,linespacing=1.5)
label(.08,.033,'ARTHUR QUINTINO  /  AI EVALUATION & DATA ANALYSIS',10,weight='bold')
fig.savefig(ROOT/'AI_Visual_Perception.png',dpi=160,facecolor=BG)

