Name:		texlive-biblatex-german-legal
Version:	66461
Release:	1
Summary:	Comprehensive citation style for German legal texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-german-legal
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-german-legal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-german-legal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims to provide citation styles (for footnotes and
bibliographies) for German legal texts. It is currently focused
on citations in books (style german-legal-book), but may be
extended to journal articles in the future. Dieses Paket
enthalt BibLaTeX-Zitierstile fur die Rechtswissenschaften in
Deutschland. Aktuell enthalt es einen auf Monographien in den
deutschen Rechtswissenschaften ausgerichteten Zitierstil namens
german-legal-book.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-german-legal
%doc %{_texmfdistdir}/doc/latex/biblatex-german-legal

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
