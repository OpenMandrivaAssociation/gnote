Summary:	NES emulato
Name:		gnote
Version:	0.3.0
Release:	%mkrel 1
Group:		TODO
License:	GPL 
URL:		http://live.gnome.org/Gnote
# TODO
BuildRequires: pkgconfig(gtkmm-2.4)
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
TODO

%prep
%setup -q

%build
# (misc) it seems that boost is not detected without
# this. Problem is likely in boost rpm, but I have no idea 
%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1

%configure --with-gnu-ld
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
