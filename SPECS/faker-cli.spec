#
# spec file for package faker-cli
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

%define faker_root /usr/lib/faker

Name:           faker-cli
Version:        1.4
Release:        1
License:        MIT
Summary:        Command Line Tool for the Faker PHP library
Url:            https://github.com/bit3/faker-cli
Group:          Productivity/Other
Source:         https://github.com/bit3/faker-cli/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  composer
Requires:       php5
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Faker is a PHP library that generates fake data for you. This is a command line
tool for easy generation of fake data in a static way.

%prep
%setup -q

%build
composer install --no-dev --prefer-dist --no-interaction

%install
%{__mkdir} -p %{buildroot}/%{faker_root}
%{__mkdir} -p %{buildroot}/%{_bindir}

%{__cp} -av . %{buildroot}/%{faker_root}

%{__ln_s} -f %{faker_root}/bin/faker-cli.php %{buildroot}%{_bindir}/faker-cli

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE readme.md
%{_bindir}/faker-cli
%{faker_root}/*
%{faker_root}/.gitignore

%changelog
* Mon Dec 05 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
