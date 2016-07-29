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

%global commit0 b49a006748a460f8dae6500ec80ed021501ce969
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global composer_bin composer.phar

Name:           composer
Version:        1.2.0
Release:        1
License:        MIT
Summary:        Dependency Management for PHP
Url:            http://getcomposer.org/
Group:          Development/Libraries/Other
Source0:        https://github.com/composer/composer/archive/%{shortcommit0}.tar.gz
Source1:        https://getcomposer.org/download/%{version}/composer.phar
Requires:       php5-json
Requires:       php5-openssl
Requires:       php5-phar
Provides:       php5-composer = %{version}
Obsoletes:      php5-composer < %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Composer is a dependency manager tracking local dependencies of your projects
and libraries.

%prep
%setup -qn %{name}-%{commit0}
cp %{S:1} %{composer_bin}

%build

%install
%__install -D -p -m 0755 composer.phar %{buildroot}%{_bindir}/composer

%post

%postun

%files
%defattr(-,root,root)
%attr(0755, root, root) %{_bindir}/composer
%doc CHANGELOG.md README.md LICENSE doc

%changelog
* Fri Jul 29 2016 Marcin Morawski <marcin@morawskim.pl>
-  Init release
