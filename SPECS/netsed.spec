#
# spec file for package netsed
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

Name:           netsed
Version:        1.2
Release:        1
License:        GPLv2+
Summary:        A tool to modify network packets
Url:            http://silicone.homelinux.org/projects/netsed/
Source:         http://silicone.homelinux.org/release/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NetSED is small and handful utility designed to alter the contents of
packets forwarded through your network in real time. It is really useful
for network hackers in following applications:

* black-box protocol auditing - whenever there are two or more
  proprietary boxes communicating over undocumented protocol (by enforcing
  changes in ongoing transmissions, you will be able to test if tested
  application is secure),
* fuzz-alike experiments, integrity tests - whenever you want to test
  stability of the application and see how it ensures data integrity,
* other common applications - fooling other people, content filtering,
  etc - choose whatever you want to.

%prep
%setup -q

%build
make %{?_smp_mflags}
make doc

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE NEWS README TODO html/
%{_bindir}/%{name}

%changelog
* Wed Nov 22 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

