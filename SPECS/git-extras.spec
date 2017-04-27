#
# spec file for package git-extras
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

Name:           git-extras
Version:        4.2.0
Release:        1
License:        MIT
Summary:        Little git extras
Url:            https://github.com/tj/%{name}
Group:          Development/Tools
Source:         https://github.com/tj/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ruby2.1-rubygem-ronn
Requires:       git
Requires:       bash-completion
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} adds the following extra-commands to git:

alias, archive-file, bug, changelog, commits-since, contrib, count,
create-branch, delete-branch, delete-submodule, delete-tag, effort,
extras, feature, fresh-branch, gh-pages, graft, ignore, info,
local-commits, obliterate, promote, refactor, release, repl, setup,
squash, summary, touch, undo

For more information about the extra-commands, see the included
README.md, HTML, mark-down or man-pages.

%prep
%setup -q
# scripts already use bash
# remove `/usr/bin/env` from hashbang
sed -i -e "s/\/usr\/bin\/.*sh/\/bin\/bash/g" bin/*

%build
# stop ruby split-method compaining about
# `invalid byte sequence in US-ASCII (ArgumentError)`
# by exporting UTF-8 encoding to C-locale.
export LC_CTYPE="en_US.UTF-8"
pushd man
# build manpages and HTML-doc
./manning-up.sh
# replace all (escaped-dots) (\.) with the proper
# escape-sequence for <dot> in manpages (\[char46])
# (rubygem-)ronn doesn't handle this correctly.
sed -ie "s/\\\\\./\\\\\[char46\]/g" *.1
popd

%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d \
     html md
     install -pm 0644 man/*.html html
     install -pm 0644 man/*.md md

%post

%postun

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/bash_completion.d
%doc AUTHORS History.md Readme.md html/ md/
%license LICENSE
%{_bindir}/*
%{_mandir}/man*/*

%changelog
* Sun Apr 23 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
