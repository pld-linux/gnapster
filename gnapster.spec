Summary:	Gnapster is a simple gnome client that implement the napster protocol
Name:		gnapster
Version:	1.3.8
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.gotlinux.org/~jasta/files/%{name}-%{version}.tar.gz
URL:		http://www.gotlinux.org/~jasta/gnapster.html
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Gnapster is a small but powerfull client for the napster (mp3 comunity)
protocol, written for Gnome by Jasta. If you would like to contribute,
please contact Jasta <jasta@gotlinux.org>.

%description -l pl
Gnapster jest ma³ym, lecz potê¿nym klientem protoko³u napstera (dla
spo³eczno¶ci wymieniaj±cej siê plikami mp3), przepisanym dla Gnome przez
Jasta. Je¶li chcecie pomóc w rozwoju tej aplikacji, mo¿na siê z nim
skontaktowac pisz±c na adres: jasta@gotlinux.org.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
%ifarch alpha
	--without-xss
%endif

make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Applications

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnapster
%{_datadir}/pixmaps/*
%{_applnkdir}/Applications/*
