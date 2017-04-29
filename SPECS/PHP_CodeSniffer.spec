#
# spec file for package PHP_CodeSniffer
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

%define code_sniffer_root /usr/lib/PHP_CodeSniffer

Name:           PHP_CodeSniffer
Version:        2.7.1
Release:        1
License:        BSD-3
Summary:        PHP_CodeSniffer tokenizes PHP, JavaScript and CSS files and detects violations of a defined set of coding standards
Url:            https://github.com/squizlabs/PHP_CodeSniffer
Group:          Development/Libraries/PHP
Source:         https://github.com/squizlabs/PHP_CodeSniffer/archive/%{version}.tar.gz
BuildRequires:  composer
Requires:       php5 >= 5.1.2
Requires:       php5-tokenizer
Requires:       php5-xmlwriter
Requires:       php5-simplexml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PHP_CodeSniffer is a set of two PHP scripts; the main phpcs script that
tokenizes PHP, JavaScript and CSS files to detect violations of a defined
coding standard, and a second phpcbf script to automatically correct coding
standard violations. PHP_CodeSniffer is an essential development tool that
ensures your code remains clean and consistent.

%prep
%setup -q

%build
composer install --no-dev --prefer-dist --no-interaction

%install
%{__mkdir} -p %{buildroot}/%{code_sniffer_root}
%{__mkdir} -p %{buildroot}/%{_bindir}

%{__cp} -av . %{buildroot}/%{code_sniffer_root}

%{__ln_s} -f %{code_sniffer_root}/scripts/phpcbf %{buildroot}%{_bindir}/phpcbf
%{__ln_s} -f %{code_sniffer_root}/scripts/phpcs %{buildroot}%{_bindir}/phpcs

%post

%postun

%files
%defattr(-,root,root)
%doc README.md licence.txt
%{_bindir}/phpcs
%{_bindir}/phpcbf
%{code_sniffer_root}/*
%{code_sniffer_root}/.gitignore
%{code_sniffer_root}/.gitattributes

%changelog
* Sat Apr 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
