%{?scl:%scl_package nodejs-strip-ansi}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-strip-ansi
Version:    0.2.0
Release:    1%{?dist}
Summary:    Strip ANSI escape codes (used for colorizing strings in the terminal)
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/sindresorhus/strip-ansi
Source0:    http://registry.npmjs.org/strip-ansi/-/strip-ansi-%{version}.tgz
Source1:    https://raw.githubusercontent.com/sindresorhus/strip-ansi/3c9b37e5381603925ba16b27a05ccbfd338906b8/test.js
# https://github.com/sindresorhus/strip-ansi/pull/1
Source2:    LICENSE

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs010

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/strip-ansi
cp -pr package.json cli.js index.js \
    %{buildroot}%{nodejs_sitelib}/strip-ansi

# `strip-ansi` is used as the command.
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/strip-ansi/cli.js \
    %{buildroot}%{_bindir}/strip-ansi

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif

%files
%doc LICENSE readme.md
%{nodejs_sitelib}/strip-ansi
%{_bindir}/strip-ansi

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.0-1
- Enable software collections support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- update to upstream release 0.2.0

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.1-1
- initial package
