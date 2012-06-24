#
Summary:	Graphical utility to configure IceWM
Summary(pl):	Graficzne narz�dzie do konfiguracji IceWM-a
Summary(pt_BR):	Uma ferramenta de configura��o para o IceWM
Summary(es):	Herramienta de configuraci�n para IceWM
Name:		icepref
Version:	1.1
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
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
Requires:	python-modules
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
IcePref jest graficznym narz�dziem do konfiguracji IceWM-a. Pozwala
u�ytkownikowi na �atwe konfigurowanie wszystkich opcji w pliku
konfiguracyjnym.

%description -l pt_BR
O IcePref � uma ferramenta de configura��o para o IceWM, baseada em
GTK+.

%description -l es
Herramienta de configuraci�n para IceWM.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS FAQ README TODO
%attr(755,root,root) %{_bindir}/icepref
%{_applnkdir}/Settings/IceWM/*
%{_pixmapsdir}/*.xpm
%{_mandir}/man1/icepref.1*
