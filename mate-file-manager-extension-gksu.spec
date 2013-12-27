Summary:	gksu extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE
Name:		mate-file-manager-extension-gksu
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/mate-file-manager-gksu-%{version}.tar.xz
# Source0-md5:	9bb03a789771c4577cf42aa68e7b1b27
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gksu
Requires:	mate-file-manager >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gksu extension for Caja (MATE file manager). It's a fork of
nautilus-gksu extension.

%description -l pl.UTF-8
Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE. Jest to
odgałęzienie rozszerzenia nautilus-gksu.

%prep
%setup -q -n mate-file-manager-gksu-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

%find_lang caja-gksu

%clean
rm -rf $RPM_BUILD_ROOT

%files -f caja-gksu.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-gksu.so
