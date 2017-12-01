#
# spec file for package composer
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


Name:           composer
Version:        1.5.2
Release:        1
License:        MIT
Summary:        Dependency Management for PHP
Url:            http://getcomposer.org/
Group:          Development/Libraries/PHP
Source0:        https://getcomposer.org/download/%{version}/composer.phar
Source1:        https://github.com/composer/composer/raw/%{version}/README.md
Source2:        https://github.com/composer/composer/raw/%{version}/LICENSE
Requires:       php-json
Requires:       php-openssl
Requires:       php-phar
Provides:       php5-composer = %{version}
Obsoletes:      php5-composer < %{version}
Provides:       php7-composer = %{version}
Obsoletes:      php7-composer < %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Composer is a dependency manager tracking local dependencies of your projects
and libraries.

%prep
%setup -q -c -T

%build

%install
# Install compiled phar file
install -d -m 0750 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/composer

# Install documents
install -d -m 0750 %{buildroot}%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}
install -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/composer
%{_docdir}/%{name}

%changelog
* Fri Dec 01 2017 Marcin Morawski <marcin@morawskim.pl>
-  Update to 1.5.2
-  Remove composer-bash-completion

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.2.0-4
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Jul 30 2016 Marcin Morawski <marcin@morawskim.pl>
-  Add bash auto-complete script

* Fri Jul 29 2016 Marcin Morawski <marcin@morawskim.pl>
-  Init release
