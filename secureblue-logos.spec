%global debug_package %{nil}
%global vendor bluefin

Name:           secureblue-logos
Version:        0.1.0
Release:        3%{?dist}
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

mv logos/* %{buildroot}%{_datadir}/pixmaps
mv icons/* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv plymouth/* %{buildroot}%{_datadir}/plymouth/themes/spinner

%files
%attr(0755,root,root) %{_datadir}/pixmaps/fedora*
%attr(0755,root,root) %{_datadir}/pixmaps/system-*
%attr(0755,root,root) %{_datadir}/plymouth/themes/spinner/watermark.png
%attr(0755,root,root) %{_datadir}/icons/hicolor/scalable/apps/start-here*