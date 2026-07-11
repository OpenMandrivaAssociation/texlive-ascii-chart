%global tl_name ascii-chart
%global tl_revision 20536

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An ASCII wall chart
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/ascii-chart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-chart.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document may be converted between Plain TeX and LaTeX (2.09) by a
simple editing action.

