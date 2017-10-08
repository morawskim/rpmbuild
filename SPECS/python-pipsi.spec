#
# spec file for package python-pipsi
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-pipsi
Version:        0.9
Release:        2
License:        BSD
Summary:        Wraps pip and virtualenv to install scripts
Url:            http://github.com/mitsuhiko/pipsi/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pipsi/pipsi-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-click
Requires:       python-setuptools
Requires:       python-virtualenv
BuildArch:      noarch

%if ! 0%{?is_spectool}
%python_subpackages
%endif

%description
pipsi
=====

pipsi = pip script installer

What does it do?  pipsi is a wrapper around virtualenv and pip
which installs scripts provided by python packages into separate
virtualenvs to shield them from your system and each other.

In other words: you can use pipsi to install things like
pygmentize without making your system painful.

How do I get it?

::

    curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python

How does it work?

pipsi installs each package into ~/.local/venvs/PKGNAME and then
symlinks all new scripts into ~/.local/bin.

Installing scripts from a package::

      $ pipsi install Pygments

Uninstalling packages and their scripts::

      $ pipsi uninstall Pygments

Upgrading a package::

      $ pipsi upgrade Pygments

Showing what's installed::

      $ pipsi list

How do I get rid of pipsi?

::

      $ pipsi uninstall pipsi

How do I upgrade pipsi?  With 0.5 and later just do this::

      $ pipsi upgrade pipsi

On older versions just uninstall and reinstall.

%prep
%setup -q -n pipsi-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pipsi
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pipsi

%postun
%python_uninstall_alternative pipsi

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pipsi
%{python_sitelib}/*

%changelog
* Sun Oct 08 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
-  fix build package python-pipsi (shebang contained python3 interpreator
   instead python2)
