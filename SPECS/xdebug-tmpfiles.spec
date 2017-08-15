#
# spec file for package xdebug-tmpfiles
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
%define dir_name xdebug

Name:           xdebug-tmpfiles
Version:        1
Release:        1
License:        MIT
Summary:        tmpfiles.d config for xdebug
Source0:        xdebug-tmpfiles.d.conf
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
tmpfiles.d config for xdebug

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}/usr/lib/tmpfiles.d/%{dir_name}.conf

%post
systemd-tmpfiles --create /usr/lib/tmpfiles.d/%{dir_name}.conf || true

%postun

%files
%defattr(-,root,root)
/usr/lib/tmpfiles.d/%{dir_name}.conf

%changelog
* Tue Aug 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
