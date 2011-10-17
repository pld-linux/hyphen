Summary:	Hyphenation library to use converted TeX hyphenation patterns
Summary(pl.UTF-8):	Biblioteka przenoszenia słów używająca przekonwertowanych wzorców TeXa
Name:		hyphen
Version:	2.8.3
Release:	1
License:	GPL v2+ or LGPL v2.1+ or MPL 1.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# Source0-md5:	86261f06c097d3e425a2f6d0b0635380
URL:		http://lingucomponent.openoffice.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyphen is a hyphenation library to use converted TeX hyphenation
patterns. This was part of libHnj library by Raph Levien.

%description -l pl.UTF-8
Hyphen to biblioteka przenoszenia słów używająca przekonwertowanych
wzorców przenoszenia z TeXa. Była częścią biblioteki libHnj autorstwa
Rapha Leviena.

%package devel
Summary:	Header files for hyphen library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hyphen
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for hyphen library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hyphen.

%package static
Summary:	Static hyphen library
Summary(pl.UTF-8):	Statyczna biblioteka hyphen
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hyphen library.

%description static -l pl.UTF-8
Statyczna biblioteka hyphen.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README* THANKS TODO doc/tb87nemeth.pdf
%attr(755,root,root) %{_bindir}/substrings.pl
%attr(755,root,root) %{_libdir}/libhyphen.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhyphen.so.0
%dir %{_datadir}/hyphen
%{_datadir}/hyphen/hyph_en_US.dic

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhyphen.so
%{_libdir}/libhyphen.la
%{_includedir}/hyphen.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libhyphen.a
