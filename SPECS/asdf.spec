#
# spec file for package asdf
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

%global commitPluginPHP 35e99ac579b08c6d391ed5ce5d4816dda2646013

Name:           asdf
Version:        0.4.0
Release:        1
License:        MIT
Summary:        Extendable version manager with support for Ruby, Node.js & more
Url:            https://github.com/asdf-vm/asdf
#Group:
Source0:        https://github.com/asdf-vm/asdf/archive/v%{version}.tar.gz
Source1:        https://github.com/odarriba/asdf-php/archive/%{commitPluginPHP}.tar.gz
Patch0:         %{name}-change-install-dir.patch
Requires:       mlocate
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package plugin-php
Summary:        PHP plugin for asdf version manager
Requires:       %{name} = %{version}

%description plugin-php
PHP plugin for asdf version manager

%description
extendable version manager

Supported languages include Ruby, Node.js, Elixir and more.



%prep
%setup -q
%patch0 -p1
%setup -T -D -a 1

%build

%install
mkdir -p %{buildroot}%{_datadir}/asdf %{buildroot}%{_datadir}/asdf/plugins
cp -r ./bin %{buildroot}%{_datadir}/asdf
cp -r ./completions %{buildroot}%{_datadir}/asdf
cp -r ./lib %{buildroot}%{_datadir}/asdf
cp ./VERSION %{buildroot}%{_datadir}/asdf
cp ./help.txt %{buildroot}%{_datadir}/asdf

mkdir -p %{buildroot}%{_datadir}/asdf/plugins/php
cp -r ./asdf-php-%{commitPluginPHP}/bin %{buildroot}%{_datadir}/asdf/plugins/php

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md docs/
%{_datadir}/asdf/help.txt
%{_datadir}/asdf/VERSION
%{_datadir}/asdf/lib
%{_datadir}/asdf/completions
%{_datadir}/asdf/bin

%files plugin-php
%{_datadir}/asdf/plugins/php
%doc ./asdf-php-%{commitPluginPHP}/CHANGELOG ./asdf-php-%{commitPluginPHP}/LICENSE ./asdf-php-%{commitPluginPHP}/README.md

%changelog
* Sun Oct 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
