#
Summary:	Graphical utility to configure IceWM
Summary(pl):	Graficzne narzêdzie do konfiguracji IceWM'a
Summary(pt_BR): Uma ferramenta de configuração para o icewm
Summary(es):	Herramienta de configuración para icewm
Name:		icepref
Version:	1.1
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://members.xoom.com/SaintChoj/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}_16x16.xpm
Source3:	%{name}_32x32.xpm
Source4:	%{name}_48x48.xpm
Patch0:		%{name}-python_path.patch
URL:		http://members.xoom.com/SaintChoj/icepref.html
Requires:	gtk+
Requires:	icewm
Requires:	pygtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
IcePref is a graphical configuration utility for the amazingly fast,
and light-weight window manager, IceWM. It allows the user to easily
configure all of the options in the IceWM preferences file (allowing
control over both the behavior and apperance). This version best
matches the options found in IceWM version 1.0.0.

%description -l pl
IcePref jest graficznym narzêdziem do konfiguracji IceWM'a. Pozwala
u¿ytkownikowi na ³atwe konfigurowanie wszystkich opcji w pliku
konfiguracyjnym.

%description -l pt_BR
O IcePref é uma ferramenta de configuração para o icewm, baseada
em GTK+.

%description -l es
Herramienta de configuración para icewm

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_applnkdir}/Settings/IceWM}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_16x16.xpm
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_48x48.xpm

gzip -9nf BUGS FAQ README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/icepref
%{_applnkdir}/Settings/IceWM/*
%{_pixmapsdir}/*.xpm
%{_mandir}/man1/icepref.1*
