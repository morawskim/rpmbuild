#
# spec file for package docker-credential-helpers
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

%global provider        github
%global provider_tld    com
%global project         docker
%global repo            docker-credential-helpers
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           docker-credential-helpers
Version:        0.6.2
Release:        1
License:        MIT
Summary:        docker-credential-helpers is a suite of programs to use native stores to keep Docker credentials safe
Url:            https://github.com/FiloSottile/gvt
Group:          Development/Languages/Other
Source:         https://github.com//%{project}/%{repo}/archive/v%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
docker-credential-helpers is a suite of programs to use native stores to keep Docker credentials safe.

%prep
%setup -q -n %{repo}-%{version}

%build
export GOPATH=$PWD/go
mkdir -p $GOPATH/src/github.com/docker

cp -r $PWD/vendor/* $GOPATH/src
ln -s $PWD $GOPATH/src/github.com/docker/docker-credential-helpers

make %{?_smp_mflags} pass

%install
install -D -m755 bin/docker-credential-pass %{buildroot}/%{_bindir}/docker-credential-pass

%post

%postun

%files
%defattr(-,root,root,-)
%doc README.md LICENSE CHANGELOG.md
%_bindir/docker-credential-pass

%changelog
* Sun Jul 21 2019 Marcin Morawski <marcin@morawskim.pl>
-  init release

