#
Summary:	Graphical utility to configure IceWM
Summary(pl.UTF-8):   Graficzne narzędzie do konfiguracji IceWM-a
Summary(pt_BR.UTF-8):   Uma ferramenta de configuração para o IceWM
Summary(es.UTF-8):   Herramienta de configuración para IceWM
Name:		icepref
Version:	1.1
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://members.xoom.com/SaintChoj/%{name}-%{version}.tar.gz
# Source0-md5:	25d1af96450d34b82d4026b1b18ca61b
Source1:	%{name}.desktop
Source2:	%{name}_16x16.xpm
Source3:	%{name}_32x32.xpm
Source4:	%{name}_48x48.xpm
Patch0:		%{name}-python_path.patch
Patch1:		%{name}-mandir.patch
URL:		http://members.xoom.com/SaintChoj/icepref.html
Requires:	gtk+
Requires:	icewm
Requires:	pygtk
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
IcePref is a graphical configuration utility for the amazingly fast,
and light-weight window manager, IceWM. It allows the user to easily
configure all of the options in the IceWM preferences file (allowing
control over both the behavior and apperance). This version best
matches the options found in IceWM version 1.0.0.

%description -l pl.UTF-8
IcePref jest graficznym narzędziem do konfiguracji IceWM-a. Pozwala
użytkownikowi na łatwe konfigurowanie wszystkich opcji w pliku
konfiguracyjnym.

%description -l pt_BR.UTF-8
O IcePref é uma ferramenta de configuração para o IceWM, baseada em
GTK+.

%description -l es.UTF-8
Herramienta de configuración para IceWM.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_16x16.xpm
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_48x48.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS FAQ README TODO
%attr(755,root,root) %{_bindir}/icepref
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
%{_mandir}/man1/icepref.1*
