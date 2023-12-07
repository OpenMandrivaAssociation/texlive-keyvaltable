Name:		texlive-keyvaltable
Version:	65416
Release:	1
Summary:	Re-usable table layouts separating content and presentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyvaltable
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyvaltable.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main goal of this package is to offer means for typesetting
tables easily and yet still looking rather nicely in a way that
separates content from presentation and with re-usable layout
for tables of the same type. For this purpose, the package
provides the environment KeyValTable, which allows one to
typeset tables that have a previously defined column layout and
whose rows can be produced in a key-value fashion.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/keyvaltable
%{_texmfdistdir}/tex/latex/keyvaltable
%doc %{_texmfdistdir}/doc/latex/keyvaltable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
