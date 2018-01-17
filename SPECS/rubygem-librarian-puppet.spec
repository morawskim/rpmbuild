#
# spec file for package rubygem-librarian-puppet
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

%define mod_name librarian-puppet
%define mod_full_name %{mod_name}-%{version}

Name:           rubygem-librarian-puppet
Version:        2.2.3
Release:        1
License:        MIT
Summary:        Bundler for your Puppet modules
Url:            http://librarian-puppet.com/
Group:          Development/Languages/Ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.9.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
PreReq:         update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a
path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge
such as Pulp
* Git modules can be installed from a branch, tag or specific commit,
optionally using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all
the modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools
that resolve, fetch, install, and isolate a project's dependencies.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md" \
  -f

# macro gem_packages fail
%{expand:%(/usr/lib/rpm/gem_packages.sh --default-gem %{mod_name}-%{version}.gem --gem-name=%{mod_name} --gem-version=%{version} --build-root %{buildroot} %{S:0})}

%changelog
* Wed Jan 17 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
