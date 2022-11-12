Name:		texlive-ascii-chart
Version:	20536
Release:	1
Summary:	An ASCII wall chart
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ascii-chart
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
