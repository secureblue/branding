%global debug_package %{nil}
%global vendor secureblue

Name:           secureblue-logos
Version:        0.3.3
Release:        1%{?dist}
Summary:        secureblue logos

License:        Apache 2.0
Provides: fedora-logos
Provides: centos-logos
Provides: system-logos
Obsoletes: fedora-logos
Obsoletes: centos-logos
Obsoletes: system-logos
URL:            https://github.com/secureblue/branding
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
Logos for secureblue

%prep
{{{ git_dir_setup_macro }}}

%install

mkdir -p -m0755 %{buildroot}%{_datadir}/pixmaps
mkdir -p -m0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p -m0755 %{buildroot}%{_datadir}/plymouth/themes/spinner
mkdir -p -m0755 %{buildroot}%{_datadir}/anaconda/pixmaps/

mv anaconda/* %{buildroot}%{_datadir}/anaconda/pixmaps/
mv logos/* %{buildroot}%{_datadir}/pixmaps
mv icons/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv plymouth/* %{buildroot}%{_datadir}/plymouth/themes/spinner
for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256; do
  mkdir -p -m0755 %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
  mv icons/hicolor/${size}/apps/fedora-logo-icon.png %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
done

%files
%attr(0755,root,root) %{_datadir}/anaconda/pixmaps/*
%attr(0755,root,root) %{_datadir}/pixmaps/fedora*
%attr(0755,root,root) %{_datadir}/pixmaps/system-*
%attr(0755,root,root) %{_datadir}/plymouth/themes/spinner/watermark.png
%attr(0755,root,root) %{_datadir}/icons/hicolor/scalable/apps/start-here*
%attr(0755,root,root) %{_datadir}/icons/hicolor/*/apps/fedora-logo-icon.png
