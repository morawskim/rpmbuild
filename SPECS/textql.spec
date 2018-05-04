#
# spec file for package textql
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

%define commit0 209924e1c31cedd133ec3a66f0a14e43cb98f114

Name:           textql
Version:        20180504
Release:        1
License:        MIT
Summary:        Execute SQL against structured text like CSV or TSV
Url:            http://dinedal.github.io/textql/
Group:          Productivity/File utilitie
Source:         https://github.com/dinedal/textql/archive/%{commit0}.tar.gz
BuildRequires:  go >= 1.4
BuildRequires:  glide
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Allows you to easily execute SQL against structured text like CSV or TSV.

%prep
%setup -qn %{name}-%{commit0}

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
mkdir -p $local_go/src/github.com/dinedal
ln -s $PWD $local_go/src/github.com/dinedal/textql
pushd $local_go/src/github.com/dinedal/textql
glide install
go build -ldflags "-X main.VERSION=`cat VERSION`" -o ./build/%{name} ./textql/main.go
popd

%install
%{__install} -Dp -m 755 ./build/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dp -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%post

%postun

%files
%defattr(-,root,root)
%doc Readme.md LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
* Fri May 04 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
