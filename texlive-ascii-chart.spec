# revision 20536
# category Package
# catalog-ctan /info/ascii-chart
# catalog-date 2010-11-22 13:41:51 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-ascii-chart
Version:	20180303
Release:	2
Summary:	An ASCII wall chart
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ascii-chart
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document may be converted between Plain TeX and LaTeX
(2.09) by a simple editing action.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/support/ascii-chart/ascii.pdf
%doc %{_texmfdistdir}/doc/support/ascii-chart/ascii.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101122-2
+ Revision: 749355
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101122-1
+ Revision: 717862
- texlive-ascii-chart
- texlive-ascii-chart
- texlive-ascii-chart
- texlive-ascii-chart

