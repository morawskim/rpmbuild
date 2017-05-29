#
# spec file for package ruby-build
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

Name:           ruby-build
Version:        20170523
Release:        1
License:        MIT
Summary:        Compile and install Ruby
Url:            https://github.com/rbenv/ruby-build
Group:          Development/Languages/Ruby
Source:         https://github.com/rbenv/ruby-build/archive/v%{version}.tar.gz
Requires:       bash
Requires:       curl
Requires:       gcc
# ruby MRI BuildRequires
Requires:       bison
Requires:       gdbm-devel
Requires:       gperf
Requires:       graphviz
Requires:       libjpeg-devel
Requires:       libressl-devel
Requires:       readline-devel
Requires:       tk-devel
Requires:       automake
Requires:       libffi-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ruby-build provides a simple way to compile and install different versions of
Ruby on UNIX-like systems.

%prep
%setup -q

%build

%install
%__mkdir_p %{buildroot}%{_bindir}
cp bin/* %{buildroot}%{_bindir}

%__mkdir_p %{buildroot}%{_datadir}/ruby-build
cp share/ruby-build/* %{buildroot}%{_datadir}/ruby-build

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/*
%dir %{_datadir}/ruby-build
%{_datadir}/ruby-build/*

%changelog
* Sun May 28 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
