#
# spec file for package hub
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

Name:           hub
Version:        2.2.9
Release:        1
License:        MIT
Summary:        hub helps you win at git
Url:            https://hub.github.com/
Group:          Applications/Internet
Source:         https://github.com/github/hub/archive/v%{version}.tar.gz
BuildRequires:  go1.6
BuildRequires:  ruby
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package bash-completion
Summary:        hub bash completion
Requires:       %{name} = %{version}
BuildArch:      noarch

%description
hub is a command line tool that wraps git in order to extend it with extra
features and commands that make working with GitHub easier.

``` bash
$ hub clone rtomayko/tilt
# expands to:
$ git clone git://github.com/rtomayko/tilt.git
```

hub is best aliased as git, so you can type `git <command>` in the shell and
get all the usual hub features.


%description bash-completion
hub bash completion

%prep
%setup -q

%build
./script/build
rake man:build

%install
%{__install} -Dp -m 755 ./bin/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dp -m 644 ./etc/hub.bash_completion.sh %{buildroot}%{_sysconfdir}/bash_completion.d/hub.bash_completion.sh
%{__install} -Dp -m 644 ./man/hub.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/%{name}
%{_mandir}/man1/hub.1%{?ext_man}

%files bash-completion
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/hub.bash_completion.sh

%changelog
* Mon Oct 16 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
