#
# spec file for package phinx
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

%define phinx_root /usr/lib/phinx

Name:           phinx
Version:        0.6.5
Release:        2
License:        MIT
Summary:        PHP Database Migrations for Everyone
Url:            https://phinx.org
Group:          Development/Libraries/PHP
Source:         https://github.com/robmorgan/phinx/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  composer
Requires:       php5 >= 5.4
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Phinx makes it ridiculously easy to manage the database migrations for your PHP
app. In less than 5 minutes you can install Phinx and create your first
database migration. Phinx is just about migrations without all the bloat of a
database ORM system or framework.

%prep
%setup -q

%build
composer install --no-dev --prefer-dist --no-interaction

%install
%{__mkdir} -p %{buildroot}/%{phinx_root}
%{__mkdir} -p %{buildroot}/%{_bindir}

%{__cp} -av . %{buildroot}/%{phinx_root}

%{__ln_s} -f %{phinx_root}/bin/phinx %{buildroot}%{_bindir}/phinx

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE README.md CHANGELOG.md
%{_bindir}/phinx
%{phinx_root}/*
%{phinx_root}/.gitignore
%{phinx_root}/.scrutinizer.yml
%{phinx_root}/.travis.yml

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Thu Dec 08 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
