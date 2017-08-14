#
# spec file for package php-development-scripts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global commit0 c03aed50fd8c1c7458694088307daec63babd95b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           php-development-scripts
Version:        20160508
Release:        3
License:        MIT
Summary:        Shell scripts to download php apps and IDE
Url:            https://github.com/morawskim/opensuse-configuration-scripts
Source:         https://github.com/morawskim/opensuse-configuration-scripts/archive/%{shortcommit0}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -qn opensuse-configuration-scripts-%{commit0}

%build
exit 0

%install
mkdir -p %{buildroot}/usr/sbin
cp development/composer.sh %{buildroot}/usr/sbin
cp development/phing.sh %{buildroot}/usr/sbin
cp development/phpdoc.sh %{buildroot}/usr/sbin
cp development/phpunit.sh %{buildroot}/usr/sbin
cp development/yuml-php.sh %{buildroot}/usr/sbin
cp jetbrains/phpstorm.sh %{buildroot}/usr/sbin
%{__install} -D -p -m 755 development/build-php.sh %{buildroot}%{_bindir}/build-php

%post
exit 0

%postun
exit 0

%files
%defattr(0750,root,root)
%{_sbindir}/composer.sh
%{_sbindir}/phing.sh
%{_sbindir}/phpdoc.sh
%{_sbindir}/phpunit.sh
%{_sbindir}/yuml-php.sh
%{_sbindir}/phpstorm.sh
%attr(0755, root, root) %{_bindir}/build-php

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20160508-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun May 08 2016 Marcin Morawski <marcin@morawskim.pl>
-  Update to commit c03aed50fd8c1c7458694088307daec63babd95b

* Sat May 07 2016 Marcin Morawski <marcin@morawskim.plW
-  Add build-php script
-  Change version numbering policy's
-  Reformat spec file
