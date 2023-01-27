report2022.pdf: report.dvi 
	dvipdfmx -p a4 report.dvi

report.dvi: report.tex 1_intro.tex 2_cgmd.tex 3_results.tex\
	Figs/fig1.pdf Figs/fig2.pdf Figs/fig3.pdf Figs/fig4.pdf Figs/fig5.pdf 
	platex report.tex

#Figs/fig1.eps: Figs/fig1.svgz
#	inkscape -z -f Figs/fig1.svgz -E Figs/fig1.eps
Figs/fig1.pdf: Figs/fig1.svgz
	inkscape Figs/fig1.svgz --export-pdf=Figs/fig1.pdf --export-text-to-path
Figs/fig2.pdf: Figs/fig2.svgz
	inkscape Figs/fig2.svgz --export-pdf=Figs/fig2.pdf --export-text-to-path
Figs/fig3.pdf: Figs/fig3.svgz
	inkscape Figs/fig3.svgz --export-pdf=Figs/fig3.pdf --export-text-to-path
Figs/fig4.pdf: Figs/fig4.svgz
	inkscape Figs/fig4.svgz --export-pdf=Figs/fig4.pdf --export-text-to-path
Figs/fig5.pdf: Figs/fig5.svgz
	inkscape Figs/fig5.svgz --export-pdf=Figs/fig5.pdf --export-text-to-path

