#
# TODO:
# - icon
#
Summary:	Graphical utility to configure IceWM
Summary(pl):	Graficzne narzêdzie do konfiguracji IceWM'a
Name:		icepref
Version:	1.1
BuildArch:	noarch
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://members.xoom.com/SaintChoj/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://members.xoom.com/SaintChoj/icepref.html
Requires:	pygtk python gtk+ icewm
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

%prep

%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix}/bin,%{_mandir}/man1,%{_applnkdir}/Settings/IceWM}
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/%{name}.desktop

gzip -9nf BUGS FAQ README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/icepref
%{_applnkdir}/Settings/IceWM/*
%{_mandir}/man1/icepref.1*
