%{?scl:%scl_package nodejs-strip-ansi}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-strip-ansi
Version:    3.0.1
Release:    1%{?dist}
Summary:    Strip ANSI escape codes (used for colorizing strings in the terminal)
License:    MIT
URL:        https://github.com/chalk/strip-ansi
Source0:    http://registry.npmjs.org/strip-ansi/-/strip-ansi-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/strip-ansi
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/strip-ansi

# `strip-ansi` is used as the command.
#mkdir -p %%{buildroot}%%{_bindir}
#ln -sf %%{nodejs_sitelib}/strip-ansi/cli.js \
#    %%{buildroot}%%{_bindir}/strip-ansi

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif

%files
%doc license readme.md
%{nodejs_sitelib}/strip-ansi
#%%{_bindir}/strip-ansi

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-2
- Use macro in -runtime dependency

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.0-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.0-1
- Enable software collections support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- update to upstream release 0.2.0

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.1-1
- initial package
