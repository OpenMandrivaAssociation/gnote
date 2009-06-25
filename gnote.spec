Summary:	Note-taking application
Name:		gnote
Version:	0.5.1
Release:	%mkrel 1
Group:		Graphical desktop/GNOME
License:	GPLv3 
URL:		http://live.gnome.org/Gnote
BuildRequires: boost-devel
BuildRequires: libext2fs-devel
BuildRequires: libxslt-devel
BuildRequires: gtkspell-devel
BuildRequires: libpanelappletmm-devel
BuildRequires: dbus-glib-devel
BuildRequires: gnome-doc-utils
BuildRequires: intltool
Source0:       http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%build
# (misc) it seems that boost is not detected without
# this. Problem is likely in boost rpm, but I have no idea 
%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1

%configure2_5x --with-gnu-ld
%make

%install
%makeinstall_std
%find_lang %{name}

rm -f %{buildroot}/%_iconsdir/hicolor/icon-theme.cache

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%_mandir/man1/%{name}.1.lzma
%_bindir/%{name}
%_libdir/%{name}
%_datadir/gnome/help/%{name}/
%_datadir/%{name}/
%_datadir/omf/%{name}/
%_sysconfdir/gconf/schemas/%{name}.schemas
%{_datadir}/applications/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_libexecdir/gnote-applet
%_libdir/bonobo/servers/GNOME_GnoteApplet.server
