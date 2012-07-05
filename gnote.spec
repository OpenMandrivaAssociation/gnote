Summary:	Note-taking application
Name:		gnote
Version:	0.7.6
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv3 
URL:		http://live.gnome.org/Gnote
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	dbus-c++-devel

%description
Gnote is a simple desktop note-taking application for GNOME. 
Easy to use, but with potential to help you organize the ideas and
information you deal with every day. Using a
WikiWiki-like linking system, organizing ideas is as simple as typing
a name. Branching an idea off is easy as pressing the Link button. And
links between your ideas won't break, even when renaming and
reorganizing them.

This is a clone of Tomboy, in C++.

%prep
%setup -q
%apply_patches

%build
export CXXFLAGS="%optflags  -DBOOST_FILESYSTEM_VERSION=2"
%configure2_5x \
	--with-gnu-ld \
	--disable-schemas-install
%make

%install
%makeinstall_std
%find_lang %{name}

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
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/gnome/help/%{name}/
%{_datadir}/%{name}/
%{_datadir}/omf/%{name}/
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_libexecdir}/gnote-applet
%{_libdir}/bonobo/servers/GNOME_GnoteApplet.server

