Summary:	Gnapster is a simple gnome client that implement the napster protocol
Summary(pl):	Gnapster jest prost± implementacj± protoko³y napster dla GNOME
Name:		gnapster
Version:	1.5.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://jasta.gotlinux.org/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://jasta.gotlinux.org/gnapster.html
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Gnapster is a small but powerfull client for the napster (mp3
comunity) protocol, written for Gnome by Jasta. If you would like to
contribute, please contact Jasta <jasta@gotlinux.org>.

%description -l pl
Gnapster jest ma³ym, lecz potê¿nym klientem protoko³u napstera (dla
spo³eczno¶ci wymieniaj±cej siê plikami mp3), przepisanym dla Gnome
przez Jasta. Je¶li chcecie pomóc w rozwoju tej aplikacji, mo¿na siê z
nim skontaktowac pisz±c na adres: jasta@gotlinux.org.

%prep
%setup -q
%patch -p1

rm -f po/essai.po

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
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
%{_pixmapsdir}/*
%{_datadir}/gnapster
%{_applnkdir}/Network/Misc/gnapster.desktop
