%global debug_package %{nil}
%global vendor bluefin

Name:           secureblue-logos
Version:        0.1.0
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

mv logos/* %{buildroot}%{_datadir}/pixmaps
