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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims to provide citation styles (for footnotes and
bibliographies) for German legal texts. It is currently focused on
citations in books (style german-legal-book), but may be extended to
journal articles in the future. Dieses Paket enthalt BibLaTeX-
Zitierstile fur die Rechtswissenschaften in Deutschland. Aktuell enthalt
es einen auf Monographien in den deutschen Rechtswissenschaften
ausgerichteten Zitierstil namens german-legal-book.

