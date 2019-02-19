#
# spec file for package python-pipx
#
# Copyright (c) 2019 Marcin Morawski <marcin@morawskim.pl>.
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

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-pipx
Version:        0.12.2.0
Release:        1
License:        MIT
Summary:        pipx: execute binaries from Python packages in isolated environments
Url:            https://github.com/pipxproject/pipx
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pipx/pipx-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-setuptools
BuildArch:      noarch

%if ! 0%{?is_spectool}
%python_subpackages
%endif

%description
## Overview
* Safely install packages to isolated virtual environments, while globally exposing their CLI applications so you can run them from anywhere
* Easily list, upgrade, and uninstall packages that were installed with pipx
* Run the latest version of a CLI application from a package in a temporary virtual environment, leaving your system untouched after it finishes
* Run binaries from the `__pypackages__` directory per PEP 582 as companion tool to [pythonloc](https://github.com/cs01/pythonloc)
* Runs with regular user permissions, never calling `sudo pip install ...` (you aren't doing that, are you? 😄).

pipx combines the features of JavaScript's [npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) - which ships with npm - and Python's [pipsi](https://github.com/mitsuhiko/pipsi). pipx does not ship with pip but it is an important part of bootstrapping your system.

### Safely installing to isolated environments
You can globally install a CLI application by running
```
pipx install PACKAGE
```

This automatically creates a virtual environment, installs the package, and adds the package's CLI entry points to a location on your `PATH`. For example, `pipx install cowsay` makes the `cowsay` command available globally, but sandboxes the cowsay package in its own virtual environment. **pipx never needs to run as sudo to do this.**

Example:
```
>> pipx install cowsay
  installed package cowsay 2.0, Python 3.6.7
  These binaries are now globally available
    - cowsay
done!

### Running in temporary, sandboxed environments
pipx makes running the latest version of a program in a one-time environment as easy as
```
pipx run BINARY [ARGS...]
```
This will install the package in a temporary directory and invoke the binary. Try it!

```
pipx run cowsay moo
```

Notice that you **don't need to execute any install commands to run the binary**. Re-running the same binary is quick because pipx caches Virtual Environments on a per-binary basis. These caches last two days.

You can run .py files directly, too.
```
pipx run https://gist.githubusercontent.com/cs01/fa721a17a326e551ede048c5088f9e0f/raw/6bdfbb6e9c1132b1c38fdd2f195d4a24c540c324/pipx-demo.py
pipx is working!
```

%prep
%setup -q -n pipx-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pipx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pipx

%postun
%python_uninstall_alternative pipx

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pipx
%{python_sitelib}/*

%changelog
* Tue Feb 19 2019 Marcin Morawski <marcin@morawskim.pl>
-  init package
