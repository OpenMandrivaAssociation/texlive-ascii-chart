# revision 20536
# category Package
# catalog-ctan /info/ascii-chart
# catalog-date 2010-11-22 13:41:51 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-ascii-chart
Version:	20101122
Release:	1
Summary:	An ASCII wall chart
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ascii-chart
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document may be converted between Plain TeX and LaTeX
(2.09) by a simple editing action.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/support/ascii-chart/ascii.pdf
%doc %{_texmfdistdir}/doc/support/ascii-chart/ascii.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
