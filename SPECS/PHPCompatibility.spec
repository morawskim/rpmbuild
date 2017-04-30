#
# spec file for package PHPCompatibility
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

%define php_compatibility_root /usr/lib/PHP_CodeSniffer/CodeSniffer/Standards/PHPCompatibility

Name:           PHPCompatibility
Version:        7.1.1
Release:        1
License:        LGPL-3
Summary:        PHP Compatibility Coding Standard for PHP_CodeSniffer
Url:            https://github.com/wimg/PHPCompatibility
Group:          Development/Libraries/PHP
Source:         https://github.com/wimg/PHPCompatibility/archive/%{version}.tar.gz
BuildRequires:  composer
Requires:       PHP_CodeSniffer
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a set of sniffs for PHP_CodeSniffer that checks for PHP version
compatibility. It will allow you to analyse your code for compatibility with
higher and lower versions of PHP.

%prep
%setup -q

%build

%install
%{__mkdir} -p %{buildroot}/%{php_compatibility_root}
%{__cp} -av . %{buildroot}/%{php_compatibility_root}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{php_compatibility_root}/*
%{php_compatibility_root}/.coveralls.yml
%{php_compatibility_root}/.gitignore
%{php_compatibility_root}/.scrutinizer.yml
%{php_compatibility_root}/.travis.yml

%changelog
* Sun Apr 30 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
