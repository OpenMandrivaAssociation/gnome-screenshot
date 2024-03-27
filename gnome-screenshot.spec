%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-screenshot
Version:	41.0
Release:	7
Summary:	GNOME Screenshot utility
License:	GPLv2+
Group:		File tools
Url:		https://live.gnome.org/GnomeUtils/Baobab
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# Upstream fix for compilation with meson 0.60+
Patch0:   https://gitlab.gnome.org/GNOME/gnome-screenshot/-/commit/b60dad3c2536c17bd201f74ad8e40eb74385ed9f.patch
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:  cmake
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	meson
Conflicts:	gnome-utils < 1:3.3.1

%description
Gnome screenshot utility.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

#handle docs with files section
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
#{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/org.gnome.Screenshot.desktop
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/metainfo/org.gnome.Screenshot.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Screenshot.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Screenshot-symbolic.svg

