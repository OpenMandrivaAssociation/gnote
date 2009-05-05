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
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
%makeinstall
%find_lang %{name}
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
