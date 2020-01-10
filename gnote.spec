%define	api	3.34
%define	major	0
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Note-taking application
Name:		gnote
Version:	3.34.1
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv3 
URL:		http://live.gnome.org/Gnote
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtkspell3-3.0)
#BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	itstool
BuildRequires:	gettext-devel
BuildRequires:	libxml2-utils


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
%autopatch -p1

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
%{_datadir}/metainfo/gnote.appdata.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man1/%{name}.1*
%{_datadir}/gnome-shell/search-providers/gnote-search-provider.ini

%files -n %{libname}
%{_libdir}/libgnote-%{api}.so.*

%files -n %{devname}
%{_libdir}/libgnote.so

