#
# $Id$
# 

%define url $URL: svn+ssh://svn.planet-lab.org/svn/pcucontrol/trunk/pcucontrol.spec $

%define name pcucontrol
%define version 1.0
%define taglevel 1

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
URL: %(echo %{url} | cut -d ' ' -f 2)

Requires: python

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
* Tue Dec 22 2009 Baris Metin <Talip-Baris.Metin@sophia.inria.fr>
- initial package
