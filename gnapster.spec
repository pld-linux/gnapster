Summary:	Gnapster is a simple GNOME client that implement the napster protocol
Summary(pl.UTF-8):	Gnapster jest prostą implementacją protokoły napster dla GNOME
Name:		gnapster
Version:	1.5.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gnapster/%{name}-%{version}.tar.gz
# Source0-md5:	f73e173c5dd78bb910dd8a5235c842a6
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://sourceforge.net/projects/gnapster/
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Gnapster is a small but powerfull client for the napster (MP3
comunity) protocol, written for GNOME by Jasta. If you would like to
contribute, please contact Jasta <jasta@gotlinux.org>.

%description -l pl.UTF-8
Gnapster jest małym, lecz potężnym klientem protokołu napstera (dla
społeczności wymieniającej się plikami MP3), przepisanym dla GNOME
przez Jasta. Jeśli chcecie pomóc w rozwoju tej aplikacji, można się z
nim skontaktować pisząc na adres: jasta@gotlinux.org.

%prep
%setup -q
%patch0 -p1

rm -f po/essai.po

%build
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnapster
%{_pixmapsdir}/*
%{_datadir}/gnapster
%{_applnkdir}/Network/Misc/gnapster.desktop
