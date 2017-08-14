#
# spec file for package packer
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

Name:           packer
Version:        1.0.0
Release:        2
License:        MPL-2.0
Summary:        Packer is a tool for creating identical machine images for multiple platforms from a single source configuration
Url:            https://www.packer.io/
Group:          System/Management
Source:         https://github.com/hashicorp/packer/archive/v%{version}.tar.gz
Patch0:         %{name}-move_packer_to_hashicorp.patch
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Packer is a free and open source tool for creating golden images for multiple
platforms from a single source configuration.

%prep
%setup -q
%patch0 -p1

%build
export GOPATH="$PWD/go"
#export GOROOT='/usr/lib64/go/1.7'
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/hashicorp
ln -s $PWD $GOPATH/src/github.com/hashicorp/packer

pushd go/src/github.com/hashicorp/packer
go build -o bin/packer .
popd

%install
%{__install} -Dp -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE
%{_bindir}/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.0.0-2
- Rebuild for openSUSE 42.3

* Sun Jun 11 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
