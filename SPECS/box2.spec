#
# spec file for package box2
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

%define box2_root /usr/lib/box2

Name:           box2
Version:        2.7.4
Release:        3
License:        MIT
Summary:        An application for building and managing Phars
Url:            https://box-project.github.io/box2/
Group:          Development/Libraries/PHP
Source:         https://github.com/box-project/box2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  composer
Requires:       php5 >= 5.3.3
Requires:       php5-phar
Suggests:       php5-openssl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Box application simplifies the Phar building process. Out of the box (no
pun intended), the application can do many great things:

* Add, replace, and remove files and stubs in existing Phars.
* Extract a whole Phar, or cherry pick which files you want.
* Retrieve information about the Phar extension, or a Phar file.
* List the contents of a Phar.
* Verify the signature of an existing Phar.
* Generate RSA (PKCS#1 encoded) private keys for OpenSSL signing.
* Extract public keys from existing RSA private keys.
* Use Git tags and short commit hashes for versioning.

Since the application is based on the Box library, you get its benefits as
well:

* On the fly search and replace of placeholders.
* Compact file contents based on file type.
* Generate custom stubs.

%prep
%setup -q

%build
composer install --no-dev --prefer-dist --no-interaction

%install
%{__mkdir} -p %{buildroot}/%{box2_root}
%{__mkdir} -p %{buildroot}/%{_bindir}

%{__cp} -av . %{buildroot}/%{box2_root}

%{__ln_s} -f %{box2_root}/bin/box %{buildroot}%{_bindir}/box

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/box
%{box2_root}/*
%{box2_root}/.gitignore
%{box2_root}/.travis.yml

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.7.4-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Apr 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
