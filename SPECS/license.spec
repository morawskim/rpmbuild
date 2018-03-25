#
# spec file for package license
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

Name:           license
Version:        1.0.0
Release:        1
License:        MIT
Summary:        Generate license files
Url:            https://github.com/nishanths/license
Group:          Development/Tools/Other
Source:         https://github.com/nishanths/license/archive/v%{version}.tar.gz
Patch0:         %{name}-os_rename_fails_on_linux.patch
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Create licenses from the command-line.

* Supports all the licenses available on GitHub
* Does not need network access (except on first run)
* Good defaults for name and year on the license; easy to customize when needed

%prep
%setup -q
%patch0 -p1

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
mkdir -p $local_go/
ln -s $PWD/vendor $local_go/src
mkdir -p $local_go/src/github.com/nishanths/
ln -s $PWD $local_go/src/github.com/nishanths/license
pushd $local_go/src/github.com/nishanths/license
go build
popd


%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Sun Mar 25 2018 Marcin Morawski <marcin@morawskim.pl>
-  Add patch to fix os.Rename fails on linux
-  No automatic checks/updates with the GitHub API (except when the
$HOME/.license directory does not exist).
-  Remove logger and base packages
-  Create license API client package
-  Use standard lib. log package and flag package
-  Vendor dependencies
-  Remove homebrew, binaries
-  Do not save licenses JSON in raw/ directory. Running license -update will
remove the directory.

