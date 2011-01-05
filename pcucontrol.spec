%define name pcucontrol
%define version 1.0
%define taglevel 9

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}
%global python_sitearch	%( python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" )

Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Vendor: PlanetLab
Packager: PlanetLab Central <support@planet-lab.org>
Distribution: PlanetLab %{plrelease}
URL: %{SCMURL}

Requires: python
Requires: OpenIPMI-tools
Obsoletes: monitor-pcucontrol

Summary: pcu controls for monitor and plcapi
Group: Applications/System

%description
both monitor and the plcapi use a set of common commands to reboot machines
using their external or internal pcus.  this package is a library of several
supported models.

%prep
%setup -q

%build
# NOTE: the build uses g++ cmdamt/
# NOTE: TMPDIR is needed here b/c the tmpfs of the build vserver is too small.
cd pcucontrol/models/intelamt
export TMPDIR=$PWD/tmp
mkdir -p $TMPDIR
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{python_sitearch}/pcucontrol/
rsync -a --exclude .svn  ./pcucontrol/    $RPM_BUILD_ROOT/%{python_sitearch}/pcucontrol/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitearch}


%changelog
* Fri Dec 03 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-9
- fix build for f14

* Thu Jul 08 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-8
- fix build issue

* Mon Jul 05 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-7
- fixes for HPiLO

* Fri Jun 18 2010 s s <soltesz@cs.princeton.edu> - pcucontrol-1.0-6
- adding a testrun parameter to the api

* Fri May 21 2010 Talip Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-5
- ePowerSwitchOld fix

* Wed May 12 2010 Talip Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-4
- * add ipmi trasport type.

* Mon May 03 2010 Talip Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-3
- remove unused import (that causes deprecated warnings in plcsh)

* Fri Apr 02 2010 Thierry Parmentelat <thierry.parmentelat@sophia.inria.fr> - pcucontrol-1.0-2
- tweak for DRAC - protect against spaces in password

* Thu Jan 21 2010 Talip Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - pcucontrol-1.0-1
- * pcucontrol obsoletes monitor-pcucontrol
- * use bash built-in instead of which to locate ssh
- * racadm fix for DRAC.

* Tue Dec 22 2009 Baris Metin <Talip-Baris.Metin@sophia.inria.fr>
- initial package
