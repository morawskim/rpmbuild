#
# spec file for package golang-github-filosottile-gvt
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
%global project         FiloSottile
%global repo            gvt
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define rev 50d83ea21cb0405e81efd284951e111b3a68d701

Name:           golang-github-FiloSottile-gvt
Version:        2016.11.18
Release:        1
License:        MIT
Summary:        gvt is the go vendoring tool
Url:            https://github.com/FiloSottile/gvt
Group:          Development/Languages/Other
Source:         https://github.com//%{project}/%{repo}/archive/%{rev}.tar.gz
BuildRequires:  golang-packaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{go_nostrip}
%{go_provides}

%description
gvt is a simple vendoring tool made for Go native vendoring (aka GO15VENDOREXPERIMENT), based on gb-vendor.

It lets you easily and "idiomatically" include external dependencies in your repository to get reproducible builds.

No need to learn a new tool or format!
You already know how to use gvt: just run gvt fetch when and like you would run go get. You can imagine what gvt update and gvt delete do. In addition, gvt also allows fetching specific commits or branch versions in packages, and fully accommodates private repos.

No need to change how you build your project!
gvt downloads packages to ./vendor/.... The stock Go compiler will find and use those dependencies automatically without import path rewriting or GOPATH changes.
(Go 1.6+, or Go 1.5 with GO15VENDOREXPERIMENT=1 set required.)

No need to manually chase, copy or cleanup dependencies!
gvt works recursively as you would expect, and lets you update vendored dependencies. It also writes a manifest to ./vendor/manifest and never touches your system GOPATH. Finally, it strips the VCS metadata so that you can commit the vendored source cleanly.

No need for your users and occasional contributors to install or even know about gvt!
Packages whose dependencies are vendored with gvt are go build-able and go get-able out of the box by Go 1.6+, or Go 1.5 with GO15VENDOREXPERIMENT=1 set.

Note that projects must live within the GOPATH tree in order to be go build-able with native vendoring.

%prep
%setup -q -n %{repo}-%{rev}

%build
%goprep %{import_path}
%gobuild

%install
%goinstall
%gosrc
%gofilelist

%post

%postun

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE
%_bindir/gvt

%changelog
* Sun Jul 01 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release

