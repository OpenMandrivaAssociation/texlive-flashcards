# revision 19667
# category Package
# catalog-ctan /macros/latex/contrib/flashcards
# catalog-date 2010-08-06 13:03:06 +0200
# catalog-license gpl
# catalog-version 1.0.1
Name:		texlive-flashcards
Version:	1.0.1
Release:	1
Summary:	A class for typesetting flashcards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flashcards
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashcards.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashcards.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flashcards.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The FlashCards class provides for the typesetting of flash
cards. By flash card, we mean a two sided card which has a
prompt or a question on one side and the response or the answer
on the flip (back) side. Flash cards come in many sizes
depending on the nature of the information they contain.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flashcards/avery5371.cfg
%{_texmfdistdir}/tex/latex/flashcards/avery5388.cfg
%{_texmfdistdir}/tex/latex/flashcards/flashcards.cls
%doc %{_texmfdistdir}/doc/latex/flashcards/COPYING
%doc %{_texmfdistdir}/doc/latex/flashcards/README
%doc %{_texmfdistdir}/doc/latex/flashcards/flashcards.pdf
%doc %{_texmfdistdir}/doc/latex/flashcards/samplecards.tex
#- source
%doc %{_texmfdistdir}/source/latex/flashcards/flashcards.dtx
%doc %{_texmfdistdir}/source/latex/flashcards/flashcards.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
