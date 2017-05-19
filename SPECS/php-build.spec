#
# spec file for package php-build
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/morawskim/rpmbuild/issues
#

%define commit 2080889de66008c0103c687dadd6afc2a705d14a

Name:           php-build
Version:        20161211
Release:        1
License:        MIT
Summary:        Builds PHP so that multiple versions can be used side by side
Url:            https://php-build.github.io/
Group:          Development/Tools/Building
Source:         https://github.com/php-build/php-build/archive/%{commit}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
php-build is a utility for building versions of PHP to use them side by side
with each other. The overall structure is loosly borrowed from Sam Stephenson's
ruby-build.

%prep
%setup -qn %{name}-%{commit}

%build

%install
PREFIX=%{buildroot}/%{_prefix} ./install.sh

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE
%{_bindir}/php-build
%{_bindir}/phpenv-install
%{_bindir}/phpenv-uninstall
%{_bindir}/phpenv-update
%{_bindir}/rbenv-install
%{_bindir}/rbenv-uninstall
%{_bindir}/rbenv-update
%dir %{_datarootdir}/%{name}
%dir %{_datarootdir}/%{name}/after-install.d
%dir %{_datarootdir}/%{name}/before-install.d
%dir %{_datarootdir}/%{name}/definitions
%dir %{_datarootdir}/%{name}/extension
%dir %{_datarootdir}/%{name}/patches
%dir %{_datarootdir}/%{name}/plugins.d
%{_datarootdir}/%{name}/after-install.d/.empty
%{_datarootdir}/%{name}/before-install.d/.empty
%{_datarootdir}/%{name}/default_configure_options
%{_datarootdir}/%{name}/definitions/5.2.17
%{_datarootdir}/%{name}/definitions/5.3.10
%{_datarootdir}/%{name}/definitions/5.3.11
%{_datarootdir}/%{name}/definitions/5.3.12
%{_datarootdir}/%{name}/definitions/5.3.13
%{_datarootdir}/%{name}/definitions/5.3.14
%{_datarootdir}/%{name}/definitions/5.3.15
%{_datarootdir}/%{name}/definitions/5.3.16
%{_datarootdir}/%{name}/definitions/5.3.17
%{_datarootdir}/%{name}/definitions/5.3.18
%{_datarootdir}/%{name}/definitions/5.3.19
%{_datarootdir}/%{name}/definitions/5.3.2
%{_datarootdir}/%{name}/definitions/5.3.20
%{_datarootdir}/%{name}/definitions/5.3.21
%{_datarootdir}/%{name}/definitions/5.3.22
%{_datarootdir}/%{name}/definitions/5.3.23
%{_datarootdir}/%{name}/definitions/5.3.24
%{_datarootdir}/%{name}/definitions/5.3.25
%{_datarootdir}/%{name}/definitions/5.3.26
%{_datarootdir}/%{name}/definitions/5.3.27
%{_datarootdir}/%{name}/definitions/5.3.28
%{_datarootdir}/%{name}/definitions/5.3.29
%{_datarootdir}/%{name}/definitions/5.3.3
%{_datarootdir}/%{name}/definitions/5.3.6
%{_datarootdir}/%{name}/definitions/5.3.8
%{_datarootdir}/%{name}/definitions/5.3.9
%{_datarootdir}/%{name}/definitions/5.4.0
%{_datarootdir}/%{name}/definitions/5.4.1
%{_datarootdir}/%{name}/definitions/5.4.10
%{_datarootdir}/%{name}/definitions/5.4.11
%{_datarootdir}/%{name}/definitions/5.4.12
%{_datarootdir}/%{name}/definitions/5.4.13
%{_datarootdir}/%{name}/definitions/5.4.14
%{_datarootdir}/%{name}/definitions/5.4.15
%{_datarootdir}/%{name}/definitions/5.4.16
%{_datarootdir}/%{name}/definitions/5.4.17
%{_datarootdir}/%{name}/definitions/5.4.18
%{_datarootdir}/%{name}/definitions/5.4.19
%{_datarootdir}/%{name}/definitions/5.4.2
%{_datarootdir}/%{name}/definitions/5.4.20
%{_datarootdir}/%{name}/definitions/5.4.21
%{_datarootdir}/%{name}/definitions/5.4.22
%{_datarootdir}/%{name}/definitions/5.4.23
%{_datarootdir}/%{name}/definitions/5.4.24
%{_datarootdir}/%{name}/definitions/5.4.25
%{_datarootdir}/%{name}/definitions/5.4.26
%{_datarootdir}/%{name}/definitions/5.4.27
%{_datarootdir}/%{name}/definitions/5.4.28
%{_datarootdir}/%{name}/definitions/5.4.29
%{_datarootdir}/%{name}/definitions/5.4.3
%{_datarootdir}/%{name}/definitions/5.4.30
%{_datarootdir}/%{name}/definitions/5.4.31
%{_datarootdir}/%{name}/definitions/5.4.32
%{_datarootdir}/%{name}/definitions/5.4.33
%{_datarootdir}/%{name}/definitions/5.4.34
%{_datarootdir}/%{name}/definitions/5.4.35
%{_datarootdir}/%{name}/definitions/5.4.36
%{_datarootdir}/%{name}/definitions/5.4.37
%{_datarootdir}/%{name}/definitions/5.4.38
%{_datarootdir}/%{name}/definitions/5.4.39
%{_datarootdir}/%{name}/definitions/5.4.4
%{_datarootdir}/%{name}/definitions/5.4.40
%{_datarootdir}/%{name}/definitions/5.4.41
%{_datarootdir}/%{name}/definitions/5.4.42
%{_datarootdir}/%{name}/definitions/5.4.43
%{_datarootdir}/%{name}/definitions/5.4.44
%{_datarootdir}/%{name}/definitions/5.4.45
%{_datarootdir}/%{name}/definitions/5.4.5
%{_datarootdir}/%{name}/definitions/5.4.6
%{_datarootdir}/%{name}/definitions/5.4.7
%{_datarootdir}/%{name}/definitions/5.4.8
%{_datarootdir}/%{name}/definitions/5.4.9
%{_datarootdir}/%{name}/definitions/5.4snapshot
%{_datarootdir}/%{name}/definitions/5.5.0
%{_datarootdir}/%{name}/definitions/5.5.1
%{_datarootdir}/%{name}/definitions/5.5.10
%{_datarootdir}/%{name}/definitions/5.5.11
%{_datarootdir}/%{name}/definitions/5.5.12
%{_datarootdir}/%{name}/definitions/5.5.13
%{_datarootdir}/%{name}/definitions/5.5.14
%{_datarootdir}/%{name}/definitions/5.5.15
%{_datarootdir}/%{name}/definitions/5.5.16
%{_datarootdir}/%{name}/definitions/5.5.17
%{_datarootdir}/%{name}/definitions/5.5.18
%{_datarootdir}/%{name}/definitions/5.5.19
%{_datarootdir}/%{name}/definitions/5.5.2
%{_datarootdir}/%{name}/definitions/5.5.20
%{_datarootdir}/%{name}/definitions/5.5.21
%{_datarootdir}/%{name}/definitions/5.5.22
%{_datarootdir}/%{name}/definitions/5.5.23
%{_datarootdir}/%{name}/definitions/5.5.24
%{_datarootdir}/%{name}/definitions/5.5.25
%{_datarootdir}/%{name}/definitions/5.5.26
%{_datarootdir}/%{name}/definitions/5.5.27
%{_datarootdir}/%{name}/definitions/5.5.28
%{_datarootdir}/%{name}/definitions/5.5.29
%{_datarootdir}/%{name}/definitions/5.5.3
%{_datarootdir}/%{name}/definitions/5.5.30
%{_datarootdir}/%{name}/definitions/5.5.31
%{_datarootdir}/%{name}/definitions/5.5.32
%{_datarootdir}/%{name}/definitions/5.5.33
%{_datarootdir}/%{name}/definitions/5.5.34
%{_datarootdir}/%{name}/definitions/5.5.35
%{_datarootdir}/%{name}/definitions/5.5.36
%{_datarootdir}/%{name}/definitions/5.5.37
%{_datarootdir}/%{name}/definitions/5.5.38
%{_datarootdir}/%{name}/definitions/5.5.4
%{_datarootdir}/%{name}/definitions/5.5.5
%{_datarootdir}/%{name}/definitions/5.5.6
%{_datarootdir}/%{name}/definitions/5.5.7
%{_datarootdir}/%{name}/definitions/5.5.8
%{_datarootdir}/%{name}/definitions/5.5.9
%{_datarootdir}/%{name}/definitions/5.5snapshot
%{_datarootdir}/%{name}/definitions/5.6.0
%{_datarootdir}/%{name}/definitions/5.6.1
%{_datarootdir}/%{name}/definitions/5.6.10
%{_datarootdir}/%{name}/definitions/5.6.11
%{_datarootdir}/%{name}/definitions/5.6.12
%{_datarootdir}/%{name}/definitions/5.6.13
%{_datarootdir}/%{name}/definitions/5.6.14
%{_datarootdir}/%{name}/definitions/5.6.15
%{_datarootdir}/%{name}/definitions/5.6.16
%{_datarootdir}/%{name}/definitions/5.6.17
%{_datarootdir}/%{name}/definitions/5.6.18
%{_datarootdir}/%{name}/definitions/5.6.19
%{_datarootdir}/%{name}/definitions/5.6.2
%{_datarootdir}/%{name}/definitions/5.6.20
%{_datarootdir}/%{name}/definitions/5.6.21
%{_datarootdir}/%{name}/definitions/5.6.22
%{_datarootdir}/%{name}/definitions/5.6.23
%{_datarootdir}/%{name}/definitions/5.6.24
%{_datarootdir}/%{name}/definitions/5.6.25
%{_datarootdir}/%{name}/definitions/5.6.26
%{_datarootdir}/%{name}/definitions/5.6.27
%{_datarootdir}/%{name}/definitions/5.6.28
%{_datarootdir}/%{name}/definitions/5.6.29
%{_datarootdir}/%{name}/definitions/5.6.3
%{_datarootdir}/%{name}/definitions/5.6.4
%{_datarootdir}/%{name}/definitions/5.6.5
%{_datarootdir}/%{name}/definitions/5.6.6
%{_datarootdir}/%{name}/definitions/5.6.7
%{_datarootdir}/%{name}/definitions/5.6.8
%{_datarootdir}/%{name}/definitions/5.6.9
%{_datarootdir}/%{name}/definitions/5.6snapshot
%{_datarootdir}/%{name}/definitions/7.0.0
%{_datarootdir}/%{name}/definitions/7.0.1
%{_datarootdir}/%{name}/definitions/7.0.10
%{_datarootdir}/%{name}/definitions/7.0.11
%{_datarootdir}/%{name}/definitions/7.0.12
%{_datarootdir}/%{name}/definitions/7.0.13
%{_datarootdir}/%{name}/definitions/7.0.14
%{_datarootdir}/%{name}/definitions/7.0.2
%{_datarootdir}/%{name}/definitions/7.0.3
%{_datarootdir}/%{name}/definitions/7.0.4
%{_datarootdir}/%{name}/definitions/7.0.5
%{_datarootdir}/%{name}/definitions/7.0.6
%{_datarootdir}/%{name}/definitions/7.0.7
%{_datarootdir}/%{name}/definitions/7.0.8
%{_datarootdir}/%{name}/definitions/7.0.9
%{_datarootdir}/%{name}/definitions/7.0snapshot
%{_datarootdir}/%{name}/definitions/7.1.0
%{_datarootdir}/%{name}/definitions/7.1snapshot
%{_datarootdir}/%{name}/definitions/master
%{_datarootdir}/%{name}/extension/definition
%{_datarootdir}/%{name}/extension/extension.sh
%{_datarootdir}/%{name}/patches/gmp.c.patch
%{_datarootdir}/%{name}/patches/php-5.4.6-libxml2-2.9.patch
%{_datarootdir}/%{name}/patches/xp_ssl.c.patch
%{_datarootdir}/%{name}/patches/zip_direct.c.patch
%{_datarootdir}/%{name}/plugins.d/apc.sh
%{_datarootdir}/%{name}/plugins.d/composer.sh
%{_datarootdir}/%{name}/plugins.d/github.sh
%{_datarootdir}/%{name}/plugins.d/uprofiler.sh
%{_datarootdir}/%{name}/plugins.d/xdebug.sh
%{_datarootdir}/%{name}/plugins.d/xhprof.sh
%{_datarootdir}/%{name}/plugins.d/zendopcache.sh
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.5%{?ext_man}


%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
-  add dir macro

* Fri Apr 28 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
