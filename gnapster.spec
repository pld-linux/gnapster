Summary:	Gnapster is a simple gnome client that implement the napster protocol
Summary(pl):	Gnapster jest prost� implementacj� protoko�y napster dla GNOME
Name:		gnapster
Version:	1.4.0
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://jasta.gotlinux.org/files/%{name}-%{version}.tar.gz
URL:		http://jasta.gotlinux.org/gnapster.html
BuildRequires:	db3-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Gnapster is a small but powerfull client for the napster (mp3
comunity) protocol, written for Gnome by Jasta. If you would like to
contribute, please contact Jasta <jasta@gotlinux.org>.

%description -l pl
Gnapster jest ma�ym, lecz pot�nym klientem protoko�u napstera (dla
spo�eczno�ci wymieniaj�cej si� plikami mp3), przepisanym dla Gnome
przez Jasta. Je�li chcecie pom�c w rozwoju tej aplikacji, mo�na si� z
nim skontaktowac pisz�c na adres: jasta@gotlinux.org.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
%ifarch alpha
	--without-xss
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install gnapster.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnapster
%{_datadir}/pixmaps/*
%{_datadir}/gnapster
%{_applnkdir}/Network/Misc
