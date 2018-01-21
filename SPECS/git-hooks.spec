#
# spec file for package git-hooks
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

Name:           git-hooks
Version:        1.1.4
Release:        1
License:        MIT
Summary:        git hooks manager
Url:            http://git-hooks.github.io/git-hooks/
Group:          Development/Tools/Version Control
Source:         https://github.com/git-hooks/git-hooks/archive/v%{version}.tar.gz
BuildRequires:  go
BuildRequires:  gox
BuildRequires:  godep
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
git-hooks is currently at the stage of managing client-side hooks. It will
support server-side hooks in the future.

git-hooks is a fork of icefox/git-hooks. The article “Managing Project, User,
and Global git hooks” explains much of the purpose of using git-hooks.

Usage

Run git hooks install to tell a git repo to use git-hooks.
Stop using git-hooks by git hooks uninstall.
List all scope of hooks by execute git hooks directly. See below for what scope
is.

%prep
%setup -q

%build
export GOPATH="$PWD/go"
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/git-hooks/
ln -s $PWD $GOPATH/src/github.com/git-hooks/git-hooks

pushd go/src/github.com/git-hooks/git-hooks
godep restore ./...
gox -os="linux" -output="build/{{.Dir}}_{{.OS}}_{{.Arch}}"
popd

%install
%{__install} -Dp -m 755 build/git-hooks_linux_amd64 %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc History.md LICENSE Readme.md
%{_bindir}/%{name}

%changelog
* Sun Jan 21 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
