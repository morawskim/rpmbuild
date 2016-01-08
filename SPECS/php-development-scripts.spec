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

%global commit0 2c63f414b0f8498c99814cb5069a4082c861523a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           php-development-scripts
Version: 0.1.0
Release: 2
License: MIT
Summary: Shell scripts to download php apps and IDE
Url: https://github.com/morawskim/opensuse-configuration-scripts
Source: https://github.com/morawskim/opensuse-configuration-scripts/archive/%{shortcommit0}.tar.gz
BuildArch: noarch
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

%post
exit 0

%postun
exit 0

%files
%defattr(0770,root,root)
%{_sbindir}/composer.sh
%{_sbindir}/phing.sh
%{_sbindir}/phpdoc.sh
%{_sbindir}/phpunit.sh
%{_sbindir}/yuml-php.sh
%{_sbindir}/phpstorm.sh

