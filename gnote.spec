%define	api	0.9
%define	major	1
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Note-taking application
Name:		gnote
Version:	0.9.1
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv3 
URL:		http://live.gnome.org/Gnote
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(uuid)

%description
Gnote is a simple desktop note-taking application for GNOME. 
Easy to use, but with potential to help you organize the ideas and
information you deal with every day. Using a
WikiWiki-like linking system, organizing ideas is as simple as typing
a name. Branching an idea off is easy as pressing the Link button. And
links between your ideas won't break, even when renaming and
reorganizing them.

This is a clone of Tomboy, in C++.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development library for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains the development library for %{name}.

%prep
%setup -q
%apply_patches

%build
export CXXFLAGS="%optflags  -DBOOST_FILESYSTEM_VERSION=2"
%configure2_5x \
	--disable-static \
	--with-gnu-ld

%make LIBS='-lX11'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--remove-only-show-in="GNOME" \
	--remove-only-show-in="XFCE" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%check
#gw this sometimes fails on 2010.2
%if %mdvver >= 201100
make check
%endif

%files -f %{name}.lang
%doc NEWS README TODO AUTHORS
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%{_libdir}/libgnote-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libgnote.so


%changelog
* Thu Jul 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.1-1
+ Revision: 808263
- new version 0.9.1
- cleaned up spec
- split out lib and dev pkgs

  + Götz Waschk <waschk@mandriva.org>
    - add some docs
    - disable check on 2010.2 build

* Mon Oct 24 2011 Götz Waschk <waschk@mandriva.org> 0.7.6-1
+ Revision: 705818
- update to new version 0.7.6

* Sat Jul 30 2011 Götz Waschk <waschk@mandriva.org> 0.7.5-1
+ Revision: 692450
- new version
- xz tarball

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.7.4-2
+ Revision: 677720
- rebuild to add gconftool as req

* Sun May 01 2011 Götz Waschk <waschk@mandriva.org> 0.7.4-1
+ Revision: 661297
- update to new version 0.7.4

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 0.7.3-2
+ Revision: 644851
- force filesystem v2
- rebuild for new boost

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 593318
- new version
- update file list
- drop patch

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 0.7.2-3mdv2011.0
+ Revision: 572250
- rebuild for new boost

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2011.0
+ Revision: 565989
- rebuild for new boost

* Fri Mar 12 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 518354
- new version
- fix build

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.7.1-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.1
+ Revision: 500081
- rebuild for new boost

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 486229
- update to new version 0.7.1

* Fri Jan 01 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-2mdv2010.1
+ Revision: 484720
- add dbus support based on dbus-c++

* Thu Dec 31 2009 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 484505
- update to new version 0.7.0

* Sat Nov 28 2009 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2010.1
+ Revision: 470854
- new version

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 0.6.2-2mdv2010.0
+ Revision: 418879
- rebuild for new libboost

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2010.0
+ Revision: 415766
- update to new version 0.6.2
- fix build deps for backports

* Tue Aug 04 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.6.1-2mdv2010.0
+ Revision: 409061
- Updated buildrequires for libuuid.

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 405331
- new version 0.6.1

* Thu Jul 30 2009 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2010.0
+ Revision: 404487
- update to new version 0.6.0

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 396179
- update to new version 0.5.3

* Wed Jul 01 2009 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 391330
- update to new version 0.5.2
- enable checks

* Fri Jun 26 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 389361
- make it appear in KDE menu as well
- spec fixes

* Thu Jun 25 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 388907
- update to new version 0.5.1
- update build deps

* Wed Jun 17 2009 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 386561
- new version
- fix build deps
- fix source URL
- update file list

  + Eugeni Dodonov <eugeni@mandriva.com>
    - Updated to 0.4.0

  + Michael Scherer <misc@mandriva.org>
    - Add BuildRequires
    - add Summary, Group, License and description
    - import gnote


