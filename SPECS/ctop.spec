#
# spec file for package ctop
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

Name:           ctop
Version:        0.5.1
Release:        2
License:        MIT
Summary:        Top-like interface for container metrics
Url:            http://ctop.sh/
Group:          System/Management
Source:         https://github.com/bcicen/ctop/archive/v%{version}.tar.gz
BuildRequires:  go1.7
BuildRequires:  glide
Requires:       docker
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Top-like interface for container metrics

ctop provides a concise and condensed overview of real-time metrics for
multiple containers

%prep
%setup -q

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
export GOROOT='/usr/lib64/go/1.7'
mkdir -p $local_go/src/github.com/bcicen
ln -s $PWD $local_go/src/github.com/bcicen/ctop

pushd $local_go/src/github.com/bcicen/ctop
glide install
make build
popd

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md _docs/* LICENSE
%{_bindir}/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 0.5.1-2
- Rebuild for openSUSE 42.3

* Sun Jun 11 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
