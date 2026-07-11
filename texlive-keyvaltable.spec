%global tl_name keyvaltable
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Re-usable table layouts separating content and presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keyvaltable
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main goal of this package is to offer means for typesetting tables
easily and yet still looking rather nicely in a way that separates
content from presentation and with re-usable layout for tables of the
same type. For this purpose, the package provides the environment
KeyValTable, which allows one to typeset tables that have a previously
defined column layout and whose rows can be produced in a key-value
fashion.

