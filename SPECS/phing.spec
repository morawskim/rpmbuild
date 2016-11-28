#
# spec file for package phing
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           phing
Version:        2.15.2
Release:        1
License:        LGPL-3.0
Summary:        A PHP project build system
Url:            https://www.phing.info
Group:          Development/Tools/Building
Source:         https://github.com/phingofficial/phing/archive/%{version}.tar.gz#/phing-%{version}.tar.gz
BuildRequires:  php5
BuildRequires:  composer
Requires:       php-dom
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Recommends:     php-xdebug >= 2.0.5
Recommends:     php-json
Recommends:     php-pdo
Recommends:     php-tokenizer
Recommends:     php-phar
Provides:       php-composer(phingofficial/phing)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PHing Is Not GNU make; it's a PHP project build system or build tool based on
Apache Ant. You can do anything with it that you could do with a traditional
build system like GNU make, and its use of simple XML build files and
extensible PHP "task" classes make it an easy-to-use and highly flexible build
framework. Features include running PHPUnit and SimpleTest unit tests
(including test result and coverage reports), file transformations (e.g.
token replacement, XSLT transformation, Smarty template transformations), file
system operations, interactive build support, SQL execution, CVS/SVN
operations, tools for creating PEAR packages, and much more.

%prep
%setup -q

%build
composer install --no-dev --no-interaction --prefer-dist

%install
%{__mkdir} -p %{buildroot}/usr/lib/phing
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} -avr . %{buildroot}/usr/lib/phing
%{__ln_s} -f /usr/lib/phing/bin/phing %{buildroot}/%{_bindir}/phing

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE CREDITS.md
%{_bindir}/phing
%dir /usr/lib/phing
/usr/lib/phing/*
/usr/lib/phing/.gitattributes
/usr/lib/phing/.gitignore
/usr/lib/phing/.gitmodules

%changelog
* Mon Nov 28 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
