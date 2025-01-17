%global srcname tornado
%global common_description %{expand:
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.}

Name:           python-%{srcname}
Version:        6.4.2
Release:        1%{?dist}
Summary:        Scalable, non-blocking web server and tools

License:        ASL 2.0
URL:            https://www.tornadoweb.org
Source0:        https://github.com/tornadoweb/tornado/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Fix timeout failure in architectures such as ppc64le.
Patch:         Increase-timeout-in-test_request_timeout.patch

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Examples for %{name}

%description doc %{common_description}

This package contains some example applications.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove shebang from files
%{__sed} -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py

%build
%py3_build

%install
%py3_install

%check
export ASYNC_TEST_TIMEOUT=10
%{__python3} -m tornado.test.runtests --verbose

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/

%files doc
%license LICENSE
%doc demos

%changelog
* Tue Nov 26 2024 Sergio Correia <scorreia@redhat.com> - 6.4.2-1
- Update to 6.4.2
  Resolves: RHEL-68663

* Tue Jul 25 2023 Sergio Correia <scorreia@redhat.com> - 6.1.0-9
- Fix an open redirect in StaticFileHandler
  Resolves: CVE-2023-28370

* Wed Jun 15 2022 Sergio Correia <scorreia@redhat.com> - 6.1.0-8
- Fix test failure in pcc64le
  Related: rhbz#2084553

* Wed Jun 15 2022 Sergio Correia <scorreia@redhat.com> - 6.1.0-7
- Add python-tornado to RHEL-9
  Resolves: rhbz#2084553

* Tue Feb 08 2022 Carl George <carl@george.computer> - 6.1.0-6
- Convert to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Fabian Affolter <mail@fabian-affolter.ch> -6.1.0-1
- Update to latest upstream release 6.1.0 (#1883858)

* Sun Sep 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.0.4-1
- Update to latest upstream release 6.0.3 (#1809858)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.3-2
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.0.3-1
- Update to 6.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-1
- Update to 6.0.2 (#1600318)

* Thu May 16 2019 Lumír Balhar <lbalhar@redhat.com> - 5.1.1-2
- New patch to not turn DeprecationWarning in tornado module into Exception
- Fixes FTBFS with Python 3.8

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-1
- Update to 5.1.1
- Fix SyntaxWarnings (turned into SyntaxErrors) on Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-3
- Rebuilt for Python 3.7

* Sat May 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-2
- Require python2-futures

* Fri May 18 2018 Charalampos Stratakis <cstratak@redhat.com> - 5.0.2-1
- Update to 5.0.2

* Thu Apr 26 2018 Lumír Balhar <lbalhar@redhat.com> - 4.5.2-5
- New conditionals for Python 2
- Drop Python 3 conditional

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.5.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Charalampos Stratakis <cstratak@redhat.com> - 4.5.2-2
- Fix dist tag and bump release for rebuild

* Tue Nov 07 2017 Charalampos Stratakis <cstratak@redhat.com> - 4.5.2-1
- Update to 4.5.2

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 4.5.1-4
- Cleanup spec file conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Orion Poplawski <orion@cora.nwra.com> - 4.5.1-1
- Update to 4.5.1

* Mon Apr 17 2017 Orion Poplawski <orion@cora.nwra.com> - 4.5-1
- Update to 4.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 4.4.2-2
- Rebuild for Python 3.6
- Added patch to fix Python 3.6 test failures

* Sun Oct 2 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.2-1
- Update to 4.4.2

* Thu Sep 15 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.1-1
- Update to 4.4.1
- Drop requires patch, fixed upstream

* Thu Sep 15 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3-5
- Remove backports.ssl_match_hostname from python2-tornado egg requires (bug #1372887)

* Thu Sep 15 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3-4
- Remove certifi from python2-tornado egg requires (bug #1372886)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3-2
- Properly build python2-tornado

* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3-1
- Update to 4.3
- Drop upstream patches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-3
- Build python2 packages, drop separate python3 doc package

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 4.2.1-2
- Rebuilt for Python3.5 rebuild
- Add patch to use getfullargspec on python3
- Add patch to fix failing tests with python3.5

* Fri Sep 18 2015 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-1
- Update to 4.2.1
- Modernize spec

* Fri Jul 10 2015 Orion Poplawski <orion@cora.nwra.com> - 4.1-3
- Do not require python-backports-ssl_match_hostname for F22+ (bug #1231368)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 1 2015 Orion Poplawski <orion@cora.nwra.com> - 4.1-1
- Update to 4.1
- Modernize spec

* Fri Dec 5 2014 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Drop requires python-simplejson

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Thomas Spura <tomspur@fedoraproject.org> - 3.2.1-1
- update to 3.2.1
- no noarch anymore
- remove defattr

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.2.1-5
- remove rhel conditional for with_python3:
  https://fedorahosted.org/fpc/ticket/200

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.1-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.1-1
- update to upstream release 2.2.1 (fixes CVE-2012-2374)
- fix typo for epel6 macro bug #822972 (Florian La Roche)

* Thu Feb 9 2012 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.2-1
- upgrade to upstream release 2.2

* Thu Feb 9 2012 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.1.1-4
- remove python3-simplejson dependency

* Fri Jan 27 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-3
- build python3 package

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.1.1-1
- new upstream version 2.1.1
- remove double word in description and rearrange it (#715272)
- fixed removal of shebangs
- added %%check section to run unittests during package build

* Tue Mar 29 2011 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.2.1-1
- new upstream version 1.2.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep  8 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.1-1
- new upstream release 1.1

* Tue Aug 17 2010 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 1.0.1-1
- new upstream bugfix release: 1.0.1

* Wed Aug  4 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0-2
- changed upstream source url

* Wed Aug  4 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0-1
- new upstream release 1.0
- there's no longer a problem with spurious permissions, so remove that fix

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Oct 21 2009 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 0.2-3
- changed -doc package group to Documentation
- use global instead of define

* Tue Oct 20 2009 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 0.2-2
- create -doc package for examples
- altered description to not include references to FriendFeed
- rename to python-tornado

* Fri Sep 25 2009 Ionuț Arțăriși <mapleoin@lavabit.com> - 0.2-1
- New upstream version
- Fixed macro usage and directory ownership in spec

* Thu Sep 10 2009 Ionuț Arțăriși <mapleoin@lavabit.com> - 0.1-1
- Initial release

