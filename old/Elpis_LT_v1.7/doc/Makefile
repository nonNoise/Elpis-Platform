# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."


pdf:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	wkhtmltopdf --print-media-type --page-size B5 _build/html/index.html ./PDF/index.pdf

	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/01.html ./PDF/01_01.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/01_column.html ./PDF/01_01_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/02.html ./PDF/01_02.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/02_column.html ./PDF/01_02_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/03.html ./PDF/01_03.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/03_column.html ./PDF/01_03_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/04.html ./PDF/01_04.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/01_syokyu/04_column.html ./PDF/01_04_column.pdf

	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/01.html ./PDF/02_01.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/01_column.html ./PDF/02_01_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/02.html ./PDF/02_02.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/02_column.html ./PDF/02_02_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/03.html ./PDF/02_03.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/03_column.html ./PDF/02_03_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/04.html ./PDF/02_04.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/02_tyuukyuu/04_column.html ./PDF/02_04_column.pdf

	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/01.html ./PDF/03_01.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/01_column.html ./PDF/03_01_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/02.html ./PDF/03_02.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/02_column.html ./PDF/03_02_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/03.html ./PDF/03_03.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/03_column.html ./PDF/03_03_column.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/04.html ./PDF/03_04.pdf
	wkhtmltopdf --print-media-type --page-size B5 _build/html/03_zyoukyuu/04_column.html ./PDF/03_04_column.pdf

	@echo
	@echo "Build finished. The PDF files are in _build/pdf."
