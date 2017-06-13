#
# spec file for package rbenv-gemset
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

Name:           rbenv-gemset
Version:        0.5.9
Release:        1
License:        MIT
Summary:        KISS yet powerful gem / gemset management for rbenv
Url:            https://github.com/jf/rbenv-gemset
Group:          Development/Languages/Ruby
Source:         https://github.com/jf/rbenv-gemset/archive/v%{version}.tar.gz
Requires:       rbenv
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
rbenv-gemset plugs in to the goodness of rbenv, and brings you gem management
that is at once simple, easy to understand and set up (just one file with the
simplest format ever!) and then use to do pretty much everything that you
really need to with gemsets.

rbenv-gemset is an extension for the rbenv ruby version manager that allows you
to use "gemsets", sandboxed collections of gems. This lets you have multiple
collections of gems installed in different sandboxes, and specify (on a
per-application basis) which sets of gems should be used.

%prep
%setup -q

%build

%install
for bin in libexec/*
do
    %{__install} -Dp -m 755 $bin %{buildroot}%{_bindir}/${bin##*/}
done

mkdir -p %{buildroot}%{_datadir}/%{name}/rbenv.d
cp -vr etc/rbenv.d/ %{buildroot}%{_datadir}/%{name}/


%post

%postun

%files
%defattr(-,root,root)
%doc README.mkd
%{_bindir}/%{name}*
%dir %{_datadir}/%{name}/rbenv.d
%{_datadir}/%{name}/rbenv.d/*

%changelog
* Tue Jun 13 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
