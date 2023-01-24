report2022.pdf: report.dvi 
	dvipdfmx -p a4 report.dvi

report.dvi: report.tex 1_intro.tex 2_cgmd.tex 3_results.tex\
	#Figs/fig1.eps Figs/fig2.eps Figs/fig3.eps Figs/fig4.eps\
       	#Figs/fig5.eps Figs/fig6.eps Figs/fig7.eps Figs/fig8.eps Figs/fig9.eps 
	platex report.tex

#Figs/fig1.eps: Figs/uhyd.svgz
#	inkscape -z -f Figs/uhyd.svgz -E Figs/fig1.eps
