# Note that this is NOT a relocatable package
# defaults for redhat
%define prefix		/usr
%define sysconfdir	/etc
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: Gnapster is a simple gnome client that implement the napster protocol.
Name: @PACKAGE@
Version: @VERSION@
Release: %rel
Copyright: GPL
Group: Applications/Communications
URL: http://www.gotlinux.org/~jasta/gnapster.html
Source: http://www.gotlinux.org/~jasta/files/%{name}-%{version}.tar.gz
Requires: gnome-libs >= 1.0.0
Requires: ORBit >= 0.4.0
Requires: gtk+ >= 1.2.0
Packager: Jasta <jasta@gotlinux.org>
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
Gnapster is a small but powerfull client for the napster (mp3 comunity)
protocol, written for Gnome by Jasta. If you would like to contribute, 
please contact Jasta <jasta@gotlinux.org>.

%prep
%setup -q

# seems as if xss support is broken on alpha :-(
%ifarch alpha
  ARCH_FLAGS="--host=alpha-redhat-linux --without-xss"
%endif

if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir}
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir}
fi

%build

if [ "$SMP" != "" ]; then
  make -j$SMP "MAKE=make -j$SMP"
else
  make
fi

%install
make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir}  install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{sysconfdir}/CORBA/servers/Gnapster.gnorba
%{prefix}/bin/gnapster
%{prefix}/share/pixmaps/*
%{prefix}/share/gnome/help/gnapster/*
%{prefix}/share/locale/*/*/*

###################################################################
%changelog
Revision 1.2  2000/02/13 13:54:35  kloczek
- made the gnome archive from the standalone sources

* Fri Jan 14 2000 Joaquim Fellmann <joaquim@hrnet.fr>
- made the gnome archive from the standalone sources
