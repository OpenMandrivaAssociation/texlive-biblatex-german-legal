%global tl_name biblatex-german-legal
%global tl_revision 66461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	003
Release:	%{tl_revision}.1
Summary:	Comprehensive citation style for German legal texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-german-legal
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-german-legal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-german-legal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims to provide citation styles (for footnotes and
bibliographies) for German legal texts. It is currently focused on
citations in books (style german-legal-book), but may be extended to
journal articles in the future. Dieses Paket enthalt BibLaTeX-
Zitierstile fur die Rechtswissenschaften in Deutschland. Aktuell enthalt
es einen auf Monographien in den deutschen Rechtswissenschaften
ausgerichteten Zitierstil namens german-legal-book.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-german-legal
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-german-legal
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-german-legal/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-german-legal/biblatex-german-legal.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-german-legal/biblatex-german-legal.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-german-legal/german-legal-book.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-german-legal/german-legal-book.cbx
