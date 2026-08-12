Name:           anki-bin
Version:        26.08.1
Release:        1%{?dist}
Summary:        Intelligent spaced-repetition flashcard program (upstream binary package)

License:        AGPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/ankitects/anki
Source0:        %{url}/releases/download/%{version}/anki-%{version}-linux-%{_arch}.tar.zst

ExclusiveArch:  x86_64 aarch64
AutoReqProv:    no
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2
BuildRequires:  zstd
Requires:       dbus-libs
Requires:       fontconfig
Requires:       freetype
Requires:       glib2
Requires:       lame
Requires:       libglvnd-glx
Requires:       libXcomposite
Requires:       libXcursor
Requires:       libXi
Requires:       libXrandr
Requires:       libXrender
Requires:       libXtst
Requires:       libxcb
Requires:       libxkbcommon
Requires:       libxkbcommon-x11
Requires:       mpv
Requires:       nss
Requires:       xcb-util-cursor
Requires:       xcb-util-image
Requires:       xcb-util-keysyms
Requires:       xcb-util-renderutil
Requires:       xcb-util-wm
Provides:       anki = %{version}-%{release}
Conflicts:      anki

# Keep the prebuilt, upstream-tested binaries intact.
%global debug_package %{nil}
%global __strip /bin/true
%undefine __brp_add_determinism
%global __brp_mangle_shebangs %{nil}
# The bundled Tcl libraries contain upstream's inert build-time RPATH.
%global __brp_check_rpaths %{nil}

%description
Anki is a program that makes remembering things easier by scheduling
flashcard reviews using spaced repetition. This package repackages the
architecture-specific Linux bundle published with the corresponding
upstream stable release.


%prep
%setup -q -n anki-linux


%build
# The application is built and published by upstream.


%install
mkdir -p %{buildroot}%{_datadir}/anki
cp -a app app_packages python anki %{buildroot}%{_datadir}/anki/

install -Dpm 0755 anki %{buildroot}%{_datadir}/anki/anki
install -d %{buildroot}%{_bindir}
ln -s ../share/anki/anki %{buildroot}%{_bindir}/anki

install -Dpm 0644 anki.desktop %{buildroot}%{_datadir}/applications/anki.desktop
install -Dpm 0644 anki.png %{buildroot}%{_datadir}/pixmaps/anki.png
install -Dpm 0644 anki.xpm %{buildroot}%{_datadir}/pixmaps/anki.xpm
install -Dpm 0644 anki.xml %{buildroot}%{_datadir}/mime/packages/anki.xml
install -Dpm 0644 anki.1 %{buildroot}%{_mandir}/man1/anki.1
install -Dpm 0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/anki.desktop
xmllint --noout %{buildroot}%{_datadir}/mime/packages/anki.xml


%files
%license %{_licensedir}/%{name}/LICENSE
%doc README.md
%{_bindir}/anki
%{_datadir}/anki/
%{_datadir}/applications/anki.desktop
%{_datadir}/mime/packages/anki.xml
%{_datadir}/pixmaps/anki.png
%{_datadir}/pixmaps/anki.xpm
%{_mandir}/man1/anki.1*


%changelog
* Wed Aug 12 2026 Ponesicek <ponesicek@users.noreply.github.com> - 26.08.1-1
- Package upstream Anki 26.08.1 binary release
* Tue Aug 04 2026 Ponesicek <ponesicek@users.noreply.github.com> - 26.08-1
- Package upstream Anki 26.08 binary release
