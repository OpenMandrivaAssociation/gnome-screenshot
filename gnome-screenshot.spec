%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-screenshot
Version:	3.4.1
Release:	%mkrel 1
Summary:	GNOME Screenshot utility
License:	GPLv2+
Group:		File tools
Url:		http://live.gnome.org/GnomeUtils/Baobab
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		gnome-screenshot-3.3.1-fix-desktop-file.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libcanberra-gtk3)
Conflicts:	gnome-utils < 1:3.3.1

%description
Gnome screenshot utility.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-rpath \
	--disable-schemas-compile

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#handle docs with files section
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*


