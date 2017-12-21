#
# spec file for package journalcheck
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

%global commit0 84b758bc9a77c4a244d768b4e9c8bcb968273b6a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           journalcheck
Version:        20161208
Release:        1
License:        GPL-3
Summary:        Like logcheck, but for journald
Url:            https://github.com/jorgenschaefer/journalcheck
Group:          Applications/System
Source:         https://github.com/jorgenschaefer/journalcheck/archive/%{commit0}.tar.gz
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Journalcheck is a simple utility which sends mails of possibly interesting
journal entries to a configurable e-mail address. Journal entries are marked as
not interesting by matching a regular expression, a list of which can be
provided in a file, one per line.

This is very similar in operation to logcheck, except it operates on the
journal instead of plain text log files.

%prep
%setup -qn %{name}-%{commit0}

%build
export GOPATH="$PWD/go"
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/jorgenschaefer
ln -s $PWD $GOPATH/src/github.com/jorgenschaefer/journalcheck
go get github.com/coreos/go-systemd/sdjournal

pushd go/src/github.com/jorgenschaefer/journalcheck
go build -o bin/%{name} .
popd

%install
%{__install} -Dp -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE example/
%{_bindir}/%{name}

%changelog
* Thu Dec 21 2017 Marcin Morawski <marcin@morawskim.pl>
-  Init release
